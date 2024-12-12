#
# spec file for package openrct2
#
# Copyright (c) 2024 SUSE LLC
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

# disable lto build - https://github.com/OpenRCT2/OpenRCT2/issues/23180
%define _lto_cflags %{nil}

# std=c++20 now required, use GCC 12 for Leap
%if 0%{?suse_version} < 1650
%define gcc_ver 12
%endif

%define lib_suffix %{nil}
%ifarch x86_64
  %define lib_suffix 64
%endif
%define title_version 0.4.14
%define title_version_url %{title_version}
%define objects_version 1.4.11
%define openmusic_version 1.6
%define opensound_version 1.0.5
%define openrct2_version 0.4.17

Name:           openrct2
Version:        %{openrct2_version}
Release:        0
Summary:        An open source re-implementation of Roller Coaster Tycoon 2
License:        GPL-3.0-only
Group:          Amusements/Games/Strategy/Other
URL:            https://openrct2.io/
Source0:        https://github.com/OpenRCT2/OpenRCT2/archive/v%{version}/OpenRCT2-%{version}.tar.gz
Source1:        https://github.com/OpenRCT2/title-sequences/archive/v%{title_version_url}/title-sequences-%{title_version_url}.tar.gz
Source2:        https://github.com/OpenRCT2/objects/archive/v%{objects_version}.tar.gz#/objects-%{objects_version}.tar.gz
Source3:        https://github.com/OpenRCT2/Openmusic/releases/download/v%{openmusic_version}/openmusic.zip#/openmusic-%{openmusic_version}.zip
Source4:        https://github.com/OpenRCT2/OpenSoundEffects/releases/download/v%{opensound_version}/opensound.zip#/opensound-%{opensound_version}.zip
Source5:        https://raw.githubusercontent.com/OpenRCT2/OpenMusic/master/COPYING
BuildRequires:  cmake >= 3.9
BuildRequires:  fdupes
BuildRequires:  gcc%{?gcc_ver}-c++
BuildRequires:  glibc-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  nlohmann_json-devel >= 3.6.0
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  zip
BuildRequires:  pkgconfig(duktape)
BuildRequires:  pkgconfig(flac)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(icu-uc) >= 59.0
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(libzip) >= 1.0
BuildRequires:  pkgconfig(openssl) >= 1.0.0
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(vorbisfile)
BuildRequires:  pkgconfig(zlib)
Recommends:     %{name}-openmusic
Recommends:     %{name}-opensound
Recommends:     %{name}-titlesequences
Recommends:     (kdialog or zenity)
ExcludeArch:    s390x

%description
An open source clone of RollerCoaster Tycoon 2
that depends on the original game assets. On first
game start it will create a ~/.config/OpenRCT2/config.ini file
where the game_path = "" setting has to be set to a directory
into which the original game has been installed to.

%package titlesequences
Version:        %{title_version}
Summary:        Titlesequences for openRCT2
License:        CC-BY-4.0
Group:          Amusements/Games/Strategy/Other
Requires:       openrct2 = %{openrct2_version}
BuildArch:      noarch

%description titlesequences
This package contains tilesequences like the original ones
used in RollerCoaster Tycoon 1 and 2.
When using RCT1 sequences, the original RCT1 files have to be installed.

%package openmusic
Version:        %{openmusic_version}
Summary:        Open soundtracks for openRCT2
License:        CC-BY-4.0
Group:          Amusements/Games/Strategy/Other
Requires:       openrct2 = %{openrct2_version}
BuildArch:      noarch

%description openmusic
High quality soundtrack as replacement for, and addition to RollerCoaster Tycoon 2's
soundtrack.

%package opensound
Version:        %{opensound_version}
Summary:        Open soundeffects for openRCT2
License:        CC-BY-SA-4.0
Group:          Amusements/Games/Strategy/Other
Requires:       openrct2 = %{openrct2_version}
BuildArch:      noarch

%description opensound
Open source sound effects for OpenRCT2

%prep
# Autosetup doesn't work here:
# https://github.com/rpm-software-management/rpm/issues/1204
%setup -q -n OpenRCT2-%{openrct2_version} -a 1 -a 2
%autopatch -p1

# Remove build time references so build-compare can do its work
sed -i "s/__DATE__/\"openSUSE\"/" src/openrct2/Version.h
sed -i "s/__TIME__/\"Build Service\"/" src/openrct2/Version.h

%build
export CXXFLAGS="%optflags -Wno-maybe-uninitialized"

%cmake \
  -DCMAKE_C_COMPILER=gcc%{?gcc_ver:-%{gcc_ver}} \
  -DCMAKE_CXX_COMPILER=g++%{?gcc_ver:-%{gcc_ver}} \
  -DDOWNLOAD_TITLE_SEQUENCES=OFF \
  -DDOWNLOAD_OBJECTS=OFF

%make_build all
# libopenrct2 is not installed when openrct2 is called by make, so set the LD_LIBRARY_PATH
export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:$(dirname $(find . -name libopenrct2.so))"
%make_build g2
# %%cmake changes directory into "build"
cd ..

# Generate titles from source (zipping as parkseq)
pushd title-sequences-%{title_version_url}/title
  mv -v v%{title_version} openrct2
  rm -rv v*
  for dir in *; do
    pushd "$dir"
    zip -9 -X -r ../"$dir"".parkseq" *
    popd
  done
popd

%install

install -dm755 %{buildroot}%{_datadir}/%{name}/

# Move preloaded openmusic and opensound in place so cmake will pick it up
cp %{_sourcedir}/openmusic-%{openmusic_version}.zip %{buildroot}%{_datadir}/%{name}/openmusic.zip
cp %{_sourcedir}/opensound-%{opensound_version}.zip %{buildroot}%{_datadir}/%{name}/opensound.zip

%cmake_install

mkdir -p '%{buildroot}%{_datadir}/%{name}/sequence'
cp -v title-sequences-%{title_version_url}/title/*.parkseq "%{buildroot}%{_datadir}/%{name}/sequence"

mkdir -p '%{buildroot}%{_datadir}/%{name}/object'
cp -vR objects-%{objects_version}/objects/* '%{buildroot}%{_datadir}/%{name}/object'

find '%{buildroot}%{_datadir}/%{name}' -type f -exec chmod 644 \{\} \;

cp %{SOURCE5} .

# We do that in the correct docdir in the files section.
rm -rf %{buildroot}%{_datadir}/doc

%fdupes %{buildroot}%{_datadir}/%{name}

%files
%license licence.txt
%doc distribution/changelog.txt distribution/readme.txt
%{_bindir}/openrct2
%{_bindir}/openrct2-cli
%{_libdir}/libopenrct2.so
%{_mandir}/man6/openrct2.6%{?ext_man}
%{_mandir}/man6/openrct2-cli.6%{?ext_man}
%{_datadir}/openrct2/
%exclude %{_datadir}/openrct2/sequence/rct*
%exclude %{_datadir}/%{name}/openmusic.zip.zipversion
%exclude %{_datadir}/%{name}/assetpack/openrct2.music.alternative.parkap
%exclude %{_datadir}/%{name}/opensound.zip.zipversion
%exclude %{_datadir}/%{name}/assetpack/openrct2.sound.parkap
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/*.desktop
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/openrct2.appdata.xml
%{_datadir}/mime/packages/openrct2.xml

%files titlesequences
%license title-sequences-%{title_version_url}/LICENSE
%{_datadir}/openrct2/sequence/rct*

%files openmusic
%license title-sequences-%{title_version_url}/LICENSE
%{_datadir}/%{name}/openmusic.zip.zipversion
%{_datadir}/%{name}/assetpack/openrct2.music.alternative.parkap

%files opensound
%license  COPYING
%{_datadir}/%{name}/opensound.zip.zipversion
%{_datadir}/%{name}/assetpack/openrct2.sound.parkap

%changelog
