#
# spec file for package ghc-js-chart
#
# Copyright (c) 2021 SUSE LLC
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


%global pkg_name js-chart
Name:           ghc-%{pkg_name}
Version:        2.9.4.1
Release:        0
Summary:        Obtain minified chart.js code
License:        MIT
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
ExcludeArch:    %{ix86}

%description
This package bundles the minified <http://www.chartjs.org/ chart.js> code into
a Haskell package, so it can be depended upon by Cabal packages. The first
three components of the version number match the upstream chart.js version.
The package is designed to meet the redistribution requirements of downstream
users (e.g. Debian). This package is a fork of
<https://hackage.haskell.org/package/js-flot js-flot> using chart.js instead of
flot.

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
%dir %{_datadir}/%{pkg_name}-%{version}
%{_datadir}/%{pkg_name}-%{version}/Chart.bundle.min.js
%{_datadir}/%{pkg_name}-%{version}/Chart.min.css
%{_datadir}/%{pkg_name}-%{version}/Chart.min.js

%files devel -f %{name}-devel.files
%doc CHANGELOG.md README.md

%changelog
