/*
===========================================================
The AAA Archive
Arquivo: FoundationPage.tsx

Objetivo:
Representar a página principal da Foundation Collection.

Nesta etapa, a página:
- utiliza a estrutura global ArchiveShell;
- carrega os jogos reais pela FastAPI;
- exibe os registros utilizando o componente GameCard;
- envia pesquisas reais para GET /games/search;
- envia filtros reais para os endpoints da FastAPI;
- ordena localmente os registros exibidos;
- representa loading, success, empty e error;
- restaura a coleção completa ao limpar uma operação.

Regras atuais:
- busca e filtro não são combinados;
- executar uma busca limpa o filtro ativo;
- executar um filtro limpa a busca ativa;
- a ordenação pode ser aplicada à coleção, busca ou filtro.

Ainda não são implementados:
- combinação entre busca e filtros;
- imagens definitivas;
- página individual dos jogos.
===========================================================
*/

import {
  type FormEvent,
  useEffect,
  useMemo,
  useState,
} from 'react'

import ArchivePanel from '../components/ArchivePanel'
import ArchiveShell from '../components/ArchiveShell'
import type { ContextSidebarItem } from '../components/ContextSidebar'
import GameCard from '../components/GameCard'
import {
  getGames,
  getGamesByDecade,
  getGamesByDeveloper,
  getGamesByFranchise,
  getGamesByGenre,
  getGamesByYear,
  searchGames,
} from '../services/api'
import type { Game } from '../types/Game'
import {
  sortGames,
  type SortOption,
} from '../utils/sortGames'

import './FoundationPage.css'


// ==========================================================
// NAVEGAÇÃO CONTEXTUAL
// ==========================================================

const foundationSidebarItems: ContextSidebarItem[] = [
  {
    label: 'ALL RECORDS',
    target: '#foundation-records',
  },
  {
    label: 'SEARCH ARCHIVE',
    target: '#foundation-search',
  },
  {
    label: 'FILTER ARCHIVE',
    target: '#foundation-filter',
  },
  {
    label: 'SORT ARCHIVE',
    target: '#foundation-sort',
  },
]


// ==========================================================
// ESTADOS POSSÍVEIS DAS REQUISIÇÕES
// ==========================================================

type CollectionRequestState =
  | 'loading'
  | 'success'
  | 'empty'
  | 'error'

type SearchRequestState =
  | 'idle'
  | 'loading'
  | 'success'
  | 'empty'
  | 'error'

type FilterRequestState =
  | 'idle'
  | 'loading'
  | 'success'
  | 'empty'
  | 'error'
  | 'invalid'

type DisplayRequestState =
  | 'loading'
  | 'success'
  | 'empty'
  | 'error'


// ==========================================================
// TIPOS DOS FILTROS
// ==========================================================

type FilterType =
  | ''
  | 'decade'
  | 'year'
  | 'genre'
  | 'developer'
  | 'franchise'

type AppliedFilterType = Exclude<
  FilterType,
  ''
>

type ActiveFilter = {
  type: AppliedFilterType
  label: string
  value: string
}


// ==========================================================
// FUNÇÕES AUXILIARES DOS FILTROS
// ==========================================================

/*
Transforma o valor técnico do filtro em um texto visual.

developer
↓
DEVELOPER
*/

function getFilterTypeLabel(
  selectedType: FilterType,
) {
  if (selectedType === 'decade') {
    return 'DECADE'
  }

  if (selectedType === 'year') {
    return 'YEAR'
  }

  if (selectedType === 'genre') {
    return 'GENRE'
  }

  if (selectedType === 'developer') {
    return 'DEVELOPER'
  }

  if (selectedType === 'franchise') {
    return 'FRANCHISE'
  }

  return ''
}


/*
Valida os valores numéricos antes de enviar a requisição.

YEAR:
deve conter exatamente quatro números.

DECADE:
deve conter quatro números e terminar em zero.
*/

function filterValueIsValid(
  selectedType: FilterType,
  value: string,
) {
  if (selectedType === 'year') {
    return /^\d{4}$/.test(value)
  }

  if (selectedType === 'decade') {
    return (
      /^\d{4}$/.test(value)
      && value.endsWith('0')
    )
  }

  return value.length > 0
}


/*
Centraliza a escolha da função correta do api.ts.
*/

async function requestFilteredGames(
  selectedType: AppliedFilterType,
  value: string,
): Promise<Game[]> {
  if (selectedType === 'decade') {
    return getGamesByDecade(Number(value))
  }

  if (selectedType === 'year') {
    return getGamesByYear(Number(value))
  }

  if (selectedType === 'genre') {
    return getGamesByGenre(value)
  }

  if (selectedType === 'developer') {
    return getGamesByDeveloper(value)
  }

  return getGamesByFranchise(value)
}


// ==========================================================
// FUNÇÃO AUXILIAR DA ORDENAÇÃO
// ==========================================================

/*
Transforma a opção técnica em um texto apresentado
na interface.
*/

function getSortOptionLabel(
  selectedOption: SortOption,
) {
  if (selectedOption === 'archive-order') {
    return 'ARCHIVE ORDER'
  }

  if (selectedOption === 'title-asc') {
    return 'TITLE: A–Z'
  }

  if (selectedOption === 'year-asc') {
    return 'OLDEST FIRST'
  }

  if (selectedOption === 'year-desc') {
    return 'NEWEST FIRST'
  }

  return 'METACRITIC: HIGHEST'
}


// ==========================================================
// COMPONENTE PRINCIPAL
// ==========================================================

function FoundationPage() {
  /*
  allGames preserva a coleção completa.

  displayedGames contém os registros que aparecem
  atualmente no grid antes da ordenação.
  */

  const [allGames, setAllGames] = useState<Game[]>([])

  const [
    displayedGames,
    setDisplayedGames,
  ] = useState<Game[]>([])


  // ========================================================
  // ESTADOS DAS REQUISIÇÕES
  // ========================================================

  const [
    collectionRequestState,
    setCollectionRequestState,
  ] = useState<CollectionRequestState>('loading')

  const [
    searchRequestState,
    setSearchRequestState,
  ] = useState<SearchRequestState>('idle')

  const [
    filterRequestState,
    setFilterRequestState,
  ] = useState<FilterRequestState>('idle')


  // ========================================================
  // ESTADOS DO SEARCH TERMINAL
  // ========================================================

  const [searchTerm, setSearchTerm] = useState('')

  const [
    activeSearchTerm,
    setActiveSearchTerm,
  ] = useState('')


  // ========================================================
  // ESTADOS DO FILTER TERMINAL
  // ========================================================

  const [filterType, setFilterType] =
    useState<FilterType>('')

  const [filterValue, setFilterValue] =
    useState('')

  const [
    activeFilter,
    setActiveFilter,
  ] = useState<ActiveFilter | null>(null)


  // ========================================================
  // ESTADO DO SORT TERMINAL
  // ========================================================

  /*
  A ordenação inicial utiliza os IDs da coleção.
  */

  const [sortOption, setSortOption] =
    useState<SortOption>('archive-order')


  // ========================================================
  // CARREGAMENTO INICIAL DA COLEÇÃO
  // ========================================================

  useEffect(() => {
    let pageIsActive = true

    async function loadGames() {
      try {
        const receivedGames = await getGames()

        if (!pageIsActive) {
          return
        }

        setAllGames(receivedGames)
        setDisplayedGames(receivedGames)

        if (receivedGames.length === 0) {
          setCollectionRequestState('empty')
        } else {
          setCollectionRequestState('success')
        }
      } catch {
        if (pageIsActive) {
          setCollectionRequestState('error')
        }
      }
    }

    loadGames()

    return () => {
      pageIsActive = false
    }
  }, [])


  // ========================================================
  // LIMPEZA INTERNA DA PESQUISA
  // ========================================================

  function resetSearchState() {
    setSearchTerm('')
    setActiveSearchTerm('')
    setSearchRequestState('idle')
  }


  // ========================================================
  // LIMPEZA INTERNA DO FILTRO
  // ========================================================

  function resetFilterState() {
    setFilterType('')
    setFilterValue('')
    setActiveFilter(null)
    setFilterRequestState('idle')
  }


  // ========================================================
  // ENVIO DA PESQUISA
  // ========================================================

  async function handleSearchSubmit(
    event: FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault()

    const normalizedTerm = searchTerm.trim()

    if (
      normalizedTerm.length === 0
      || collectionRequestState !== 'success'
    ) {
      return
    }

    /*
    Uma busca remove o filtro ativo.

    A ordenação, porém, permanece aplicada.
    */

    resetFilterState()

    setActiveSearchTerm(normalizedTerm)
    setSearchRequestState('loading')

    try {
      const receivedGames =
        await searchGames(normalizedTerm)

      setDisplayedGames(receivedGames)

      if (receivedGames.length === 0) {
        setSearchRequestState('empty')
      } else {
        setSearchRequestState('success')
      }
    } catch {
      setDisplayedGames([])
      setSearchRequestState('error')
    }
  }


  // ========================================================
  // LIMPEZA VISUAL DA PESQUISA
  // ========================================================

  function handleSearchClear() {
    resetSearchState()
    setDisplayedGames(allGames)
  }


  // ========================================================
  // ENVIO DO FILTRO
  // ========================================================

  async function handleFilterSubmit(
    event: FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault()

    const normalizedValue = filterValue.trim()

    if (
      filterType === ''
      || normalizedValue.length === 0
      || collectionRequestState !== 'success'
    ) {
      return
    }

    if (
      !filterValueIsValid(
        filterType,
        normalizedValue,
      )
    ) {
      setActiveFilter(null)
      setFilterRequestState('invalid')

      return
    }

    const selectedFilter: ActiveFilter = {
      type: filterType,
      label: getFilterTypeLabel(filterType),
      value: normalizedValue,
    }

    /*
    Um filtro remove a busca ativa.

    A ordenação permanece aplicada aos novos resultados.
    */

    resetSearchState()

    setActiveFilter(selectedFilter)
    setFilterRequestState('loading')

    try {
      const receivedGames =
        await requestFilteredGames(
          selectedFilter.type,
          selectedFilter.value,
        )

      setDisplayedGames(receivedGames)

      if (receivedGames.length === 0) {
        setFilterRequestState('empty')
      } else {
        setFilterRequestState('success')
      }
    } catch {
      setDisplayedGames([])
      setFilterRequestState('error')
    }
  }


  // ========================================================
  // ALTERAÇÃO DO TIPO DE FILTRO
  // ========================================================

  function handleFilterTypeChange(
    selectedType: FilterType,
  ) {
    setFilterType(selectedType)
    setFilterValue('')
    setActiveFilter(null)
    setFilterRequestState('idle')

    if (activeFilter) {
      setDisplayedGames(allGames)
    }
  }


  // ========================================================
  // LIMPEZA VISUAL DO FILTRO
  // ========================================================

  function handleFilterClear() {
    resetFilterState()
    setDisplayedGames(allGames)
  }


  // ========================================================
  // CONTROLE DA ORDENAÇÃO
  // ========================================================

  function handleSortReset() {
    setSortOption('archive-order')
  }


  // ========================================================
  // PLACEHOLDER DO FILTRO
  // ========================================================

  let filterPlaceholder =
    'Select a filter type first...'

  if (filterType === 'decade') {
    filterPlaceholder = 'Example: 2000'
  }

  if (filterType === 'year') {
    filterPlaceholder = 'Example: 2018'
  }

  if (filterType === 'genre') {
    filterPlaceholder = 'Example: Survival Horror'
  }

  if (filterType === 'developer') {
    filterPlaceholder = 'Example: Capcom'
  }

  if (filterType === 'franchise') {
    filterPlaceholder = 'Example: Resident Evil'
  }


  // ========================================================
  // CONTROLE DOS FORMULÁRIOS
  // ========================================================

  const searchIsLoading =
    searchRequestState === 'loading'

  const filterIsLoading =
    filterRequestState === 'loading'

  const operationIsLoading =
    searchIsLoading || filterIsLoading

  const searchCanExecute =
    searchTerm.trim().length > 0
    && collectionRequestState === 'success'
    && !operationIsLoading

  const searchCanClear =
    !operationIsLoading
    && (
      searchTerm.length > 0
      || activeSearchTerm.length > 0
    )

  const filterCanExecute =
    filterType !== ''
    && filterValue.trim().length > 0
    && collectionRequestState === 'success'
    && !operationIsLoading

  const filterCanClear =
    !operationIsLoading
    && (
      filterType !== ''
      || filterValue.length > 0
      || activeFilter !== null
      || filterRequestState === 'invalid'
    )

  const sortCanReset =
    sortOption !== 'archive-order'
    && !operationIsLoading


  // ========================================================
  // LISTA ORDENADA
  // ========================================================

  /*
  useMemo recalcula a lista ordenada somente quando:
  - os jogos exibidos mudam;
  - a opção de ordenação muda.

  displayedGames permanece preservado.
  */

  const sortedDisplayedGames = useMemo(
    () => sortGames(
      displayedGames,
      sortOption,
    ),
    [
      displayedGames,
      sortOption,
    ],
  )


  // ========================================================
  // ESTADO ATUAL DO GRID
  // ========================================================

  let displayRequestState: DisplayRequestState =
    collectionRequestState

  if (collectionRequestState === 'success') {
    displayRequestState = 'success'
  }

  if (
    collectionRequestState === 'success'
    && searchRequestState !== 'idle'
  ) {
    displayRequestState = searchRequestState
  }

  if (
    collectionRequestState === 'success'
    && (
      filterRequestState === 'loading'
      || filterRequestState === 'success'
      || filterRequestState === 'empty'
      || filterRequestState === 'error'
    )
  ) {
    displayRequestState = filterRequestState
  }


  // ========================================================
  // FEEDBACK DO SEARCH TERMINAL
  // ========================================================

  let searchFeedbackTitle = 'WAITING FOR INPUT'

  let searchFeedbackDetail =
    'Enter a term to search the Foundation Collection.'

  if (searchRequestState === 'loading') {
    searchFeedbackTitle = 'RETRIEVING RECORDS...'

    searchFeedbackDetail =
      `Searching archive for: ${activeSearchTerm}`
  }

  if (searchRequestState === 'success') {
    searchFeedbackTitle =
      `${displayedGames.length} RECORDS FOUND`

    searchFeedbackDetail =
      `Results returned for: ${activeSearchTerm}`
  }

  if (searchRequestState === 'empty') {
    searchFeedbackTitle = 'NO RECORDS FOUND'

    searchFeedbackDetail =
      `No archive records correspond to: ${activeSearchTerm}`
  }

  if (searchRequestState === 'error') {
    searchFeedbackTitle = 'ARCHIVE NODE UNAVAILABLE'

    searchFeedbackDetail =
      'The search query could not be completed.'
  }


  // ========================================================
  // FEEDBACK DO FILTER TERMINAL
  // ========================================================

  let filterFeedbackTitle =
    'WAITING FOR FILTER'

  let filterFeedbackDetail =
    'Select a category and enter a value.'

  if (
    filterType !== ''
    && filterRequestState === 'idle'
  ) {
    filterFeedbackTitle =
      `${getFilterTypeLabel(filterType)} SELECTED`

    filterFeedbackDetail =
      'Enter a value and execute the archive filter.'
  }

  if (filterRequestState === 'loading') {
    filterFeedbackTitle = 'APPLYING FILTER...'

    filterFeedbackDetail = activeFilter
      ? `${activeFilter.label} / ${activeFilter.value}`
      : 'Preparing archive request.'
  }

  if (filterRequestState === 'success') {
    filterFeedbackTitle =
      `${displayedGames.length} RECORDS FOUND`

    filterFeedbackDetail = activeFilter
      ? `${activeFilter.label} / ${activeFilter.value}`
      : 'Filter completed.'
  }

  if (filterRequestState === 'empty') {
    filterFeedbackTitle = 'NO RECORDS FOUND'

    filterFeedbackDetail = activeFilter
      ? `No records correspond to ${activeFilter.label} / ${activeFilter.value}.`
      : 'The filter returned an empty collection.'
  }

  if (filterRequestState === 'error') {
    filterFeedbackTitle =
      'ARCHIVE NODE UNAVAILABLE'

    filterFeedbackDetail =
      'The filter request could not be completed.'
  }

  if (filterRequestState === 'invalid') {
    filterFeedbackTitle =
      'INVALID FILTER VALUE'

    filterFeedbackDetail =
      filterType === 'decade'
        ? 'Enter a four-digit decade ending in zero. Example: 2000.'
        : 'Enter a valid four-digit year. Example: 2018.'
  }


  // ========================================================
  // ESTADO DO SORT TERMINAL
  // ========================================================

  const sortFeedbackTitle =
    getSortOptionLabel(sortOption)

  const sortFeedbackDetail =
    sortOption === 'archive-order'
      ? 'Records follow the original Foundation archive identification.'
      : `Local ordering applied to ${displayedGames.length} displayed records.`


  // ========================================================
  // ESTADO DO PAINEL DE REGISTROS
  // ========================================================

  let recordsTitle = 'ALL RECORDS'

  let recordsCode = 'ARCHIVE QUERY'

  let statusMessage = 'RETRIEVING RECORDS...'

  let statusDetail =
    'Establishing connection with archive node.'

  if (displayRequestState === 'success') {
    recordsCode =
      `${displayedGames.length} RECORDS`

    if (activeSearchTerm) {
      recordsTitle = 'SEARCH RESULTS'
    }

    if (activeFilter) {
      recordsTitle = 'FILTER RESULTS'
    }
  }

  if (displayRequestState === 'loading') {
    if (activeSearchTerm) {
      recordsTitle = 'SEARCH RESULTS'
      recordsCode = 'SEARCHING'

      statusDetail =
        `Searching the archive for: ${activeSearchTerm}`
    }

    if (activeFilter) {
      recordsTitle = 'FILTER RESULTS'
      recordsCode = 'FILTERING'

      statusDetail =
        `Applying ${activeFilter.label}: ${activeFilter.value}`
    }
  }

  if (displayRequestState === 'empty') {
    recordsCode = '00 RESULTS'
    statusMessage = 'NO RECORDS FOUND'

    if (activeSearchTerm) {
      recordsTitle = 'SEARCH RESULTS'

      statusDetail =
        'Nenhum registro corresponde ao termo consultado.'
    }

    if (activeFilter) {
      recordsTitle = 'FILTER RESULTS'

      statusDetail =
        `No records correspond to ${activeFilter.label} / ${activeFilter.value}.`
    }

    if (
      !activeSearchTerm
      && !activeFilter
    ) {
      recordsCode = '00 RECORDS'

      statusDetail =
        'The archive node returned an empty collection.'
    }
  }

  if (displayRequestState === 'error') {
    recordsCode = 'QUERY FAILED'
    statusMessage = 'ARCHIVE NODE UNAVAILABLE'

    if (activeSearchTerm) {
      recordsTitle = 'SEARCH RESULTS'

      statusDetail =
        'The search query could not be completed.'
    }

    if (activeFilter) {
      recordsTitle = 'FILTER RESULTS'

      statusDetail =
        'The filter request could not be completed.'
    }

    if (
      !activeSearchTerm
      && !activeFilter
    ) {
      recordsCode = 'NODE OFFLINE'

      statusDetail =
        'The collection could not be retrieved.'
    }
  }


  // ========================================================
  // INTEGRIDADE DO HEADER
  // ========================================================

  let collectionIntegrity = 'retrieving'

  if (collectionRequestState === 'success') {
    collectionIntegrity = 'stable'
  }

  if (collectionRequestState === 'empty') {
    collectionIntegrity = 'empty'
  }

  if (
    collectionRequestState === 'error'
    || searchRequestState === 'error'
    || filterRequestState === 'error'
  ) {
    collectionIntegrity = 'unavailable'
  }


  // ========================================================
  // ITEM ATIVO DA NAVEGAÇÃO LATERAL
  // ========================================================

  let activeSidebarItem = 'ALL RECORDS'

  if (sortOption !== 'archive-order') {
    activeSidebarItem = 'SORT ARCHIVE'
  }

  if (activeFilter) {
    activeSidebarItem = 'FILTER ARCHIVE'
  }

  if (activeSearchTerm) {
    activeSidebarItem = 'SEARCH ARCHIVE'
  }


  // ========================================================
  // INTERFACE
  // ========================================================

  return (
    <ArchiveShell
      sidebarTitle="FOUNDATION COLLECTION"
      sidebarItems={foundationSidebarItems}
      activeSidebarItem={activeSidebarItem}
    >
      <section className="archive-panel foundation-hero">
        <div className="foundation-hero__content">
          <p className="archive-eyebrow">
            // FOUNDATION / COLLECTION
          </p>

          <h1>FOUNDATION COLLECTION</h1>

          <p className="foundation-hero__description">
            Registros preservados de jogos que ajudaram
            a construir o meio.
            <br />
            Explorar, pesquisar, lembrar.
          </p>

          <p
            className={
              collectionIntegrity === 'unavailable'
                ? 'archive-system-message foundation-hero__integrity foundation-hero__integrity--error'
                : 'archive-system-message foundation-hero__integrity'
            }
          >
            &gt; collection integrity:

            <span>{collectionIntegrity}</span>
          </p>
        </div>

        <div
          className="foundation-hero__visual"
          aria-label="Representação atmosférica do acervo da Foundation Collection"
        >
          <div
            className="foundation-hero__shelves"
            aria-hidden="true"
          />

          <div className="foundation-hero__visual-content">
            <span>FOUNDATION STORAGE FEED</span>

            <strong>ARCHIVE VAULT 01</strong>

            <small>
              atmospheric image awaiting local asset
            </small>
          </div>
        </div>
      </section>

      <ArchivePanel
        id="foundation-search"
        title="SEARCH TERMINAL"
        code="API SEARCH"
        className="foundation-search"
      >
        <form
          className="foundation-search__form"
          onSubmit={handleSearchSubmit}
        >
          <div className="foundation-search__command">
            <label
              htmlFor="foundation-search-input"
              className="foundation-search__label"
            >
              SEARCH QUERY
            </label>

            <input
              id="foundation-search-input"
              type="search"
              value={searchTerm}
              onChange={(event) => {
                setSearchTerm(event.target.value)
              }}
              placeholder="Search by title, developer, franchise, or keyword..."
              autoComplete="off"
              disabled={
                collectionRequestState !== 'success'
                || operationIsLoading
              }
            />

            <button
              type="submit"
              disabled={!searchCanExecute}
            >
              {searchIsLoading
                ? 'SEARCHING...'
                : 'EXECUTE'}
            </button>
          </div>

          <div
            className="foundation-search__feedback"
            aria-live="polite"
          >
            <div className="foundation-search__feedback-text">
              <span>SEARCH STATUS</span>

              <strong>{searchFeedbackTitle}</strong>

              <p>{searchFeedbackDetail}</p>
            </div>

            {searchCanClear && (
              <button
                type="button"
                className="foundation-search__clear"
                onClick={handleSearchClear}
              >
                CLEAR SEARCH
              </button>
            )}
          </div>
        </form>
      </ArchivePanel>

      <ArchivePanel
        id="foundation-filter"
        title="FILTER TERMINAL"
        code="API FILTER"
        className="foundation-filter"
      >
        <form
          className="foundation-filter__form"
          onSubmit={handleFilterSubmit}
        >
          <div className="foundation-filter__command">
            <label
              htmlFor="foundation-filter-type"
              className="foundation-filter__label"
            >
              FILTER QUERY
            </label>

            <select
              id="foundation-filter-type"
              value={filterType}
              onChange={(event) => {
                handleFilterTypeChange(
                  event.target.value as FilterType,
                )
              }}
              disabled={
                collectionRequestState !== 'success'
                || operationIsLoading
              }
            >
              <option value="">
                SELECT TYPE
              </option>

              <option value="decade">
                DECADE
              </option>

              <option value="year">
                YEAR
              </option>

              <option value="genre">
                GENRE
              </option>

              <option value="developer">
                DEVELOPER
              </option>

              <option value="franchise">
                FRANCHISE
              </option>
            </select>

            <input
              type="text"
              inputMode={
                filterType === 'decade'
                || filterType === 'year'
                  ? 'numeric'
                  : 'text'
              }
              value={filterValue}
              onChange={(event) => {
                setFilterValue(event.target.value)

                if (
                  filterRequestState === 'invalid'
                ) {
                  setFilterRequestState('idle')
                }
              }}
              placeholder={filterPlaceholder}
              autoComplete="off"
              disabled={
                filterType === ''
                || collectionRequestState !== 'success'
                || operationIsLoading
              }
            />

            <button
              type="submit"
              disabled={!filterCanExecute}
            >
              {filterIsLoading
                ? 'FILTERING...'
                : 'EXECUTE'}
            </button>
          </div>

          <div
            className="foundation-filter__feedback"
            aria-live="polite"
          >
            <div className="foundation-filter__feedback-text">
              <span>FILTER STATUS</span>

              <strong>{filterFeedbackTitle}</strong>

              <p>{filterFeedbackDetail}</p>
            </div>

            {filterCanClear && (
              <button
                type="button"
                className="foundation-filter__clear"
                onClick={handleFilterClear}
              >
                CLEAR FILTER
              </button>
            )}
          </div>
        </form>
      </ArchivePanel>

      <ArchivePanel
        id="foundation-sort"
        title="SORT TERMINAL"
        code="LOCAL ORDER"
        className="foundation-sort"
      >
        <div className="foundation-sort__command">
          <label
            htmlFor="foundation-sort-option"
            className="foundation-sort__label"
          >
            SORT ORDER
          </label>

          <select
            id="foundation-sort-option"
            value={sortOption}
            onChange={(event) => {
              setSortOption(
                event.target.value as SortOption,
              )
            }}
            disabled={
              collectionRequestState !== 'success'
              || operationIsLoading
            }
          >
            <option value="archive-order">
              ARCHIVE ORDER
            </option>

            <option value="title-asc">
              TITLE: A–Z
            </option>

            <option value="year-asc">
              OLDEST FIRST
            </option>

            <option value="year-desc">
              NEWEST FIRST
            </option>

            <option value="metacritic-desc">
              METACRITIC: HIGHEST
            </option>
          </select>

          <button
            type="button"
            onClick={handleSortReset}
            disabled={!sortCanReset}
          >
            RESET ORDER
          </button>
        </div>

        <div
          className="foundation-sort__feedback"
          aria-live="polite"
        >
          <div className="foundation-sort__feedback-text">
            <span>SORT STATUS</span>

            <strong>{sortFeedbackTitle}</strong>

            <p>{sortFeedbackDetail}</p>
          </div>

          <span className="foundation-sort__local">
            NO API REQUEST
          </span>
        </div>
      </ArchivePanel>

      <ArchivePanel
        id="foundation-records"
        title={recordsTitle}
        code={recordsCode}
        className="foundation-records"
      >
        {displayRequestState !== 'success' && (
          <div
            className={
              `foundation-records__status ` +
              `foundation-records__status--${displayRequestState}`
            }
            aria-live="polite"
          >
            <span className="foundation-records__status-label">
              ARCHIVE STATUS
            </span>

            <strong>{statusMessage}</strong>

            <p>{statusDetail}</p>
          </div>
        )}

        {displayRequestState === 'success' && (
          <div className="foundation-records__collection">
            <div className="foundation-records__collection-header">
              <span>
                {activeSearchTerm
                  ? `QUERY: ${activeSearchTerm}`
                  : activeFilter
                    ? `${activeFilter.label}: ${activeFilter.value}`
                    : 'FOUNDATION ARCHIVE'}
              </span>

              <small>
                DISPLAYING {sortedDisplayedGames.length} RECORDS
                {' / '}
                {getSortOptionLabel(sortOption)}
              </small>
            </div>

            <div className="foundation-records__grid">
              {sortedDisplayedGames.map((game) => (
                <GameCard
                  key={game.id}
                  game={game}
                />
              ))}
            </div>
          </div>
        )}
      </ArchivePanel>

      <footer className="archive-quote">
        <span>
          “We archive not for nostalgia, but for continuity.”
        </span>

        <span>— The Archivist</span>
      </footer>
    </ArchiveShell>
  )
}

export default FoundationPage