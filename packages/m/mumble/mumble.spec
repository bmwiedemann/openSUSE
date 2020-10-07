#
# spec file for package mumble
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


%define ver 1.3.3
%if 0%{?fedora_version}
%bcond_without ice
%else
%bcond_with ice
%endif
%bcond_without pulseaudio
%bcond_without systemd
%bcond_without bonjour
%bcond_without system_opus
%bcond_without system_speex
# mumble must be able to talk to other clients which may use
# different versions of celt. Since each celt release is
# incompatible to each other mumble bundles some specific
# versions.
%bcond_with     system_celt
Name:           mumble
Version:        %{ver}%{?snapshot:_%{snapshot}}
Release:        0
Summary:        Voice Communication Client for Gamers
# For Legal: the bundled opus and speex subdirectories are not built.
# Most files are BSD-3-Clause, celt also contains BSD-2-Clause files.
License:        BSD-2-Clause AND BSD-3-Clause
Group:          Productivity/Multimedia/Sound/Utilities
URL:            http://mumble.sourceforge.net/
Source:         https://github.com/mumble-voip/mumble/releases/download/%{ver}%{?snapshot:-%{snapshot}}/%{name}-%{ver}%{?snapshot:-%{snapshot}}.tar.gz
Source1:        https://github.com/mumble-voip/mumble/releases/download/%{ver}%{?snapshot:-%{snapshot}}/%{name}-%{ver}%{?snapshot:-%{snapshot}}.tar.gz.sig
Source2:        mumble-server.init
Source3:        murmur.apparmor
# http://mumble.info/gpg/gpg.txt
Source4:        https://raw.githubusercontent.com/mumble-voip/mumble-gpg-signatures/master/mumble-auto-build-2020.asc#/%{name}.keyring
Source5:        mumble-server.service
Source6:        baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  libcap-devel
BuildRequires:  libogg-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libspeechd-devel
BuildRequires:  protobuf-devel
Requires:       lsb-release
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif
%if %{with bonjour}
%if 0%{?suse_version}
BuildRequires:  pkgconfig(avahi-compat-libdns_sd)
%else
BuildRequires:  avahi-compat-libdns_sd-devel
%endif
%endif
%if %{with system_celt}
BuildRequires:  libcelt-devel
Requires:       libcelt0 > 0.7.0
%endif
%if %{with system_opus}
BuildRequires:  pkgconfig(opus)
%endif
%if %{with system_speex}
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(speexdsp)
%endif
%if 0%{?suse_version}
BuildRequires:  libqt5-linguist
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5TextToSpeech)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libopenssl)
BuildRequires:  pkgconfig(xi)
%endif
%if 0%{?fedora_version}
BuildRequires:  Mesa-libGL-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  libQt5DBus-devel
BuildRequires:  libQt5Gui-devel
BuildRequires:  libQt5Network-devel
BuildRequires:  libQt5Sql-devel
BuildRequires:  libQt5Xml-devel
BuildRequires:  libXevie-devel
BuildRequires:  libXi-devel
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtsvg-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
%endif
%if %{with ice}
BuildRequires:  ice-devel
%endif
%if 0%{?mandriva_version}
BuildRequires:  -alsa-plugins
BuildRequires:  Mesa-libGL-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  libQt5DBus-devel
BuildRequires:  libQt5Gui-devel
BuildRequires:  libQt5Network-devel
BuildRequires:  libQt5Sql-devel
BuildRequires:  libQt5Xml-devel
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtsvg-devel
BuildRequires:  libxevie-devel
BuildRequires:  libxi-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
%endif
%if %{with pulseaudio}
BuildRequires:  pulseaudio-devel
%endif
%if 0%{?suse_version}
%ifarch x86_64
Recommends:     %{name}-32bit
Conflicts:      %{name}-32bit < %{version}
%endif
%ifarch ppc
Recommends:     %{name}-64bit
Conflicts:      %{name}-64bit < %{version}
%endif
%endif
#
%if 0%{?snapshot:1}
Conflicts:      mumble < %{version}
Provides:       mumble = %{version}
%endif
#

%description
Low-latency, high-quality voice communication for gamers. Includes game
linking, so voice from other players comes from the direction of their
characters, and has echo cancellation so the sound from your loudspeakers
won't be audible to other players.

%package server
Summary:        Voice Communication Server for Gamers
Group:          Productivity/Multimedia/Sound/Utilities
Requires:       libQt5Sql5-sqlite
Requires:       lsb-release
Requires(pre):  %{_sbindir}/useradd
Recommends:     libQt5Sql5-mysql
Recommends:     libQt5Sql5-postgresql
%if 0%{?snapshot:1}
Conflicts:      mumble-server < %{version}
Provides:       mumble-server = %{version}
%endif
%if %{with systemd}
%{?systemd_requires}
%endif

%description server
Low-latency, high-quality voice communication for gamers. Includes game
linking, so voice from other players comes from the direction of their
characters, and has echo cancellation so the sound from your loudspeakers
won't be audible to other players.

%prep
%setup -q -n %{name}-%{ver}
rm -v scripts/*.bak

%build
#
#
%if 0
# for not having to wait for compile when testing packaging stuff..
mkdir release
touch release/mumble release/murmurd release/libmumble.so.1.1.1
%endif
%qmake5 \
        QMAKE_CFLAGS_RELEASE="%{optflags} -Wall -fno-strict-aliasing" \
        QMAKE_CXXFLAGS_RELEASE="%{optflags} -Wall -fno-strict-aliasing" \
        QMAKE_LRELEASE="%{_bindir}/lrelease-qt5" \
        DEFINES*=NO_UPDATE_CHECK \
        DEFINES*=MUMBLE_VERSION=%{version} \
        DEFINES*=PLUGIN_PATH=%{_libdir}/mumble/plugins \
        CONFIG*=packaged \
%if 0%{?suse_version}
        DEFINES*=NO_SYSTEM_CA_OVERRIDE \
%endif
        CONFIG*=no-g15 \
        CONFIG*=no-embed-qt-translations \
%if !%{with ice}
        CONFIG*=no-ice \
%endif
%if %{with system_celt}
        CONFIG*=no-bundled-celt \
%endif
%if %{with system_speex}
        CONFIG*=no-bundled-opus \
%endif
%if %{with system_speex}
        CONFIG*=no-bundled-speex \
%endif
%if !%{with bonjour}
        CONFIG*=no-bonjour \
%endif
%if !%{with pulseaudio}
        CONFIG*=no-pulseaudio \
%endif
        CONFIG*=no-crash-report \
        -recursive
#
# Include is broken for openSUSE, so fix it.
sed -i "s,<libspeechd.h>,<speech-dispatcher/libspeechd.h>," src/mumble/TextToSpeech_unix.cpp
###
#
# deps for *.pb.cc are broken and fail for high -j so generate
# them manually first
for i in src/* ; do
       grep -q compiler_pb_make_all $i/Makefile.Release || continue
       %make_build -C $i -f Makefile.Release compiler_pb_make_all
done

%make_build

%install
# client
install -d -m 0755 "%{buildroot}%{_bindir}"
# hack to make loading libs from applicationDirPath work
install -D -m 0755 release/mumble %{buildroot}%{_libdir}/mumble/mumble
ln -s "%{_libdir}/mumble/mumble" "%{buildroot}%{_bindir}/mumble"
#
install -d -m 0755 "%{buildroot}%{_libdir}/mumble/plugins"
install -m 0755 release/plugins/*.so "%{buildroot}%{_libdir}/mumble/plugins"
install -m 755 scripts/mumble-overlay "%{buildroot}%{_bindir}/mumble-overlay"
install -d -m 0755 "%{buildroot}%{_mandir}/man1"
install -m 0644 man/*.1 "%{buildroot}%{_mandir}/man1"
#
install -D -m 0644 icons/mumble.xpm "%{buildroot}%{_datadir}/pixmaps/mumble.xpm"
install -D -m 0644 icons/mumble.svg "%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/mumble.svg"
#
install -d -m0755 "%{buildroot}%{_libdir}/mumble"
install -m0755 release/libmumble.so.*.*.* "%{buildroot}%{_libdir}/mumble"
/sbin/ldconfig -n "%{buildroot}%{_libdir}/mumble"
# do this after ldconfig as we don't need the links
%if !%{with system_celt}
install -m 644 release/libcelt0.so.0.*.* "%{buildroot}%{_libdir}/mumble"
%endif

#
# server
install -D -m 0755 release/murmurd "%{buildroot}%{_sbindir}/murmurd"
%if %{with systemd}
mkdir -p %{buildroot}%{_tmpfilesdir}
cat >> %{buildroot}%{_tmpfilesdir}/mumble-server.conf <<EOF
d %{_localstatedir}/run/mumble-server 0755 mumble-server mumble-server -
EOF
#
install -D -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/mumble-server.service
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcmumble-server
%else
install -D -m 0755 %{SOURCE2} %{buildroot}%{_initddir}/mumble-server
ln -s %{_initddir}/mumble-server %{buildroot}%{_sbindir}/rcmumble-server
%endif
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/apparmor.d/usr.sbin.murmurd
install -d -m 0755 %{buildroot}%{_bindir}
# can be launched as user too but apparmor profile doesn't make
# sense in that case. So use link to avoid the profile.
ln -s %{_sbindir}/murmurd %{buildroot}%{_bindir}/murmurd
install -D -m 0644 scripts/murmur.conf %{buildroot}%{_sysconfdir}/dbus-1/system.d/mumble-server.conf
install -D -m 0640 scripts/murmur.ini %{buildroot}%{_sysconfdir}/mumble-server.ini
# fix up config file
sed -i -e 's/^dbus=session/dbus=system/' \
        -e 's/#uname=/uname=mumble-server/' \
        -e 's@#pidfile=@pidfile=%{_localstatedir}/run/mumble-server/mumble-server.pid@' \
        -e 's@#logfile=@logfile=%{_localstatedir}/log/mumble-server/@' \
        %{buildroot}%{_sysconfdir}/mumble-server.ini
install -D -m 0755 scripts/murmur-user-wrapper %{buildroot}%{_bindir}/murmur-user-wrapper
sed -i -e '/^SYSDIR=/s@=.*@=%{_docdir}/%{name}/scripts@' %{buildroot}%{_bindir}/murmur-user-wrapper
for i in log lib run; do
        install -d -m755 %{buildroot}%{_localstatedir}/$i/mumble-server
done
#
install -d %{buildroot}/%{_datadir}/applications
%if 0%{?suse_version}
sed 's/^Categories.*/Categories=X-SuSE-Core-Game;/' \
        < scripts/mumble.desktop \
        > %{buildroot}/%{_datadir}/applications/mumble.desktop
%suse_update_desktop_file mumble
%else
install -m 644 scripts/mumble.desktop %{buildroot}/%{_datadir}/applications/mumble.desktop
%endif

mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a scripts LICENSE README README.Linux %{buildroot}%{_docdir}/%{name}
#
mkdir -p %{buildroot}%{_datadir}/appdata/
install -m 644 scripts/mumble.appdata.xml %{buildroot}%{_datadir}/appdata/mumble.appdata.xml
#

%pre server
getent group mumble-server >/dev/null || groupadd -r mumble-server || :
getent passwd mumble-server >/dev/null || \
	%{_sbindir}/useradd -r -d %{_localstatedir}/lib/mumble-server -s /bin/false -c "Mumble VoIP Server" -g mumble-server mumble-server 2> /dev/null || :
%if %{with systemd}
%service_add_pre mumble-server.service
%endif

%preun server
%if %{with systemd}
%service_del_preun mumble-server.service
%else
%stop_on_removal mumble-server
%endif

%post server
%if %{with systemd}
systemd-tmpfiles --create %{_tmpfilesdir}/mumble-server.conf || true
%service_add_post mumble-server.service
%else
%fillup_and_insserv mumble-server
%endif

%postun server
%if %{with systemd}
%service_del_postun mumble-server.service
%else
%restart_on_update mumble-server
%insserv_cleanup
%endif

%files
%exclude %{_docdir}/%{name}/scripts/murmur.ini
%doc %{_docdir}/%{name}
%{_bindir}/mumble
%{_bindir}/mumble-overlay
%{_mandir}/man1/mumble-overlay.*
%{_mandir}/man1/mumble.*
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/mumble.*
%{_datadir}/pixmaps/*
%{_datadir}/applications/*
%{_libdir}/mumble

%files server
%doc %{_docdir}/%{name}/scripts/murmur.ini
%config %{_sysconfdir}/dbus-1/system.d/mumble-server.conf
%config(noreplace) %{_sysconfdir}/mumble-server.ini
%if %{with systemd}
%{_tmpfilesdir}/mumble-server.conf
%{_unitdir}/mumble-server.service
%else
%{_initddir}/mumble-server
%endif
%{_sbindir}/rcmumble-server
%dir %{_sysconfdir}/apparmor.d
%config %{_sysconfdir}/apparmor.d/usr.sbin.murmurd
%{_sbindir}/murmurd
%{_bindir}/murmurd
%{_bindir}/murmur-user-wrapper
%{_mandir}/man1/murmurd.*
%{_mandir}/man1/murmur-user-wrapper.*
%dir %attr(-,mumble-server,mumble-server) %{_localstatedir}/lib/mumble-server
%dir %{_localstatedir}/log/mumble-server
%ghost %{_rundir}/mumble-server
%dir %{_datadir}/appdata/
%{_datadir}/appdata/mumble.appdata.xml

%changelog
