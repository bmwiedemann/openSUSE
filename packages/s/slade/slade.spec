#
# spec file for package slade
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           slade
Version:        3.1.1.5
Release:        0
Summary:        An editor for DOOM maps and WAD/PK3 archives
License:        GPL-2.0-or-later
Group:          Amusements/Games/3D/Shoot
Url:            https://github.com/sirjuddington/SLADE
Source:         https://github.com/sirjuddington/%name/archive/%version.tar.gz
Source2:        slade.desktop
Source100:      slade.appdata.xml
Patch1:         basepk3.diff
Patch2:         wxChar.patch
Patch10:        disable_sse.patch
# PATCH-FIX-UPSTREAM https://github.com/sirjuddington/SLADE/pull/892 
Patch11:        reproducible.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ImageMagick
BuildRequires:  cmake
BuildRequires:  freeimage-devel
BuildRequires:  gcc-c++
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-3_0-devel
BuildRequires:  zip
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(ftgl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(sfml-all)
BuildRequires:  pkgconfig(x11)
%if 0%{?suse_version} > 1320
BuildRequires:  strip-nondeterminism
%endif

%description
SLADE3 is a modern editor for Doom-engine based games and source
ports. It has the ability to view, modify, and write many different
game-specific formats, and even convert between some of them, or
from/to other generic formats such as PNG.

%prep
%setup -qn SLADE-%version
%patch -P 1 -P 2 -p1
%ifnarch %{ix86} x86_64
%patch10 -p0
%endif
%patch11 -p1

%build
%cmake -DUSE_WEBKIT_STARTPAGE=ON
make %{?_smp_mflags}

%install
%if 0%{?suse_version} > 1320
strip-nondeterminism build/slade.pk3
%endif
b="%buildroot"
install -Dm755 build/slade "$b/%_bindir/slade"
install -Dm644 build/slade.pk3 "$b/%_datadir/slade3/slade.pk3"

convert -strip "build/msvc/slade.ico[0]" -alpha on "%name.png"
install -Dpm0644 "%name.png" "$b/%_datadir/pixmaps/%name.png"
install -Dpm0644 %{SOURCE100} "$b/%_datadir/appdata/%name.appdata.xml"

pushd misc
for txtfile in detect_functions.txt old-simage-formats.txt stuff.txt udmf11.txt \
               udmf_zdoom.txt usdf.txt usdf_zdoom.txt
do
	install -Dm644 $txtfile "$b/%_datadir/slade3/misc/$txtfile"
done
popd

install -Dm644 "%_sourcedir/slade.desktop" "$b/%_datadir/applications/%name.desktop"

%if 0%{?suse_version} <= 1320
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%defattr(-,root,root)
%doc gpl-2.0.txt README.md
%_bindir/slade
%_datadir/slade3/
%_datadir/pixmaps/%name.png
%_datadir/applications/%name.desktop
%_datadir/appdata/%name.appdata.xml

%changelog
