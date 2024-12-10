#
# spec file for package mumble
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
# Copyright (c) 2024 Tobias Burnus <burnus@gmx.de>
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


%bcond_without tests
%bcond_without server
Name:           mumble
Version:        1.5.735
Release:        0
Summary:        Voice Communication Client for Gamers
# Most files are BSD-3-Clause
# 3rdparty/arc4random/LICENSE: MIT
# 3rdparty/SPSCQueue: MIT
# 3rdparty/flag-icons: MIT
License:        BSD-2-Clause AND BSD-3-Clause AND MIT
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://www.mumble.info/
Source:         %{name}-%{version}.tar.xz
Source6:        baselibs.conf
# PATCH-FIX-UPSTREAM fix-64bit-only-plugins.patch -- Requires 64bit memory alignment ( https://github.com/mumble-voip/mumble/issues/5849 )
Patch0:         fix-64bit-only-plugins.patch
# Patches related to dependency unbundling
Patch100:       licenses.patch
Patch101:       mumble-unbundle-tracy.patch
Patch103:       mumble-1.5.629-unbundle-audio-backends.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.20
BuildRequires:  libboost_headers-devel
BuildRequires:  pkgconfig
BuildRequires:  cmake(Microsoft.GSL)
BuildRequires:  cmake(PocoXML)
BuildRequires:  cmake(PocoZip)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5TextToSpeech)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(avahi-compat-libdns_sd)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(nlohmann_json)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(speech-dispatcher)
BuildRequires:  pkgconfig(speexdsp)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(zlib)
%if %{with tests}
BuildRequires:  cmake(Qt5Test)
%endif
%if %{with server}
BuildRequires:  pkgconfig(libcap)
%endif
%if 0%{?suse_version} <= 1550
BuildRequires:  protobuf-devel
%else
BuildRequires:  cmake(protobuf)
%endif
%if 0%{?suse_version} > 1600
BuildRequires:  cmake(SndFile)
%else
BuildRequires:  libsndfile-devel
%endif
%ifarch x86_64
BuildRequires:  gcc-c++-32bit
Recommends:     %{name}-32bit
Conflicts:      %{name}-32bit < %{version}
%endif
%ifarch ppc
Recommends:     %{name}-64bit
Conflicts:      %{name}-64bit < %{version}
%endif

%description
Low-latency, high-quality voice communication for gamers. Includes game
linking, so voice from other players comes from the direction of their
characters, and has echo cancellation so the sound from your loudspeakers
won't be audible to other players.

%if %{with server}
%package server
Summary:        Voice Communication Server for Gamers
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       lsb-release
Recommends:     libQt5Sql5-mysql
Recommends:     libQt5Sql5-postgresql
Recommends:     libQt5Sql5-sqlite
%{?systemd_requires}

%description server
Low-latency, high-quality voice communication for gamers. Includes game
linking, so voice from other players comes from the direction of their
characters, and has echo cancellation so the sound from your loudspeakers
won't be audible to other players.
%endif

%prep
%autosetup -p1

%build
%cmake \
%if %{with server}
	-Dserver:BOOL=ON \
	-Dice:BOOL=OFF \
%else
	-Dserver:BOOL=OFF \
%endif
	-Dupdate:BOOL=OFF \
	-Dcrash-report:BOOL=OFF \
	-Ddisplay-install-paths:BOOL=ON \
	-Doverlay-xcompile:BOOL=OFF \
	-Dsymbols:BOOL=ON \
	-DMUMBLE_INSTALL_PLUGINDIR=%{_libdir}/mumble/plugins \
	-Dbundled-gsl:BOOL=OFF \
	-Dbundled-json:BOOL=OFF \
	-Dbundled-renamenoise:BOOL=ON \
	-Dbundled-speex:BOOL=OFF \
	-Dqtspeech:BOOL=ON \
	-Dbundle-qt-translations:BOOL=OFF \
%if 0%{?suse_version} > 1600
	-DCMAKE_SHARED_LINKER_FLAGS="-lGL" \
%endif
%if 0%{?suse_version} < 1600
	-Dwarnings-as-errors:BOOL=OFF \
%endif
%ifarch %{ix86}
	-Dwarnings-as-errors:BOOL=OFF \
%endif
%if 0%{?suse_version} <= 1550
	-DCMAKE_MODULE_LINKER_FLAGS="" \
	-DCMAKE_SHARED_LINKER_FLAGS="" \
%endif
%if %{with tests}
	-Dtests:BOOL=ON \
%endif
	-DCMAKE_CXX_STANDARD=17 \
%{nil}

%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a scripts README.md %{buildroot}%{_docdir}/%{name}
find %{buildroot}%{_docdir}/%{name}/scripts -type f -name '*.py' -exec chmod -x {} \;
find %{buildroot}%{_docdir}/%{name}/scripts -type f -name '*.rb' -exec chmod -x {} \;
find %{buildroot}%{_docdir}/%{name}/scripts -type f -name '*.sh' -exec chmod -x {} \;
find %{buildroot}%{_docdir}/%{name}/scripts -type f -name '*.bat' -exec chmod -x {} \;

%if %{with server}
# This was messed up by https://github.com/mumble-voip/mumble/pull/6100
# I wasted enough time trying to patch this, so this is brute force
# Also see -Ddisplay-install-paths and output of cmake
mkdir -p %{buildroot}%{_sysconfdir}/mumble
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysusersdir}
mv -v %{buildroot}%{_prefix}%{_sysconfdir}/mumble/mumble-server.ini %{buildroot}%{_sysconfdir}/mumble/mumble-server.ini
mv -v %{buildroot}%{_prefix}%{_sysconfdir}/systemd/system/mumble-server.service %{buildroot}%{_unitdir}/mumble-server.service
mv -v %{buildroot}%{_prefix}%{_sysconfdir}/sysusers.d/mumble-server.conf %{buildroot}%{_sysusersdir}/mumble-server.conf
# z not authorized and not required
rm %{buildroot}%{_prefix}%{_sysconfdir}/tmpfiles.d/mumble-server.conf
# fix path in service
sed -i -e 's|%{_prefix}%{_sysconfdir}|%{_sysconfdir}|g' %{buildroot}%{_unitdir}/mumble-server.service
%endif

%check
%if %{with tests}
# TestSettingsJSONSerialization fails loading qt xcb in headless
export QT_QPA_PLATFORM=offscreen
%ctest
%endif

%if %{with server}
%pre server
%service_add_pre mumble-server.service

%preun server
%service_del_preun mumble-server.service

%post server
%service_add_post mumble-server.service

%postun server
%service_del_postun mumble-server.service
%endif

%files
%license LICENSE
%doc %{_docdir}/%{name}
%{_bindir}/mumble
%{_bindir}/mumble-overlay
%{_mandir}/man1/mumble-overlay.1%{?ext_man}
%{_mandir}/man1/mumble.1%{?ext_man}
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/mumble.*
%{_datadir}/applications/*
%{_libdir}/mumble
%{_datadir}/metainfo/info.mumble.Mumble.appdata.xml

%if %{with server}
%files server
%license LICENSE
%{_bindir}/mumble-server
%{_bindir}/mumble-server-user-wrapper
%dir %{_sysconfdir}/mumble
%config(noreplace) %{_sysconfdir}/mumble/mumble-server.ini
%{_unitdir}/mumble-server.service
%{_sysusersdir}/mumble-server.conf
%{_mandir}/man1/mumble-server.1%{?ext_man}
%{_mandir}/man1/mumble-server-user-wrapper.1%{?ext_man}
%endif

%changelog
