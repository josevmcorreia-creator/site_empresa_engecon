# Midnight Blueprint Design System

### 1. Overview & Creative North Star
**Creative North Star: The Industrial Monolith**
Midnight Blueprint is a design system built for the high-stakes world of industrial management and construction logistics. It eschews the "softness" of modern consumer apps in favor of a "Technical Editorial" aesthetic. It utilizes a deep "Midnight Navy" (#000033) foundation to provide a sense of grounded authority, contrasted against sharp primary blues and safety-inspired oranges. The system breaks traditional grid-rigidness by using heavy typographic weights and high-density information clusters that feel like a digital architectural plan.

### 2. Colors
The palette is a mix of high-contrast functional colors and deep professional neutrals.
- **Midnight Navy (#000033):** Used for sidebar navigation and "Hero" KPI cards to establish depth.
- **Signal Orange (#FF9200):** Reserved for primary actions, active indicators, and high-priority status shifts.
- **Electric Blue (#0000EF):** The functional primary for links and instructional elements.
- **The "No-Line" Rule:** Sectioning is achieved through color blocks (e.g., the Midnight Navy sidebar against the Light Gray canvas) or tonal shifts in the surface container hierarchy. 1px borders should be minimized, appearing only as a subtle `white/5` or `white/10` when high-contrast backgrounds require a "Technical Bleed" limit.
- **Surface Hierarchy:** Depth is created by nesting `surface_container_low` (f3f3f5) inputs within `surface_container_lowest` (ffffff) cards.

### 3. Typography
The system uses **Manrope** exclusively, leveraging its geometric construction to mimic industrial labeling.
- **Display & Headlines:** High-impact bold and extra-bold weights (up to 2.25rem/36px for KPIs) create a "dashboard-at-a-glance" hierarchy.
- **The "Technical Detail" Scale:** A significant portion of the UI operates on a 10px to 12px scale. This high-density approach reflects a professional environment where information volume is prioritized over whitespace.
- **Typography as Branding:** The logo uses a black-weight tracking-tighter treatment to simulate a structural beam.

### 4. Elevation & Depth
Elevation is conveyed through **Tonal Layering** rather than heavy drop shadows.
- **The Layering Principle:** A light gray background (#f4f4f5) hosts pure white cards (#ffffff), which in turn host slightly recessed input fields (#f3f3f5).
- **Ambient Shadows:** Standard shadows are `shadow-md` or `shadow-lg`, but specifically utilized with color-matching blurs (e.g., `shadow-secondary/20` for orange buttons) to create a subtle glow rather than a gray smudge.
- **Glassmorphism:** Navigation headers use `white/90` with a backdrop blur to maintain the architectural "stack" while scrolling.

### 5. Components
- **Buttons:** Sharp corners (radius: 0.125rem). Primary buttons are heavy blocks of Signal Orange. Secondary "outline" buttons use low-opacity borders (10%) of the text color.
- **Status Badges:** Use a "Safety Label" style—background tint with a 2px solid left-border (e.g., Green-600 for ENTRADA, Red-600 for SAÍDA).
- **Tables:** High-density with 10px text. The header uses the `secondary` orange to anchor the data.
- **Sidebar:** The "Active" state uses a `white/8` background and a 3px `secondary` orange left-border, providing a clear vertical indicator.

### 6. Do's and Don'ts
- **Do:** Use high-contrast status colors (Green-500, Red-500, Yellow-500) for data indicators within the Midnight Navy cards.
- **Do:** Maintain the 10px uppercase tracking-widest style for utility labels (e.g., "GESTÃO DE REFORMAS").
- **Don't:** Use rounded corners above 12px (0.75rem). The system is designed to feel engineered and precise.
- **Don't:** Introduce generic gray shadows. If a shadow is needed, use the object's primary color at a very low opacity (10-20%).