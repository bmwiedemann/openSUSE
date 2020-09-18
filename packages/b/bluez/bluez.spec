#
# spec file for package bluez
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2010-2020 B1 Systems GmbH, Vohburg, Germany
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


%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150200
%bcond_without mesh
%else
%bcond_with    mesh
%endif
%bcond_without bluez_deprecated
# maintained at https://github.com/seifes-opensuse-packages/bluez.git
# contributions via pull requests are welcome!
#
Name:           bluez
Version:        5.55
Release:        0
Summary:        Bluetooth Stack for Linux
License:        GPL-2.0-or-later
Group:          Hardware/Mobile
URL:            http://www.bluez.org
Source:         http://www.kernel.org/pub/linux/bluetooth/bluez-%{version}.tar.xz
# we still want debuginfo
#KEEP NOSOURCE DEBUGINFO
Source5:        baselibs.conf
Source7:        bluetooth.modprobe
# unused in the package, but allows to use "extract *.*" in source service
Source42:       README.md
NoSource:       42
# fix some logitech HID devices, bnc#681049, bnc#850478 --seife+obs@b1-systems.com
Patch1:         bluez-5.11-logitech-hid2hci.patch
Patch2:         bluez-sdp-unix-path.patch
# PATCH-FIX-UPSTREAM: find the cups dir in libexec not in libdir
Patch3:         bluez-cups-libexec.patch
# workaround for broken tests (reported upstream but not yet fixed)
Patch4:         bluez-disable-broken-tests.diff
# Move 43xx firmware path for RPi3 bluetooth support bsc#1140688
Patch10:        RPi-Move-the-43xx-firmware-into-lib-firmware.patch
# Upstream suggests to use btmon instead of hcidump and does not want those patches
# => PATCH-FIX-OPENSUSE for those two :-)
# fix some memory leak with malformed packet (reported upstream but not yet fixed)
Patch101:       CVE-2016-9800-tool-hcidump-Fix-memory-leak-with-malformed-packet.patch
Patch102:       CVE-2016-9804-tool-hcidump-Fix-memory-leak-with-malformed-packet.patch
BuildRequires:  automake
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(check)
BuildRequires:  pkgconfig(dbus-1) >= 1.6
BuildRequires:  pkgconfig(glib-2.0) >= 2.28
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(udev)
# libgio-2_0-0 has a runtime dependency on shared-mime-info, which is not
# required for building here, but causes a build loop
#!BuildIgnore:  shared-mime-info
Requires(post): systemd
Recommends:     sbc
Provides:       bluez-utils = 3.36
Obsoletes:      bluez-utils <= 3.36
Provides:       bluez-audio = 3.36
Obsoletes:      bluez-audio <= 3.36
Obsoletes:      bluez-hcidump < 5.0
Provides:       bluez-hcidump = %{version}
Obsoletes:      obexd-client < 5.0
Provides:       obexd-client = %{version}
%{?systemd_requires}
%if 0%{?suse_version} >= 1550
BuildRequires:  pkgconfig(ell) >= 0.28
%endif
%if %{with mesh}
# json-c is needed for --enable-mesh
BuildRequires:  pkgconfig(json-c)
%endif

%description
BlueZ provides support for the core Bluetooth layers and protocols.

%package devel
Summary:        Files needed for BlueZ development
License:        GPL-2.0-or-later
Group:          Development/Languages/C and C++
Requires:       libbluetooth3 = %{version}

%description devel
Files needed to develop applications for the BlueZ Bluetooth protocol
stack.

%package -n libbluetooth3
Summary:        Bluetooth Libraries
License:        GPL-2.0-or-later
Group:          System/Libraries
Provides:       bluez-libs = 3.36
Obsoletes:      bluez-libs <= 3.36

%description -n libbluetooth3
BlueZ provides support for the core Bluetooth layers and protocols.
It is uses a modular implementation. It has many interesting features:

* Multithreaded data processing
* Support for multiple Bluetooth devices
* Real hardware abstraction
* Standard socket interface to all layers
* Device and service level security support

%package cups
Summary:        CUPS Driver for Bluetooth Printers
License:        GPL-2.0-or-later
Group:          Hardware/Printing

%description cups
Contains the files required by CUPS for printing to Bluetooth-connected
printers.

%package test
Summary:        Tools for testing of various Bluetooth-functions
License:        GPL-2.0-or-later AND MIT
Group:          Development/Tools/Debuggers
Requires:       python3-dbus-python
Requires:       python3-gobject2

%description test
Contains a few tools for testing various bluetooth functions. The
BLUETOOTH trademarks are owned by Bluetooth SIG, Inc., U.S.A.

%package auto-enable-devices
Summary:        Configuration that automatically enables all bluetooth devices
License:        GPL-2.0-or-later
Group:          Hardware/Mobile
BuildArch:      noarch

%description auto-enable-devices
Contains configuration that automatically enables all bluetooth devices
that are connected to the system if no other tool is handling them (e.g.
desktop specific applets like blueman or GNOME or KDE applets).

%post auto-enable-devices
{  systemctl status -n0 bluetooth.service > /dev/null && systemctl restart bluetooth.service ; } ||:

%postun auto-enable-devices
{  systemctl status -n0 bluetooth.service > /dev/null && systemctl restart bluetooth.service ; } ||:

%if %{with bluez_deprecated}
%package deprecated
Summary:        Bluez tools that upstream considers obsolete
License:        GPL-2.0-or-later
Group:          Hardware/Mobile

%description deprecated
This package contains tools from the bluez package that are only built
if the "--enable-deprecated" switch is used. These are considered obsolete
by the upstream developers and might contain serious issues, even security
bugs. Use at your own risk.

Note that this package will go away before end of 2020, change your code
to use the modern tools instead.
%endif

%prep
%setup -q
%autopatch -p1
mkdir dbus-apis
cp -a doc/*.txt dbus-apis/
# FIXME: Change the dbus service to be a real service, not systemd launched
sed -i "s:Exec=/bin/false:Exec=%{_libexecdir}/bluetooth/obexd:g" obexd/src/org.bluez.obex.service
sed -i "/SystemdService=.*/d" obexd/src/org.bluez.obex.service
# END FIXME

# for auto-enable subpackage
echo AutoEnable=true >> src/main.conf

%build
# because of patch4...
autoreconf -fi
# --enable-experimental is needed or btattach does not build (bug?)
%configure \
	--disable-silent-rules  \
	--enable-pie		\
	--enable-library	\
	--enable-tools		\
	--enable-cups		\
	--enable-hid2hci        \
%if %{with mesh}
	--enable-mesh		\
%endif
	--enable-midi		\
	--enable-test		\
	--enable-experimental	\
%if %{with bluez_deprecated}
	--enable-deprecated	\
%endif
	--enable-datafiles	\
	--enable-sixaxis	\
%if 0%{?suse_version} >= 1550
	--enable-external-ell	\
%endif
	--with-systemdsystemunitdir=%{_unitdir}		\
	--with-systemduserunitdir=%{_userunitdir}

%make_build all

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
install --mode=0644 -D %{SOURCE7} %{buildroot}/%{_sysconfdir}/modprobe.d/50-bluetooth.conf
# no idea why this is suddenly necessary...
install --mode 0755 -d %{buildroot}%{_localstatedir}/lib/bluetooth

# FIXME: Do not delete the systemd service once we support systemd user/session services
rm %{buildroot}%{_userunitdir}/obex.service
# end FIXME

## same as in fedora...
# "make install" fails to install gatttool, used with Bluetooth Low Energy
# boo#970628
%if %{with bluez_deprecated}
install -m0755 attrib/gatttool %{buildroot}%{_bindir}
%endif

## install btgatt-client for -test package, see
## https://www.spinics.net/lists/linux-bluetooth/msg63258.html
install -m0755 tools/btgatt-client %{buildroot}%{_bindir}
# btmgmt can be useful
install -m0755 tools/btmgmt %{buildroot}%{_bindir}
# avinfo can be useful for debugging
install -m0755 tools/avinfo %{buildroot}%{_bindir}

# for auto-enable subpackage
find . -name main.conf
install --mode 0644 -D src/main.conf %{buildroot}/%{_sysconfdir}/bluetooth/main.conf

# rpmlint warnings...
cd %{buildroot}%{_libdir}/bluez/test
chmod 0644 *.py *.xml *.dtd

# fix python shebang
sed -i -e '1s/env p/p/' %{buildroot}%{_libdir}/bluez/test/{example-gatt-{client,server},test-mesh}

%if %{with mesh}
# boo#1151518
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
mv %{buildroot}%{_sysconfdir}/dbus-1/system.d/bluetooth-mesh.conf %{buildroot}%{_defaultdocdir}/%{name}
mv %{buildroot}%{_datadir}/dbus-1/system-services/org.bluez.mesh.service %{buildroot}%{_defaultdocdir}/%{name}
cat > %{buildroot}%{_defaultdocdir}/%{name}/README-mesh.SUSE << EOF
The bluetooth-mesh dbus system config has been disabled due to security
concerns. See https://bugzilla.opensuse.org/show_bug.cgi?id=1151518 for
details.

If you want to use this feature anyway, copy
bluetooth-mesh.conf to %{_sysconfdir}/dbus-1/systemd.d/ and
org.bluez.mesh.service to %{_datadir}/dbus-1/system-services/,
then reboot.
EOF
touch -r %{SOURCE0} %{buildroot}%{_defaultdocdir}/%{name}/README-mesh.SUSE
%endif

%if %{with bluez_deprecated}
mkdir -p %{buildroot}%{_localstatedir}/adm/update-messages
UM=%{buildroot}%{_localstatedir}/adm/update-messages/bluez-deprecated-%{version}-%{release}-1
cat >> $UM << EOF
WARNING:
The bluez-deprecated package contains tools that are considered obsolete by
bluez upstream. They may contain serious issues, even unfixed security bugs.
Use at your own risk.

Note that this package will go away before end of 2020, so fix your code to
use the modern tools instead!.

Have a lot of fun...
EOF
touch -r %{SOURCE0} $UM
%endif

%check
%if ! 0%{?qemu_user_space_build}
##make %%{?_smp_mflags} check
# deliberately not running parallel, as the test suite has spurious failures otherwise
%make_build check V=0
%endif

%pre
%service_add_pre bluetooth.service bluetooth-mesh.service

%post
%{?udev_rules_update:%udev_rules_update}
# todo: check if this is still obeyed / needed with systemd
%{fillup_only -n bluetooth}
# We need the bluez systemd service enabled at any time. It won't start up
# on its own, as it is triggered by udev in the end (bnc#796671)
%{_bindir}/systemctl enable bluetooth.service 2>&1 || :
%{_bindir}/systemctl daemon-reload >/dev/null 2>&1 || :

%preun
%service_del_preun bluetooth.service bluetooth-mesh.service

%postun
%service_del_postun bluetooth.service bluetooth-mesh.service

%post -n libbluetooth3 -p /sbin/ldconfig
%postun -n libbluetooth3 -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog README dbus-apis src/main.conf
%if %{with mesh}
%doc %{_defaultdocdir}/%{name}/*
%endif
%license COPYING
%{_bindir}/bluemoon
%{_bindir}/btattach
%{_bindir}/l2ping
%{_bindir}/hex2hcd
%{_bindir}/mpris-proxy
%dir %{_libdir}/bluetooth
%dir %{_libdir}/bluetooth/plugins
%{_libdir}/bluetooth/plugins/sixaxis.so
%dir %{_libexecdir}/bluetooth
%{_libexecdir}/bluetooth/bluetoothd
%if %{with mesh}
%{_libexecdir}/bluetooth/bluetooth-meshd
%endif
%{_libexecdir}/bluetooth/obexd
%{_bindir}/bluetoothctl
%{_bindir}/btmon
%if %{with mesh}
%{_bindir}/meshctl
%{_bindir}/mesh-cfgclient
%endif
%{_bindir}/bccmd
%{_prefix}/lib/udev/
%{_mandir}/man1/btattach.1%{?ext_man}
%{_mandir}/man8/bluetoothd.8%{?ext_man}
%{_mandir}/man1/bccmd.1%{?ext_man}
%{_mandir}/man1/hid2hci.1%{?ext_man}
%{_mandir}/man1/l2ping.1%{?ext_man}
%{_mandir}/man1/rctest.1%{?ext_man}
%config %{_sysconfdir}/dbus-1/system.d/bluetooth.conf
# not packaged, boo#1151518
###%%config %%{_sysconfdir}/dbus-1/system.d/bluetooth-mesh.conf
%dir %{_localstatedir}/lib/bluetooth
%dir %{_sysconfdir}/modprobe.d
%config(noreplace) %{_sysconfdir}/modprobe.d/50-bluetooth.conf
%{_unitdir}/bluetooth.service
%if %{with mesh}
%{_unitdir}/bluetooth-mesh.service
%endif
%{_datadir}/dbus-1/system-services/org.bluez.service
%{_datadir}/dbus-1/services/org.bluez.obex.service
# not packaged, boo#1151518
###%%{_datadir}/dbus-1/system-services/org.bluez.mesh.service
%{_datadir}/zsh/site-functions/_bluetoothctl

%if %{with bluez_deprecated}
%files deprecated
%{_bindir}/gatttool
%{_bindir}/hcitool
%{_bindir}/rfcomm
%{_bindir}/sdptool
%{_bindir}/ciptool
%{_bindir}/hciattach
%{_bindir}/hciconfig
%{_bindir}/hcidump
%{_mandir}/man1/hcidump.1%{?ext_man}
%{_mandir}/man1/hciattach.1%{?ext_man}
%{_mandir}/man1/hciconfig.1%{?ext_man}
%{_mandir}/man1/hcitool.1%{?ext_man}
%{_mandir}/man1/sdptool.1%{?ext_man}
%{_mandir}/man1/ciptool.1%{?ext_man}
%{_mandir}/man1/rfcomm.1%{?ext_man}
%{_localstatedir}/adm/update-messages/bluez-deprecated-%{version}-%{release}-1
%endif

%files devel
%{_includedir}/bluetooth
%{_libdir}/libbluetooth.so
%{_libdir}/pkgconfig/bluez.pc

%files -n libbluetooth3
%{_libdir}/libbluetooth.so.*
%doc AUTHORS ChangeLog README
%license COPYING

%files cups
%dir %{_libexecdir}/cups
%dir %{_libexecdir}/cups/backend
%{_libexecdir}/cups/backend/bluetooth

%files test
%{_bindir}/avinfo
#{_bindir}/hciemu
%{_bindir}/l2test
%{_bindir}/rctest
%{_bindir}/btgatt-client
%{_bindir}/btmgmt
%dir %{_libdir}/bluez
%{_libdir}/bluez/test

%files auto-enable-devices
%dir %{_sysconfdir}/bluetooth
%config(noreplace) %{_sysconfdir}/bluetooth/main.conf

%changelog
