#
# spec file for package svxlink
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define QTEL			1.2.2
# Version for the EchoLib library
%define ECHOLIB			1.3.2
# Version for the Async library
%define LIBASYNC		1.4.0
# SvxLink versions
%define SVXLINK			1.5.0
%define REMOTERX		1.2.0
# Sounds version
%define SOUNDS			18.03.1
Name:           svxlink
Version:        17.12.2
Release:        0
Summary:        Multi purpose voice services system for ham radio
License:        GPL-2.0-only
Group:          Productivity/Hamradio/Other
URL:            https://www.svxlink.org/
Source:         https://github.com/sm0svx/svxlink/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/sm0svx/svxlink-sounds-en_US-heather/releases/download/%{SOUNDS}/svxlink-sounds-en_US-heather-16k-%{SOUNDS}.tar.bz2
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  groff-full
BuildRequires:  gzip
BuildRequires:  libgcrypt-devel
BuildRequires:  libgsm-devel
BuildRequires:  libqt4-devel
BuildRequires:  pkgconfig
BuildRequires:  tcl-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(librtlsdr)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRequires:  pkgconfig(speex)

%description
The SvxLink project is a multi purpose voice services system for
ham radio use. For example, EchoLink connections are supported.
Also, the SvxLink server can act as a repeater controller.

Author Tobias Blomberg (SM0SVX)

%package -n svxlink-server
Version:        %{SVXLINK}
Summary:        SvxLink - A general purpose voice services system
Group:          Productivity/Hamradio/Other
Requires:       logrotate
Requires:       pwdutils

%description -n svxlink-server
The SvxLink server is a general purpose voice services system for ham radio use.
Each voice service is implemented as a plugin called a module. Some examples of
voice services are: Help system, Simplex repeater, EchoLink connection.

The core of the system handle the radio interface and is quite flexible as well.
It can act both as a simplex node and as a repeater controller.

%package -n qtel
Version:        %{QTEL}
Summary:        The QT EchoLink Client
Group:          Productivity/Hamradio/Other

%description -n qtel
This package contains Qtel, the Qt EchoLink client. It is an implementation of
the EchoLink software in Qt. This is only an EchoLink client, that is it can not
be connected to a transciever to create a link. If it is a pure link node you
want, install the svxlink-server package.

%package -n libecholib1_3
Version:        %{ECHOLIB}
Summary:        EchoLink library
Group:          Productivity/Hamradio/Other

%description -n libecholib1_3
EchoLink communications library

%package -n libecholib1_3-devel
Version:        %{ECHOLIB}
Summary:        Development files for the EchoLink
Group:          Development/Libraries/Other
Requires:       libecholib1_3 = %{version}

%description -n libecholib1_3-devel
Development files for the EchoLink communications library

%package -n libasync
Version:        %{LIBASYNC}
Summary:        SvxLink Async libs
Group:          Productivity/Hamradio/Other

%description -n libasync
The Async library files.

%package -n libasync-devel
Version:        %{LIBASYNC}
Summary:        SvxLink Async development files
Group:          Development/Libraries/Other
Requires:       libasync = %{version}

%description -n libasync-devel
The Async library development files

%prep
%setup -q
tar -xjvf $RPM_SOURCE_DIR/svxlink-sounds-en_US-heather-16k-%{SOUNDS}.tar.bz2

%build
cd src
%cmake \
    -DLOCAL_STATE_DIR=%{_localstatedir}
%make_jobs
make %{?_smp_mflags} man

%install
cd src
%cmake_install
cp -r ../en_US-heather-16k/* %{buildroot}%{_datadir}/svxlink/sounds
rm -f %{buildroot}/%{_libdir}/libsvxmisc.a
%suse_update_desktop_file -c qtel Qtel "EchoLink Client" qtel "%{_datadir}/icons/link.xpm" "Network;HamRadio"
%fdupes -s %{buildroot}

%post -n libecholib1_3 -p /sbin/ldconfig
%postun -n libecholib1_3 -p /sbin/ldconfig
%post -n libasync -p /sbin/ldconfig
%postun -n libasync -p /sbin/ldconfig

%files -n svxlink-server
%doc src/svxlink/ChangeLog
%{_bindir}/svxlink
%{_bindir}/remotetrx
%{_bindir}/siglevdetcal
%{_bindir}/devcal
%{_bindir}/svxreflector
%{_sbindir}/svxlink_gpio_down
%{_sbindir}/svxlink_gpio_up
%{_datadir}/svxlink
%{_datadir}/doc/svxlink
%config(noreplace) %{_sysconfdir}/svxlink
%dir %{_libdir}/svxlink
%{_libdir}/svxlink/Module*.so
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
%{_mandir}/man5/remotetrx.conf.5%{?ext_man}
%{_mandir}/man5/svxlink.conf.5%{?ext_man}
%{_mandir}/man5/svxreflector.conf.5%{?ext_man}
%exclude %{_includedir}/svxlink

%files -n qtel
%doc src/qtel/ChangeLog
%{_bindir}/qtel
%{_datadir}/qtel
%{_datadir}/icons/link.xpm
%{_datadir}/applications/qtel.desktop
%{_mandir}/man1/qtel.1%{?ext_man}

%files -n libecholib1_3
%license COPYRIGHT
%doc src/echolib/ChangeLog
%{_libdir}/libecholib.so.*

%files -n libecholib1_3-devel
%dir %{_includedir}/svxlink
%{_includedir}/svxlink/EchoLink*
%{_libdir}/libecholib.so

%files -n libasync
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
