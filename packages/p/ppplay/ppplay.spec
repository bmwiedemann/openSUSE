#
# spec file for package ppplay
#
# Copyright (c) 2023, Martin Hauke <mardnh@gmx.de>
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

Name:           ppplay
Version:        0.1.3+git20190918
Release:        0
Summary:        Music Tracker Modules player
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Players
URL:            https://github.com/stohrendorf/ppplay
Source0:        %{name}-%{version}.tar.xz
Patch0:         ppplay-modern-boost.patch
Patch1:         ppplay-cmake.patch
Patch2:         ppplay-sdl.patch
BuildRequires:  ImageMagick
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_serialization-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_test-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libmp3lame)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(sdl2)
#### Bundled libs
##./src/adplug/
#Provides:       bundled(adplug)

%description
PPPlay aims to combine a good old DOS looking interface with
modern technologies for playing back tracker modules.

Features
 * Module to MP3/OGG/WAV Conversion
 * Accurate forward/backward seeking
 * Plays XM, S3M, MOD, HSC and IMF
 * High-accuracy OPL Emulator

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%if 0%{?suse_version} <= 1550
%patch2 -p1
%endif

%build
%cmake \
  -DWITH_MP3LAME=OFF \
  -DWITH_OGG=OFF
%cmake_build

%install
%cmake_install
install -d %{buildroot}%{_datadir}/icons/hicolor/32x32/apps
convert ppplay.ico -strip %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/ppplay.png

%files
%license gpl-3.0.txt
%doc README.md
%{_bindir}/ppplay
%{_bindir}/badplay
%{_bindir}/imfplay
%{_datadir}/applications/ppplay.desktop
%{_datadir}/mime/packages/ppplay-hsc.xml
%{_datadir}/icons/hicolor/*x*/apps/ppplay.png
%dir %{_datadir}/ppplay
%{_datadir}/ppplay/bankdb.xml

%changelog
