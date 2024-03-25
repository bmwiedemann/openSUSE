## Modifications since last major version

### 29.0.2

* Add characters:
  - SYMBOL FOR DELETE SQUARE CHECKER BOARD FORM (`U+2427`)  (Proposed for Unicode 16; L2/21-235).
  - SYMBOL FOR DELETE RECTANGULAR CHECKER BOARD FORM (`U+2428`)  (Proposed for Unicode 16; L2/21-235).
  - LEFT-POINTING STICK FIGURE (`U+1CC02`)  (Proposed for Unicode 16; L2/21-235).
  - RIGHT-POINTING STICK FIGURE (`U+1CC03`)  (Proposed for Unicode 16; L2/21-235).
  - DOWN-POINTING STICK FIGURE (`U+1CC04`)  (Proposed for Unicode 16; L2/21-235).
  - UPPER LEFT TWELFTH CIRCLE (`U+1CC30`) ... DENSE HORIZONTAL FILL (`U+1CC45`)  (Proposed for Unicode 16; L2/21-235).
  - SQUARE SPIRAL FROM TOP LEFT (`U+1CC7C`) ... HORIZONTAL LADDER (`U+1CC85`)  (Proposed for Unicode 16; L2/21-235).
  - RIGHT HALF AND LEFT HALF WHITE CIRCLE (`U+1CE00`)  (Proposed for Unicode 16; L2/21-235).
  - LOWER HALF AND UPPER HALF WHITE CIRCLE (`U+1CE01`)  (Proposed for Unicode 16; L2/21-235).
  - UPPER HALF HEAVY WHITE SQUARE (`U+1CE03`)  (Proposed for Unicode 16; L2/21-235).
  - LOWER HALF HEAVY WHITE SQUARE (`U+1CE04`)  (Proposed for Unicode 16; L2/21-235).
  - HEAVY WHITE SQUARE CONTAINING BLACK VERY SMALL SQUARE (`U+1CE05`)  (Proposed for Unicode 16; L2/21-235).
  - TOP JUSTIFIED LOWER HALF WHITE CIRCLE (`U+1FBE0`) ... LEFT JUSTIFIED RIGHT HALF WHITE CIRCLE (`U+1FBE3`)  (Proposed for Unicode 16; L2/21-235).
  - TOP JUSTIFIED LOWER HALF BLACK CIRCLE (`U+1FBE8`) ... TOP LEFT JUSTIFIED LOWER RIGHT QUARTER BLACK CIRCLE (`U+1FBEF`)  (Proposed for Unicode 16; L2/21-235).
* Quasi-proportional will now use `four` = `closed-serifless` and `four` = `closed-serifed` for Aile and Etoile respectively.


### 29.0.1

* Fix broken `s`/`t` variants for `U+01BE`. (#2223).
* Fix precomposed iota with double marks (#2229).
* Fix leaning mark placement on letters around i/l.
* Fix sans-serif linking for `U+2781`..`U+2784` and `U+278B`..`U+278E`.


### 29.0.0

* \[**BREAKING**\] Add separate serifed variants for digits `2` through `5`. As a result, current variants are partially renamed and reordered (#1965). Change of variant names:
  - `two`.`straight-neck` → `two`.`straight-neck-serifless`
  - `two`.`curly-neck` → `two`.`curly-neck-serifless`
  - `three`.`flat-top` → `three`.`flat-top-serifless`
  - `four`.`closed` → `four`.`closed-serifless`
  - `four`.`closed-non-crossing` → `four`.`closed-non-crossing-serifless`
  - `four`.`semi-open` → `four`.`semi-open-serifless`
  - `four`.`semi-open-non-crossing` → `four`.`semi-open-non-crossing-serifless`
  - `four`.`open` → `four`.`open-serifless`
  - `four`.`open-non-crossing` → `four`.`open-non-crossing-serifless`
  - `five`.`upright-arched` → `five`.`upright-arched-serifless`
  - `five`.`upright-flat` → `five`.`upright-flat-serifless`
  - `five`.`oblique-arched` → `five`.`oblique-arched-serifless`
  - `five`.`oblique-flat` → `five`.`oblique-flat-serifless`
* \[**BREAKING**\] Reorder of glyph variants:
   - Influenced characters: `I`, `U`, `Z`, `i`, `l`, `u`, `z`, Greek Lower Mu (`μ`), Micro Sign (`µ`).
* \[**BREAKING**\] Quasi-proportional will now use a six-unit system instead of four. Metrics of various letters (`f`, `t`, `r`, `m`, `w`, etc.) are adjusted.
* Add characters:
  - UPWARDS WHITE ARROW FROM BAR (`U+21EA`) ... RIGHTWARDS WHITE ARROW FROM WALL (`U+21F0`).
  - RETURN SYMBOL (`U+23CE`).
  - SYMBOL FOR DELETE MEDIUM SHADE FORM  (`U+2429`).
  - GEAR WITHOUT HUB (`U+26ED`).
  - GEAR WITH HANDLES (`U+26EE`).
  - MAP SYMBOL FOR LIGHTHOUSE (`U+26EF`).
  - THREE-D TOP-LIGHTED RIGHTWARDS ARROWHEAD (`U+27A2`).
  - THREE-D BOTTOM-LIGHTED RIGHTWARDS ARROWHEAD (`U+27A3`).
  - SHUFFLE PRODUCT (`U+29E2`).
  - GLEICH STARK (`U+29E6`).
  - INTERIOR PRODUCT (`U+2A3C`).
  - RIGHTHAND INTERIOR PRODUCT (`U+2A3D`).
  - SHORT LEFT TACK (`U+2ADE`) ... SHORT UP TACK (`U+2AE0`).
  - VERTICAL BAR TRIPLE RIGHT TURNSTILE (`U+2AE2`) ... REVERSED DOUBLE STROKE NOT SIGN (`U+2AED`).
  - UPWARDS WHITE ARROW FROM BAR WITH HORIZONTAL BAR (`U+2BB8`).
  - LEFT RAISED OMISSION BRACKET (`U+2E0C`).
  - RIGHT RAISED OMISSION BRACKET (`U+2E0C`).
  - LEFT LOW PARAPHRASE BRACKET (`U+2E1C`).
  - RIGHT LOW PARAPHRASE BRACKET (`U+2E1C`).
  - LOWER HORIZONTAL RULER SEGMENT (`U+1CC05`)  (Proposed for Unicode 16; L2/21-235).
  - RIGHT VERTICAL RULER SEGMENT (`U+1CC06`)  (Proposed for Unicode 16; L2/21-235).
  - LOWER RIGHT RULER SEGMENT (`U+1CC07`)  (Proposed for Unicode 16; L2/21-235).
  - BOX DRAWINGS LIGHT HORIZONTAL AND UPPER RIGHT (`U+1CC1B`) ... SEPARATED BLOCK QUADRANT-1234 (`U+1CC2F`)  (Proposed for Unicode 16; L2/21-235).
  - EIGHT RAYS INWARD (`U+1CC69`) ... BLACK NEUTRAL FACE (`U+1CC6F`)  (Proposed for Unicode 16; L2/21-235).
  - SQUARE FOUR CORNER SALTIRES (`U+1CC89`) ... INVERSE BLACK DIAMOND (`U+1CC8D`)  (Proposed for Unicode 16; L2/21-235).
  - VERTICAL LINE WITH FOUR TICK MARKS (`U+1CC90`)  (Proposed for Unicode 16; L2/21-235).
  - HORIZONTAL LINE WITH FOUR TICK MARKS (`U+1CC91`)  (Proposed for Unicode 16; L2/21-235).
  - WHITE VERTICAL RECTANGLE WITH HORIZONTAL BAR (`U+1CE06`)  (Proposed for Unicode 16; L2/21-235).
  - BOX DRAWINGS DOUBLE DIAGONAL LOWER LEFT TO MIDDLE CENTRE TO LOWER RIGHT (`U+1CE09`)  (Proposed for Unicode 16; L2/21-235).
  - BOX DRAWINGS DOUBLE DIAGONAL UPPER LEFT TO MIDDLE CENTRE TO UPPER RIGHT (`U+1CE0A`)  (Proposed for Unicode 16; L2/21-235).
  - SEPARATED BLOCK SEXTANT-1 (`U+1CE51`) ... SEPARATED BLOCK SEXTANT-123456 (`U+1CE8F`)  (Proposed for Unicode 16; L2/21-235).
  - UPPER LEFT ONE SIXTEENTH BLOCK (`U+1CE90`) ... LOWER HALF RIGHT ONE QUARTER BLOCK (`U+1CEAF`)  (Proposed for Unicode 16; L2/21-235).
  - FOLDER (`U+1F5C0`) (#2181).
  - DOWNWARDS BLACK ARROW TO BAR (`U+1F8B3`) ... SOUTH WEST ARROW FROM BAR (`U+1F8BB`)  (Proposed for Unicode 16; L2/21-235).
  - RAISED LEFT SMALL SQUARE BRACKET (`U+1FBCC`)  (Proposed for Unicode 16; L2/21-235).
  - LEFT TWO THIRDS BLOCK (`U+1FBCE`)  (Proposed for Unicode 16; L2/21-235).
  - LEFT ONE THIRD BLOCK (`U+1FBCF`)  (Proposed for Unicode 16; L2/21-235).
  - BOX DRAWINGS LIGHT DIAGONAL MIDDLE RIGHT TO LOWER LEFT (`U+1FBD0`) ... BOX DRAWINGS LIGHT DIAGONAL UPPER LEFT TO MIDDLE RIGHT TO LOWER LEFT (`U+1FBDF`)  (Proposed for Unicode 16; L2/21-235).
  - UPPER CENTRE ONE QUARTER BLOCK (`U+1FBE4`) ... MIDDLE RIGHT ONE QUARTER BLOCK (`U+1FBE7`)  (Proposed for Unicode 16; L2/21-235).
* Fix a disjoint stroke of Outlined Curly `Z` under some weights (#2195).
* Unify diagonal box drawings' angles (#2197).
* Fix Large Type Piece `U+1CE3B` (#2206).
* Added a `MOSC` feature that turns certain geometric shapes into mosaics (#2212).
* Fix `frac` feature for better recognizing fraction patterns (#2214).
* Fix broken shape of `U+1FB95`, `U+1FB96` and `U+1FB97` (#2218). 
* Increase weight for `U+276E`/`U+276F` (#2217).
* Fix ligation for `[|]` (#2221).

