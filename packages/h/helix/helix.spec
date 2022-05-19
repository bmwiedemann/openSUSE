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


%global _helix_runtimedir %{_sharedstatedir}/%{name}/runtime/
%global rustflags -Clink-arg=-Wl,-z,relro,-z,now -C debuginfo=2

Name:           helix
Version:        22.03~0
Release:        0
Summary:        A post-modern modal text editor written in Rust
License:        (Apache-2.0 OR MIT) AND BSD-3-Clause AND (Apache-2.0 OR BSL-1.0) AND (Apache-2.0 OR MIT) AND (MIT OR Apache-2.0 OR Zlib) AND (MIT or Unlicense) AND (Zlib OR Apache-2.0 OR MIT) AND Apache-2.0 AND BSL-1.0 AND ISC AND MIT AND MPL-2.0+ AND Zlib AND MPL-2.0
URL:            https://github.com/helix-editor/helix
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.xz
Source2:        cargo_config
Source3:        helix.sh
Source4:        helix-rpmlintrc
Source5:        README.SUSE
BuildRequires:  cargo-packaging
BuildRequires:  rust >= 1.46
ExclusiveArch:  %{rust_arches}

%description
A kakoune/neovim inspired modal text editor with built-in LSP and
has treesitter support for syntax highlighting and improved navigation

%prep
%autosetup -a1
mkdir -p .cargo
cp %{SOURCE2} .cargo/config
cp %{SOURCE5} docs/README.SUSE

%build
export RUSTFLAGS="%{rustflags}"

# We must disable fetching and building the treesitter grammars because this is a limitation with OBS cargo-packaging for now
export HELIX_DISABLE_AUTO_GRAMMAR_BUILD=true
cargo build --locked --offline --release

%install
mkdir -p %{buildroot}%{_libdir}/%{name}
mkdir -p %{buildroot}%{_helix_runtimedir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/hx %{buildroot}%{_libdir}/%{name}/hx
cp -rv "runtime/queries" %{buildroot}%{_helix_runtimedir}
cp -rv "runtime/themes" %{buildroot}%{_helix_runtimedir}
install -Dm644 runtime/tutor.txt -t %{buildroot}%{_helix_runtimedir}
ln -sv %{_helix_runtimedir} %{buildroot}%{_libdir}/%{name}/runtime
install -D -d -m 0755 %{buildroot}%{_bindir}
install -Dm755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md docs/README.SUSE CHANGELOG.md languages.toml docs/CONTRIBUTING.md docs/architecture.md docs/vision.md
%{_bindir}/%{name}
%dir %{_sharedstatedir}/%{name}
%dir %{_helix_runtimedir}
%dir %{_helix_runtimedir}/queries
%dir %{_helix_runtimedir}/queries/bash
%dir %{_helix_runtimedir}/queries/c
%dir %{_helix_runtimedir}/queries/c-sharp
%dir %{_helix_runtimedir}/queries/cmake
%dir %{_helix_runtimedir}/queries/comment
%dir %{_helix_runtimedir}/queries/cpp
%dir %{_helix_runtimedir}/queries/css
%dir %{_helix_runtimedir}/queries/dart
%dir %{_helix_runtimedir}/queries/dockerfile
%dir %{_helix_runtimedir}/queries/elixir
%dir %{_helix_runtimedir}/queries/elm
%dir %{_helix_runtimedir}/queries/erlang
%dir %{_helix_runtimedir}/queries/fish
%dir %{_helix_runtimedir}/queries/git-commit
%dir %{_helix_runtimedir}/queries/git-config
%dir %{_helix_runtimedir}/queries/git-diff
%dir %{_helix_runtimedir}/queries/git-rebase
%dir %{_helix_runtimedir}/queries/glsl
%dir %{_helix_runtimedir}/queries/go
%dir %{_helix_runtimedir}/queries/graphql
%dir %{_helix_runtimedir}/queries/haskell
%dir %{_helix_runtimedir}/queries/hcl
%dir %{_helix_runtimedir}/queries/html
%dir %{_helix_runtimedir}/queries/iex
%dir %{_helix_runtimedir}/queries/java
%dir %{_helix_runtimedir}/queries/javascript
%dir %{_helix_runtimedir}/queries/json
%dir %{_helix_runtimedir}/queries/julia
%dir %{_helix_runtimedir}/queries/kotlin
%dir %{_helix_runtimedir}/queries/latex
%dir %{_helix_runtimedir}/queries/lean
%dir %{_helix_runtimedir}/queries/ledger
%dir %{_helix_runtimedir}/queries/llvm
%dir %{_helix_runtimedir}/queries/llvm-mir
%dir %{_helix_runtimedir}/queries/llvm-mir-yaml
%dir %{_helix_runtimedir}/queries/lua
%dir %{_helix_runtimedir}/queries/make
%dir %{_helix_runtimedir}/queries/markdown
%dir %{_helix_runtimedir}/queries/nix
%dir %{_helix_runtimedir}/queries/ocaml
%dir %{_helix_runtimedir}/queries/ocaml-interface
%dir %{_helix_runtimedir}/queries/org
%dir %{_helix_runtimedir}/queries/perl
%dir %{_helix_runtimedir}/queries/php
%dir %{_helix_runtimedir}/queries/protobuf
%dir %{_helix_runtimedir}/queries/python
%dir %{_helix_runtimedir}/queries/regex
%dir %{_helix_runtimedir}/queries/rescript
%dir %{_helix_runtimedir}/queries/ruby
%dir %{_helix_runtimedir}/queries/rust
%dir %{_helix_runtimedir}/queries/scala
%dir %{_helix_runtimedir}/queries/solidity
%dir %{_helix_runtimedir}/queries/svelte
%dir %{_helix_runtimedir}/queries/tablegen
%dir %{_helix_runtimedir}/queries/toml
%dir %{_helix_runtimedir}/queries/tsq
%dir %{_helix_runtimedir}/queries/tsx
%dir %{_helix_runtimedir}/queries/twig
%dir %{_helix_runtimedir}/queries/typescript
%dir %{_helix_runtimedir}/queries/vue
%dir %{_helix_runtimedir}/queries/wgsl
%dir %{_helix_runtimedir}/queries/yaml
%dir %{_helix_runtimedir}/queries/zig
%dir %{_helix_runtimedir}/themes

%{_helix_runtimedir}/queries/bash/highlights.scm
%{_helix_runtimedir}/queries/bash/injections.scm
%{_helix_runtimedir}/queries/c-sharp/highlights.scm
%{_helix_runtimedir}/queries/c-sharp/injections.scm
%{_helix_runtimedir}/queries/c/highlights.scm
%{_helix_runtimedir}/queries/c/indents.toml
%{_helix_runtimedir}/queries/c/injections.scm
%{_helix_runtimedir}/queries/c/textobjects.scm
%{_helix_runtimedir}/queries/cmake/highlights.scm
%{_helix_runtimedir}/queries/cmake/indents.toml
%{_helix_runtimedir}/queries/cmake/injections.scm
%{_helix_runtimedir}/queries/cmake/textobjects.scm
%{_helix_runtimedir}/queries/comment/highlights.scm
%{_helix_runtimedir}/queries/cpp/highlights.scm
%{_helix_runtimedir}/queries/cpp/indents.toml
%{_helix_runtimedir}/queries/cpp/injections.scm
%{_helix_runtimedir}/queries/cpp/textobjects.scm
%{_helix_runtimedir}/queries/css/highlights.scm
%{_helix_runtimedir}/queries/css/injections.scm
%{_helix_runtimedir}/queries/dart/highlights.scm
%{_helix_runtimedir}/queries/dart/indents.toml
%{_helix_runtimedir}/queries/dart/injections.scm
%{_helix_runtimedir}/queries/dart/locals.scm
%{_helix_runtimedir}/queries/dockerfile/highlights.scm
%{_helix_runtimedir}/queries/dockerfile/injections.scm
%{_helix_runtimedir}/queries/elixir/highlights.scm
%{_helix_runtimedir}/queries/elixir/injections.scm
%{_helix_runtimedir}/queries/elm/highlights.scm
%{_helix_runtimedir}/queries/elm/injections.scm
%{_helix_runtimedir}/queries/elm/locals.scm
%{_helix_runtimedir}/queries/elm/tags.scm
%{_helix_runtimedir}/queries/erlang/highlights.scm
%{_helix_runtimedir}/queries/erlang/injections.scm
%{_helix_runtimedir}/queries/fish/highlights.scm
%{_helix_runtimedir}/queries/fish/indents.toml
%{_helix_runtimedir}/queries/fish/injections.scm
%{_helix_runtimedir}/queries/fish/textobjects.scm
%{_helix_runtimedir}/queries/git-commit/highlights.scm
%{_helix_runtimedir}/queries/git-commit/injections.scm
%{_helix_runtimedir}/queries/git-config/highlights.scm
%{_helix_runtimedir}/queries/git-diff/highlights.scm
%{_helix_runtimedir}/queries/git-rebase/highlights.scm
%{_helix_runtimedir}/queries/git-rebase/injections.scm
%{_helix_runtimedir}/queries/glsl/folds.scm
%{_helix_runtimedir}/queries/glsl/highlights.scm
%{_helix_runtimedir}/queries/glsl/indents.toml
%{_helix_runtimedir}/queries/glsl/injections.scm
%{_helix_runtimedir}/queries/glsl/locals.scm
%{_helix_runtimedir}/queries/go/highlights.scm
%{_helix_runtimedir}/queries/go/indents.toml
%{_helix_runtimedir}/queries/go/injections.scm
%{_helix_runtimedir}/queries/go/locals.scm
%{_helix_runtimedir}/queries/go/tags.scm
%{_helix_runtimedir}/queries/go/textobjects.scm
%{_helix_runtimedir}/queries/graphql/highlights.scm
%{_helix_runtimedir}/queries/haskell/highlights.scm
%{_helix_runtimedir}/queries/haskell/injections.scm
%{_helix_runtimedir}/queries/haskell/locals.scm
%{_helix_runtimedir}/queries/hcl/folds.scm
%{_helix_runtimedir}/queries/hcl/highlights.scm
%{_helix_runtimedir}/queries/hcl/indents.toml
%{_helix_runtimedir}/queries/hcl/injections.scm
%{_helix_runtimedir}/queries/html/highlights.scm
%{_helix_runtimedir}/queries/html/injections.scm
%{_helix_runtimedir}/queries/iex/highlights.scm
%{_helix_runtimedir}/queries/iex/injections.scm
%{_helix_runtimedir}/queries/java/highlights.scm
%{_helix_runtimedir}/queries/java/injections.scm
%{_helix_runtimedir}/queries/javascript/highlights-jsx.scm
%{_helix_runtimedir}/queries/javascript/highlights-params.scm
%{_helix_runtimedir}/queries/javascript/highlights.scm
%{_helix_runtimedir}/queries/javascript/indents.toml
%{_helix_runtimedir}/queries/javascript/injections.scm
%{_helix_runtimedir}/queries/javascript/locals.scm
%{_helix_runtimedir}/queries/javascript/tags.scm
%{_helix_runtimedir}/queries/json/highlights.scm
%{_helix_runtimedir}/queries/json/indents.toml
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
%{_helix_runtimedir}/queries/llvm-mir-yaml/indents.toml
%{_helix_runtimedir}/queries/llvm-mir-yaml/injections.scm
%{_helix_runtimedir}/queries/llvm-mir/highlights.scm
%{_helix_runtimedir}/queries/llvm-mir/indents.toml
%{_helix_runtimedir}/queries/llvm-mir/injections.scm
%{_helix_runtimedir}/queries/llvm-mir/textobjects.scm
%{_helix_runtimedir}/queries/llvm/highlights.scm
%{_helix_runtimedir}/queries/llvm/indents.toml
%{_helix_runtimedir}/queries/llvm/injections.scm
%{_helix_runtimedir}/queries/llvm/locals.scm
%{_helix_runtimedir}/queries/llvm/textobjects.scm
%{_helix_runtimedir}/queries/lua/highlights.scm
%{_helix_runtimedir}/queries/lua/indents.toml
%{_helix_runtimedir}/queries/lua/injections.scm
%{_helix_runtimedir}/queries/make/highlights.scm
%{_helix_runtimedir}/queries/make/injections.scm
%{_helix_runtimedir}/queries/markdown/highlights.scm
%{_helix_runtimedir}/queries/markdown/injections.scm
%{_helix_runtimedir}/queries/nix/highlights.scm
%{_helix_runtimedir}/queries/nix/indents.toml
%{_helix_runtimedir}/queries/ocaml-interface/highlights.scm
%{_helix_runtimedir}/queries/ocaml-interface/injections.scm
%{_helix_runtimedir}/queries/ocaml/highlights.scm
%{_helix_runtimedir}/queries/ocaml/indents.toml
%{_helix_runtimedir}/queries/ocaml/injections.scm
%{_helix_runtimedir}/queries/ocaml/locals.scm
%{_helix_runtimedir}/queries/org/highlights.scm
%{_helix_runtimedir}/queries/org/injections.scm
%{_helix_runtimedir}/queries/perl/highlights.scm
%{_helix_runtimedir}/queries/perl/indents.toml
%{_helix_runtimedir}/queries/perl/injections.scm
%{_helix_runtimedir}/queries/perl/textobjects.scm
%{_helix_runtimedir}/queries/php/highlights.scm
%{_helix_runtimedir}/queries/php/indents.toml
%{_helix_runtimedir}/queries/php/injections.scm
%{_helix_runtimedir}/queries/php/tags.scm
%{_helix_runtimedir}/queries/php/textobjects.scm
%{_helix_runtimedir}/queries/protobuf/highlights.scm
%{_helix_runtimedir}/queries/protobuf/indents.toml
%{_helix_runtimedir}/queries/protobuf/injections.scm
%{_helix_runtimedir}/queries/python/highlights.scm
%{_helix_runtimedir}/queries/python/indents.toml
%{_helix_runtimedir}/queries/python/injections.scm
%{_helix_runtimedir}/queries/python/tags.scm
%{_helix_runtimedir}/queries/python/textobjects.scm
%{_helix_runtimedir}/queries/regex/highlights.scm
%{_helix_runtimedir}/queries/rescript/highlights.scm
%{_helix_runtimedir}/queries/rescript/injections.scm
%{_helix_runtimedir}/queries/rescript/textobjects.scm
%{_helix_runtimedir}/queries/ruby/highlights.scm
%{_helix_runtimedir}/queries/ruby/indents.toml
%{_helix_runtimedir}/queries/ruby/injections.scm
%{_helix_runtimedir}/queries/ruby/locals.scm
%{_helix_runtimedir}/queries/ruby/tags.scm
%{_helix_runtimedir}/queries/rust/highlights.scm
%{_helix_runtimedir}/queries/rust/indents.toml
%{_helix_runtimedir}/queries/rust/injections.scm
%{_helix_runtimedir}/queries/rust/locals.scm
%{_helix_runtimedir}/queries/rust/textobjects.scm
%{_helix_runtimedir}/queries/scala/highlights.scm
%{_helix_runtimedir}/queries/scala/indents.toml
%{_helix_runtimedir}/queries/scala/injections.scm
%{_helix_runtimedir}/queries/solidity/highlights.scm
%{_helix_runtimedir}/queries/svelte/highlights.scm
%{_helix_runtimedir}/queries/svelte/indents.toml
%{_helix_runtimedir}/queries/svelte/injections.scm
%{_helix_runtimedir}/queries/tablegen/highlights.scm
%{_helix_runtimedir}/queries/tablegen/indents.toml
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
%{_helix_runtimedir}/queries/typescript/indents.toml
%{_helix_runtimedir}/queries/typescript/injections.scm
%{_helix_runtimedir}/queries/typescript/locals.scm
%{_helix_runtimedir}/queries/typescript/tags.scm
%{_helix_runtimedir}/queries/vue/highlights.scm
%{_helix_runtimedir}/queries/vue/injections.scm
%{_helix_runtimedir}/queries/wgsl/highlights.scm
%{_helix_runtimedir}/queries/wgsl/injections.scm
%{_helix_runtimedir}/queries/yaml/highlights.scm
%{_helix_runtimedir}/queries/yaml/indents.toml
%{_helix_runtimedir}/queries/yaml/injections.scm
%{_helix_runtimedir}/queries/zig/highlights.scm
%{_helix_runtimedir}/queries/zig/indents.toml
%{_helix_runtimedir}/queries/zig/injections.scm
%{_helix_runtimedir}/themes/README.md
%{_helix_runtimedir}/themes/base16_default_dark.toml
%{_helix_runtimedir}/themes/base16_default_light.toml
%{_helix_runtimedir}/themes/base16_terminal.toml
%{_helix_runtimedir}/themes/bogster.toml
%{_helix_runtimedir}/themes/dark_plus.toml
%{_helix_runtimedir}/themes/dracula.toml
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
%{_helix_runtimedir}/themes/nord.toml
%{_helix_runtimedir}/themes/onedark.toml
%{_helix_runtimedir}/themes/rose_pine.toml
%{_helix_runtimedir}/themes/rose_pine_dawn.toml
%{_helix_runtimedir}/themes/serika-dark.toml
%{_helix_runtimedir}/themes/serika-light.toml
%{_helix_runtimedir}/themes/solarized_dark.toml
%{_helix_runtimedir}/themes/solarized_light.toml
%{_helix_runtimedir}/themes/spacebones_light.toml
%{_helix_runtimedir}/tutor.txt

%dir %{_libdir}/%{name}
%{_libdir}/%{name}/runtime
%{_libdir}/%{name}/hx

%changelog
