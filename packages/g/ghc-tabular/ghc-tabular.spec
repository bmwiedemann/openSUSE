#
# spec file for package ghc-tabular
#
# Copyright (c) 2020 SUSE LLC
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


%global pkg_name tabular
Name:           ghc-%{pkg_name}
Version:        0.2.2.8
Release:        0
Summary:        Two-dimensional data tables with rendering functions
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-csv-devel
BuildRequires:  ghc-html-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-rpm-macros

%description
Tabular provides a Haskell representation of two-dimensional data tables, the
kind that you might find in a spreadsheet or or a research report. It also
comes with some default rendering functions for turning those tables into ASCII
art, simple text with an arbitrary delimiter, CSV, HTML or LaTeX.

Below is an example of the kind of output this library produces. The tabular
package can group rows and columns, each group having one of three separators
(no line, single line, double line) between its members.

> || memtest 1 | memtest 2 || time test | time test 2 >
====++===========+===========++=============+============ > A 1 || hog |
terrible || slow | slower > A 2 || pig | not bad || fast | slowest >
----++-----------+-----------++-------------+------------ > B 1 || good | awful
|| intolerable | bearable > B 2 || better | no chance || crawling | amazing > B
3 || meh | well... || worst ever | ok.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%autosetup -n %{pkg_name}-%{version}

%build
%ghc_lib_build

%install
%ghc_lib_install

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc example

%changelog
