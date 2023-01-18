#
# spec file for package ghc-cairo
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


%global pkg_name cairo
Name:           ghc-%{pkg_name}
Version:        0.13.8.2
Release:        0
Summary:        Binding to the Cairo library
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-gtk2hs-buildtools-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-pdf)
BuildRequires:  pkgconfig(cairo-ps)
BuildRequires:  pkgconfig(cairo-svg)
ExcludeArch:    %{ix86}

%description
Cairo is a library to render high quality vector graphics. There exist various
backends that allows rendering to Gtk windows, PDF, PS, PNG and SVG documents,
amongst others.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires:       pkgconfig
Requires:       pkgconfig(cairo)
Requires:       pkgconfig(cairo-pdf)
Requires:       pkgconfig(cairo-ps)
Requires:       pkgconfig(cairo-svg)
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
%license COPYRIGHT
%dir %{_datadir}/%{pkg_name}-%{version}
%dir %{_datadir}/%{pkg_name}-%{version}/gtk2
%dir %{_datadir}/%{pkg_name}-%{version}/gtk3
%{_datadir}/%{pkg_name}-%{version}/cairo-clock-icon.png
%{_datadir}/%{pkg_name}-%{version}/gtk2/CairoGhci.hs
%{_datadir}/%{pkg_name}-%{version}/gtk2/Clock.hs
%{_datadir}/%{pkg_name}-%{version}/gtk2/Drawing.hs
%{_datadir}/%{pkg_name}-%{version}/gtk2/Drawing2.hs
%{_datadir}/%{pkg_name}-%{version}/gtk2/Graph.hs
%{_datadir}/%{pkg_name}-%{version}/gtk2/Makefile
%{_datadir}/%{pkg_name}-%{version}/gtk2/StarAndRing.hs
%{_datadir}/%{pkg_name}-%{version}/gtk2/Text.hs
%{_datadir}/%{pkg_name}-%{version}/gtk3/CairoGhci.hs
%{_datadir}/%{pkg_name}-%{version}/gtk3/Clock.hs
%{_datadir}/%{pkg_name}-%{version}/gtk3/Drawing.hs
%{_datadir}/%{pkg_name}-%{version}/gtk3/Drawing2.hs
%{_datadir}/%{pkg_name}-%{version}/gtk3/Graph.hs
%{_datadir}/%{pkg_name}-%{version}/gtk3/Makefile
%{_datadir}/%{pkg_name}-%{version}/gtk3/StarAndRing.hs
%{_datadir}/%{pkg_name}-%{version}/gtk3/Text.hs

%files devel -f %{name}-devel.files

%changelog
