#
# spec file for package omnidiff
#
# Copyright (c) 2026, Martin Hauke <mardnh@gmx.de>
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


Name:           omnidiff
Version:        0.5.0
Release:        0
Summary:        Content-aware diffing tool
License:        AGPL-3.0-only
URL:            https://github.com/ivankovic/omnidiff
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
BuildRequires:  git-core
Requires:       git-core
Requires:       jujutsu

%description
OmniDiff is a content-aware diff tool. Instead of aligning two files line by line, it
parses code with tree-sitter and matches the two syntax trees, so a change is reported
as what it structurally is - an insertion, a deletion, an update, or a move - rather
than as whichever lines happened to line up. Pictures, archives, fonts, cursors,
message catalogs and PDFs are diffed by what they hold: pixels, files, glyphs, frames,
messages and pages.

It runs as an interactive terminal UI, as a plain-text batch formatter, or as a JSON
emitter for editor integrations, and it works as a git difftool backend and a
Jujutsu (jj) diff formatter.

%prep
%autosetup -p 1 -a 1

%build
%{cargo_build}
# generate manpage and completions
mkdir -p ./target/dist/
./target/release/omnidiff util man                > target/dist/omnidiff.1
./target/release/omnidiff util completions bash   > target/dist/omnidiff.bash
./target/release/omnidiff util completions fish   > target/dist/omnidiff.fish
./target/release/omnidiff util completions zsh    > target/dist/_omnidiff

%install
%{cargo_install}
install -D -m 0644 target/dist/omnidiff.1 %{buildroot}%{_mandir}/man1/omnidiff.1
install -D -m 0644 target/dist/omnidiff.bash %{buildroot}/%{_datadir}/bash-completion/completions/omnidiff.bash
install -D -m 0644 target/dist/omnidiff.fish %{buildroot}/%{_datadir}/fish/vendor_completions.d/omnidiff.fish
install -D -m 0644 target/dist/_omnidiff %{buildroot}/%{_datadir}/zsh/site-functions/_omnidiff

%check
# Skip Swift fixture tests
%{cargo_test} --lib -- --skip test::fixtures::full::swift_ --skip test::fixtures::small::swift_ --skip test::fixtures::stratified::swift_

%files
%license LICENSE
%doc README.md
%{_bindir}/omnidiff
%{_mandir}/man1/omnidiff.1%{?ext_man}
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/omnidiff.bash
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/omnidiff.fish
%dir %{_datadir}/zsh
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_omnidiff

%changelog
