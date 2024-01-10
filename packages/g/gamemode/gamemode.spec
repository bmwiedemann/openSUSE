#
# spec file for package gamemode
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2020 Matthias Bach <marix@marix.org>.
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
Version:        1.8.1
Release:        0
Summary:        Daemon/library combo for changing Linux system performance on demand
License:        BSD-3-Clause
Group:          Amusements/Games/Other
URL:            https://github.com/FeralInteractive/gamemode
Source0:        %{URL}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        %{URL}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        gamemode-rpmlintrc
Source3:        README.openSUSE
Source4:        baselibs.conf
Source5:        feral.keyring
BuildRequires:  cmake
BuildRequires:  libinih-devel
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconfig
BuildRequires:  polkit-devel
BuildRequires:  sysuser-tools
BuildRequires:  pkgconfig(dbus-1)
# Yes, it needs both
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(systemd)
# We need to explicitly define the dependency as this is used via
# LD_PRELOAD from a shell script and thus cannot be inferred.
Requires:       libgamemodeauto0
Provides:       gamemoded:%{_bindir}/gamemoderun
Provides:       gamemoded:%{_bindir}/gamemodelist

%description
GameMode is a daemon/lib combo for Linux that allows games to request
a set of optimisations be temporarily applied to the host OS.

GameMode was designed primarily as a stop-gap solution to problems
with the Intel and AMD CPU powersave or ondemand governors, but is
now able to launch custom user defined plugins, and is intended to be
expanded further, as there are a wealth of automation tasks one might
want to apply.

For applications that don't implement the GameMode activation themselves,
you can toggle the GameMode by running them via the gamemoderun command.

    gamemoderun ./game

For Steam games this can be done by editing the launch options:

    gamemoderun %%command%%

Note that some functionalities, like modifying the CPU governor, require
the user to be in the priviledged "gamemode" group.

%package -n gamemoded
Summary:        The GameMode daemon required by GameMode enabled games
Group:          Amusements/Games/Other
Recommends:     libgamemode
Suggests:       gamemode
Suggests:       libgamemodeauto
%sysusers_requires

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

Nowadays this however can be easier done by using the gamemoderun command
from the gamemode package.

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
%autosetup -p1

cp %{SOURCE3} .

%build
%meson -Dwith-examples=false
%meson_build

%check
%meson_test

%install
%meson_install

# Fix gamemode PolKit rules being overriden by default rules
mv %{buildroot}/%{_datadir}/polkit-1/rules.d/gamemode.rules %{buildroot}/%{_datadir}/polkit-1/rules.d/40-gamemode.rules

%post -n libgamemode0 -p /sbin/ldconfig
%postun -n libgamemode0 -p /sbin/ldconfig
%post -n libgamemodeauto0 -p /sbin/ldconfig
%postun -n libgamemodeauto0 -p /sbin/ldconfig

%post -n gamemoded
%sysusers_create %{name}.conf

%files
%{_bindir}/gamemodelist
%{_bindir}/gamemoderun
%{_mandir}/*/gamemodelist*
%{_mandir}/*/gamemoderun*
%license LICENSE.txt

%files -n gamemoded
%{_bindir}/gamemoded
%{_libexecdir}/cpugovctl
%{_libexecdir}/cpucorectl
%{_libexecdir}/gpuclockctl
%{_libexecdir}/procsysctl
%{_userunitdir}/gamemoded.service
%{_datadir}/polkit-1/actions/com.feralinteractive.GameMode.policy
%{_datadir}/polkit-1/rules.d/40-gamemode.rules
%{_datadir}/dbus-1/services/com.feralinteractive.GameMode.service
%{_datadir}/metainfo/io.github.feralinteractive.gamemode.metainfo.xml
%{_mandir}/*/gamemoded*
%{_sysusersdir}/%{name}.conf
%dir %{_sysconfdir}/security/limits.d
%config(noreplace) %{_sysconfdir}/security/limits.d/10-gamemode.conf
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
%{_libdir}/pkgconfig/libgamemode*
%license LICENSE.txt

%changelog
