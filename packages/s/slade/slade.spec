#
# spec file for package slade
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


Name:           slade
Version:        3.1.12
Release:        0
Summary:        An editor for DOOM maps and WAD/PK3 archives
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Shoot
URL:            https://github.com/sirjuddington/SLADE
Source:         https://github.com/sirjuddington/%name/archive/%version.tar.gz
Source2:        slade.desktop
Source100:      slade.appdata.xml
Patch1:         basepk3.diff
Patch2:         wx.diff
Patch3:         clzma.diff
Patch4:         0001-build-allow-deactivating-the-crash-handler-at-build-.patch
Patch10:        disable_sse.patch
Patch11:        0001-build-add-cmake-option-to-skip-Lua-components-1175.patch
# slade 3.2 will need gcc-c++>=8 and pkgconfig(fmt)>=6
BuildRequires:  ImageMagick
BuildRequires:  cmake >= 3.1
BuildRequires:  freeimage-devel
BuildRequires:  gcc-c++ >= 6
BuildRequires:  pkg-config
BuildRequires:  strip-nondeterminism
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-3_0-devel
BuildRequires:  zip
BuildRequires:  pkgconfig(clzma)
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(ftgl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(sfml-all)
BuildRequires:  pkgconfig(x11)
Provides:       bundled(dumb) = 0.9.3

%description
SLADE is an editor for Doom-engine based games and source
ports. It has the ability to view, modify, and write many different
game-specific formats, and even convert between some of them, or
from/to other generic formats such as PNG.

%prep
%setup -q -n SLADE-%version
%patch -P 1 -P 2 -P 3 -P 4 -p1
%ifnarch %ix86 x86_64
%patch10 -p0
%endif
%if 0%{?suse_version} >= 1550
%patch -P 11 -p1
%endif

%build
%define _lto_cflags %nil
%cmake -DNO_WEBVIEW=ON -DWX_GTK3=OFF -DNO_CRASHHANDLER=ON \
	-DCMAKE_C_FLAGS_RELWITHDEBINFO:STRING="%optflags" \
	-DCMAKE_CXX_FLAGS_RELWITHDEBINFO:STRING="%optflags" \
	-DNO_LUA:BOOL=TRUE
%cmake_build

%install
strip-nondeterminism build/slade.pk3
b="%buildroot"
install -Dm755 build/slade "$b/%_bindir/slade"
install -Dm644 build/slade.pk3 "$b/%_datadir/slade3/slade.pk3"

convert -strip "build/msvc/slade.ico[0]" -alpha on "%name.png"
install -Dpm0644 "%name.png" "$b/%_datadir/pixmaps/%name.png"
install -Dpm0644 %{SOURCE100} "$b/%_datadir/appdata/%name.appdata.xml"

pushd misc
for txtfile in detect_functions.txt old-simage-formats.txt stuff.txt \
    udmf11.txt udmf_zdoom.txt usdf.txt usdf_zdoom.txt
do
	install -Dm644 "$txtfile" "$b/%_datadir/slade3/misc/$txtfile"
done
popd

install -Dm644 "%_sourcedir/slade.desktop" "$b/%_datadir/applications/%name.desktop"

%files
%license gpl-2.0.txt
%doc README.md
%_bindir/slade
%_datadir/slade3/
%_datadir/pixmaps/%name.png
%_datadir/applications/%name.desktop
%_datadir/appdata/%name.appdata.xml

%changelog
