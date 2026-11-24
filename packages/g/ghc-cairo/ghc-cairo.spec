#
# spec file for package ghc-cairo
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


%global pkg_name cairo
%bcond_with ghc_prof
Name:           ghc-%pkg_name
Version:        0.13.12.0
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        Binding to the Cairo library
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%pkg_name
Source0:        https://hackage.haskell.org/package/%pkg_name-%{version}/%pkg_name-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-gtk2hs-buildtools-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-pdf)
BuildRequires:  pkgconfig(cairo-ps)
BuildRequires:  pkgconfig(cairo-svg)
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-Cabal-prof
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-gtk2hs-buildtools-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-utf8-string-prof
%endif

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

%package -n ghc-%pkg_name-doc
Summary:        Haskell %{pkg_name} library documentation
Requires:       ghc-filesystem
BuildArch:      noarch

%description -n ghc-%pkg_name-doc
This package provides the Haskell %{pkg_name} library documentation.

%if %{with ghc_prof}
%package -n ghc-%pkg_name-prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       ghc-%pkg_name-devel = %{version}-%{release}
Supplements:    (ghc-%pkg_name-devel and ghc-prof)

%description -n ghc-%pkg_name-prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
%autosetup -p1 -n %pkg_name-%{version}

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
%dir %{_datadir}/%pkg_name-%{version}
%dir %{_datadir}/%pkg_name-%{version}/gtk2
%dir %{_datadir}/%pkg_name-%{version}/gtk3
%{_datadir}/%pkg_name-%{version}/cairo-clock-icon.png
%{_datadir}/%pkg_name-%{version}/gtk2/CairoGhci.hs
%{_datadir}/%pkg_name-%{version}/gtk2/Clock.hs
%{_datadir}/%pkg_name-%{version}/gtk2/Drawing.hs
%{_datadir}/%pkg_name-%{version}/gtk2/Drawing2.hs
%{_datadir}/%pkg_name-%{version}/gtk2/Graph.hs
%{_datadir}/%pkg_name-%{version}/gtk2/Makefile
%{_datadir}/%pkg_name-%{version}/gtk2/StarAndRing.hs
%{_datadir}/%pkg_name-%{version}/gtk2/Text.hs
%{_datadir}/%pkg_name-%{version}/gtk3/CairoGhci.hs
%{_datadir}/%pkg_name-%{version}/gtk3/Clock.hs
%{_datadir}/%pkg_name-%{version}/gtk3/Drawing.hs
%{_datadir}/%pkg_name-%{version}/gtk3/Drawing2.hs
%{_datadir}/%pkg_name-%{version}/gtk3/Graph.hs
%{_datadir}/%pkg_name-%{version}/gtk3/Makefile
%{_datadir}/%pkg_name-%{version}/gtk3/StarAndRing.hs
%{_datadir}/%pkg_name-%{version}/gtk3/Text.hs

%files devel -f %{name}-devel.files

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license COPYRIGHT

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
