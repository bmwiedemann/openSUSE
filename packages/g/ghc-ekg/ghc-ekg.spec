#
# spec file for package ghc-ekg
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


%global pkg_name ekg
Name:           ghc-%{pkg_name}
Version:        0.4.0.15
Release:        0
Summary:        Remote monitoring of processes
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/revision/8.cabal#/%{pkg_name}.cabal
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-ekg-core-devel
BuildRequires:  ghc-ekg-json-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-snap-core-devel
BuildRequires:  ghc-snap-server-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unordered-containers-devel
ExcludeArch:    %{ix86}

%description
This library lets you remotely monitor a running process over HTTP. It provides
a simple way to integrate a monitoring server into any application.

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
cp -p %{SOURCE1} %{pkg_name}.cabal

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
%dir %{_datadir}/%{pkg_name}-%{version}/assets
%{_datadir}/%{pkg_name}-%{version}/assets/bootstrap-1.4.0.min.css
%{_datadir}/%{pkg_name}-%{version}/assets/chart_line_add.png
%{_datadir}/%{pkg_name}-%{version}/assets/cross.png
%{_datadir}/%{pkg_name}-%{version}/assets/index.html
%{_datadir}/%{pkg_name}-%{version}/assets/jquery-1.6.4.min.js
%{_datadir}/%{pkg_name}-%{version}/assets/jquery.flot.min.js
%{_datadir}/%{pkg_name}-%{version}/assets/monitor.css
%{_datadir}/%{pkg_name}-%{version}/assets/monitor.js

%files devel -f %{name}-devel.files
%license LICENSE.icons LICENSE.javascript
%doc CHANGES.md README.md examples

%changelog
