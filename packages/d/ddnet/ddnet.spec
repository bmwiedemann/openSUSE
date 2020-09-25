#
# spec file for package ddnet
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

Name:           ddnet
Version:        14.5.1
Release:        0
Summary:        DDraceNetwork, a cooperative racing mod of Teeworlds
License:        Zlib AND CC-BY-SA-3.0 AND Apache-2.0 AND MIT AND SUSE-Public-Domain
URL:            https://ddnet.tw/
Source:         https://github.com/ddnet/ddnet/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/ddnet/ddnet/pull/2684
Patch0:         steam-api.patch
Group:          Amusements/Games/Action/Race
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pnglite-devel
BuildRequires:  python3
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(gtest)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(opusfile)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(wavpack)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  libminiupnpc-devel
Requires:       %{name}-data = %{version}-%{release}
BuildRequires:  appstream-glib

%description
DDraceNetwork (DDNet) is an actively maintained version of DDRace,
a Teeworlds modification with a unique cooperative gameplay.
Help each other play through custom maps with up to 64 players,
compete against the best in international tournaments, design your
own maps, or run your own server.

%package        data
Summary:        Data files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       hicolor-icon-theme
BuildArch:      noarch

%description    data
Data files for DDraceNetwork (DDNet).

%package        server
Summary:        Standalone server for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    server
Standalone server for DDraceNetwork (DDNet).

%prep
%autosetup -p1

%build
mkdir build && cd build
cmake .. \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DPREFER_BUNDLED_LIBS=OFF \
        -DAUTOUPDATE=OFF \
        -DANTIBOT=ON \
        -DUPNP=ON \
        -DSTEAM=OFF \
        -DCMAKE_BUILD_TYPE=RelWithDebInfo
    
%make_build

%install
%cmake_install

install -Dp -m 0644 man/DDNet.6 %{buildroot}%{_mandir}/man6/DDNet.6
install -Dp -m 0644 man/DDNet-Server.6 %{buildroot}%{_mandir}/man6/DDNet-Server.6

%fdupes %{buildroot}%{_datadir}

%files
%license license.txt
%doc README.md
%{_mandir}/man6/DDNet.6%{?ext_man}
%{_bindir}/DDNet
%{_libdir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/*.appdata.xml

%files data
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/*/
%dir %{_datadir}/icons/hicolor/*/apps/

%files server
%{_mandir}/man6/DDNet-Server.6%{?ext_man}
%{_bindir}/DDNet-Server

%changelog
