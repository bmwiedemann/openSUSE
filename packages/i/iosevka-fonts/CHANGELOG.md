## Modifications since last major version

### 30.0.0

* \[**Breaking**\] A separate variant selector, `tittle`, was added to allow users to configure the shape of the dots in `i` and `j` separately.
  - As a result, feature tags for `cv95` ... `cv99`, `VSAA` ... `VSAQ` are shifted by one place to `cv96` ... `cv99` `VSAA`, `VSAB` ... `VSAR`.
* \[**BREAKING**\] Add `semi-chancery-straight-serifed` and `semi-chancery-curly-serifed` variants for `x` (`cv48`). As a result, variants of `x` are reordered. Change of variant names:
  - `x`.`semi-chancery-straight` → `x`.`semi-chancery-straight-serifless`
  - `x`.`semi-chancery-curly` → `x`.`semi-chancery-curly-serifless`
* Refine shape of CYRILLIC CAPITAL LETTER SHHA (`U+04BA`).
* Fix leaning mark anchors for letters with top hooks (`U+0187`, `U+0188`, `U+0193`, `U+0199`, `U+01A5`, `U+01AD`, `U+0253`, `U+0257`, `U+0260`, `U+0266`, `U+0267`, `U+0284`, `U+029B`, `U+0280`, `U+1D91`, `U+1DF09`).
* Fix H bar position of CYRILLIC {CAPITAL|SMALL} LETTER NJE (`U+040A`, `U+045A`).
* Fix earedness of Bulgarian Cyrillic Lower Pe (`U+043F`).
* Add Italic form for CYRILLIC SMALL LETTER REVERSED TSE (`U+A661`).
* Make CYRILLIC SMALL LETTER REVERSED YU (`U+A655`) follow tailed variants of Cyrillic Lower Yery (`cv82`).
* Fix mapping of LEFT-FACING SNAKE HEAD WITH OPEN MOUTH (`U+1CC70`) ... DOWN-FACING SNAKE HEAD WITH CLOSED MOUTH (`U+1CC77`).
* Add characters:
  - BOTTOM RIGHT CROP (`U+230C`) ... TOP LEFT CROP (`U+230F`).
  - KEYBOARD (`U+2328`).
  - COUNTERBORE (`U+2334`).
  - LESS-THAN ABOVE SIMILAR OR EQUAL (`U+2A8D`).
  - GREATER-THAN ABOVE SIMILAR OR EQUAL (`U+2A8E`).

