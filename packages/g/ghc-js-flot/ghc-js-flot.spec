#
# spec file for package ghc-js-flot
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


%global pkg_name js-flot
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        0.8.3
Release:        0
Summary:        Obtain minified flot code
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-HTTP-devel
%endif

%description
This package bundles the minified <http://www.flotcharts.org/ Flot> code (a
jQuery plotting library) into a Haskell package, so it can be depended upon by
Cabal packages. The first three components of the version number match the
upstream flot version. The package is designed to meet the redistribution
requirements of downstream users (e.g. Debian).

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

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE
%dir %{_datadir}/%{pkg_name}-%{version}
%{_datadir}/%{pkg_name}-%{version}/jquery.flot.canvas.min.js
%{_datadir}/%{pkg_name}-%{version}/jquery.flot.categories.min.js
%{_datadir}/%{pkg_name}-%{version}/jquery.flot.crosshair.min.js
%{_datadir}/%{pkg_name}-%{version}/jquery.flot.errorbars.min.js
%{_datadir}/%{pkg_name}-%{version}/jquery.flot.fillbetween.min.js
%{_datadir}/%{pkg_name}-%{version}/jquery.flot.image.min.js
%{_datadir}/%{pkg_name}-%{version}/jquery.flot.min.js
%{_datadir}/%{pkg_name}-%{version}/jquery.flot.navigate.min.js
%{_datadir}/%{pkg_name}-%{version}/jquery.flot.pie.min.js
%{_datadir}/%{pkg_name}-%{version}/jquery.flot.resize.min.js
%{_datadir}/%{pkg_name}-%{version}/jquery.flot.selection.min.js
%{_datadir}/%{pkg_name}-%{version}/jquery.flot.stack.min.js
%{_datadir}/%{pkg_name}-%{version}/jquery.flot.symbol.min.js
%{_datadir}/%{pkg_name}-%{version}/jquery.flot.threshold.min.js
%{_datadir}/%{pkg_name}-%{version}/jquery.flot.time.min.js

%files devel -f %{name}-devel.files
%doc CHANGES.txt README.md

%changelog
