#
# spec file for package gamemode
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 Matthias Bach <marix@marix.org>.
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


Name:           gamemode
Version:        1.4
Release:        0
Summary:        Daemon/library combo for changing Linux system performance on demand
License:        BSD-3-Clause
Group:          Amusements/Games/Other
URL:            https://github.com/FeralInteractive/gamemode
Source0:        gamemode-%{version}.tar.xz
Source1:        gamemode-rpmlintrc
Source2:        README.openSUSE
Source3:        baselibs.conf
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  polkit-devel
BuildRequires:  pkgconfig(dbus-1)
# Yes, it needs both
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
%if 0%{?sle_version} == 120300 && 0%{?is_opensuse}
BuildRequires:  gcc7
%endif

%description
GameMode is a daemon/lib combo for Linux that allows games to request
a set of optimisations be temporarily applied to the host OS.

GameMode was designed primarily as a stop-gap solution to problems
with the Intel and AMD CPU powersave or ondemand governors, but is
now able to launch custom user defined plugins, and is intended to be
expanded further, as there are a wealth of automation tasks one might
want to apply.

%package -n gamemoded
Summary:        The GameMode daemon required by GameMode enabled games
Group:          Amusements/Games/Other
Recommends:     libgamemode
Suggests:       libgamemodeauto

%description -n gamemoded
GameMode is a daemon/lib combo for Linux that allows games to request
a set of optimisations be temporarily applied to the host OS.

The GameMode daemon is installed as a D-Bus Service and will start
automatically on first access by a client.

%package -n libgamemode0
Summary:        GameMode client library
Group:          System/Libraries
Requires:       gamemoded
%systemd_requires

%description -n libgamemode0
GameMode is a daemon/lib combo for Linux that allows games to request
a set of optimisations be temporarily applied to the host OS.

Libgamemode is the client library used by games or libgamemodeauto to
talk to the GameMode daemon.

%package -n libgamemodeauto0
Summary:        Helper library allowing to equip any game with GameMode support
Group:          System/Libraries
Requires:       libgamemode0

%description -n libgamemodeauto0
GameMode is a daemon/lib combo for Linux that allows games to request
a set of optimisations be temporarily applied to the host OS.

Libgamemodeauto allows you to use GameMode with any Game by
preloading it into the game.

    LD_PRELOAD=%{_libdir}/libgamemodeauto.so.0 ./game

For Steam games this can be done by editing the launch options:

    LD_PRELOAD=$LD_PRELOAD:%{_libdir}/libgamemodeauto.so.0 %%command%%

%package -n libgamemode-devel
Summary:        Headers for compiling games using GameMode
Group:          Development/Libraries/C and C++
Requires:       libgamemode0 = %{version}
Requires:       libgamemodeauto0 = %{version}

%description -n libgamemode-devel
GameMode is a daemon/lib combo for Linux that allows games to request
a set of optimisations be temporarily applied to the host OS.

This package contains the headers required to compile games with
built-in GameMode support.

%prep
%setup -q

cp %{SOURCE2} .

%build
%if 0%{?sle_version} == 120300 && 0%{?is_opensuse}
export CC=gcc-7  # gcc4.8 does not work because of https://gcc.gnu.org/bugzilla/show_bug.cgi?id=58016
%endif
%meson
%meson_build

%check
%meson_test

%install
%meson_install

%post -n libgamemode0 -p /sbin/ldconfig
%postun -n libgamemode0 -p /sbin/ldconfig
%post -n libgamemodeauto0 -p /sbin/ldconfig
%postun -n libgamemodeauto0 -p /sbin/ldconfig

%files -n gamemoded
%{_bindir}/gamemoded
%{_bindir}/gamemoderun
%{_libexecdir}/cpugovctl
%{_libexecdir}/gpuclockctl
%{_userunitdir}/gamemoded.service
%{_datadir}/polkit-1/actions/com.feralinteractive.GameMode.policy
%{_datadir}/dbus-1/services/com.feralinteractive.GameMode.service
%{_mandir}/*/*
%doc example/gamemode.ini README.openSUSE
%license LICENSE.txt

%files -n libgamemode0
%{_libdir}/libgamemode.so.0*
%license LICENSE.txt

%files -n libgamemodeauto0
%{_libdir}/libgamemodeauto.so.0*
%license LICENSE.txt

%files -n libgamemode-devel
%{_includedir}/gamemode_client.h
%{_libdir}/libgamemode.so
%{_libdir}/libgamemodeauto.so
%{_libdir}/pkgconfig/gamemode*
%license LICENSE.txt

%changelog
