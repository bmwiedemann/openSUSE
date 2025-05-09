#
# spec file for package xmoto
#
# Copyright (c) 2025 SUSE LLC
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


Name:           xmoto
Version:        0.6.3
Release:        0
Summary:        2D motocross platform game
License:        GPL-2.0-or-later
Group:          Amusements/Games/Action/Other
URL:            https://xmoto.org/
Source0:        https://github.com/xmoto/xmoto/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
# PATCH-FIX-UPSTREAM xmoto-install-icon.patch - fix install xmoto icon into the correct directory
Patch0:         xmoto-install-icon.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-data = %{version}

%description
X-Moto is a challenging 2D motocross platform game, where physics play
an all important role in the gameplay. You need to control your bike to
its limit, if you want to have a chance finishing the more difficult of
the challenges.  First you'll try just to complete the levels, while
later you'll compete with yourself and others, racing against the
clock.

%package data
Summary:        Xmoto architecture independent data
Group:          Amusements/Games/Action/Other
Requires:       %{name} = %{version}
BuildArch:      noarch

%description data
Xmoto translations and some other architecture independent data.

%prep
%autosetup -p1

%build
%cmake -DPREFER_SYSTEM_BZip2=ON -DPREFER_SYSTEM_Lua=ON -DPREFER_SYSTEM_XDG=OFF \
    -DDEFAULT_ASIAN_TTF_FILE=%{_datadir}/fonts/truetype/bkai00mp.ttf
%make_build

%install
%cmake_install
%fdupes %{buildroot}%{_datadir}/locale
mkdir -p %{buildroot}%{_datadir}/appdata
install -p -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml
%suse_update_desktop_file -i %{name}
%find_lang %{name}

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}.6%{?ext_man}

%files data -f %{name}.lang
%{_datadir}/%{name}

%changelog
