#
# spec file for package openrct2
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


%define lib_suffix %{nil}
%ifarch x86_64
  %define lib_suffix 64
%endif
%define title_version 0.4.0
%define title_version_url %{title_version}
%define objects_version 1.3.5
Name:           openrct2
Version:        0.4.3
Release:        0
Summary:        An open source re-implementation of Roller Coaster Tycoon 2
License:        GPL-3.0-only
Group:          Amusements/Games/Strategy/Other
URL:            https://openrct2.io/
Source0:        https://github.com/OpenRCT2/OpenRCT2/archive/v%{version}/OpenRCT2-%{version}.tar.gz
Source1:        https://github.com/OpenRCT2/title-sequences/archive/v%{title_version_url}/title-sequences-%{title_version_url}.tar.gz
Source2:        https://github.com/OpenRCT2/objects/archive/v%{objects_version}.tar.gz#/objects-%{objects_version}.tar.gz
BuildRequires:  cmake >= 3.9
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  nlohmann_json-devel >= 3.6.0
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
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
Recommends:     (kdialog or zenity)
ExcludeArch:    s390x

%description
An open source clone of RollerCoaster Tycoon 2
that depends on the original game assets. On first
game start it will create a ~/.config/OpenRCT2/config.ini file
where the game_path = "" setting has to be set to a directory
into which the original game has been installed to.

%package titlesequences
Summary:        Titlesequences for openRCT2
Group:          Amusements/Games/Strategy/Other
Requires:       %{name} = %{version}

%description titlesequences
This package contains tilesequences like the original ones
used in RollerCoaster Tycoon 1 and 2.
When using RCT1 sequences, the original RCT1 files have to be installed.

%prep
%setup -q -n OpenRCT2-%{version} -a 1 -a 2

# Remove build time references so build-compare can do its work
sed -i "s/__DATE__/\"openSUSE\"/" src/openrct2/Version.h
sed -i "s/__TIME__/\"Build Service\"/" src/openrct2/Version.h

%build
export CXXFLAGS="%optflags -Wno-maybe-uninitialized"
%cmake -DDOWNLOAD_TITLE_SEQUENCES=OFF -DDOWNLOAD_OBJECTS=OFF
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
%cmake_install

mkdir -p '%{buildroot}%{_datadir}/%{name}/title'
cp -v title-sequences-%{title_version_url}/title/*.parkseq "%{buildroot}%{_datadir}/%{name}/title"

mkdir -p '%{buildroot}%{_datadir}/%{name}/object'
cp -vR objects-%{objects_version}/objects/* '%{buildroot}%{_datadir}/%{name}/object'

find '%{buildroot}%{_datadir}/%{name}' -type f -exec chmod 644 \{\} \;

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
%exclude %{_datadir}/openrct2/title/rct*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/applications/*.desktop
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/openrct2.appdata.xml
%{_datadir}/mime/packages/openrct2.xml

%files titlesequences
%license licence.txt
%{_datadir}/openrct2/title/rct*

%changelog
