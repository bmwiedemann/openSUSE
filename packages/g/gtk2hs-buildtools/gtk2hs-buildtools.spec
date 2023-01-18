#
# spec file for package gtk2hs-buildtools
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


%global pkg_name gtk2hs-buildtools
Name:           %{pkg_name}
Version:        0.13.8.3
Release:        0
Summary:        Tools to build the Gtk2Hs suite of User Interface libraries
License:        GPL-2.0-only
URL:            https://hackage.haskell.org/package/%{name}
Source0:        https://hackage.haskell.org/package/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  alex
BuildRequires:  chrpath
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hashtables-devel
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  happy
ExcludeArch:    %{ix86}

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

%prep
%autosetup

%build
%ghc_lib_build

%install
%ghc_lib_install
%ghc_fix_rpath %{pkg_name}-%{version}

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

%changelog
