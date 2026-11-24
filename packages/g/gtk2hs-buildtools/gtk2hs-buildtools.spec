#
# spec file for package gtk2hs-buildtools
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


%global pkg_name gtk2hs-buildtools
%bcond_with ghc_prof
Name:           %pkg_name
Version:        0.13.12.0
Release:        0
%global pkgver %pkg_name-%{version}
Summary:        Tools to build the Gtk2Hs suite of User Interface libraries
License:        GPL-2.0-only
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  alex
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hashtables-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-rpm-macros >= 2.9.2
BuildRequires:  happy
ExcludeArch:    %{ix86}
%if %{with ghc_prof}
BuildRequires:  ghc-Cabal-prof
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-hashtables-prof
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-random-prof
%endif

%description
This package provides a set of helper programs necessary to build the Gtk2Hs
suite of libraries. These tools include a modified c2hs binding tool that is
used to generate FFI declarations, a tool to build a type hierarchy that
mirrors the C type hierarchy of GObjects found in glib, and a generator for
signal declarations that are used to call back from C to Haskell.
These tools are not needed to actually run Gtk2Hs programs.

%package -n ghc-%{name}
Summary:        Haskell %{name} library

%description -n ghc-%{name}
This package provides the Haskell %{name} shared library.

%package -n ghc-%{name}-devel
Summary:        Haskell %{name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-%{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description -n ghc-%{name}-devel
This package provides the Haskell %{name} library development files.

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
%autosetup -p1

%build
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %pkg_name-%{version}

%post -n ghc-%{name}-devel
%ghc_pkg_recache

%postun -n ghc-%{name}-devel
%ghc_pkg_recache

%files
%license COPYING
%{_bindir}/gtk2hsC2hs
%{_bindir}/gtk2hsHookGenerator
%{_bindir}/gtk2hsTypeGen
%dir %{_datadir}/%{name}-%{version}
%dir %{_datadir}/%{name}-%{version}/callbackGen
%dir %{_datadir}/%{name}-%{version}/hierarchyGen
%{_datadir}/%{name}-%{version}/callbackGen/Signal.chs.template
%{_datadir}/%{name}-%{version}/hierarchyGen/Hierarchy.chs.template
%{_datadir}/%{name}-%{version}/hierarchyGen/hierarchy.list

%files -n ghc-%{name} -f ghc-%{name}.files
%license COPYING

%files -n ghc-%{name}-devel -f ghc-%{name}-devel.files

%files -n ghc-%pkg_name-doc -f ghc-%pkg_name-doc.files
%license COPYING

%if %{with ghc_prof}
%files -n ghc-%pkg_name-prof -f ghc-%pkg_name-prof.files
%endif

%changelog
