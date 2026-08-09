#
# spec file for package svxlink
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define QTEL			1.3.0
# Version for the EchoLib library
%define ECHOLIB			1.3.7
# Version for the Async library
%define LIBASYNC		1.9.1
# SvxLink versions
%define SVXLINK			1.10.1
%define REMOTERX		1.6.1
# Sounds version
%define SOUNDS			25.05
Name:           svxlink
Version:        26.05.1
Release:        0
Summary:        Multi purpose voice services system for ham radio
License:        GPL-2.0-only
URL:            https://www.svxlink.org/
Source:         https://github.com/sm0svx/svxlink/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/sm0svx/svxlink-sounds-en_US-heather/releases/download/%{SOUNDS}/svxlink-sounds-en_US-heather-16k-%{SOUNDS}.tar.bz2
# PATCH-FIX-UPSTREAM svxlink-sigc-cxx17.patch gh#sm0svx/svxlink#825 mpluskal@suse.com -- the sigc++-2 find modules force --std=c++11, which overrides CMAKE_CXX_STANDARD and breaks the Qt 6 targets
Patch0:         svxlink-sigc-cxx17.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  groff-full
BuildRequires:  gzip
# qtel installs into the hicolor theme; owns the directory chain
BuildRequires:  hicolor-icon-theme
BuildRequires:  libgcrypt-devel
BuildRequires:  libgsm-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgpiod)
BuildRequires:  pkgconfig(librtlsdr)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(tcl)

%description
The SvxLink project is a multi purpose voice services system for
ham radio use. For example, EchoLink connections are supported.
Also, the SvxLink server can act as a repeater controller.

Author Tobias Blomberg (SM0SVX)

%package -n svxlink-server
Version:        %{SVXLINK}
Release:        0
Summary:        SvxLink - A general purpose voice services system
Requires:       logrotate
Requires:       shadow

%description -n svxlink-server
The SvxLink server is a general purpose voice services system for ham radio use.
Each voice service is implemented as a plugin called a module. Some examples of
voice services are: Help system, Simplex repeater, EchoLink connection.

The core of the system handle the radio interface and is quite flexible as well.
It can act both as a simplex node and as a repeater controller.

%package -n qtel
Version:        %{QTEL}
Release:        0
Summary:        The QT EchoLink Client

%description -n qtel
This package contains Qtel, the Qt EchoLink client. It is an implementation of
the EchoLink software in Qt. This is only an EchoLink client, that is it can not
be connected to a transciever to create a link. If it is a pure link node you
want, install the svxlink-server package.

%package -n libecholib1_3
Version:        %{ECHOLIB}
Release:        0
Summary:        EchoLink library

%description -n libecholib1_3
EchoLink communications library

%package -n libecholib-devel
Version:        %{ECHOLIB}
Release:        0
Summary:        Development files for the EchoLink
Requires:       libecholib1_3 = %{version}
Obsoletes:      libecholib1_3-devel < %{version}-%{release}

%description -n libecholib-devel
Development files for the EchoLink communications library

%package -n libasync1_9
Version:        %{LIBASYNC}
Release:        0
Summary:        SvxLink Async libs
Conflicts:      libasync
# soname moved 1.6 -> 1.9 with the 26.05 release
Obsoletes:      libasync1_6 < %{version}-%{release}
Provides:       libasync1_6 = %{version}-%{release}

%description -n libasync1_9
The Async library files.

%package -n libasync-devel
Version:        %{LIBASYNC}
Release:        0
Summary:        SvxLink Async development files
Requires:       libasync1_9 = %{version}

%description -n libasync-devel
The Async library development files

%prep
%autosetup -p1
tar -xjvf %{_sourcedir}/svxlink-sounds-en_US-heather-16k-%{SOUNDS}.tar.bz2

%build
cd src
%cmake \
    -DCMAKE_INSTALL_DOCDIR:PATH=%{_docdir}/%{name} \
    -DLOCAL_STATE_DIR=%{_localstatedir}
%make_jobs
%make_build man

%install
cd src
%cmake_install
cp -r ../en_US-heather-16k/* %{buildroot}%{_datadir}/svxlink/sounds
rm -f %{buildroot}/%{_libdir}/libsvxmisc.a
# 26.05 adds python helpers with "#!/usr/bin/env python3", which rpmlint rejects
for f in %{buildroot}%{_bindir}/svxreflector-status \
         %{buildroot}%{_datadir}/svxlink/ca-hook.py; do
    [ -e "$f" ] && sed -i '1s|^#!%{_bindir}/env python3$|#!%{_bindir}/python3|' "$f"
done

%suse_update_desktop_file -c qtel Qtel "EchoLink Client" qtel qtel "Network;HamRadio"
%fdupes -s %{buildroot}

%post -n libecholib1_3 -p /sbin/ldconfig
%postun -n libecholib1_3 -p /sbin/ldconfig
%post -n libasync1_9 -p /sbin/ldconfig
%postun -n libasync1_9 -p /sbin/ldconfig

%files -n svxlink-server
%doc src/svxlink/ChangeLog
%{_bindir}/svxlink
%{_bindir}/remotetrx
%{_bindir}/siglevdetcal
%{_bindir}/devcal
%{_bindir}/svxreflector
%{_bindir}/svxreflector-status
%{_sbindir}/svxlink_gpio_down
%{_sbindir}/svxlink_gpio_up
%{_datadir}/svxlink
%{_docdir}/svxlink
%config(noreplace) %{_sysconfdir}/svxlink
%dir %{_libdir}/svxlink
# 26.05 splits the logic cores out as plugins alongside the modules
%{_libdir}/svxlink/*.so
%{_mandir}/man1/devcal.1%{?ext_man}
%{_mandir}/man1/svxreflector.1%{?ext_man}
%{_mandir}/man1/remotetrx.1%{?ext_man}
%{_mandir}/man1/siglevdetcal.1%{?ext_man}
%{_mandir}/man1/svxlink.1%{?ext_man}
%{_mandir}/man5/ModuleDtmfRepeater.conf.5%{?ext_man}
%{_mandir}/man5/ModuleEchoLink.conf.5%{?ext_man}
%{_mandir}/man5/ModuleHelp.conf.5%{?ext_man}
%{_mandir}/man5/ModuleFrn.conf.5%{?ext_man}
%{_mandir}/man5/ModuleParrot.conf.5%{?ext_man}
%{_mandir}/man5/ModulePropagationMonitor.conf.5%{?ext_man}
%{_mandir}/man5/ModuleSelCallEnc.conf.5%{?ext_man}
%{_mandir}/man5/ModuleTclVoiceMail.conf.5%{?ext_man}
%{_mandir}/man5/ModuleTrx.conf.5%{?ext_man}
%{_mandir}/man5/remotetrx.conf.5%{?ext_man}
%{_mandir}/man5/svxlink.conf.5%{?ext_man}
%{_mandir}/man5/svxreflector.conf.5%{?ext_man}
%exclude %{_includedir}/svxlink

%files -n qtel
%doc src/qtel/ChangeLog
%{_bindir}/qtel
%{_datadir}/qtel
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/128x128/apps
%{_datadir}/icons/hicolor/128x128/apps/qtel.png
%{_datadir}/applications/qtel.desktop
%{_datadir}/metainfo/org.svxlink.Qtel.metainfo.xml
%{_mandir}/man1/qtel.1%{?ext_man}

%files -n libecholib1_3
%license COPYRIGHT
%doc src/echolib/ChangeLog
%{_libdir}/libecholib.so.*

%files -n libecholib-devel
%dir %{_includedir}/svxlink
%{_includedir}/svxlink/EchoLink*
%{_libdir}/libecholib.so

%files -n libasync1_9
%doc src/async/ChangeLog
%{_libdir}/libasyncaudio.so.*
%{_libdir}/libasynccore.so.*
%{_libdir}/libasynccpp.so.*
%{_libdir}/libasyncqt.so.*

%files -n libasync-devel
%dir %{_includedir}/svxlink
%{_includedir}/svxlink/Async*
%{_libdir}/libasyncaudio.so
%{_libdir}/libasynccore.so
%{_libdir}/libasynccpp.so
%{_libdir}/libasyncqt.so

%changelog
