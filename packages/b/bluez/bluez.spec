#
# spec file for package bluez
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2010-2017 B1 Systems GmbH, Vohburg, Germany
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


Name:           bluez
Version:        5.50
Release:        0
Summary:        Bluetooth Stack for Linux
License:        GPL-2.0-or-later
Group:          Hardware/Mobile
Url:            http://www.bluez.org
Source:         http://www.kernel.org/pub/linux/bluetooth/bluez-%{version}.tar.xz
Source5:        baselibs.conf
Source7:        bluetooth.modprobe
# fix some logitech HID devices, bnc#681049, bnc#850478 --seife+obs@b1-systems.com
Patch1:         bluez-5.11-logitech-hid2hci.patch
Patch2:         bluez-sdp-unix-path.patch
# PATCH-FIX-UPSTREAM: find the cups dir in libexec not in libdir
Patch3:         bluez-cups-libexec.patch
# workaround for broken tests (reported upstream but not yet fixed)
Patch4:         bluez-5.45-disable-broken-tests.diff
# PATCH-FIX-UPSTREAM: obexd not compiled with -fpie -- seife+obs@b1-systems.com
Patch5:         0001-obexd-use-AM_LDFLAGS-for-linking.patch
# disable tests for bypass boo#1078285
Patch6:         disable_some_obex_tests.patch
# PATCH-FIX-UPSTREAM: improve profile availability on some audio devices
Patch7:         0001-policy-Add-logic-to-connect-a-Sink.patch
# PATCH-FIX-UPSTREAM a2dp fixes for newer codecs
Patch8:         bluez-5.50-a2dp-backports.patch
# PATCH-FIX-UPSTREAM tools: Fix build after y2038 changes in glibc
Patch9:         0001-tools-Fix-build-after-y2038-changes-in-glibc.patch
# Move 43xx firmware path for RPi3 bluetooth support bsc#1140688
Patch10:        RPi-Move-the-43xx-firmware-into-lib-firmware.patch
# PATCH-FIX-UPSTREAM fix build with gcc 9, picked from upstream and rebased (boo#1121404, bko#202213)
Patch11:        bluez-5.50-gcc9.patch
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
%if 0%{?suse_version} >= 1550
BuildRequires:  pkgconfig(ell) >= 0.3
%endif
BuildRequires:  pkgconfig(glib-2.0) >= 2.28
# json-c is needed for --enable-mesh
BuildRequires:  pkgconfig(json-c)
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(udev)
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
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}

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
Requires:       dbus-1-python
Requires:       python-gobject2

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

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%ifarch ppc ppc64 ppc64le
%patch6 -p1
%endif
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch101 -p1
%patch102 -p1
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
%if 0%{?suse_version} >= 1550
	--enable-mesh		\
%endif
	--enable-midi		\
	--enable-test		\
	--enable-experimental	\
	--enable-deprecated	\
	--enable-datafiles	\
	--enable-sixaxis	\
	--with-systemdsystemunitdir=%{_unitdir}		\
	--with-systemduserunitdir=%{_userunitdir}

make %{?_smp_mflags} all

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
install -m0755 attrib/gatttool %{buildroot}%{_bindir}

## install btgatt-client for -test package, see
## https://www.spinics.net/lists/linux-bluetooth/msg63258.html
install -m0755 tools/btgatt-client %{buildroot}%{_bindir}
# btmgmt can be useful
install -m0755 tools/btmgmt %{buildroot}%{_bindir}
# avinfo can be useful for debugging
install -m0755 tools/avinfo $RPM_BUILD_ROOT%{_bindir}

# for auto-enable subpackage
find . -name main.conf
install --mode 0644 -D src/main.conf %{buildroot}/%{_sysconfdir}/bluetooth/main.conf

# rpmlint warnings...
cd %{buildroot}%{_libdir}/bluez/test
chmod 0644 *.py *.xml *.dtd

# fix python shebang
sed -i -e '1s/env p/p/' %{buildroot}%{_libdir}/bluez/test/example-gatt-{client,server}

%check
%if ! 0%{?qemu_user_space_build}
##make %%{?_smp_mflags} check
# deliberately not running parallel, as the test suite has spurious failures otherwise
make check V=0
%endif

%pre
%service_add_pre bluetooth.service

%post
%{?udev_rules_update:%udev_rules_update}
# todo: check if this is still obeyed / needed with systemd
%{fillup_only -n bluetooth}
# We need the bluez systemd service enabled at any time. It won't start up
# on it's own, as it is triggered by udev in the end (bnc#796671)
/bin/systemctl enable bluetooth.service 2>&1 || :
/bin/systemctl daemon-reload >/dev/null 2>&1 || :

%preun
%service_del_preun bluetooth.service

%postun
%service_del_postun bluetooth.service

%post -n libbluetooth3 -p /sbin/ldconfig
%postun -n libbluetooth3 -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS ChangeLog README dbus-apis src/main.conf
%license COPYING
%{_bindir}/bluemoon
%{_bindir}/btattach
%{_bindir}/gatttool
%{_bindir}/hcitool
%{_bindir}/l2ping
%{_bindir}/rfcomm
%{_bindir}/sdptool
%{_bindir}/ciptool
%{_bindir}/hciattach
%{_bindir}/hciconfig
%{_bindir}/hex2hcd
%{_bindir}/mpris-proxy
%dir %{_libdir}/bluetooth
%dir %{_libdir}/bluetooth/plugins
%{_libdir}/bluetooth/plugins/sixaxis.so
%dir %{_libexecdir}/bluetooth
%{_libexecdir}/bluetooth/bluetoothd
%{_libexecdir}/bluetooth/obexd
%{_bindir}/bluetoothctl
%{_bindir}/btmon
%if 0%{?suse_version} >= 1550
%{_bindir}/meshctl
%endif
%{_bindir}/hcidump
%{_bindir}/bccmd
%{_libexecdir}/udev/
%{_mandir}/man1/btattach.1%{ext_man}
%{_mandir}/man1/hcidump.1%{ext_man}
%{_mandir}/man1/hciattach.1%{ext_man}
%{_mandir}/man1/hciconfig.1%{ext_man}
%{_mandir}/man8/bluetoothd.8%{ext_man}
%{_mandir}/man1/hid2hci.1%{ext_man}
%{_mandir}/man1/bccmd.1%{ext_man}
%{_mandir}/man1/l2ping.1%{ext_man}
%{_mandir}/man1/hcitool.1%{ext_man}
%{_mandir}/man1/sdptool.1%{ext_man}
%{_mandir}/man1/ciptool.1%{ext_man}
%{_mandir}/man1/rfcomm.1%{ext_man}
%{_mandir}/man1/rctest.1%{ext_man}
%config %{_sysconfdir}/dbus-1/system.d/bluetooth.conf
%dir %{_localstatedir}/lib/bluetooth
%dir %{_sysconfdir}/modprobe.d
%config(noreplace) %{_sysconfdir}/modprobe.d/50-bluetooth.conf
%{_unitdir}/bluetooth.service
%{_datadir}/dbus-1/system-services/org.bluez.service
%{_datadir}/dbus-1/services/org.bluez.obex.service

%files devel
%defattr(-, root, root)
%{_includedir}/bluetooth
%{_libdir}/libbluetooth.so
%{_libdir}/pkgconfig/bluez.pc

%files -n libbluetooth3
%defattr(-, root, root)
%{_libdir}/libbluetooth.so.*
%doc AUTHORS ChangeLog README
%license COPYING

%files cups
%defattr(-,root,root)
%dir %{_libexecdir}/cups
%dir %{_libexecdir}/cups/backend
%{_libexecdir}/cups/backend/bluetooth

%files test
%defattr(-,root,root)
%{_bindir}/avinfo
#{_bindir}/hciemu
%{_bindir}/l2test
%{_bindir}/rctest
%{_bindir}/btgatt-client
%{_bindir}/btmgmt
%dir %{_libdir}/bluez
%{_libdir}/bluez/test

%files auto-enable-devices
%defattr(-,root,root)
%dir %{_sysconfdir}/bluetooth
%config(noreplace) %{_sysconfdir}/bluetooth/main.conf

%changelog
