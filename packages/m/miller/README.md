# miller

URL: [miller](https://github.com/johnkerl/miller)

----

[readthedocs](https://miller.readthedocs.io)

Miller is like awk, sed, cut, join, and sort for name-indexed data such as CSV, TSV, and tabular JSON

TEST COMMANDS:

```shell
mlr --icsv --opprint sort -f color,shape /usr/share/doc/packages/miller/example.csv ; echo ;
mlr --icsv --ojson filter '$color=="yellow"' /usr/share/doc/packages/miller/example.csv ; echo ;
mlr --c2p --from /usr/share/doc/packages/miller/example.csv put '$qr = $quantity * $rate'
```
