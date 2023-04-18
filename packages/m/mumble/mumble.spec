#
# spec file for package mumble
#
# Copyright (c) 2023 SUSE LLC
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


# requires libzeroc-ice, not available yet
%bcond_without ice
%bcond_without jack
%bcond_without pulseaudio
%bcond_without system_opus
%bcond_without system_speex
# mumble must be able to talk to other clients which may use
# different versions of celt. Since each celt release is
# incompatible to each other mumble bundles some specific
# versions.
%bcond_with     system_celt
Name:           mumble
Version:        1.5.517
Release:        0
Summary:        Voice Communication Client for Gamers
# For Legal: the bundled opus and speex subdirectories are not built.
# Most files are BSD-3-Clause, celt also contains BSD-2-Clause files.
License:        BSD-2-Clause AND BSD-3-Clause
Group:          Productivity/Multimedia/Sound/Utilities
URL:            http://mumble.sourceforge.net/
Source:         https://github.com/mumble-voip/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/mumble-voip/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz.sig
Source3:        murmur.apparmor
# http://mumble.info/gpg/gpg.txt
Source4:        https://raw.githubusercontent.com/mumble-voip/mumble-gpg-signatures/master/mumble-auto-build-2023.asc#/%{name}.keyring
Source5:        mumble-server.service
Source6:        baselibs.conf
# PATCH-FIX-UPSTREAM fix-64bit-only-plugins.patch -- Requires 64bit memory alignment ( https://github.com/mumble-voip/mumble/issues/5849 )
Patch0:         fix-64bit-only-plugins.patch
# PATCH-FIX-UPSTREAM fix-pkg_get_variable.patch -- CMake does not use the correct pkgconf variables ( https://github.com/mumble-voip/mumble/issues/6038 )
Patch1:         fix-pkg_get_variable.patch
BuildRequires:  cmake >= 3.15
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  libcap-devel
BuildRequires:  libogg-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libspeechd-devel
BuildRequires:  pkgconfig
BuildRequires:  protobuf-devel
BuildRequires:  update-desktop-files
BuildRequires:  cmake(PocoZip)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5TextToSpeech)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(avahi-compat-libdns_sd)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libopenssl)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xi)
Requires:       lsb-release
%if 0%{?suse_version}
BuildRequires:  sysuser-tools
%sysusers_requires
%else
Requires(pre):  /usr/sbin/useradd
Requires(pre):  /usr/sbin/groupadd
%endif
%if 0%{?sle_version} >= 150300 && 0%{?is_opensuse}
BuildRequires:  pcre2-devel
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
%if %{with ice}
BuildRequires:  pkgconfig(ice)
%endif
%if %{with pulseaudio}
BuildRequires:  pulseaudio-devel
%endif
%if %{with jack}
BuildRequires:  libjack-devel
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
Requires:       lsb-release
Requires(pre):  %{_sbindir}/useradd
Recommends:     libQt5Sql5-mysql
Recommends:     libQt5Sql5-postgresql
Recommends:     libQt5Sql5-sqlite
%{?systemd_requires}
%if 0%{?snapshot:1}
Conflicts:      mumble-server < %{version}
Provides:       mumble-server = %{version}
%endif

%description server
Low-latency, high-quality voice communication for gamers. Includes game
linking, so voice from other players comes from the direction of their
characters, and has echo cancellation so the sound from your loudspeakers
won't be audible to other players.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake \
        -Dupdate:BOOL=OFF \
        -Doverlay-xcompile:BOOL=OFF \
        -Dsymbols:BOOL=ON \
        -Dcrash-report:BOOL=OFF \
        -DMUMBLE_INSTALL_PLUGINDIR=%{_libdir}/mumble/plugins \
        -DCMAKE_MODULE_LINKER_FLAGS="" \
        -DCMAKE_SHARED_LINKER_FLAGS="" \
%if 1
        -Dice=OFF \
%endif
%if %{with system_celt}
        -Dbundled-celt:BOOL=OFF \
%endif
%if %{with system_speex}
        -Dbundled-opus:BOOL=OFF \
%endif
%if %{with system_speex}
        -Dbundled-speex:BOOL=OFF \
%endif
%if !%{with pulseaudio}
        -Dpulseaudio:BOOL=OFF \
%endif

# build fails for high -j so we overwrite with a max value that is known to work
%cmake_build -j8

%if 0%{?suse_version}
%sysusers_generate_pre auxiliary_files/config_files/mumble-server.sysusers user
%else
>server.pre
%endif

%install
%cmake_install

mkdir -p %{buildroot}%{_docdir}/%{name}
cp -a scripts LICENSE README.md %{buildroot}%{_docdir}/%{name}
find %{buildroot}%{_docdir}/%{name}/scripts -type f -name '*.py' -exec chmod -x {} \;
find %{buildroot}%{_docdir}/%{name}/scripts -type f -name '*.rb' -exec chmod -x {} \;
find %{buildroot}%{_docdir}/%{name}/scripts -type f -name '*.sh' -exec chmod -x {} \;
find %{buildroot}%{_docdir}/%{name}/scripts -type f -name '*.bat' -exec chmod -x {} \;
# Server
##
mkdir -p %{buildroot}%{_tmpfilesdir}
cat >> %{buildroot}%{_tmpfilesdir}/mumble-server.conf <<EOF
d %{_localstatedir}/run/mumble-server 0755 _mumble-server _mumble-server -
EOF
install -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/apparmor.d/usr.sbin.murmurd
install -D -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/mumble-server.service

# Mumble does not respect _sysconfdir
if [ -d %{buildroot}/usr/etc/mumble ]; then
  mv %{buildroot}/usr/etc/mumble %{buildroot}%{_sysconfdir}/
fi

# Do not package dbus service (boo#1209338)
rm -f %{buildroot}%{_datadir}/dbus-1/system.d/mumble-server.conf

%pre server
%service_add_pre mumble-server.service
%if !0%{?suse_version}
getent group _mumble-server >/dev/null || groupadd -r _mumble-server || :
getent passwd _mumble-server >/dev/null || \
    %{_sbindir}/useradd -r -d %{_localstatedir}/lib/mumble-server \
    -s /bin/false -c "Mumble VoIP Server" \
    -g _mumble-server _mumble-server 2> /dev/null || :
%endif

%preun server
%service_del_preun mumble-server.service

%post server
systemd-tmpfiles --create %{_tmpfilesdir}/mumble-server.conf || true
%service_add_post mumble-server.service

%postun server
%service_del_postun mumble-server.service

%files
%doc %{_docdir}/%{name}
%{_bindir}/mumble
%{_bindir}/mumble-overlay
%{_mandir}/man1/mumble-overlay.*
%{_mandir}/man1/mumble.*
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/mumble.*
%{_datadir}/applications/*
%{_libdir}/mumble

%files server
%{_bindir}/mumble-server*
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/mumble/*
%{_tmpfilesdir}/mumble-server.conf
%{_unitdir}/mumble-server.service
%{_sysusersdir}/mumble-server.conf
%{_mandir}/man1/mumble-server.*
%{_mandir}/man1/mumble-server-user-wrapper.*
%{_datadir}/metainfo/info.mumble.Mumble.appdata.xml
%dir %{_sysconfdir}/apparmor.d
%config %{_sysconfdir}/apparmor.d/usr.sbin.murmurd

%changelog
