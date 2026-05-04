# KADU-WORKSPACE

## Live Pokédex
Check out the live Pokédex here: 

[https://kaduvercosa.github.io/KADU-WORKSPACE/Pokedex/](https://kaduvercosa.github.io/KADU-WORKSPACE/Pokedex/)

## Features
* **Detailed View:** View individual Pokémon with attributes, stats, moves, abilities, items, and evolutions.
* **List View:** Full Pokédex grid view for easy browsing.
* **Search & Autocomplete:** Find any Pokémon by name or ID.
* **Filters:** Filter Pokémon by Generation, Type, and Rarity (Legendary, Mythical, Baby).
* **Randomizer:** Discover new Pokémon with the random roll feature.
* **Dynamic Styling:** Colors adapt dynamically based on the primary type of the selected Pokémon.
* **Localization:** Automatic translation using Google Translate API.
* **Dark Mode:** Supports OS-level dark mode preference.

## File Organization (index.html)
The `Pokedex/index.html` file is a single-file application containing all HTML, CSS, and JavaScript. Here is a guide to help you find and modify specific sections:

### 1. CSS Styles (`<style>` tag)
* **Lines ~15 to ~30:** Root variables (Colors, Gradients, Liquid Glass themes).
* **Lines ~30 to ~120:** Basic resets, typography, global animations (`float`, `fadeIn`), and the `liquid-glass` class definition.
* **Lines ~120 to ~190:** Header & Navigation Bar styling (`#search-container`, `#autocomplete-list`, buttons).
* **Lines ~190 to ~250:** Main Pokémon Card styling (`#main-card`, `#poke-image`, typography, stat bars, move badges).
* **Lines ~250 to ~280:** Grid View styling (`#full-pokedex`, `.pokedex-card`, `.mini-type`).
* **Lines ~280 to ~320:** Modals & Overlays general styling (Liquid Glass close buttons, modal backgrounds).
* **Lines ~320 to ~350:** Specific Modal rules (`#compare-modal-content`, `.details-content`, `#settings-modal`).

### 2. HTML Structure (`<body>` tag)
* **Lines ~350 to ~390:** Top Navigation Bar (Search input, Select filters, Buttons: Favorites, Random, Settings).
* **Lines ~390 to ~460:** Main Application Content.
  * `#main-card`: The currently selected Pokémon (Image, Types, Stats, Moves, Extrainfo).
  * `#evolutions` & `#varieties`: The evolution tree and alternate forms.
  * `#list-view`: The grid container for the full Pokédex list.
* **Lines ~460 to ~630:** Modals Structure.
  * `#compare-modal`: The side-by-side Pokémon comparator.
  * `#info-modal`: Small modal for Moves and Abilities details.
  * `#image-viewer-modal`: Fullscreen image viewer for sprites.
  * `#details-modal`: Expanded Pokémon details (Sprite Gallery, Breeding, Training).
  * `#settings-modal`: User preferences (Theme, Font Size, Effects toggles).
* **Lines ~630 to ~640:** Footer.

### 3. JavaScript Logic (`<script>` tag)
* **Lines ~640 to ~670:** Initial variables, mapping dictionaries (types, colors, generation names), and initial data load (`loadAllPokemon`).
* **Lines ~670 to ~760:** Autocomplete logic (for main search and compare search) and scroll-hide header logic.
* **Lines ~760 to ~860:** Grid View Logic (`loadPokedex`, `handleFilter`). Fetches and renders the grid of cards.
* **Lines ~860 to ~1100:** Main Pokémon Fetching (`fetchPokemon`). The core function! Loads details, updates DOM, translates flavor text, and calculates stats.
* **Lines ~1100 to ~1150:** Type Matchups logic (`calculateTypeMatchups`).
* **Lines ~1150 to ~1210:** Evolution Chain fetching (`fetchEvolutions`).
* **Lines ~1210 to ~1320:** Utilities (Search, Random, URL parameter handling).
* **Lines ~1320 to ~1410:** Settings & LocalStorage Logic (`saveSettings`, `applySettings`, `updatePokemonUI`).
* **Lines ~1410 to ~1480:** Favorites Logic (`toggleFavorite`, `updateFavoriteButton`).
* **Lines ~1480 to ~1550:** Modals Opening/Closing Logic (`openDetailsModal`, `openImageViewer`, etc.). Included here is the logic for rendering the sprite gallery.
* **Lines ~1550 to ~1650:** Compare Modal Logic (`searchCompare`). Calculates side-by-side stat bars.
* **Lines ~1650 to ~1730:** Info Modals Logic (`fetchAbilityInfo`, `fetchMoveInfo`).

## Technologies Used
* HTML5
* CSS3
* JavaScript (Vanilla)
* [PokeAPI](https://pokeapi.co/)

## How to run locally
1. Clone the repository:
   ```bash
   git clone https://github.com/kaduvercosa/KADU-WORKSPACE.git
   ```
2. Navigate to the repository root directory:
   ```bash
   cd KADU-WORKSPACE
   ```
3. Start a local server. For example, using Python 3:
   ```bash
   python3 -m http.server --directory Pokedex/
   ```
4. Open your browser and go to
   ```bash
   http://localhost:8000
   ```