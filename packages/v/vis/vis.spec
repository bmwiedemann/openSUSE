#
# spec file for package vis
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%if 0%{?suse_version} > 1600
%define flavor lua54
%else
%define flavor lua53
%endif
Name:           vis
Version:        0.9+git.1793606990.d89b6c27
Release:        0
Summary:        An editor combining the strengths of both vi(m) and sam
License:        ISC
URL:            https://sr.ht/~martanne/vis
Source:         %{name}-%{version}.tar.zst
BuildRequires:  %{flavor}-devel
BuildRequires:  %{flavor}-lpeg
BuildRequires:  %{flavor}-penlight
BuildRequires:  doxygen
BuildRequires:  mandoc
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  python3-breathe
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  vim-small
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(termkey)
BuildRequires:  pkgconfig(tre)
Requires:       %{flavor}
Requires:       %{flavor}-lpeg
Suggests:       %{flavor}-editorconfig-core-lua
Suggests:       par_text

%description
Vis aims to be a modern, legacy free, simple yet efficient editor
combining the strengths of both vi(m) and sam.

It extends vi's modal editing with built-in support for multiple
cursors/selections and combines it with sam's structural regular
expression based command language.

%prep
%autosetup

%build
export CFLAGS="%{optflags} -fcommon"
%configure
%make_build debug

%if 0%{?suse_version} > 1550
# Race conditions due to recursive make invocations (can’t track shared
# dependencies properly), hence -j1. Passing the -j option to sphinx-build
# (via SPHINXOPTS) may be more reliable, but is considered experimental.
%make_build -j1 -C doc singlehtml epub
cp doc/build/sphinx/singlehtml/{index,VisEditor}.html
%make_build -j1 man
%endif

%install
%make_install
rm -r %{buildroot}%{_datadir}/doc/vis

%check
# Only one test at a time because there seem to be file system race conditions
# in Vim (which the test suite runs to compare behavior).
%make_build -j1 test

%files
%{_bindir}/vis*
%{_datadir}/vis
%{_mandir}/man1/vis*.1%{?ext_man}
%license LICENSE
%doc README.md
%if 0%{?suse_version} > 1550
%doc doc/build/sphinx/epub/VisEditor.epub
%doc doc/build/sphinx/singlehtml/VisEditor.html
%endif

%changelog
