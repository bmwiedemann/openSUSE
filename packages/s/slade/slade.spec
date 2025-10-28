#
# spec file for package slade
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Version:        3.2.8
Release:        0
Summary:        An editor for DOOM maps and WAD/PK3 archives
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Shoot
URL:            https://github.com/sirjuddington/SLADE
Source:         https://github.com/sirjuddington/SLADE/archive/refs/tags/%version.tar.gz
Patch1:         basepk3.diff
Patch2:         wx.diff
Patch3:         clzma.diff
Patch4:         0001-build-allow-deactivating-the-crash-handler-at-build-.patch
Patch10:        disable_sse.patch
BuildRequires:  ImageMagick
BuildRequires:  cmake >= 3.1
BuildRequires:  freeimage-devel
BuildRequires:  gcc-c++ >= 8
BuildRequires:  pkg-config
BuildRequires:  strip-nondeterminism
BuildRequires:  update-desktop-files
BuildRequires:  wxGTK3-devel >= 3.1.6
BuildRequires:  zip
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(ftgl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libmpg123) >= 1.28.1
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(sfml-all)
BuildRequires:  pkgconfig(x11)
%if 0%{?suse_version} >= 1690
BuildRequires:  sfml3-devel
%endif
%if 0%{?suse_version} >= 1690
BuildRequires:  pkgconfig(lzma-sdk)
%else
BuildRequires:  pkgconfig(clzma)
%endif
%if 0%{?suse_version} >= 1600
BuildRequires:  fmt-devel
%else
Provides:       bundled(fmt) = 11.1.3
%endif
Provides:       bundled(dumb) = 0.9.3

%description
SLADE is an editor for Doom-engine based games and source
ports. It has the ability to view, modify, and write many different
game-specific formats, and even convert between some of them, or
from/to other generic formats such as PNG.

%prep
%autosetup -p1 -n SLADE-%version

%build
%define _lto_cflags %nil
%if 0%{?suse_version} >= 1600 && 0%{?suse_version} < 1690
perl -i -lpe 's{ -llzmasdk }{ -lclzma }g' thirdparty/CMakeLists.txt
%endif
%cmake -DNO_WEBVIEW=ON -DWX_GTK3=OFF -DNO_CRASHHANDLER=ON \
	-DCMAKE_C_FLAGS_RELWITHDEBINFO:STRING="$CFLAGS" \
	-DCMAKE_CXX_FLAGS_RELWITHDEBINFO:STRING="$CFLAGS" \
%if 0%{?suse_version} >= 1600
	-DUSE_SYSTEM_FMT:BOOL=ON \
%endif
	-DNO_LUA:BOOL=ON
%cmake_build

%install
strip-nondeterminism build/slade.pk3
%cmake_install

%files
%license LICENSE
%doc README.md
%_bindir/slade
%_datadir/slade3/
%_datadir/icons/hicolor/scalable/apps/net.mancubus.SLADE.svg
%_datadir/applications/net.mancubus.SLADE.desktop
%_datadir/metainfo/net.mancubus.SLADE.metainfo.xml

%changelog
