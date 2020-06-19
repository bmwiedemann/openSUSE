#
# spec file for package ghc-SDL-mixer
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


%global pkg_name SDL-mixer
Name:           ghc-%{pkg_name}
Version:        0.6.3.0
Release:        0
Summary:        Binding to libSDL_mixer
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-SDL-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  libSDL_mixer-devel

%description
SDL_mixer is a sample multi-channel audio mixer library. It supports any number
of simultaneously playing channels of 16 bit stereo audio, plus a single
channel of music, mixed by the popular MikMod MOD, Timidity MIDI, Ogg Vorbis,
and SMPEG MP3 libraries.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires:       libSDL_mixer-devel
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
%{_datadir}/%{pkg_name}-%{version}/MACOSX
%{_datadir}/%{pkg_name}-%{version}/README
%{_datadir}/%{pkg_name}-%{version}/issues.txt

%files devel -f %{name}-devel.files

%changelog
