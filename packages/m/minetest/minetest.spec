#
# spec file for package minetest
#
# Copyright (c) 2021 SUSE LLC
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


%define minetestuser %{name}
%define minetestgroup %{name}
%bcond_without leveldb
%bcond_without redis
%bcond_without postgresql
Name:           minetest
Version:        5.4.1
Release:        0
Summary:        A InfiniMiner/Minecraft inspired game
License:        LGPL-2.1-or-later AND CC-BY-SA-3.0
Group:          Amusements/Games/3D/Simulation
URL:            https://minetest.net/
Source:         https://github.com/minetest/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        minetest-rpmlintrc
Source2:        minetest@.service
# PATCH-FIX-UPSTREAM - minetest-fix-luajit-include-path.diff -- Fixes the FindLuaJIT CMake module so it also looks for moonjit’s include path
Patch0:         minetest-fix-luajit-include-path.patch
# PATCH-FIX-OPENSUSE old-desktopfile-standard.patch dmueller@suse.com -- build without 'PrefersNonDefaultGPU' option in desktopfile on Leap 15.3 and below
Patch1:         old-desktopfile-standard.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  gmp-devel
BuildRequires:  google-arimo-fonts
BuildRequires:  google-cousine-fonts
BuildRequires:  google-droid-fonts
BuildRequires:  hicolor-icon-theme
BuildRequires:  irrlicht-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  ncurses-devel
# Needed for symlink checking
BuildRequires:  opengl-games-utils
BuildRequires:  pkgconfig
BuildRequires:  spatialindex-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(zlib)
%if 0%{?sle_version} > 0 && 0%{?sle_version} <= 150300
BuildRequires:  desktop-file-utils
%else
BuildRequires:  desktop-file-utils >= 0.25
%endif
%if %{with leveldb}
BuildRequires:  leveldb-devel
%endif
%if %{with redis}
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(hiredis)
%endif
%if %{with postgresql}
BuildRequires:  postgresql-devel
# Workaround for CMake's FindPostgreSQL.cmake depending on internal
# server headers even if just building a client application.
BuildRequires:  postgresql-server-devel
%endif
Requires:       %{name}-data = %{version}
Requires:       opengl-games-utils
Recommends:     %{name}-lang
Recommends:     minetest-game
Provides:       minetest-runtime = %{version}

%description
An infinite-world block sandbox game and a game engine, inspired by
InfiniMiner, Minecraft and the like.

%lang_package

%package -n %{name}server
Summary:        Minetest server
License:        LGPL-2.1-or-later
Group:          Amusements/Games/3D/Simulation
Requires:       %{name}-data = %{version}
Requires(pre):  shadow
Recommends:     minetest-game
Provides:       minetest-runtime = %{version}
%{?systemd_requires}

%description -n %{name}server
An infinite-world block sandbox game and a game engine, inspired by
InfiniMiner, Minecraft and the like.

This package contains a minetest server.

%package data
Summary:        Minetest shared data
License:        LGPL-2.1-or-later AND CC-BY-SA-3.0
Group:          Amusements/Games/3D/Simulation
Requires:       google-arimo-fonts
Requires:       google-cousine-fonts
Requires:       google-droid-fonts
BuildArch:      noarch

%description data
An infinite-world block sandbox game and a game engine, inspired by
InfiniMiner, Minecraft and the like.

This package contains data for minetest and minetestserver.

%prep
%setup -q
%patch0 -p1
%if 0%{?sle_version} > 0 && 0%{?sle_version} <= 150300
%patch1 -p1
%endif

# Purge bundled libraries.
rm -rf lib

%build
%cmake \
  -DCUSTOM_DOCDIR="%{_docdir}/%{name}" \
  -DCUSTOM_LOCALEDIR="%{_datadir}/locale" \
  -DCUSTOM_SHAREDIR="%{_datadir}/%{name}" \
  -DBUILD_SERVER=ON \
  -DRUN_IN_PLACE=OFF \
  -DENABLE_GETTEXT=ON \
  -DENABLE_FREETYPE=ON \
  -DENABLE_SYSTEM_JSONCPP=ON \
  -DPNG_PNG_INCLUDE_DIR=$(pkg-config libpng --variable=includedir) \
  -DENABLE_SPATIAL=ON \
%if %{with leveldb}
  -DENABLE_LEVELDB=ON \
%else
  -DENABLE_LEVELDB=OFF \
%endif
%if %{with redis}
  -DENABLE_REDIS=ON \
%else
  -DENABLE_REDIS=OFF \
%endif
%if %{with postgresql}
  -DENABLE_POSTGRESQL=ON
%else
  -DENABLE_POSTGRESQL=OFF
%endif
%make_build

%install
%cmake_install

# Install the wrapper.
ln -s opengl-game-wrapper.sh %{buildroot}%{_bindir}/%{name}-wrapper
sed -i 's/^Exec=.*$/Exec=%{name}-wrapper/' \
  %{buildroot}%{_datadir}/applications/net.minetest.minetest.desktop
%suse_update_desktop_file -r net.minetest.minetest Game Simulation

# Replace fonts with symlinks (we use the system ones).
for font in Arimo-Regular Cousine-Regular DroidSansFallbackFull; do
    rm %{buildroot}%{_datadir}/%{name}/fonts/$font.ttf
    ln -s %{_datadir}/fonts/truetype/$font.ttf \
      %{buildroot}%{_datadir}/%{name}/fonts/$font.ttf
done

# Clean up.
%fdupes %{buildroot}%{_datadir}/

install -Dpm 0644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}@.service
install -Dpm 0644 minetest.conf.example \
  %{buildroot}%{_sysconfdir}/%{name}/minetest.conf.example

mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}/

%find_lang %{name}

%post
desktop-file-validate %{_datadir}/applications/net.minetest.minetest.desktop

%pre -n %{name}server
getent group %{name} > /dev/null || %{_sbindir}/groupadd -r %{minetestgroup}
getent passwd %{name} > /dev/null || \
  %{_sbindir}/useradd -r -g %{minetestgroup} -d %{_localstatedir}/lib/%{name} \
  -s /sbin/nologin -c "user for %{name}server" %{minetestuser}
%service_add_pre %{name}@.service

%post -n %{name}server
%service_add_post %{name}@.service

%preun -n %{name}server
%service_del_preun %{name}@.service

%postun -n %{name}server
%service_del_postun %{name}@.service

%files
%license LICENSE.txt
%{_bindir}/%{name}
%{_bindir}/%{name}-wrapper
%{_datadir}/applications/net.minetest.minetest.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/*%{name}.appdata.xml
%{_mandir}/man6/%{name}.6%{?ext_man}

%files lang -f %{name}.lang

%files -n %{name}server
%license LICENSE.txt
%{_bindir}/%{name}server
%attr(0755,%{minetestuser},%{minetestgroup}) %{_localstatedir}/lib/%{name}/
%{_mandir}/man6/%{name}server.6%{?ext_man}
%dir %{_sysconfdir}/%{name}
%config %{_sysconfdir}/%{name}/minetest.conf.example
%{_unitdir}/%{name}@.service

%files data
%license LICENSE.txt
%doc README.md
%doc .github/CONTRIBUTING.md
%doc .github/SECURITY.md
%doc %{_docdir}/%{name}/
%{_datadir}/%{name}/

%changelog
