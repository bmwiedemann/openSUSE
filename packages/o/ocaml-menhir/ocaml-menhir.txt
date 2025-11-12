# Changes

## 2025/09/12

* In the new code back-end, fix a problem that could lead to an internal error
  in `StackLangCheck` with the message `Failed stack subtype check (jump)`.
  This problem could appear only when shift/reduce conflicts were resolved in
  favor of reduction, causing edges to be removed in the LR(1) automaton.
  (Reported by Wiktor Kuchta; fixed by François Pottier.)

* Fix a vulnerability in the code produced by the table back-end.
  With `--table` and `--external-tokens`, if the user proposed two
  inconsistent views of the types of the tokens, then Menhir would
  produce code that contains incorrect unsafe type casts, which the
  OCaml compiler would silently accept. (Reported by Fay Carsons;
  fixed by Frédéric Bour.)

## 2025/09/03

* The table back-end uses a new table compression algorithm.

  This algorithm is significantly faster than the previous algorithm:
  in our tests, it can be up to 8 times faster.
  This results in observably faster compilation:
  for example, the time required to compile the OCaml parser
  drops from 1.2 seconds to 0.6 seconds.

  Compared with the previous algorithm,
  the new algorithm produces results of roughly similar quality:
  the size of the compressed tables can increase or decrease
    by a few percent, up to 20% in the most dramatic cases.
  On average, we observe a 1% increase in size.

  The use of the previous algorithm can be requested
  by the command line switch `--pack-classic`.
  This command line switch may disappear in the future.

  (Contributed by Frédéric Bour; reviewed by François Pottier.)

## 2024/07/15

* Fix a bug that could in principle cause `menhir --list-errors` to produce
  incorrect output in some cases. This bug was never observed in real life.
  (Contributed by Frédéric Bour.)

* `menhir --coq` now generates `From Coq.extraction Require Extraction.`,
  which is required for compatibility with future versions of Coq.
  (Requested by Xavier Leroy; implemented by Jacques-Henri Jourdan.)

## 2023/12/31

* The new command line switch `--unparsing` (which must be used in conjunction
  with `--table`) causes Menhir to generate an unparsing API. In short,
  unparsing is the process of transforming abstract syntax trees back into
  text. The unparsing API is intended to help users write correct unparsers,
  but does not automate the whole process.

  For more details, please see the paper [Correct, Fast LR(1)
  Unparsing](http://cambium.inria.fr/~fpottier/publis/pottier-unparsing-2024.pdf).

  The unparsing API requires linking with the library `MenhirCST`, and
  requires OCaml 4.08.

* Attributes can now be attached with a production. (In previous versions of
  Menhir, attributes could be attached only with a symbol, with a specific
  occurrence of a symbol in the right-hand side of a production, or with the
  whole grammar.) This is achieved by letting one or more attributes appear
  immediately after the semantic action.

  During the two grammar transformation phases (expansion of parameterized
  nonterminal symbols and elimination of `%inline` nonterminal symbols), the
  `[@name]` attributes attached with productions receive special treatment,
  so as to allow each production to receive a unique name.

* Minor additions in `MenhirSdk`:

  + The functions `hash`, `equal`, and `compare` appear in the signature
    `INDEXED`, so this signature now conforms with the standard signatures
    `HashedType` and `OrderedType`.

  + The submodule `Symbol` appears in the signature `GRAMMAR`.
    Thus, the type `Symbol.t` is now synonymous with `symbol`,
    and the function `Symbol.name` is now synonymous with `symbol_name`.
    The submodule `Symbol` contains the new functions `hash`, `equal`,
    and `compare`.

  + The functor `Cmly_read.FromString` appears. This functor allows decoding
    a `.cmly` file whose content is stored in a string.

* Minor changes in `MenhirSdk`:

  + In the signature `GRAMMAR`, the function `Production.attributes` now
    returns the attributes of the production itself. It used to return the
    attributes of the nonterminal symbol that forms the left-hand side of the
    production. The previous behavior of this function can be obtained by
    writing `Nonterminal.attributes (Production.lhs prod)`.

* Internal changes in `MenhirLib`:

  + The functions `lhs`, `maybe_shift_t` and `may_reduce_prod` appear
    in the signature `EngineTypes.TABLE`.

## 2023/06/08

* The new command line switch `--dump-menhirLib <directory>` causes the source
  files `menhirLib.ml` and `menhirLib.mli` to be created in the designated
  directory. This command can be useful to users with special needs who wish
  to use `menhirLib` but do not want to rely on it being installed somewhere
  in the file system. (Contributed by Nicolás Ojeda Bär.)

* Changes in the public API of the library `MenhirSdk`.
  (Contributed by Frédéric Bour.)

  + The function `Lr1.reductions`,
    whose type is `t -> (terminal * production list) list`,
    is still present but is now deprecated.
    The function `Lr1.get_reductions`,
    whose type is `t -> (terminal * production) list`,
    should be used instead.
    The library offers a view of the automaton after conflict resolution,
    so, for each token, at most one production can be reduced.

  + The function `Lr1.default_reduction : Lr1.t -> production option`
    appears. This function indicates which states have a default reduction.

  + The function `Cmly_read.read_channel` appears.

  + The module `Cmly_read.Lift` appears.

* The new experimental flag `--specialize-token` causes the code back-end
  to perform code specialization so as to guarantee that each token is
  examined exactly once (thus never more than once) by the parser. This
  causes an increase in code size and does not (yet) allow a performance
  increase. This feature is independent of the choice between `-O 0`,
  `-O 1` and `-O 2`. It may disappear in the future.

* Inconsistent type definitions used to be produced when `--only-tokens` and
  `--inspection` were passed on the command line. The type `terminal` was
  defined at the toplevel, whereas it should always be defined inside the
  submodule `MenhirInterpreter`. (Reported and fixed by Frédéric Bour.)

* Malformed code and type definitions used to be produced when
  `--external-tokens` and `--inspection` were passed on the command line.
  Fixed. (Reported by Maxime Dénès.)

* Enable OCaml warning 39 (unused rec flag) in the OCaml code produced
  by Menhir's code back-end. Menhir now carefully emits `let` instead
  of `let rec` when a function is not recursive.

## 2023/04/15

* When using the code back-end, the default optimization level is now `-O 1`
  instead of `-O 2`. Some users reported that `-O 2` is too aggressive and
  can cause a blow-up in the size of the code.

* Tweak the code for compatibility with OCaml 5.1. (Contributed by
  Florian Angeletti.)

* The new function `MenhirLib.LexerUtil.tabulate` makes it easy to run
  the lexer and parser in two separate phases. This can be useful when
  one wishes to benchmark them separately.

* To use the interpreter and print a concrete syntax tree, it used to be
  necessary to pass both `--interpret` and `--interpret-show-cst`. It is
  now sufficient to pass just `--interpret-show-cst`. (If both are passed,
  then only the last one is obeyed.) This fixes the assertion failure that
  would be observed when `--interpret-show-cst` alone was used.
  (Reported by Reed Mullanix.)

## 2022/02/10

* In the new code back-end, every semantic action in the generated code is now
  annotated with its result type. This should allow type-directed
  disambiguation to work (in most cases) inside the semantic actions.
  (Type-directed disambiguation works in the ancient code back-end and in the
  table back-end, but is broken in the new code back-end in version
  2021/12/30.)

* Fix an assertion failure that would occur when a point-free semantic action
  `<A>` was used in a production that binds zero identifiers. (Reported by
  Romain Calascibetta, fixed by Frédéric Bour.)

* Fix an assertion failure in `menhir --list-errors` that would occur when a
  state was unreachable due to conflict resolution. (Reported by Enrico Tassi,
  fixed by Frédéric Bour.)

* Fix the description of the differences between the *legacy* error-handling
  strategy and the *simplified* strategy in the change log (below). The
  previous description incorrectly claimed that there is no difference between
  these strategies when the grammar obeys the restrictions imposed by the
  simplified strategy. This is not true. (Reported by Andreas Abel.)

* Fix `menhir --interpret` so as to allow either `--strategy legacy` or
  `--strategy simplified`, as desired by the user. This possibility had
  been inadvertently removed in 2021/12/30.

## 2021/12/30

* The code back-end has been rewritten from the ground up by Émile Trotignon
  and François Pottier, and now produces efficient and **well-typed** OCaml
  code. The infamous `Obj.magic` is not used any more.

  The table back-end and the Coq back-end are unaffected by this change.

  The main side effects of this change are as follows:

  - The code back-end now needs type information. This means that
    *either* Menhir's type inference mechanism must be enabled
             (the easiest way of enabling it is to use Menhir via `dune`
              and to check that the `dune-project` file says
              `(using menhir 2.0)` or later)
    *or* the type of every nonterminal symbol must be
         explicitly given via a `%type` declaration.

  - The code back-end no longer allows the type of any symbol to be an
    open polymorphic variant type, such as ```[> `A ]```. As a workaround,
    we suggest using a closed polymorphic variant instead.

  - The code back-end now adheres to the *simplified* error-handling strategy,
    as opposed to the *legacy* strategy.

    For grammars that do *not* use the `error` token, this makes no difference.

    The simplified strategy makes the following requirement: the `error` token
    should always appear at the end of a production, whose semantic action
    should abort the parser by raising an exception. So, under the simplified
    strategy, not all grammars are accepted. Furthermore, even a grammar that
    obeys this requirement can behave differently under the legacy strategy
    and under the simplified strategy. Under the legacy strategy, the parser
    can discard items off the parser's stack before shifting the `error`
    token; under the simplified strategy, it cannot. To give an example,
    assume the grammar contains the definition `foo: A B | error`, and assume
    that the input is `A C`. An error is detected after `A` has been shifted.
    The next token in the input stream, which is `C`, is conceptually replaced
    with an `error` token. In the legacy strategy, `A` is discarded from the
    parser's stack and the production `foo: error` can then be reduced. In the
    simplified strategy, `A` is not discarded, and the parser aborts by
    raising an exception. Changing the grammar to `foo: A B | A error | error`
    should allow it to work in the same way under both strategies.

    A grammar that needs the `legacy` strategy cannot be compiled by the new
    code back-end. As a workaround, it is possible to switch to the table
    back-end (using `--table --strategy legacy`) or to the ancient code
    back-end (using `--code-ancient`). **In the long run, we recommend
    abandoning the use of the `error` token**. Support for the `error` token
    may be removed entirely at some point in the future.

  The original code back-end, which has been around since the early days of
  Menhir (2005), temporarily remains available (using `--code-ancient`). It
  will be removed at some point in the future.

  The new code back-end offers several levels of optimization, which remain
  undocumented and are subject to change in the future. At present, the main
  levels are roughly as follows:

  - `-O 0 --represent-everything` uses a uniform representation of the stack
    and produces straightforward code.
  - `-O 0` uses a non-uniform representation of the stack; some stack cells
    have fewer fields; some stack cells disappear altogether.
  - `-O 1` reduces memory traffic by moving `PUSH` operations so that they
    meet `POP` operations and cancel out.
  - `-O 2` optimizes the reduction of unit productions (that is, productions
    whose right-hand side has length 1) by performing a limited amount of
    code specialization.

  The default level of optimization is the maximum level, `-O 2`.

* The new command line switch `--exn-carries-state` causes the exception
  `Error` to carry an integer parameter: `exception Error of int`. When the
  parser detects a syntax error, the number of the current state is reported
  in this way. This allows the caller to select a suitable syntax error
  message, along the lines described in the manual
  (see *Error handling: the new way*)
  This command line switch is currently supported by the code
  back-end only.

* The `$syntaxerror` keyword is no longer supported.

* Document the trick of wrapping module aliases in `open struct ... end`,
  like this: `%{ open struct module alias M = MyLongModuleName end %}`.
  This allows you to use the short name `M` in your grammar, but forces
  OCaml to infer types that refer to the long name `MyLongModuleName`.
  (Suggested by Frédéric Bour.)

## 2021/11/28

* Revert a change in version 2021/11/25 regarding the printing of universally
  quantified variables in type schemes. (They were explicitly printed in
  2021/11/25; they are omitted again.) Printing these universal quantifiers
  would trigger a type-checker bug in OCaml between versions 4.07 and 4.10.

* Avoid using the expression `raise Not_found` in the mock `.ml` files
  generated by `menhir --infer` for type inference purposes. The use
  of this expression can trigger deprecation warnings in some projects.

* Update the `man` page.

## 2021/11/25

* The command `menhir --list-errors` has been sped up by a factor of up
  to x100, and requires up to x1000 less memory, thanks to a new LR(1)
  reachability algorithm, which has been designed and implemented by
  Frédéric Bour. This algorithm is described in the paper
  [Faster Reachability Analysis for LR(1) Parsers](http://cambium.inria.fr/~fpottier/publis/bour-pottier-reachability.pdf)
  by Frédéric Bour and François Pottier.

* Better document the restricted way in which the `error` token must be
  used when using `--strategy simplified`. Menhir now checks that this
  token is used only at the end of a production, and warns if this is
  not the case. (Better yet, our suggestion is to not use the `error`
  token at all!)

* The `$syntaxerror` keyword is now forbidden when using
  `--strategy simplified`. This keyword will be entirely removed
  in the next release. Incidentally, we have just found out that
  it behaves differently under the code back-end and under the
  table back-end.

* Disable OCaml warning 39 (unused rec flag) in the OCaml code produced
  by Menhir's code back-end. This does not affect the table back-end.
  (Reported by Armaël Guéneau.)

* Fix a bug in `--random-*` which could cause Menhir to diverge if the
  grammar uses the `error` token.

* Warn if a terminal symbol is named `Error`. This creates a name clash
  in the public interface of the generated parser.

* Menhir now requires OCaml 4.03.0 (instead of 4.02.3)
  and Dune 2.8.0 (instead of 2.0.0).

## 2021/10/12

* Fix a bug in the code back-end which, in some rare cases, could lead to
  computing an incorrect position. (The table back-end was not affected.)
  A necessary (but not sufficient) condition for the bug to appear was to
  mark an epsilon production as `%inline`.

## 2021/09/29

* Fix a problem (introduced on 2021/09/28) that would cause
  OCaml warning 41 to be triggered in the generated code.

## 2021/09/28

* Coq back-end and `coq-menhirlib`: avoid the new warnings in Coq 8.14.

* The new command line switches `--random-*` can be used to randomly generate
  sentences that are valid with respect to the grammar. If the grammar is in
  the class LR(1) (that is, if it has no conflicts at all), then the generated
  sentences are also accepted by the automaton.

* At verbosity level `-lg 2`, for each nonterminal symbol `N`, display the
  maximal length of a sentence (composed of terminal symbols) generated by
  `N`.

* Fix a bug in `--only-preprocess` that would cause `%on_error_reduce`
  declarations involving parameterized symbols to be printed in an incorrect
  manner.

* Fix a name collision that would cause the code back-end to produce ill-typed
  code if a token was named `Error`.

## 2021/04/19

* Mention the demo [coq-minicalc](demos/coq-minicalc) in the manual.

* Parsers generated with the Coq mode now have support for non-certified basic
  error reporting without an additional parser. This is supported thanks to an
  extension of the return type `parse_result` in the `coq-menhirlib` library and
  thanks to the new generated helper function `Aut.N_of_state`. See the new
  demo [coq-syntax-errors](demos/coq-syntax-errors) and the updated manual for
  more details. (Contributed by Brian Ward.)

## 2021/03/10

* Menhir now detects and rejects grammars that have a cycle and grammars that
  exhibit hidden left recursion. A grammar has a cycle when a nonterminal
  symbol `A` expands (in one or more steps) to itself. This implies that the
  grammar is ambiguous. A grammar has hidden left recursion when a nonterminal
  symbol `A` expands (in one step) to `B beta`, where `B` expands (in zero or
  more steps) to nothing and `beta` expands (in zero or more steps) to `A
  ...`. This implies that the grammar is not in the class *LR(k)* for any
  value of *k*. Both of these anomalies create a shift/reduce conflict which,
  if resolved in favor of reduction, leads to a nonterminating parser.

* Disallow the escape sequence `\n` in a token alias. It was allowed by
  mistake. Disallowing it ensures that the `## Concrete syntax:` comments
  generated as part of `.messages` files fit on a single line.

* Internal changes in the expansion of `%inline` symbols, eliminating certain
  useless variable renamings that would appear in semantic actions after
  expansion.

* Internal changes in the code back-end, eliminating certain useless bindings
  of variables to a unit value.

## 2020/12/16

* The new command line switch `--strategy <strategy>` allows choosing an error
  handling strategy between `legacy` and `simplified`. This matters only if
  the grammar uses the `error` token. The `legacy` strategy yields Menhir's
  traditional behavior. The `simplified` strategy should be preferred if the
  `error` token is used only to catch an error and stop. (In this restricted
  style, the `error` token always appears at the end of a production, whose
  semantic action raises an exception.)

## 2020/12/14

* The new command line switch `--require-aliases` causes Menhir to check
  that a token alias has been defined for every token.

* The escaped characters `\\`, `\'`, `\"`, `\n`, `\t`, `\b`, `\r`, `\ ` are
  now accepted in token aliases.

* If a token alias has been defined for every token, then, in every
  `.messages` file produced by Menhir, every sentence is now followed by its
  concrete syntax, in an auto-generated comment that begins with `## Concrete
  syntax: `. This feature relies on the assumption that the concrete syntax
  allows separating two tokens with a space character.

* The new command `--echo-errors-concrete` reads a `.messages` files and
  echoes every sentence, immediately followed with its `## Concrete syntax: `
  auto-generated comment.

* Update the demo `calc-syntax-errors` to show how to compile a parser
  simultaneously via the code back-end and via the table back-end, so as to
  obtain both optimal performance and good error messages.

* Rename the undocumented option `--graph` to `--reference-graph`.

* Add an undocumented option `--automaton-graph` which produces an
  (incomplete) graphical representation of the LR(1) automaton.

* At log level `--log-automaton 2`, Menhir now shows which states have a
  conflict between multiple `%on_error_reduce` declarations.

## 2020/12/01

* The module `MenhirLib.ErrorReports` is extended with new functions:
  `wrap_supplier`, `extract`, `sanitize`, `compress`, `shorten`, `expand`.

* The new module `MenhirLib.LexerUtil` offers a few functions that help
  reading a file, setting up a lexing buffer, printing source code positions,
  etc.

* The new demo `calc-syntax-errors` demonstrates how to produce customized
  syntax error messages. Here are examples of the messages that this little
  parser can produce:

  Incorrect Input | Error Message
  --------------- | -------------
  [calc01.in](demos/calc-syntax-errors/calc01.in) | [calc01.exp](demos/calc-syntax-errors/calc01.exp)
  [calc02.in](demos/calc-syntax-errors/calc02.in) | [calc02.exp](demos/calc-syntax-errors/calc02.exp)
  [calc03.in](demos/calc-syntax-errors/calc03.in) | [calc03.exp](demos/calc-syntax-errors/calc03.exp)
  [calc04.in](demos/calc-syntax-errors/calc04.in) | [calc04.exp](demos/calc-syntax-errors/calc04.exp)
  [calc05.in](demos/calc-syntax-errors/calc05.in) | [calc05.exp](demos/calc-syntax-errors/calc05.exp)
  [calc06.in](demos/calc-syntax-errors/calc06.in) | [calc06.exp](demos/calc-syntax-errors/calc06.exp)
  [calc07.in](demos/calc-syntax-errors/calc07.in) | [calc07.exp](demos/calc-syntax-errors/calc07.exp)

* The new command `--merge-errors` merges two `.messages` files. It can be
  useful when two or more users have independently produced partial
  `.messages` files and wish to combine their work.
  (Suggested by Gabriel Scherer and François Bobot.)

* The commands that read `.messages` files have been hardened so as to
  tolerate situations where a sentence mentions a nonexistent symbol or does
  not lead to an error state. When such a sentence is encountered, an error
  message is produced on the standard error channel; then, this sentence is
  ignored and processing continues. (As an exception, the command
  `--compile-errors` refuses to proceed in the presence of such sentences.)

## 2020/11/22

* The new command line switch `--dump-resolved` writes a description of the
  automaton to the file `.automaton.resolved` after all conflicts have been
  resolved and after extra reductions have been introduced. This file also
  shows which states have a default reduction.

* The command line switch `--dump` writes a description of the automaton to
  the file `.automaton` after benign conflicts have been silently resolved,
  but *before* severe conflicts are resolved and before extra reductions are
  introduced. (This behavior is unchanged.) The manner in which end-of-stream
  conflicts are displayed in this file has been improved.

* In the files `.automaton` and `.automaton.resolved`, the reduction table in
  each state is now presented in a much more compact and readable way.

* In the files `.automaton` and `.automaton.resolved`, the known suffix of the
  stack in each state is now explicitly shown. (Although it can be deduced
  from the LR(1) items, showing it helps.)

* Document the problem caused by placing a module alias declaration
  in an `.mly` file. (See *Questions and Answers* in the manual.)

* Turn off a costly internal well-formedness assertion.
  This allows a 30% speedup in the construction of large automata
  and in the conflict explanation process. (Reported by Joe.)

## 2020/06/24

* Fix a bug introduced on 2020/02/11 that causes all reduce/reduce conflicts
  to be mistakenly declared unexplainable, provided the grammar has at least
  62 terminal symbols. (Reported by Joe.)

## 2020/06/19

* Fix the suggestions printed by `--suggest-link-flags-byte` and
  `--suggest-link-flags-opt` so as to suggest `menhirLib.cma` or
  `menhirLib.cmxa` instead of `menhirLib.cmo` or `menhirLib.cmx`. This change
  should have been made on 2020/01/21, when we switched to automated
  installation via `opam` and `dune`.

## 2020/06/12

* When a semantic value is unused in a semantic action, the warning (or error)
  should now be correctly reported in the `.mly` file, not in a generated
  `.ml` file. (This works only when `--infer` is enabled, because we are lazy.
  If you use `dune`, this works out of the box.)

## 2020/05/25

* Fix a problem that could arise when an open polymorphic variant, such as
  ```[> `A ]```, was used in a `%type` or `%start` declaration. A type that
  was too general could possibly be inferred. This could in turn lead to an
  incorrect compilation of pattern matching and to a segmentation fault.
  (Problem reported by Joe.)

* Fix the static check that is performed prior to expanding the parameterized
  nonterminal symbols. The previous check was incorrect: it would sometimes
  accept a grammar whose expansion would diverge. (Fix by Yann Régis-Gianas.)

## 2020/02/11

* Re-implement Menhir's default algorithm for constructing LR(1) automata,
  namely Pager's algorithm. This closes issue #21 (reported by Andrej Bauer),
  a bug that would sometimes cause unexplainable conflicts to appear, because
  states were merged too aggressively. This also removes an unreported bug
  that would cause the automaton to have too many states, because states were
  *not* merged aggressively enough. In summary, the old and new construction
  algorithms differ: in many cases, the resulting automaton is unchanged, but
  in some cases, the automaton produced by the new algorithm may have slightly
  more or slightly fewer states.

* Re-implement Menhir's algorithm for constructing automata in `--no-pager`
  mode. In this (undocumented) mode, Menhir does not merge any states, but
  allows itself to redirect a transition from a state `s` to a *larger* state
  `s'`. This method yields an automaton whose states form a subset of the
  states of the canonical LR(1) automaton. It usually has significantly fewer
  states than the canonical automaton, and significantly more states than the
  automaton produced by Pager's algorithm. The new construction method removes
  an unreported bug that would cause the automaton to have too many states.
  The automaton produced by the new algorithm will usually have significantly
  fewer states than the automaton produced by the previous algorithm.

* Re-implement Menhir's algorithms for constructing automata in `--lalr` and
  `--canonical` modes. The previous algorithms were correct, as far as we
  know, so the output of the new algorithms is the same, up to a possible
  renumbering of the states. The new algorithms are slightly faster.

* Increase the maximum length of a production, which used to be 127,
  up to 1023. Display a polite error message if this length is exceeded.
  (Problem reported by Andreas Abel.)

* The new switch `--timings-to <filename>` causes internal timing
  information to be written to the file `<filename>`.

* A version of the library `fix` is now vendored (included) inside Menhir.
  This should have no impact for end users, but implies that `dune` 2.2.0
  or later is required.

## 2020/01/21

* There used to be a distinction between two slightly different ways of
  installing Menhir, namely with and without `ocamlfind`. This distinction
  disappears. The command line switch `--suggest-ocamlfind` is deprecated
  and causes Menhir to print `false`.

* Menhir is now built and installed by `dune`. This should make life easier
  for Menhir's developers: in particular, `make test` and `make speed` can be
  run straight away and do not require installing Menhir first. This should
  also make compilation much faster on multi-core machines. (Contributed by
  Nicolás Ojeda Bär, to whom many thanks are due.)

## 2019/09/24

* Build Menhir's standard library into the Menhir executable instead of
  storing it in a separate file `standard.mly`. This removes the need to
  hardcode the path to this file into the Menhir executable. This also removes
  the need for the command line switch `--stdlib`, which remains supported but
  is now ignored, and for the environment variable `$MENHIR_STDLIB`, which is
  now ignored. A positive side effect of this change is that the full path of
  the file `standard.mly` no longer appears in generated parsers; this removes
  a source of spurious variation. (Suggested and implemented by Nicolás Ojeda
  Bär.)

## 2019/06/20

* When compiled with OCaml 4.02.3, Menhir could produce OCaml code
  containing invalid string literals. This was due to a problem in
  `String.escaped`. Fixed. (Reported by ELLIOTCABLE.)

## 2019/06/13

* Relax the syntax of point-free actions to allow `< >` (with arbitrary
  whitespace inside the angle brackets) instead of just `<>`.
  (Suggested by Lélio Brun.)

* When a cycle of `%inline` nonterminal symbols is encountered,
  the error message now shows the entire cycle,
  as opposed to just one symbol that participates in the cycle.

* Fix the treatment of the `error` token when printing the grammar for
  `ocamlyacc`. Its semantic value must not be referred to; a unit value
  must be used instead. The switch `--only-preprocess-for-ocamlyacc`
  remains undocumented. (Reported by kris.)

* Coq back-end: multiple changes to stay up-to-date with respect to
  `coq-menhirlib`. See [coq-menhirlib/CHANGES.md](coq-menhirlib/CHANGES.md).

* Coq back-end: the generated parser now contains a dedicated inductive
  type for tokens. This removes the need for `Obj.magic` in client code
  when the parser is used via extraction.

* Coq back-end: the generated parser checks that the version of
  MenhirLib matches. This check can be disabled with
  `--coq-no-version-check`.

* Coq back-end: the fuel parameter is now given as the *logarithm* of
  the maximum number of steps to perform. Therefore, using e.g., 50
  makes sure we will not run out of fuel in any reasonable
  computation time.

## 2018/11/13

* In `.mly` files, a new syntax for rules has been introduced, which is
  slightly more pleasant than the old syntax. (A rule is the definition of a
  nonterminal symbol.) The old syntax remains available; the user chooses
  between the two syntaxes on a per-rule basis. The new syntax is fully
  documented in the manual;
  [a brief summary of the differences](doc/new-rule-syntax-summary.md)
  with respect to the old syntax is also available.
  **The new syntax is considered experimental**
  and is subject to change in the near future.

* In the Coq back-end, avoid pattern-matching at type `int31`,
  which will disappear in future versions of Coq.
  Instead, convert `int31` to `Z`, and perform pattern matching in `Z`.
  (Reported by Vincent Laporte, implemented by Jacques-Henri Jourdan.)

* Implement a more economical renaming scheme for OCaml variables
  during the elimination of `%inline` symbols. This leads to slightly
  more readable code (more reasonable variables names, fewer `let`
  bindings).

* Another attempt at removing all trailing spaces in auto-generated
  `.messages` files. (I hope I got it right, this time.)

## 2018/10/26

* A new syntactic sugar facility, "token aliases", has been added.
  The declaration of a terminal symbol may also declare an alias,
  which takes the form of a name between double quotes, as in
  `%token PLUS "+"`.
  Thereafter, `"+"` may be used freely in place of `PLUS` throughout
  the grammar. This makes it slightly easier to read grammars.
  (Contributed by Perry E. Metzger.)

* Until today, the semicolon character `;` was insignificant: it was
  considered as whitespace by Menhir. It is now accepted only in a
  few specific places, namely: after a declaration; after a rule;
  after a producer. If Menhir suddenly complains about a semicolon,
  just remove it. This change is being made in preparation for
  further syntactic changes.

* New flag `--no-dollars`, which disallows the use of `$i` in semantic actions.
  The default behavior remains to allow the use of `$i`.

* When generating OCaml code, include all record fields in record patterns,
  even when bound to a wildcard pattern. Thus, avoid triggering OCaml's
  warning 9.

## 2018/10/06

* Standard library: add `rev`, `flatten`, `append`.
  Add a link from the manual to `standard.mly` in the repository.

* Update the manual to explain how to use `dune` and `menhir` together.

* Install `.cmxs` files for menhirLib and menhirSdk.

* Remove all references to `Pervasives` in the generated OCaml code.
  These references were infrequent anyway,
  and `Pervasives` is about to be deprecated in OCaml 4.08, it seems.

* In `--interpret` mode, print `Ready!` once ready to accept input.

* At verbosity level `-lg 2`, for each nonterminal symbol `N`, display
  a sentence (composed of terminal symbols) of minimal length generated
  by `N`.

* When writing a `.cmly` file, open it in binary mode. This should
  eliminate the failure that was observed under Windows:
  `output_value: not a binary channel`. (Reported by Bryan Phelps.
  A fix was present in the `mingw` patches for Menhir.)

* Change the logic used in the root `Makefile` to deal with Unix and Windows
  in a uniform way. (Also inspired by the `mingw` patches for Menhir.)

* Coq back-end: add a few newlines in the generated file for readability.
  (Suggested by Bernhard Schommer.)

* Remove the trailing space at the end of every sentence in
  auto-generated `.messages` files. (Suggested by Xavier Leroy.)

## 2018/09/05

* When `--explain` is enabled, always create a fresh `.conflicts` file
  (wiping out any pre-existing file), even if there are in fact no conflicts.
  This should avoid confusion with outdated `.conflicts` files.

* Fix several bugs in the treatment of `--strict`. No `.conflicts` file
  was created when `--strict` and `--explain` were both enabled. Also,
  some warnings were not properly turned into errors by `--strict`.

## 2018/07/04

* Update the `man` page, which was woefully out of date.

## 2018/07/03

* New location keywords.
  `$loc` is sugar for the pair `($startpos, $endpos)`.
  `$loc(x)` is sugar for the pair `($startpos(x), $endpos(x))`.
  `$sloc` is sugar for the pair `($symbolstartpos, $endpos)`.
  (Contributed by Nicolás Ojeda Bär.)

## 2018/06/08

* Add two new parameterized nonterminal symbols, `endrule(X)` and `midrule(X)`,
  to the standard library. These symbols have been available since 2015/02/11
  under the names `anonymous(X)` and `embedded(X)`, but were not yet documented.
  `endrule(X)` and `midrule(X)` are now documented,
  while `anonymous(X)` and `embedded(X)` remain present but are deprecated.

## 2018/05/30

* In `--coq` mode, Menhir now produces references to `MenhirLib.Grammar`
  instead of just `Grammar`, and similarly for all modules in Menhir's support
  library.

* New command line option `--coq-lib-no-path` to suppress the above behavior
  and retain the previous (now-deprecated) behavior, that is, produce
  unqualified references the modules in Menhir's support library.

* New command line option `--coq-lib-path <path>` to indicate under what name
  (or path) the support library has been installed. Its default value is
  `MenhirLib`.

## 2018/05/23

* New commands `--infer-write-query`, `--infer-read-reply`, and
  `--infer-protocol-supported`. These commands remove the need for Menhir to
  invoke `ocamlc` and `ocamldep` behind the scenes, and make it easier to
  write correct build rules for Menhir projects. The command line options
  `--infer`, `--raw-depend` and `--depend` remain supported, but are no longer
  preferred. (Suggested by Fabrice Le Fessant.)

* Remove the warning that was issued when `%inline` was used but `--infer` was
  turned off. Most people should use a build system that knows how to enable
  OCaml type inference, such as `ocamlbuild` or `dune`.

* New HTML rendering of the manual, available both online and as part of
  Menhir's installation. (Implemented by Gabriel Scherer.)

## 2017/12/22

* Add a flag `--unused-precedence-levels` to suppress all warnings about
  useless `%left`, `%right`, `%nonassoc` and `%prec` declarations.
  (Suggested by Zachary Tatlock.)

## 2017/12/06

* Fix the termination test that takes place before parameterized symbols are
  expanded away. The previous test was both unsound (it would accept grammars
  whose expansion did not terminate) and incomplete (it would reject grammars
  whose expansion did terminate). The new test is believed to be sound and
  complete. (Thanks to Martin Bodin for prompting us to look into this issue.)

## 2017/11/12

* Documentation: clarify the fact that `%type` declarations should carry types
  whose meaning does not depend on the headers `%{ ... %}`.

## 2017/10/13

* Remove the OCaml version check at installation time, for greater simplicity,
  and because for some reason it did not work properly under Cygwin.
  (Reported by Andrew Appel.)

## 2017/09/26

* `Makefile` fix: when determining whether the suffix `.exe` should be used,
  one should test whether the OS is Windows,
  not whether the compiler is MSVC.
  (Suggested by Jonathan Protzenko.)

## 2017/07/12

* Include the LaTeX sources of the manual in the official `.tar.gz` archive.
  This should allow the manual to be included as part of the Debian package.

* Mention [Obelisk](https://github.com/Lelio-Brun/Obelisk),
  a pretty-printer for `.mly` files, in the manual.

## 2017/06/07

* Removed an undeclared dependency of MenhirSdk on Unix. (Reported and fixed
  by Frédéric Bour.)

## 2017/05/09

* Menhir now always places OCaml line number directives in the generated `.ml`
  file. (Until now, this was done only when `--infer` was off.) Thus, if a
  semantic action contains an `assert` statement, the file name and line
  number information carried by the `Assert_failure` exception should now be
  correct. (Reported by Helmut Brandl.)

## 2017/04/18

* Changed Menhir's license from QPL to GPLv2.
  MenhirLib remains under LGPLv2, with a linking exception.

* Moved the repository to
  [gitlab.inria.fr](https://gitlab.inria.fr/fpottier/menhir/).

* Introduced a new command line switch, `--cmly`, which causes Menhir to
  create a `.cmly` file, containing a description of the grammar and
  automaton. (Suggested by Frédéric Bour.)

* Introduced a new library, MenhirSdk, which allows reading a `.cmly` file.
  The purpose of this library is to allow external tools to take advantage
  of the work performed by Menhir's front-end. (Suggested by Frédéric Bour.)

* Introduced new syntax for attributes in a `.mly` file. Attributes are
  ignored by Menhir's back-ends, but are written to `.cmly` files, thus
  can be exploited by external tools via MenhirSdk. (Suggested by Frédéric Bour.)

* The definition of a `%public` nonterminal symbol can now be split into several
  parts within a single `.mly` file. (This used to be permitted only over
  multiple `.mly` files.) (Suggested by Frédéric Bour.)

* New functions in the incremental API:
  `shifts`, `acceptable`, `current_state_number`.

* New functions in the incremental API and inspection API:
  `top`, `pop`, `pop_many`, `get`, `equal`,
  `force_reduction`, `feed`, `input_needed`,
  `state_has_default_reduction`,
  `production_index`, `find_production`.
  (Suggested by Frédéric Bour.)

* New module `MenhirLib.ErrorReports`. This module is supposed to offer
  auxiliary functions that help produce good syntax error messages.
  This module does not yet contain much functionality and is expected
  to evolve in the future.

* Incompatible change in the incremental API: the type `env` becomes `'a env`.

* Incompatible change in the incremental API: the function
  `has_default_reduction` is renamed `env_has_default_reduction`.

* The type `stack` and the function `stack` in the incremental API are
  deprecated. The new functions `top` and `pop` can be used instead to
  inspect the parser's stack. The module `MenhirLib.General` is deprecated
  as well. Deprecated functionality will be removed in the future.

* Incompatible change in the incremental API: the type of the function
  `print_stack` in the result signature of the functor
  `MenhirLib.Printers.Make` changes to `'a env -> unit`.
   (Anyway, as of now, `MenhirLib.Printers` remains undocumented.)

* Improved the syntax error message that is displayed when a `.mly` file
  is incorrect: the previous and next token are shown.

* Fixed a bug where the module name `Basics` was shadowed (that is, if the user's
  project happened to contain a toplevel module by this name, then it could not
  be referred to from a `.mly` file). (Reported by François Thiré.)

## 2017/01/01

* Add `$MENHIR_STDLIB` as a way of controlling where Menhir looks for the file
  `standard.mly`. This environment variable overrides the installation-time
  default setting, and is itself overridden by the `--stdlib` command line
  switch. (Requested by Jonathan Protzenko.)

* `Makefile` fix: filter out `'\r'` in the output of `menhir --suggest-ocamlfind`,
  so that the `Makefile` works when Menhir is compiled as a Windows executable.
  (Suggested by Jonathan Protzenko.)

## 2016/12/01

* Updated the Coq back-end for compatibility with Coq 8.6.
  (Jacques-Henri Jourdan.)

## 2016/11/15

* Fix in `--only-preprocess-for-ocamlyacc` mode: avoid printing newline characters
  inside a `%type` declaration, as this is forbidden by `ocamlyacc`. (Reported by
  Kenji Maillard.)
* Fix in `--only-preprocess-for-ocamlyacc` mode: avoid variable capture caused by
  `ocamlyacc` internally translating `$i` to `_i`. (Reported by Kenji Maillard.)

## 2016/09/01

* New command line switch `--only-preprocess-for-ocamlyacc`, supposed to print the
  grammar in a form that `ocamlyacc` can accept. As of now, this feature is
  incomplete (in particular, support for Menhir's position keywords is missing),
  untested, and undocumented. It could be removed in the future.

## 2016/08/26

* Fixes in the output of `--only-preprocess`:
  * The order of productions is now preserved.
      (It was not. This matters if there are reduce/reduce conflicts.)
  * `%parameter` directives are now printed. (They were not).
  * `%on_error_reduce` directives are now printed. (They were not.)

## 2016/08/25

* `Makefile` fix, undoing a change made on 2016/03/03, which caused installation
  to fail under (some versions of?) Windows where dynamic linking is not
  supported. (Reported by Andrew Appel.)

## 2016/08/05

* `%on_error_reduce` declarations now have implicit priority levels, so as to
  tell Menhir what to do when two such declarations are applicable.
  Also, the well-formedness checks on `%type` and `%on_error_reduce` declarations
  have been reinforced.

## 2016/06/23

* A small change in the generated code (both in the code and table back-ends) so
  as to avoid OCaml's warning 41. The warning would arise (when compiling a
  generated parser with OCaml 4.03) because Menhir's exception `Error` has the
  same name as the data constructor `Error` in OCaml's pervasive library.
  (Reported by Bernhard Schommer.)

## 2016/05/18

* Anonymous rules now work also when used inside a parameterized rule.
  (This did not work until now.) When an anonymous rule is hoisted out
  of a parameterized rule, it may itself become parameterized. Menhir
  parameterizes it only over the parameters that it actually needs.

## 2016/05/04

* In the Coq back-end, split the largest definitions into smaller
  ones. This circumvents a limitation of vm_compute on 32 bit
  machines. This also enables us to perform sharing between
  definitions, so that the generated files are much smaller.

## 2016/04/10

* When printing a grammar (which is done by the `--only-preprocess` options),
  remove the leading bar `|`, for compatibility with `yacc` and `bison`.

## 2016/03/11

* In the code back-end, generate type annotations when extracting a semantic
  value out of the stack. When working with a semantic value of some function
  type, OCaml would incorrectly warn that this function does not use its
  argument. This warning should now be gone.

## 2016/03/03

* Makefile changes, so as to support `ocamlbuild` 4.03, which seems to have
  stricter hygiene rules than previous versions.

## 2015/12/30

* Prevented an incorrect installation that would take place if `USE_OCAMLFIND`
  was given during `make all` but not during `make install`. Added a command
  line directive `--suggest-ocamlfind`.

## 2015/11/11

* Fixed a severe bug in Menhir 20151110 which (when using the code back-end)
  could cause a generated parser to crash. Thanks to ygrek for reporting the
  bug.

* The code produced by version `XXXXXXXX` of `menhir --table` can now be linked only
  against a matching version of MenhirLib. If an incorrect version of MenhirLib
  is installed, the OCaml compiler should complain that
  `MenhirLib.StaticVersion.require_XXXXXXXX` is undefined.

## 2015/11/10

* Optimized the computation of `$symbolstartpos`, based on a couple of assumptions
  about the lexer. (See the manual.)

## 2015/11/04

* Modified the treatment of `%inline` so that the positions that are computed are
  the same, regardless of whether `%inline` is used. This property did not hold
  until now. It now does. Of course, this means that the positions computed by
  the new Menhir are not the same as those computed by older versions of Menhir.

* Fixed a bug in the treatment of `%inline` that would lead to an incorrect
  position being computed when the caller and callee had a variable by the
  same name.

* Modified Menhir so as to compute the start and end positions in the exact same
  way as `ocamlyacc`. (There used to be a difference in the treatment of epsilon
  productions.) Of course, this means that the positions computed by the new
  Menhir are not the same as those computed by older versions of Menhir. Added
  the keyword `$symbolstartpos` so as to simulate `Parsing.symbol_start_pos()`
  in the `ocamlyacc` world. The keyword `$startpos` sometimes produces a position
  that is too far off to the left; `$symbolstartpos` produces a more accurate
  position.

* Incompatible change of the incremental API: instead of a unit argument, the
  entry points (which are named after the start symbols) now require an initial
  position, which typically should be `lexbuf.lex_curr_p`.

## 2015/11/03

* Fix-fix-and-re-fix the `Makefile` in an attempt to allow installation under
  opam/Windows. Thanks to Daniel Weil for patient explanations and testing.

## 2015/10/29

* MenhirLib is now installed in both binary and source forms.
  `menhir --suggest-menhirLib` reports where MenhirLib is installed.
  This can be used to retrieve a snapshot of MenhirLib in source form
  and include it in your project (if you wish to use `--table` mode, yet
  do not wish to have a dependency on MenhirLib).

## 2015/10/26

* Allow `--list-errors` to work on 32-bit machines (with low hard limits).
  This should fix a problem whereby the 2015/10/23 release could not
  bootstrap on a 32-bit machine.

## 2015/10/23

* New declaration `%on_error_reduce foo`, where `foo` is a nonterminal symbol.
  This modifies the automaton as follows. In every state where a production of
  the form `foo -> ...` is ready to be reduced, every error action is replaced
  with a reduction of this production. (If there is a conflict between several
  productions that could be reduced in this manner, nothing is done.) This does
  not affect the language that is accepted by the automaton, but delays the
  detection of an error: more reductions take place before the error is
  detected.

* Fixed a bug whereby Menhir would warn about a useless `%prec` declaration,
  even though it was useful. This would happen when the declaration was
  duplicated (by inlining or by macro-expansion) and some but not all of
  the copies were useful.

* Added `has_default_reduction` to the incremental API.

* Modified the meaning of `--canonical` to allow default reductions to take
  place. This implies no loss of precision in terms of lookahead sets,
  and should allow gaining more contextual information when a syntax
  error is encountered. (It should also lead to a smaller automaton.)

* A brand new set of tools to work on syntax errors.
* New command `--list-errors`, which produces a list of input sentences which
  are representative of all possible syntax errors. (Costly.)
* New command `--interpret-error`, which confirms that one particular input
  sentence ends in a syntax error, and prints the number of the state in
  which this error occurs.
* New command `--compile-errors`, which compiles a list of erroneous sentences
  (together with error messages) to OCaml code.
* New command `--compare-errors`, which compares two lists of erroneous sentences
  to check if they cover the same error states.
* New command `--update-errors`, which updates the auto-generated comments in
  a list of erroneous sentences.
* New command `--echo-errors`, which removes all comments and messages from
  a list of erroneous sentences, and echoes just the sentences.

## 2015/10/16

* Additions to the incremental API.
  * A `supplier` is a function that produces tokens on demand.
  * `lexer_lexbuf_to_supplier` turns a lexer and a lexbuf into a supplier.
  * `loop` is a ready-made made main parsing loop.
  * `loop_handle` is a variant that lets the user do her own error handling.
  * `loop_handle_undo` is a variant that additionally allows undoing the last
    few "spurious" reductions.
  * `number` maps a state of the LR(1) automaton to its number.

* Incompatible change of the incremental API: renamed the type `'a result`
  to `'a checkpoint`. This is a better name anyway, and should help avoid
  confusion with the type `'a result` introduced in OCaml 4.03.

## 2015/10/12

* Avoid using `$(shell pwd)` in `Makefile`, for better Windows compatibility.

## 2015/10/05

* Fixed a bug where inconsistent OCaml code was generated when `--table`
  and `--external-tokens` were used together. (Reported by Darin Morrison.)

* In `--infer` mode, leave the `.ml` file around (instead of removing it) if
  `ocamlc` fails, so we have a chance to understand what's wrong.

## 2015/09/21

* Re-established some error messages concerning the mis-use of `$i` which
  had disappeared on 2015/06/29.

## 2015/09/11

* Fixed the mysterious message that would appear when a nonterminal symbol
  begins with an uppercase letter and `--infer` is turned on. Clarified the
  documentation to indicate that a (non-start) nonterminal symbol can begin
  with an uppercase letter, but this is not recommended.

## 2015/08/27

* New option `--inspection` (added last January, documented only now). This
  generates an inspection API which allows inspecting the automaton's stack,
  among other things. This API can in principle be used to write custom code
  for error reporting, error recovery, etc. It is not yet mature and may
  change in the future.

## 2015/07/20

* Added the command line options `--unused-token <symbol>` and `--unused-tokens`.

## 2015/06/29

* Changed the treatment of the positional keywords `$i`. They are now
  rewritten into variables of the form `_i` where `i` is an integer.
  Users are advised not to use variables of this form inside semantic
  actions.

## 2015/02/11

* Added support for anonymous rules. This allows writing, e.g.,
  `list(e = expression SEMI { e })`
  whereas previously one should have written
  `list(terminated(e, SEMI))`.

## 2015/02/09

* Moved all of the demos to `ocamlbuild` (instead of `make`).

## 2015/01/18

* Incompatible change of the incremental API.
  The incremental API now exposes shift events too.

## 2015/01/16

* Fixed a couple bugs in `Makefile` and `src/Makefile` which would cause
  compilation and installation to fail with `TARGET=byte`. (Reported
  by Jérémie Courrèges-Anglas and Daniel Dickman.)

## 2015/01/01

* Incompatible change of the incremental API.
  The entry point `main_incremental` is now named `Incremental.main`.

## 2014/12/29

* Incompatible change of the incremental API.
  * The API now exposes reduction events.
  * The type `'a result` is now private.
  * The type `env` is no longer parameterized.
  * `handle` is renamed to `resume`.
  * `offer` and `resume` now expect a result, not an environment.

## 2014/12/22

* Documented the Coq back-end (designed and implemented by Jacques-Henri Jourdan).

## 2014/12/15

* New incremental API (in `--table` mode only), inspired by Frédéric Bour.

## 2014/12/11

* Menhir now reports an error if one of the start symbols produces
  either the empty language or the singleton language {epsilon}.

* Although some people out there actually define a start symbol that recognizes
  {epsilon} (and use it as a way of initializing or re-initializing some global
  state), this is considered bad style. Furthermore, by ruling out this case, we
  are able to simplify the table back-end a little bit.

## 2014/12/12

* A speed improvement in the code back-end.

## 2014/12/08

* Menhir now requires OCaml 4.02 (instead of 3.09).

## 2014/12/02

* Removed support for the `$previouserror` keyword.
* Removed support for `--error-recovery` mode.

## 2014/02/18

* In the Coq back-end, use `'` instead of `_` as separator in identifiers.
  Also, correct a serious bug that was inadvertently introduced on
  2013/03/01 (r319).

## 2014/02/14

* Lexer fix so as to support an open variant type `[> ...]` within
  a `%type<...>` declaration.

## 2013/12/16

* Updated the `Makefile` so that `install` no longer depends on `all`.

* Updated the demos so that the lexer does not invoke `exit 0`
  when encoutering `eof`. (This should be more intuitive.)

## 2013/09/11

* Fixed a newline conversion problem that would prevent Menhir from
  building on Windows when using ocaml 4.01.

## 2013/03/02

* Switched to ocamlbuild. Many thanks to Daniel Weil for offering
  very useful guidance.

## 2013/01/16

* `menhir --depend` was broken since someone added new whitespace in the output
  of `ocamldep`. Fixed.

## 2012/12/19

* Fixed a compilation problem that would arise when a file produced
  by Menhir on a 64-bit platform was compiled by ocaml on a 32-bit
  platform.

## 2012/08/25

* Performance improvements in the computation of various information
  about the automaton (module `Invariant`). The improvements will be
  noticeable only for very large automata.

## 2012/06/07

* The option `--log-grammar 3` (and above) now causes the `FOLLOW` sets for
  terminal symbols to be computed and displayed.

## 2012/05/25

* Added the flag `--canonical`, which causes Menhir to produce a canonical LR(1)
  automaton in the style of Knuth. This means that no merging of states takes
  place during the construction of the automaton, and that no default reductions
  are allowed.

## 2012/01/23

* Fixed a bug whereby a `%nonassoc` declaration was not respected. This
  declaration requests that a shift/reduce conflict be reduced in favor of
  neither shifting nor reducing, that is, a syntax error must occur. However,
  due to an unforeseen interaction with the default reduction mechanism, this
  declaration was sometimes ignored and reduction would take place.

## 2012/01/09

* Changes in the (undocumented) Coq back-end so as to match the ESOP 2012
  paper.

## 2011/10/19

* The `Makefile` now tests whether Unix or Windows is used (the test is performed
  by evaluating `Sys.os_type` under `ocaml`) and changes a couple settings accordingly:
  * the executable file name is either `menhir` or `menhir.exe`
  * the object file suffix is either `.o` or `.obj`

* Added `--strict`, which causes many warnings about the grammar and about the
  automaton to be considered errors.

* The `#` annotations that are inserted in the generated `.ml` file now retain their
  full path. (That is, we no longer use `Filename.basename`.) This implies that
  the `#` annotations depend on how Menhir is invoked
  -- e.g., `menhir foo/bar.mly` and `cd foo && menhir bar.mly` will produce different
  results. Nevertheless, this seems reasonable and useful (e.g., in conjunction
  with `ocamlbuild` and a hierarchy of files). Thanks to Daniel Weil.

## 2011/10/06

* With the `-lg 1` switch, Menhir now indicates whether the grammar is SLR(1).

## 2011/05/24

* Removed the lock in `ocamldep.wrapper`. It is the responsibility of the user
  to avoid interferences with other processes (or other instances of the script)
  that create and/or remove files.

## 2011/04/28

* The (internal) computation of the automaton's invariant was broken and has
  been fixed. Surprisingly, this does not seem to affect the generated code,
  (which was correct,) so no observable bug is fixed. Hopefully no bug is
  introduced!

## 2011/04/07

* The grammar description files (`.mly`) are now read in up front and stored in
  memory while they are parsed. This allows us to avoid the use of `pos_in` and
  `seek_in`, which do not work correctly when CRLF conversion is being performed.

## 2011/04/05

* Fixed a bug in the type inference module (for parameterized non-terminals)
  which would cause an infinite loop.

## 2011/01/24

* Fixed a bug that would cause an assertion failure in the generated parser
  in some situations where the input stream was incorrect and the grammar
  involved the error token. The fix might cause grammars that use the error
  token to behave differently (hopefully more accurately) as of now.

## 2009/06/18

* `Makefile` changes: build and install only the bytecode version of MenhirLib
  when `TARGET=byte` is set.

## 2009/02/06

* Fixed `ocamldep.wrapper` to avoid quoting the name of the `ocaml` command.
  This is hoped to fix a compilation problem under MinGW.

## 2009/02/04

* A `Makefile` fix to avoid a problem under Windows/Cygwin.
* Renamed the `ocaml-check-version` script so as to avoid a warning.

## 2008/09/05

* Ocaml summer project: added `--interpret`, `--table`, and `--suggest-*`.

## 2008/08/06

* Fixed a problem that would cause the code inliner to abort when a semantic
  value and a non-terminal symbol happened to have the same name.

* Removed code sharing.

## 2008/06/20

* Removed an incorrect assertion that caused failures (`lr1.ml`, line 134).

## 2007/12/05

* Disabled code sharing by default, as it is currently broken. (See Yann's
  message; assertion failure at runtime.)

## 2007/12/01

* Added an optimization to share code among states that have identical
  outgoing transition tables.

## 2007/08/30

* Small `Makefile` change: create an executable file for `check-ocaml-version` in
  order to work around the absence of dynamic loading on some platforms.

## 2007/05/20

* Made a fundamental change in the construction of the LR(1) automaton
  in order to eliminate a bug that could lead to spurious conflicts --
  thanks to Ketti for submitting a bug report.

## 2007/05/18

* Added `--follow-construction` to help understand the construction of the
  LR(1) automaton (very verbose).

## 2007/05/11

* Code generation: more explicit qualifications with `Pervasives` so as
  to avoid capture when the user redefines some of the built-in operators,
  such as `(+)`.
* Added a new demo (`calc-param`) that shows how to use `%parameter`.

## 2007/03/22

* `Makefile` improvements (check for `PREFIX`; bootstrap in bytecode now
  also available). Slight changes to `OMakefile.shared`.

## 2007/02/15

* Portability fix in `Makefile` and `Makefile.shared` (avoided `which`).

## 2006/12/15

* Portability fix in `Makefile.shared` (replaced `&>` with `2>&1 >`).

## 2006/06/23

* Made a slight restriction to Pager's criterion so as to never introduce
  fake conflict tokens (see `Lr0.compatible`). This might help make conflict
  explanations more accurate in the future.

## 2006/06/16

* Fixed bug that would cause positions to become invalid after inlining.

## 2006/06/15

* Fixed `--depend` to be more lenient when analyzing `ocamldep`'s output.
* Added `--raw-depend` which transmits `ocamldep`'s output unchanged (for
  use in conjunction with `omake`).

## 2006/06/12

* Fixed bug that would cause `--only-preprocess` to print `%token` declarations
  also for pseudo-tokens.
* Fixed bug that caused some precedence declarations to be incorrectly
  reported as useless.
* Improved things so that useless pseudo-tokens now also cause warnings.
* Fixed bug that would cause `%type` directives for terminal symbols to
  be incorrectly accepted.
* Fixed bug that would occur when a semantic action containing `$i` keywords
  was inlined.

## 2006/05/05

* Fixed problem that caused some end-of-stream conflicts not to be reported.
* Fixed Pager's compatibility criterion to avoid creating end-of-stream conflicts.

## 2006/04/21

* Fixed problem that allowed generating incorrect but apparently well-typed
  Objective Caml code when a semantic action was ill-typed and `--infer` was
  omitted.

## 2006/03/29

* Improved conflict reports by factoring out maximal common derivation contexts.

## 2006/03/28

* Fixed bug that could arise when explaining a conflict in a non-LALR(1) grammar.

## 2006/03/27

* Changed count of reduce/reduce conflicts to allow a comparison
  with `ocamlyacc`'s diagnostics.
* When refusing to resolve a conflict, report all diagnostics before dying.

## 2006/03/18

* Added display of `FOLLOW` sets when using `--log-grammar 2`.
* Added `--graph` option.
* Fixed behavior of `--depend` option.

## 2006/01/06

* Removed reversed lists from the standard library.
