#
# spec file for package ghc-SDL
#
# Copyright (c) 2019 SUSE LLC
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


%global pkg_name SDL
Name:           ghc-%{pkg_name}
Version:        0.6.7.0
Release:        0
Summary:        Binding to libSDL
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  libSDL-devel

%description
Simple DirectMedia Layer (libSDL) is a cross-platform multimedia library
designed to provide low level access to audio, keyboard, mouse, joystick, 3D
hardware via OpenGL, and 2D video framebuffer. It is used by MPEG playback
software, emulators, and many popular games, including the award winning Linux
port of "Civilization: Call To Power.".

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires:       libSDL-devel
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%setup -q -n %{pkg_name}-%{version}

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
%dir %{_datadir}/%{pkg_name}-%{version}/Examples
%dir %{_datadir}/%{pkg_name}-%{version}/Examples/MacOSX
%{_datadir}/%{pkg_name}-%{version}/Examples/MacOSX/Main.hs
%{_datadir}/%{pkg_name}-%{version}/Examples/MacOSX/MainWrapper.hs
%{_datadir}/%{pkg_name}-%{version}/Examples/MacOSX/Makefile
%{_datadir}/%{pkg_name}-%{version}/Examples/MacOSX/mainc.c
%{_datadir}/%{pkg_name}-%{version}/MACOSX
%{_datadir}/%{pkg_name}-%{version}/README
%{_datadir}/%{pkg_name}-%{version}/WIN32

%files devel -f %{name}-devel.files
%doc changes.txt

%changelog
