#
# spec file for package doxx
#
# Copyright (c) 2025, Martin Hauke <mardnh@gmx.de>
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


Name:           doxx
Version:        0.1.1
Release:        0
Summary:        Terminal document viewer for .docx files
License:        MIT
URL:            https://bgreenwell.github.io/doxx/doxx/
#Git-Clone:     https://github.com/bgreenwell/doxx.git
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo-packaging
ExclusiveArch:  %{rust_tier1_arches}

%description
A fast, terminal-native document viewer for Word files.
View, search, and export .docx documents without leaving
your command line.

Features:
 * Beautiful terminal rendering with formatting, tables, and lists.
 * Fast search with highlighting
 * Smart tables with proper alignment and Unicode borders
 * Copy to clipboard — grab content directly from the terminal
 * Export formats — Markdown, CSV, JSON, plain text,
   ANSI-colored output.
 * Terminal images for Kitty, iTerm2, WezTerm.
 * Color support — see Word document colors in your terminal.

%prep
%autosetup -a 1

%build
%{cargo_build}

%install
%{cargo_install}

%check
%{cargo_test}

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/doxx
%exclude %{_bindir}/generate_test_docs

%changelog
