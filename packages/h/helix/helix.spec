#
# spec file for package helix
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%global _helix_runtimedir %{_sharedstatedir}/%{name}/runtime

Name:           helix
Version:        22.05
Release:        0
Summary:        A post-modern modal text editor written in Rust
License:        (Apache-2.0 OR MIT) AND BSD-3-Clause AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT or Unlicense) AND (Zlib OR Apache-2.0 OR MIT) AND Apache-2.0 AND BSL-1.0 AND ISC AND MIT AND MPL-2.0+ AND Zlib AND MPL-2.0
URL:            https://github.com/helix-editor/helix
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source3:        helix-rpmlintrc
BuildRequires:  c++_compiler
BuildRequires:  c_compiler
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_arches}

%description
A kakoune/neovim inspired modal text editor with built-in LSP and
has treesitter support for syntax highlighting and improved navigation

%prep
%autosetup -a1 -n %{name}
mkdir -p .cargo
cp %{SOURCE2} .cargo/config

%build
export HELIX_DISABLE_AUTO_GRAMMAR_BUILD=true
%{cargo_build}
HELIX_RUNTIME="$PWD/runtime" ./target/release/hx --grammar build

%install

mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_helix_runtimedir}
install -m 0755 %{_builddir}/%{name}/target/release/hx %{buildroot}%{_libdir}/%{name}/hx
cp -rv "runtime/queries" %{buildroot}%{_helix_runtimedir}
cp -rv "runtime/themes" %{buildroot}%{_helix_runtimedir}
find "%{_builddir}/%{name}/runtime/grammars" -type f -name '*.so' -exec \
    install --verbose -Dm 755 {} -t "%{buildroot}%{_helix_runtimedir}/grammars" \;
install -Dm644 runtime/tutor.txt -t %{buildroot}%{_helix_runtimedir}
ln -sv %{_helix_runtimedir} %{buildroot}%{_libdir}/%{name}/runtime
install -D -d -m 0755 %{buildroot}%{_bindir}
ln -sv %{_libdir}/%{name}/hx %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md CHANGELOG.md languages.toml docs/CONTRIBUTING.md docs/architecture.md docs/vision.md

# hx symlinked as helix
%{_bindir}/%{name}

# The real hx binary
%{_libdir}/%{name}/hx

# Runtimes and runtime files
%dir %{_libdir}/%{name}
%dir %{_sharedstatedir}/%{name}
%dir %{_helix_runtimedir}
%dir %{_helix_runtimedir}/queries
%dir %{_helix_runtimedir}/themes
%dir %{_helix_runtimedir}/grammars

# Grammars
%{_helix_runtimedir}/grammars/bash.so 
%{_helix_runtimedir}/grammars/c-sharp.so 
%{_helix_runtimedir}/grammars/c.so 
%{_helix_runtimedir}/grammars/cairo.so
%{_helix_runtimedir}/grammars/cmake.so 
%{_helix_runtimedir}/grammars/comment.so 
%{_helix_runtimedir}/grammars/cpon.so
%{_helix_runtimedir}/grammars/cpp.so 
%{_helix_runtimedir}/grammars/css.so 
%{_helix_runtimedir}/grammars/dart.so 
%{_helix_runtimedir}/grammars/devicetree.so
%{_helix_runtimedir}/grammars/dockerfile.so 
%{_helix_runtimedir}/grammars/eex.so 
%{_helix_runtimedir}/grammars/elixir.so 
%{_helix_runtimedir}/grammars/elm.so 
%{_helix_runtimedir}/grammars/embedded-template.so 
%{_helix_runtimedir}/grammars/erlang.so 
%{_helix_runtimedir}/grammars/fish.so 
%{_helix_runtimedir}/grammars/gdscript.so 
%{_helix_runtimedir}/grammars/git-commit.so 
%{_helix_runtimedir}/grammars/git-config.so 
%{_helix_runtimedir}/grammars/git-diff.so 
%{_helix_runtimedir}/grammars/git-rebase.so 
%{_helix_runtimedir}/grammars/gitattributes.so
%{_helix_runtimedir}/grammars/gitignore.so
%{_helix_runtimedir}/grammars/gleam.so 
%{_helix_runtimedir}/grammars/glsl.so 
%{_helix_runtimedir}/grammars/go.so 
%{_helix_runtimedir}/grammars/gomod.so
%{_helix_runtimedir}/grammars/gowork.so
%{_helix_runtimedir}/grammars/graphql.so 
%{_helix_runtimedir}/grammars/hare.so
%{_helix_runtimedir}/grammars/haskell.so 
%{_helix_runtimedir}/grammars/hcl.so 
%{_helix_runtimedir}/grammars/heex.so 
%{_helix_runtimedir}/grammars/html.so 
%{_helix_runtimedir}/grammars/iex.so 
%{_helix_runtimedir}/grammars/java.so
%{_helix_runtimedir}/grammars/javascript.so 
%{_helix_runtimedir}/grammars/json.so 
%{_helix_runtimedir}/grammars/julia.so 
%{_helix_runtimedir}/grammars/kotlin.so 
%{_helix_runtimedir}/grammars/latex.so 
%{_helix_runtimedir}/grammars/lean.so 
%{_helix_runtimedir}/grammars/ledger.so 
%{_helix_runtimedir}/grammars/llvm-mir.so 
%{_helix_runtimedir}/grammars/llvm.so 
%{_helix_runtimedir}/grammars/lua.so 
%{_helix_runtimedir}/grammars/make.so 
%{_helix_runtimedir}/grammars/markdown.so 
%{_helix_runtimedir}/grammars/meson.so
%{_helix_runtimedir}/grammars/nickel.so
%{_helix_runtimedir}/grammars/nix.so 
%{_helix_runtimedir}/grammars/nu.so
%{_helix_runtimedir}/grammars/ocaml-interface.so 
%{_helix_runtimedir}/grammars/ocaml.so 
%{_helix_runtimedir}/grammars/odin.so
%{_helix_runtimedir}/grammars/org.so 
%{_helix_runtimedir}/grammars/perl.so 
%{_helix_runtimedir}/grammars/php.so 
%{_helix_runtimedir}/grammars/protobuf.so 
%{_helix_runtimedir}/grammars/python.so 
%{_helix_runtimedir}/grammars/r.so 
%{_helix_runtimedir}/grammars/regex.so 
%{_helix_runtimedir}/grammars/rescript.so 
%{_helix_runtimedir}/grammars/ruby.so 
%{_helix_runtimedir}/grammars/rust.so 
%{_helix_runtimedir}/grammars/scala.so 
%{_helix_runtimedir}/grammars/scheme.so
%{_helix_runtimedir}/grammars/solidity.so 
%{_helix_runtimedir}/grammars/sql.so 
%{_helix_runtimedir}/grammars/sshclientconfig.so
%{_helix_runtimedir}/grammars/svelte.so 
%{_helix_runtimedir}/grammars/swift.so 
%{_helix_runtimedir}/grammars/tablegen.so 
%{_helix_runtimedir}/grammars/toml.so 
%{_helix_runtimedir}/grammars/tsq.so 
%{_helix_runtimedir}/grammars/tsx.so 
%{_helix_runtimedir}/grammars/twig.so 
%{_helix_runtimedir}/grammars/typescript.so 
%{_helix_runtimedir}/grammars/vala.so
%{_helix_runtimedir}/grammars/verilog.so
%{_helix_runtimedir}/grammars/vue.so 
%{_helix_runtimedir}/grammars/wgsl.so 
%{_helix_runtimedir}/grammars/yaml.so 
%{_helix_runtimedir}/grammars/zig.so 

# Queries
%{_helix_runtimedir}/queries/bash
%{_helix_runtimedir}/queries/c
%{_helix_runtimedir}/queries/c-sharp
%{_helix_runtimedir}/queries/cairo
%{_helix_runtimedir}/queries/cmake
%{_helix_runtimedir}/queries/comment
%{_helix_runtimedir}/queries/cpon
%{_helix_runtimedir}/queries/cpp
%{_helix_runtimedir}/queries/css
%{_helix_runtimedir}/queries/dart
%{_helix_runtimedir}/queries/devicetree
%{_helix_runtimedir}/queries/dockerfile
%{_helix_runtimedir}/queries/eex
%{_helix_runtimedir}/queries/ejs
%{_helix_runtimedir}/queries/elixir
%{_helix_runtimedir}/queries/elm
%{_helix_runtimedir}/queries/erb
%{_helix_runtimedir}/queries/erlang
%{_helix_runtimedir}/queries/fish
%{_helix_runtimedir}/queries/gdscript
%{_helix_runtimedir}/queries/git-attributes
%{_helix_runtimedir}/queries/git-commit
%{_helix_runtimedir}/queries/git-config
%{_helix_runtimedir}/queries/git-diff
%{_helix_runtimedir}/queries/git-ignore
%{_helix_runtimedir}/queries/git-rebase
%{_helix_runtimedir}/queries/gleam
%{_helix_runtimedir}/queries/glsl
%{_helix_runtimedir}/queries/go
%{_helix_runtimedir}/queries/gomod
%{_helix_runtimedir}/queries/gowork
%{_helix_runtimedir}/queries/graphql
%{_helix_runtimedir}/queries/hare
%{_helix_runtimedir}/queries/haskell
%{_helix_runtimedir}/queries/hcl
%{_helix_runtimedir}/queries/heex
%{_helix_runtimedir}/queries/html
%{_helix_runtimedir}/queries/iex
%{_helix_runtimedir}/queries/java
%{_helix_runtimedir}/queries/javascript
%{_helix_runtimedir}/queries/json
%{_helix_runtimedir}/queries/jsx
%{_helix_runtimedir}/queries/julia
%{_helix_runtimedir}/queries/kotlin
%{_helix_runtimedir}/queries/latex
%{_helix_runtimedir}/queries/lean
%{_helix_runtimedir}/queries/ledger
%{_helix_runtimedir}/queries/llvm
%{_helix_runtimedir}/queries/llvm-mir
%{_helix_runtimedir}/queries/llvm-mir-yaml
%{_helix_runtimedir}/queries/lua
%{_helix_runtimedir}/queries/make
%{_helix_runtimedir}/queries/markdown
%{_helix_runtimedir}/queries/meson
%{_helix_runtimedir}/queries/nickel
%{_helix_runtimedir}/queries/nix
%{_helix_runtimedir}/queries/nu
%{_helix_runtimedir}/queries/ocaml
%{_helix_runtimedir}/queries/ocaml-interface
%{_helix_runtimedir}/queries/odin
%{_helix_runtimedir}/queries/org
%{_helix_runtimedir}/queries/perl
%{_helix_runtimedir}/queries/php
%{_helix_runtimedir}/queries/protobuf
%{_helix_runtimedir}/queries/python
%{_helix_runtimedir}/queries/r
%{_helix_runtimedir}/queries/regex
%{_helix_runtimedir}/queries/rescript
%{_helix_runtimedir}/queries/rmarkdown
%{_helix_runtimedir}/queries/ron
%{_helix_runtimedir}/queries/ruby
%{_helix_runtimedir}/queries/rust
%{_helix_runtimedir}/queries/scala
%{_helix_runtimedir}/queries/scheme
%{_helix_runtimedir}/queries/solidity
%{_helix_runtimedir}/queries/sql
%{_helix_runtimedir}/queries/sshclientconfig
%{_helix_runtimedir}/queries/svelte
%{_helix_runtimedir}/queries/swift
%{_helix_runtimedir}/queries/tablegen
%{_helix_runtimedir}/queries/toml
%{_helix_runtimedir}/queries/tsq
%{_helix_runtimedir}/queries/tsx
%{_helix_runtimedir}/queries/twig
%{_helix_runtimedir}/queries/typescript
%{_helix_runtimedir}/queries/vala
%{_helix_runtimedir}/queries/verilog
%{_helix_runtimedir}/queries/vue
%{_helix_runtimedir}/queries/wgsl
%{_helix_runtimedir}/queries/yaml
%{_helix_runtimedir}/queries/zig

%{_helix_runtimedir}/queries/bash/highlights.scm
%{_helix_runtimedir}/queries/bash/injections.scm
%{_helix_runtimedir}/queries/c-sharp/highlights.scm
%{_helix_runtimedir}/queries/c-sharp/injections.scm
%{_helix_runtimedir}/queries/c/highlights.scm
%{_helix_runtimedir}/queries/c/indents.scm
%{_helix_runtimedir}/queries/c/injections.scm
%{_helix_runtimedir}/queries/c/textobjects.scm
%{_helix_runtimedir}/queries/cairo/highlights.scm
%{_helix_runtimedir}/queries/cairo/injections.scm
%{_helix_runtimedir}/queries/cmake/highlights.scm
%{_helix_runtimedir}/queries/cmake/indents.scm
%{_helix_runtimedir}/queries/cmake/injections.scm
%{_helix_runtimedir}/queries/cmake/textobjects.scm
%{_helix_runtimedir}/queries/comment/highlights.scm
%{_helix_runtimedir}/queries/cpon/highlights.scm
%{_helix_runtimedir}/queries/cpon/indents.scm
%{_helix_runtimedir}/queries/cpp/highlights.scm
%{_helix_runtimedir}/queries/cpp/indents.scm
%{_helix_runtimedir}/queries/cpp/injections.scm
%{_helix_runtimedir}/queries/cpp/textobjects.scm
%{_helix_runtimedir}/queries/css/highlights.scm
%{_helix_runtimedir}/queries/css/injections.scm
%{_helix_runtimedir}/queries/dart/highlights.scm
%{_helix_runtimedir}/queries/dart/indents.scm
%{_helix_runtimedir}/queries/dart/injections.scm
%{_helix_runtimedir}/queries/dart/locals.scm
%{_helix_runtimedir}/queries/devicetree/highlights.scm
%{_helix_runtimedir}/queries/devicetree/indents.scm
%{_helix_runtimedir}/queries/dockerfile/highlights.scm
%{_helix_runtimedir}/queries/dockerfile/injections.scm
%{_helix_runtimedir}/queries/eex/highlights.scm
%{_helix_runtimedir}/queries/eex/injections.scm
%{_helix_runtimedir}/queries/ejs/highlights.scm
%{_helix_runtimedir}/queries/ejs/injections.scm
%{_helix_runtimedir}/queries/elixir/highlights.scm
%{_helix_runtimedir}/queries/elixir/injections.scm
%{_helix_runtimedir}/queries/elm/highlights.scm
%{_helix_runtimedir}/queries/elm/injections.scm
%{_helix_runtimedir}/queries/elm/locals.scm
%{_helix_runtimedir}/queries/elm/tags.scm
%{_helix_runtimedir}/queries/erb/highlights.scm
%{_helix_runtimedir}/queries/erb/injections.scm
%{_helix_runtimedir}/queries/erlang/highlights.scm
%{_helix_runtimedir}/queries/erlang/injections.scm
%{_helix_runtimedir}/queries/fish/highlights.scm
%{_helix_runtimedir}/queries/fish/indents.scm
%{_helix_runtimedir}/queries/fish/injections.scm
%{_helix_runtimedir}/queries/fish/textobjects.scm
%{_helix_runtimedir}/queries/gdscript/highlights.scm
%{_helix_runtimedir}/queries/gdscript/indents.scm
%{_helix_runtimedir}/queries/gdscript/tags.scm
%{_helix_runtimedir}/queries/git-attributes/highlights.scm
%{_helix_runtimedir}/queries/git-commit/highlights.scm
%{_helix_runtimedir}/queries/git-commit/injections.scm
%{_helix_runtimedir}/queries/git-config/highlights.scm
%{_helix_runtimedir}/queries/git-diff/highlights.scm
%{_helix_runtimedir}/queries/git-ignore/highlights.scm
%{_helix_runtimedir}/queries/git-rebase/highlights.scm
%{_helix_runtimedir}/queries/git-rebase/injections.scm
%{_helix_runtimedir}/queries/gleam/highlights.scm
%{_helix_runtimedir}/queries/gleam/locals.scm
%{_helix_runtimedir}/queries/glsl/folds.scm
%{_helix_runtimedir}/queries/glsl/highlights.scm
%{_helix_runtimedir}/queries/glsl/indents.scm
%{_helix_runtimedir}/queries/glsl/injections.scm
%{_helix_runtimedir}/queries/glsl/locals.scm
%{_helix_runtimedir}/queries/go/highlights.scm
%{_helix_runtimedir}/queries/go/indents.scm
%{_helix_runtimedir}/queries/go/injections.scm
%{_helix_runtimedir}/queries/go/locals.scm
%{_helix_runtimedir}/queries/go/tags.scm
%{_helix_runtimedir}/queries/go/textobjects.scm
%{_helix_runtimedir}/queries/gomod/highlights.scm
%{_helix_runtimedir}/queries/gomod/injections.scm
%{_helix_runtimedir}/queries/gowork/highlights.scm
%{_helix_runtimedir}/queries/gowork/injections.scm
%{_helix_runtimedir}/queries/graphql/highlights.scm
%{_helix_runtimedir}/queries/hare/highlights.scm
%{_helix_runtimedir}/queries/hare/indents.scm
%{_helix_runtimedir}/queries/hare/locals.scm
%{_helix_runtimedir}/queries/haskell/highlights.scm
%{_helix_runtimedir}/queries/haskell/injections.scm
%{_helix_runtimedir}/queries/haskell/locals.scm
%{_helix_runtimedir}/queries/hcl/folds.scm
%{_helix_runtimedir}/queries/hcl/highlights.scm
%{_helix_runtimedir}/queries/hcl/indents.scm
%{_helix_runtimedir}/queries/hcl/injections.scm
%{_helix_runtimedir}/queries/heex/highlights.scm
%{_helix_runtimedir}/queries/heex/injections.scm
%{_helix_runtimedir}/queries/html/highlights.scm
%{_helix_runtimedir}/queries/html/injections.scm
%{_helix_runtimedir}/queries/iex/highlights.scm
%{_helix_runtimedir}/queries/iex/injections.scm
%{_helix_runtimedir}/queries/java/highlights.scm
%{_helix_runtimedir}/queries/java/injections.scm
%{_helix_runtimedir}/queries/javascript/highlights-params.scm
%{_helix_runtimedir}/queries/javascript/highlights.scm
%{_helix_runtimedir}/queries/javascript/indents.scm
%{_helix_runtimedir}/queries/javascript/injections.scm
%{_helix_runtimedir}/queries/javascript/locals.scm
%{_helix_runtimedir}/queries/javascript/tags.scm
%{_helix_runtimedir}/queries/json/highlights.scm
%{_helix_runtimedir}/queries/json/indents.scm
%{_helix_runtimedir}/queries/jsx/highlights.scm
%{_helix_runtimedir}/queries/jsx/indents.scm
%{_helix_runtimedir}/queries/jsx/injections.scm
%{_helix_runtimedir}/queries/jsx/locals.scm
%{_helix_runtimedir}/queries/julia/folds.scm
%{_helix_runtimedir}/queries/julia/highlights.scm
%{_helix_runtimedir}/queries/julia/injections.scm
%{_helix_runtimedir}/queries/julia/locals.scm
%{_helix_runtimedir}/queries/kotlin/folds.scm
%{_helix_runtimedir}/queries/kotlin/highlights.scm
%{_helix_runtimedir}/queries/kotlin/injections.scm
%{_helix_runtimedir}/queries/latex/folds.scm
%{_helix_runtimedir}/queries/latex/highlights.scm
%{_helix_runtimedir}/queries/latex/injections.scm
%{_helix_runtimedir}/queries/lean/folds.scm
%{_helix_runtimedir}/queries/lean/highlights.scm
%{_helix_runtimedir}/queries/lean/injections.scm
%{_helix_runtimedir}/queries/lean/locals.scm
%{_helix_runtimedir}/queries/ledger/highlights.scm
%{_helix_runtimedir}/queries/ledger/injections.scm
%{_helix_runtimedir}/queries/llvm-mir-yaml/highlights.scm
%{_helix_runtimedir}/queries/llvm-mir-yaml/indents.scm
%{_helix_runtimedir}/queries/llvm-mir-yaml/injections.scm
%{_helix_runtimedir}/queries/llvm-mir/highlights.scm
%{_helix_runtimedir}/queries/llvm-mir/indents.scm
%{_helix_runtimedir}/queries/llvm-mir/injections.scm
%{_helix_runtimedir}/queries/llvm-mir/textobjects.scm
%{_helix_runtimedir}/queries/llvm/highlights.scm
%{_helix_runtimedir}/queries/llvm/indents.scm
%{_helix_runtimedir}/queries/llvm/injections.scm
%{_helix_runtimedir}/queries/llvm/locals.scm
%{_helix_runtimedir}/queries/llvm/textobjects.scm
%{_helix_runtimedir}/queries/lua/highlights.scm
%{_helix_runtimedir}/queries/lua/indents.scm
%{_helix_runtimedir}/queries/lua/injections.scm
%{_helix_runtimedir}/queries/make/highlights.scm
%{_helix_runtimedir}/queries/make/injections.scm
%{_helix_runtimedir}/queries/markdown/highlights.scm
%{_helix_runtimedir}/queries/markdown/injections.scm
%{_helix_runtimedir}/queries/meson/highlights.scm
%{_helix_runtimedir}/queries/meson/indents.scm
%{_helix_runtimedir}/queries/nickel/highlights.scm
%{_helix_runtimedir}/queries/nickel/indents.scm
%{_helix_runtimedir}/queries/nix/highlights.scm
%{_helix_runtimedir}/queries/nix/indents.scm
%{_helix_runtimedir}/queries/nu/folds.scm
%{_helix_runtimedir}/queries/nu/highlights.scm
%{_helix_runtimedir}/queries/nu/injections.scm
%{_helix_runtimedir}/queries/nu/locals.scm
%{_helix_runtimedir}/queries/ocaml-interface/highlights.scm
%{_helix_runtimedir}/queries/ocaml-interface/injections.scm
%{_helix_runtimedir}/queries/ocaml/highlights.scm
%{_helix_runtimedir}/queries/ocaml/indents.scm
%{_helix_runtimedir}/queries/ocaml/injections.scm
%{_helix_runtimedir}/queries/ocaml/locals.scm
%{_helix_runtimedir}/queries/odin/highlights.scm
%{_helix_runtimedir}/queries/org/highlights.scm
%{_helix_runtimedir}/queries/org/injections.scm
%{_helix_runtimedir}/queries/perl/highlights.scm
%{_helix_runtimedir}/queries/perl/indents.scm
%{_helix_runtimedir}/queries/perl/injections.scm
%{_helix_runtimedir}/queries/perl/textobjects.scm
%{_helix_runtimedir}/queries/php/highlights.scm
%{_helix_runtimedir}/queries/php/indents.scm
%{_helix_runtimedir}/queries/php/injections.scm
%{_helix_runtimedir}/queries/php/tags.scm
%{_helix_runtimedir}/queries/php/textobjects.scm
%{_helix_runtimedir}/queries/protobuf/highlights.scm
%{_helix_runtimedir}/queries/protobuf/indents.scm
%{_helix_runtimedir}/queries/protobuf/injections.scm
%{_helix_runtimedir}/queries/python/highlights.scm
%{_helix_runtimedir}/queries/python/indents.scm
%{_helix_runtimedir}/queries/python/injections.scm
%{_helix_runtimedir}/queries/python/tags.scm
%{_helix_runtimedir}/queries/python/textobjects.scm
%{_helix_runtimedir}/queries/r/highlights.scm
%{_helix_runtimedir}/queries/r/locals.scm
%{_helix_runtimedir}/queries/regex/highlights.scm
%{_helix_runtimedir}/queries/rescript/highlights.scm
%{_helix_runtimedir}/queries/rescript/injections.scm
%{_helix_runtimedir}/queries/rescript/textobjects.scm
%{_helix_runtimedir}/queries/rmarkdown/highlights.scm
%{_helix_runtimedir}/queries/rmarkdown/indents.scm
%{_helix_runtimedir}/queries/rmarkdown/injections.scm
%{_helix_runtimedir}/queries/ron/highlights.scm
%{_helix_runtimedir}/queries/ron/indents.scm
%{_helix_runtimedir}/queries/ron/injections.scm
%{_helix_runtimedir}/queries/ruby/highlights.scm
%{_helix_runtimedir}/queries/ruby/indents.scm
%{_helix_runtimedir}/queries/ruby/injections.scm
%{_helix_runtimedir}/queries/ruby/locals.scm
%{_helix_runtimedir}/queries/ruby/tags.scm
%{_helix_runtimedir}/queries/ruby/textobjects.scm
%{_helix_runtimedir}/queries/rust/highlights.scm
%{_helix_runtimedir}/queries/rust/indents.scm
%{_helix_runtimedir}/queries/rust/injections.scm
%{_helix_runtimedir}/queries/rust/locals.scm
%{_helix_runtimedir}/queries/rust/textobjects.scm
%{_helix_runtimedir}/queries/scala/highlights.scm
%{_helix_runtimedir}/queries/scala/indents.scm
%{_helix_runtimedir}/queries/scala/injections.scm
%{_helix_runtimedir}/queries/scheme/highlights.scm
%{_helix_runtimedir}/queries/scheme/injections.scm
%{_helix_runtimedir}/queries/solidity/highlights.scm
%{_helix_runtimedir}/queries/sql/highlights.scm
%{_helix_runtimedir}/queries/sshclientconfig/highlights.scm
%{_helix_runtimedir}/queries/svelte/highlights.scm
%{_helix_runtimedir}/queries/svelte/indents.scm
%{_helix_runtimedir}/queries/svelte/injections.scm
%{_helix_runtimedir}/queries/swift/highlights.scm
%{_helix_runtimedir}/queries/swift/locals.scm
%{_helix_runtimedir}/queries/tablegen/highlights.scm
%{_helix_runtimedir}/queries/tablegen/indents.scm
%{_helix_runtimedir}/queries/tablegen/injections.scm
%{_helix_runtimedir}/queries/tablegen/textobjects.scm
%{_helix_runtimedir}/queries/toml/highlights.scm
%{_helix_runtimedir}/queries/toml/injections.scm
%{_helix_runtimedir}/queries/tsq/highlights.scm
%{_helix_runtimedir}/queries/tsq/injections.scm
%{_helix_runtimedir}/queries/tsx/highlights.scm
%{_helix_runtimedir}/queries/tsx/injections.scm
%{_helix_runtimedir}/queries/twig/highlights.scm
%{_helix_runtimedir}/queries/twig/injections.scm
%{_helix_runtimedir}/queries/typescript/highlights.scm
%{_helix_runtimedir}/queries/typescript/indents.scm
%{_helix_runtimedir}/queries/typescript/injections.scm
%{_helix_runtimedir}/queries/typescript/locals.scm
%{_helix_runtimedir}/queries/typescript/tags.scm
%{_helix_runtimedir}/queries/vala/highlights.scm
%{_helix_runtimedir}/queries/verilog/highlights.scm
%{_helix_runtimedir}/queries/verilog/injections.scm
%{_helix_runtimedir}/queries/verilog/locals.scm
%{_helix_runtimedir}/queries/verilog/textobjects.scm
%{_helix_runtimedir}/queries/vue/highlights.scm
%{_helix_runtimedir}/queries/vue/injections.scm
%{_helix_runtimedir}/queries/wgsl/highlights.scm
%{_helix_runtimedir}/queries/wgsl/injections.scm
%{_helix_runtimedir}/queries/yaml/highlights.scm
%{_helix_runtimedir}/queries/yaml/indents.scm
%{_helix_runtimedir}/queries/yaml/injections.scm
%{_helix_runtimedir}/queries/zig/highlights.scm
%{_helix_runtimedir}/queries/zig/indents.scm
%{_helix_runtimedir}/queries/zig/injections.scm

# Themes
%{_helix_runtimedir}/themes/README.md
%{_helix_runtimedir}/themes/autumn.toml
%{_helix_runtimedir}/themes/base16_default_dark.toml
%{_helix_runtimedir}/themes/base16_default_light.toml
%{_helix_runtimedir}/themes/base16_terminal.toml
%{_helix_runtimedir}/themes/bogster.toml
%{_helix_runtimedir}/themes/boo_berry.toml
%{_helix_runtimedir}/themes/catpuccin.toml
%{_helix_runtimedir}/themes/dark_plus.toml
%{_helix_runtimedir}/themes/dracula.toml
%{_helix_runtimedir}/themes/dracula_at_night.toml
%{_helix_runtimedir}/themes/everforest_dark.toml
%{_helix_runtimedir}/themes/everforest_light.toml
%{_helix_runtimedir}/themes/gruvbox.toml
%{_helix_runtimedir}/themes/gruvbox_light.toml
%{_helix_runtimedir}/themes/ingrid.toml
%{_helix_runtimedir}/themes/monokai.toml
%{_helix_runtimedir}/themes/monokai_pro.toml
%{_helix_runtimedir}/themes/monokai_pro_machine.toml
%{_helix_runtimedir}/themes/monokai_pro_octagon.toml
%{_helix_runtimedir}/themes/monokai_pro_ristretto.toml
%{_helix_runtimedir}/themes/monokai_pro_spectrum.toml
%{_helix_runtimedir}/themes/night_owl.toml
%{_helix_runtimedir}/themes/nord.toml
%{_helix_runtimedir}/themes/onedark.toml
%{_helix_runtimedir}/themes/onelight.toml
%{_helix_runtimedir}/themes/pop-dark.toml
%{_helix_runtimedir}/themes/rose_pine.toml
%{_helix_runtimedir}/themes/rose_pine_dawn.toml
%{_helix_runtimedir}/themes/serika-dark.toml
%{_helix_runtimedir}/themes/serika-light.toml
%{_helix_runtimedir}/themes/snazzy.toml
%{_helix_runtimedir}/themes/solarized_dark.toml
%{_helix_runtimedir}/themes/solarized_light.toml
%{_helix_runtimedir}/themes/spacebones_light.toml
%{_helix_runtimedir}/themes/tokyonight.toml
%{_helix_runtimedir}/themes/tokyonight_storm.toml
%{_helix_runtimedir}/tutor.txt

# Symlinked runtime directory
%{_libdir}/%{name}/runtime

%changelog
