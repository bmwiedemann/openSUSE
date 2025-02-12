#
# spec file for package lirc
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


%bcond_with portaudio_drv

%define _udevdir %(pkg-config --variable udevdir udev)
%if ! %{defined _rundir}
%define _rundir /run
%endif
Name:           lirc
Version:        0.10.2
Release:        0
Summary:        Tools for Infrared Receivers
License:        GPL-2.0-or-later
Group:          Hardware/Other
URL:            http://www.lirc.org/
Source0:        https://downloads.sourceforge.net/project/lirc/LIRC/%{version}/lirc-%{version}.tar.bz2
Source1:        baselibs.conf
Patch0:         reproducible.patch
Patch1:         harden_irexec.service.patch
Patch2:         harden_lircd-uinput.service.patch
Patch3:         harden_lircd.service.patch
Patch4:         harden_lircmd.service.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gobject-introspection
BuildRequires:  kmod-compat
BuildRequires:  libxslt-tools
# for hw_atilibusb driver
BuildRequires:  pkgconfig
BuildRequires:  python3-PyYAML
BuildRequires:  python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libftdi1)
BuildRequires:  pkgconfig(libirman)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
%if %{with portaudio_drv}
BuildRequires:  pkgconfig(portaudio-2.0)
%endif
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(udev)
BuildRequires:  pkgconfig(x11)
Requires:       udev
Recommends:     lirc-remotes
Suggests:       lirc-kmp
Supplements:    lirc-kmp
%ifnarch s390 s390x
# for hw_i2cuser driver
BuildRequires:  linux-kernel-headers
%endif

%description
LIRC is a package that supports receiving and sending IR signals with
the most common IR remote controls. It contains a daemon that decodes
and sends IR signals, a mouse daemon that translates IR signals to
mouse movements, and a couple of user programs that allow you to
control your computer with a remote control.

%package        core
Summary:        LIRC core, always needed to run LIRC
License:        GPL-2.0-or-later
Group:          Hardware/Other
Requires(pre):  shadow
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
%{?systemd_requires}

%description    core
The LIRC core contains the lircd daemons, the devinput and
default driver and most of the applications.

%package        config
Summary:        LIRC Configuration Tools and Data
License:        GPL-2.0-or-later
Group:          Hardware/Other
Requires:       lirc-core = %{version}
Requires:       python3-PyYAML
Requires:       python3-gobject
Provides:       %{name}-remotes = %{version}
Obsoletes:      %{name}-remotes < %{version}
BuildArch:      noarch

%description    config
The LIRC config package contains tools and data  to ease the
LIRC configuration process.

%package        devel
Summary:        LIRC development files
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Requires:       libirrecord0 = %{version}
Requires:       liblirc0 = %{version}
Requires:       liblirc_client0 = %{version}
Requires:       liblirc_driver0 = %{version}

%description    devel
LIRC is a package that supports receiving and sending IR signals with
the most common IR remote controls. It contains a daemon that decodes
and sends IR signals, a mouse daemon that translates IR signals to
mouse movements, and a couple of user programs that allow you to
control your computer with a remote control.

%package -n liblirc_client0
Summary:        LIRC client library
License:        GPL-2.0-or-later
Group:          Hardware/Other

%description -n liblirc_client0
The LIRC client library. To actually use LIRC the lircd daemon from
the 'lirc' package has to be configured and started.

%package -n liblirc_driver0
Summary:        LIRC driver library
License:        GPL-2.0-or-later
Group:          Hardware/Other

%description -n liblirc_driver0
The LIRC driver library. To actually use the lirc plugins.

%package -n libirrecord0
Summary:        LIRC record library
License:        GPL-2.0-or-later
Group:          Hardware/Other

%description -n libirrecord0
The LIRC record library. To actually use the lirc plugins.

%package -n liblirc0
Summary:        LIRC driver library
License:        GPL-2.0-or-later
Group:          Hardware/Other

%description -n liblirc0
The LIRC library. LIRC is a package that supports receiving
and sending IR signals with the most common IR remote controls.

%package        disable-kernel-rc
Summary:        Disable kernel ir device handling in favor of lirc
License:        GPL-2.0-or-later
Group:          Hardware/Other
Requires:       %{name}-core = %{version}-%{release}
Recommends:     lirc-core = %{version}

%description  disable-kernel-rc
Udev rule which disables the kernel built-in handling of infrared devices
(i. e., rc* ones) by making lirc the only used protocol.

%package        drv-ftdi
Summary:        Ftdi LIRC User-Space Driver
License:        GPL-2.0-or-later
Group:          Hardware/Other
Requires:       lirc-core = %{version}

%description    drv-ftdi
LIRC user-space driver which works together with the kernel, providing
full support for the ftdi device.

%package        drv-portaudio
Summary:        Portaudio LIRC User-Space Driver
License:        LGPL-2.0-only
Group:          Hardware/Other
Requires:       lirc-core = %{version}

%description    drv-portaudio
LIRC user space driver which supports  a IR receiver in microphone input
using the portaudio library.

%package        tools-gui
Summary:        LIRC GUI tools
License:        GPL-2.0-or-later
Group:          Hardware/Other
Requires:       lirc-core = %{version}
Requires:       xorg-x11-fonts-core

%description   tools-gui
Some seldom used X11-based tools for debugging lirc configurations.

%prep
%autosetup -p1

# fix up timestamps from patching (lirc-autoconf-py310.patch)
touch tools/Makefile.in

# Don't provide or require anything from _docdir, per policy.
%global __provides_exclude_from ^%{_docdir}/.*$
%global __requires_exclude_from ^%{_docdir}/.*$

sed -i -e 's|/usr/local/etc/|%{_sysconfdir}/|' contrib/irman2lirc
sed -i -e 's/#effective-user/effective-user /' lirc_options.conf
sed -i -e '/^effective-user/s/=$/= lirc/' lirc_options.conf
sed -i -e "1{s|/usr/bin/env bash|$(which bash)|}" \
  tools/lirc-config-tool \
  tools/lirc-make-devinput

%build
%configure --enable-devinput
make %{?_smp_mflags}

%install
%make_install
chmod a+x %{buildroot}%{_bindir}/pronto2lirc
%if 0%{?suse_version} < 1600
# Create backward compatibility symlink
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}d
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}md
%endif
mkdir -p %{buildroot}%{_tmpfilesdir}
echo "d /run/lirc  0755  root  root  10d" \
    > %{buildroot}/%{_tmpfilesdir}/lirc.conf
#
# udev stuff
install -d -m 755 %{buildroot}/%{_udevdir}/rules.d
install -Dpm 644 contrib/60-lirc.rules \
    %{buildroot}%{_udevrulesdir}/60-lirc.rules
#
install -Dpm 644 contrib/99-remote-control-lirc.rules \
    %{buildroot}%{_udevrulesdir}/99-remote-control-lirc.rules
# get rid of libtool file
find %{buildroot} -type f -name "*.la" -delete -print
#
#
# Don't install documentation in a non standard directory
rm -rf %{buildroot}%{_datadir}/{,%{name}/}doc
# hide python dependency
chmod a+x %{buildroot}%{_bindir}/pronto2lirc
mkdir -p %{buildroot}%{_rundir}
# Remove old %%{_rundir}; deprecated but still installed by lirc, which is not looking for it
rm -rf %{buildroot}%{_localstatedir}
# Remove contrib folder; we will copy it into doc directory
rm -rf %{buildroot}%{_datadir}/lirc/contrib
#
rm -rf %{buildroot}%{_datadir}/lirc/plugindocs
#
rm -rf contrib/.release-process.txt.swp
# remove sources
rm -rf %{buildroot}/%{_datadir}/lirc/lirc-%{version}.tar.gz %{buildroot}/%{_datadir}/lirc/python-pkg
%fdupes -s %{buildroot}
%fdupes -s .
%python3_fix_shebang
%if %{suse_version} >= 1600
%python3_fix_shebang_path %{buildroot}%{python3_sitearch}/lirc-setup/*
%endif

%post -n liblirc_client0 -p /sbin/ldconfig
%post -n liblirc_driver0 -p /sbin/ldconfig
%post -n liblirc0 -p /sbin/ldconfig
%post -n libirrecord0 -p /sbin/ldconfig
%postun -n liblirc_client0 -p /sbin/ldconfig
%postun -n liblirc_driver0 -p /sbin/ldconfig
%postun -n liblirc0 -p /sbin/ldconfig
%postun -n libirrecord0 -p /sbin/ldconfig

%pre core
getent group lirc >/dev/null || groupadd -r lirc
getent passwd lirc >/dev/null || \
    useradd -r -g lirc -d %{_localstatedir}/log/lirc -s /sbin/nologin \
        -c "LIRC daemon user, runs lircd." lirc
usermod -a -G dialout lirc &> /dev/null || :
usermod -a -G lock lirc &> /dev/null || :
usermod -a -G input lirc &> /dev/null || :
%service_add_pre lircd.service lircmd.service lircd-uinput.service lircd-setup.service lircd.socket irexec.service

%post core
%service_add_post lircd.service lircmd.service lircd-uinput.service lircd-setup.service lircd.socket irexec.service
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%preun core
%service_del_preun lircd.service lircmd.service lircd-uinput.service lircd-setup.service lircd.socket irexec.service

%postun core
%service_del_postun lircd.service lircmd.service lircd-uinput.service lircd-setup.service lircd.socket irexec.service

%files core
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%doc doc/irxevent.keys
%doc contrib
%dir %{_datadir}/%{name}
%dir %{_libdir}/%{name}
%dir %ghost %{_rundir}/lirc
%ghost %{_rundir}/lirc/lircm
%ghost %{_rundir}/lirc/lircd
%exclude %{_bindir}/irxevent
%exclude %{_bindir}/xmode2
%{_bindir}/*
%{_sbindir}/*
%{_udevdir}/rules.d/60-%{name}.rules
%{_libdir}/%{name}/plugins
%exclude %{_libdir}/%{name}/plugins/ftdi.so
%exclude %{_mandir}/man1/irxevent.*
%exclude %{_mandir}/man1/xmode2.*
%{_mandir}/man1/*
%{_mandir}/man5/*
%{_mandir}/man8/*
%{python3_sitearch}/lirc
%{python3_sitearch}/lirc-setup
%dir %{_sysconfdir}/%{name}
%dir %{_sysconfdir}/%{name}/lircd.conf.d
%config(noreplace,missingok) %{_sysconfdir}/%{name}/lircd.conf
%config(noreplace,missingok) %{_sysconfdir}/%{name}/lircmd.conf
%config(noreplace,missingok) %{_sysconfdir}/%{name}/lirc_options.conf
%config(noreplace,missingok) %{_sysconfdir}/%{name}/lircd.conf.d/README.conf.d
%config(noreplace,missingok) %{_sysconfdir}/%{name}/lircd.conf.d/devinput.lircd.conf
%config(noreplace,missingok) %{_sysconfdir}/%{name}/irexec.lircrc
%{_unitdir}/lirc*
%{_unitdir}/irexec.service
%{_tmpfilesdir}/lirc.conf

%files devel
%dir %{_includedir}/lirc
%{_includedir}/lirc/*
%{_includedir}/lirc_client.h
%{_includedir}/lirc_driver.h
%{_includedir}/lirc_private.h
%{_libdir}/liblirc.so
%{_libdir}/libirrecord.so
%{_libdir}/liblirc_client.so
%{_libdir}/liblirc_driver.so
%{_libdir}/pkgconfig/lirc-driver.pc
%{_libdir}/pkgconfig/lirc.pc

%if %{with portaudio_drv}
%files drv-portaudio
%{_libdir}/lirc/plugins/audio.so
%{_datadir}/lirc/configs/audio.conf
%endif

%files drv-ftdi
%{_libdir}/lirc/plugins/ftdi.so
%{_datadir}/lirc/configs/ftdi.conf

%files config
%{_datadir}/lirc/configs
%exclude %{_datadir}/lirc/configs/ftdi.conf
%exclude %{_datadir}/lirc/configs/audio.conf

%files -n liblirc0
%{_libdir}/liblirc.so.*

%files -n liblirc_client0
%{_libdir}/liblirc_client.so.*

%files -n liblirc_driver0
%{_libdir}/liblirc_driver.so.*

%files -n libirrecord0
%{_libdir}/libirrecord.so.*

%files disable-kernel-rc
%{_udevrulesdir}/99-remote-control-lirc.rules

%files tools-gui
%{_bindir}/xmode2
%{_bindir}/irxevent
%{_mandir}/man1/irxevent*
%{_mandir}/man1/xmode2.1%{?ext_man}

%changelog
