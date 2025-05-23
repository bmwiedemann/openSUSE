#
# spec file for package bluez
#
# Copyright (c) 2025 SUSE LLC
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

%if 0%{?suse_version} < 1550 && 0%{?sle_version} <= 150300
# systemd-rpm-macros is wrong in 15.3 and below
%global _modprobedir /lib/modprobe.d
%endif
%global modprobe_d_files 50-bluetooth.conf

%if %{undefined _firmwaredir}
%define _firmwaredir /lib/firmware
%endif

Name:           bluez
Version:        5.79
Release:        0
Summary:        Bluetooth Stack for Linux
License:        GPL-2.0-or-later
Group:          Hardware/Mobile
URL:            https://www.bluez.org
Source:         https://www.kernel.org/pub/linux/bluetooth/bluez-%{version}.tar.xz
# we still want debuginfo
#KEEP NOSOURCE DEBUGINFO
Source5:        baselibs.conf
Source7:        bluetooth.modprobe
Source9:        bluez.changes.sle
# fix some logitech HID devices, bnc#681049, bnc#850478 --seife+obs@b1-systems.com
Patch1:         bluez-5.11-logitech-hid2hci.patch
Patch2:         bluez-sdp-unix-path.patch
# avoid cups-devel buildrequires --seife+obs@b1-systems.com
Patch3:         bluez-no-cups-devel-buildreq.patch
# workaround for broken tests (reported upstream but not yet fixed)
Patch4:         bluez-disable-broken-tests.diff
# disable tests for bypass boo#1078285
Patch12:        disable_some_obex_tests.patch
# bsc#1013708 CVE-2016-9797
Patch14:        hcidump-Add-assoc-dump-function-assoc-date-length-ch.patch
# bsc#1015171 CVE-2016-9917
Patch15:        hcidump-Fix-memory-leak-with-malformed-packet.patch
# bsc#1013712 CVE-2016-9798
Patch16:        hcidump-Fixed-malformed-segment-frame-length.patch
# Upstream suggests to use btmon instead of hcidump and does not want those patches
# => PATCH-FIX-OPENSUSE for those two :-)
Patch17:        bluez-5.79-c23.patch
Patch18:        bluez-5.79-stdarg.patch
# fix some memory leak with malformed packet (reported upstream but not yet fixed)
Patch101:       CVE-2016-9800-tool-hcidump-Fix-memory-leak-with-malformed-packet.patch
Patch102:       CVE-2016-9804-tool-hcidump-Fix-memory-leak-with-malformed-packet.patch
# Move 43xx firmware path for RPi3 bluetooth support bsc#1140688 bsc#995059 bsc#1094902
Patch201:       0001-rpi3-bcm43xx-The-UART-speed-must-be-reset-after-the-firmw.patch
# mesh-cfgtest only compiles with gcc8 or newer, Leap 15 has gcc7.5.0 as default
%if 0%{?suse_version} < 1550
BuildRequires:  gcc8
%endif
BuildRequires:  automake
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(check)
## we use bluez-no-cups-devel-buildreq.patch instead to avoid a build loop
# BuildRequires:  pkgconfig(cups)
BuildRequires:  pkgconfig(dbus-1) >= 1.6
BuildRequires:  pkgconfig(glib-2.0) >= 2.28
BuildRequires:  pkgconfig(libcap-ng)
BuildRequires:  pkgconfig(libical)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(udev)
# for rst2man
BuildRequires:  python3-docutils
BuildRequires:  python3-Pygments
# libgio-2_0-0 has a runtime dependency on shared-mime-info, which is not
# required for building here, but causes a build loop
#!BuildIgnore:  shared-mime-info
Requires(post): systemd
Recommends:     sbc
Provides:       bluez-utils = 3.36
Obsoletes:      bluez-utils < 3.36
Provides:       bluez-audio = 3.36
Obsoletes:      bluez-audio < 3.36
Obsoletes:      bluez-hcidump < 5.0
Provides:       bluez-hcidump = %{version}
Obsoletes:      obexd-client < 5.0
Provides:       obexd-client = %{version}
%{?systemd_requires}
%if 0%{?suse_version} >= 1550
BuildRequires:  pkgconfig(ell) >= 0.39
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
Obsoletes:      bluez-libs < 3.36

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
Requires:       %{name}
Requires:       cups
Supplements:    (%{name} and cups)

%description cups
Contains the files required by CUPS for printing to Bluetooth-connected
printers.

%package test
Summary:        Tools for testing of various Bluetooth-functions
License:        GPL-2.0-or-later AND MIT
Group:          Development/Tools/Debuggers
Requires:       python3-dbus-python
Requires:       python3-gobject

%description test
Contains a few tools for testing various bluetooth functions. The
BLUETOOTH trademarks are owned by Bluetooth SIG, Inc., U.S.A.

%package auto-enable-devices
Summary:        Configuration that automatically enables all bluetooth devices
License:        GPL-2.0-or-later
Group:          Hardware/Mobile
BuildArch:      noarch
Requires(post): systemd

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

%package obexd
Summary:        Object Exchange daemon for sharing binary objects
License:        GPL-2.0-or-later
Group:          Hardware/Mobile
Requires:       bluez = %{version}
Supplements:    bluedevil5
Supplements:    bluedevil6
Supplements:    blueman
Supplements:    gnome-bluetooth

%description obexd
This is an object exchange daemon for binary objects transferring between
devices. obexd is necessary to install for sharing files, contacts
etc. through bluetooth.

%package zsh-completion
Summary:        Zsh completion for bluez
Group:          System/Management
Requires:       %{name}
Requires:       zsh
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
This package contain the zsh completion command for the Bluetooth Stack for Linux.

%prep
%autosetup -p1
mkdir dbus-apis
cp -a doc/*.txt dbus-apis/

# for auto-enable subpackage
sed -i '/^#AutoEnable=false/aAutoEnable=true' src/main.conf

# Fix shebangs in test files
%{?python3_fix_shebang_path:%python3_fix_shebang_path test/*}

%build
%if 0%{?suse_version} < 1550
echo 0%{?suse_version}
export CC=gcc-8
%endif
# header file has "#ifndef FIRMWARE_DIR...#define FIRMWARE_DIR /etc/firmare"
# instead of patching, just supply FIRMWARE_DIR on compiler's command line
export CPPFLAGS="$CPPFLAGS -DFIRMWARE_DIR='\"%{_firmwaredir}\"'"
# because of patch4... and patch18
autoreconf -fi
# --enable-experimental is needed or btattach does not build (bug?)
%configure \
	--disable-silent-rules  \
	--enable-pie		\
	--enable-library	\
	--enable-tools		\
	--enable-cups		\
	--enable-hid2hci        \
	--enable-admin		\
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
	--with-dbusconfdir=%{_datadir}	\
%if 0%{?suse_version} >= 1550
	--enable-external-ell	\
%endif
	--with-systemdsystemunitdir=%{_unitdir}		\
	--with-systemduserunitdir=%{_userunitdir}

%make_build all

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
install --mode=0644 -D %{SOURCE7} %{buildroot}/%{_modprobedir}/50-bluetooth.conf
# no idea why this is suddenly necessary...
install --mode 0755 -d %{buildroot}%{_localstatedir}/lib/bluetooth

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

mkdir -p %{buildroot}%{_defaultdocdir}/%{name}
cp %{SOURCE9} %{buildroot}%{_defaultdocdir}/%{name}
%if %{with mesh}
# boo#1151518
mv %{buildroot}%{_datadir}/dbus-1/system.d/bluetooth-mesh.conf %{buildroot}%{_defaultdocdir}/%{name}
mv %{buildroot}%{_datadir}/dbus-1/system-services/org.bluez.mesh.service %{buildroot}%{_defaultdocdir}/%{name}
cat > %{buildroot}%{_defaultdocdir}/%{name}/README-mesh.SUSE << EOF
The bluetooth-mesh dbus system config has been disabled due to security
concerns. See https://bugzilla.opensuse.org/show_bug.cgi?id=1151518 for
details.

If you want to use this feature anyway, copy
bluetooth-mesh.conf to %{_sysconfdir}/dbus-1/systemd.d/ and
org.bluez.mesh.service to %{_sysconfdir}/dbus-1/system-services/,
then reboot.
EOF
touch -r %{SOURCE0} %{buildroot}%{_defaultdocdir}/%{name}/README-mesh.SUSE
%endif

%check
%if ! 0%{?qemu_user_space_build}
##make %%{?_smp_mflags} check
# deliberately not running parallel, as the test suite has spurious failures otherwise
%make_build check V=0
%endif

%pre
%service_add_pre bluetooth.service bluetooth-mesh.service
# Avoid restoring outdated stuff in posttrans
for _f in %{?modprobe_d_files}; do
    [ ! -f "/etc/modprobe.d/${_f}.rpmsave" ] || \
	mv -f "/etc/modprobe.d/${_f}.rpmsave" "/etc/modprobe.d/${_f}.rpmsave.old" || :
done

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

%posttrans
# Migration of modprobe.conf files to _modprobedir
for _f in %{?modprobe_d_files}; do
    [ ! -f "/etc/modprobe.d/${_f}.rpmsave" ] || \
	mv -fv "/etc/modprobe.d/${_f}.rpmsave" "/etc/modprobe.d/${_f}" || :
done

%post -n libbluetooth3 -p /sbin/ldconfig
%postun -n libbluetooth3 -p /sbin/ldconfig

%pre obexd
%systemd_user_pre obex.service

%post obexd
%systemd_user_post obex.service

%preun obexd
%systemd_user_preun obex.service

%postun obexd
%systemd_user_postun obex.service

%files
%doc AUTHORS ChangeLog README dbus-apis src/main.conf
%if %{with mesh}
%doc %{_defaultdocdir}/%{name}/*
%endif
%license COPYING
%{_bindir}/bluemoon
%{_bindir}/btattach
%{_bindir}/btmgmt
%{_bindir}/l2ping
%{_bindir}/hex2hcd
%{_bindir}/isotest
%{_bindir}/mpris-proxy
%dir %{_libexecdir}/bluetooth
%{_libexecdir}/bluetooth/bluetoothd
%if %{with mesh}
%{_libexecdir}/bluetooth/bluetooth-meshd
%{_bindir}/mesh-cfgtest
%{_mandir}/man8/bluetooth-meshd.8%{?ext_man}
%endif
%{_bindir}/bluetoothctl
%{_bindir}/btmon
%if %{with mesh}
%{_bindir}/meshctl
%{_bindir}/mesh-cfgclient
%endif
%{_prefix}/lib/udev/
%{_mandir}/man1/btattach.1%{?ext_man}
%{_mandir}/man1/btmon.1%{?ext_man}
%{_mandir}/man1/isotest.1%{?ext_man}
%{_mandir}/man8/bluetoothd.8%{?ext_man}
%{_mandir}/man1/hid2hci.1%{?ext_man}
%{_mandir}/man1/l2ping.1%{?ext_man}
%{_mandir}/man1/rctest.1%{?ext_man}
%{_mandir}/man1/bluetoothctl.1%{?ext_man}
%{_mandir}/man1/bluetoothctl-mgmt.1%{?ext_man}
%{_mandir}/man1/bluetoothctl-monitor.1%{?ext_man}
%{_mandir}/man1/bluetoothctl-admin.1%{?ext_man}
%{_mandir}/man1/bluetoothctl-advertise.1%{?ext_man}
%{_mandir}/man1/bluetoothctl-endpoint.1%{?ext_man}
%{_mandir}/man1/bluetoothctl-gatt.1%{?ext_man}
%{_mandir}/man1/bluetoothctl-player.1%{?ext_man}
%{_mandir}/man1/bluetoothctl-scan.1%{?ext_man}
%{_mandir}/man1/bluetoothctl-transport.1%{?ext_man}
%{_mandir}/man1/bluetoothctl-assistant.1%{?ext_man}
%{_mandir}/man1/btmgmt.1%{?ext_man}
%{_mandir}/man5/org.bluez.*.5%{?ext_man}
%{_mandir}/man7/hci.7%{?ext_man}
%{_datadir}/dbus-1/system.d/bluetooth.conf
# not packaged, boo#1151518
###%%{_datadir}/dbus-1/system.d/bluetooth-mesh.conf
%dir %{_localstatedir}/lib/bluetooth
%dir %{_modprobedir}
%{_modprobedir}/50-bluetooth.conf
%{_unitdir}/bluetooth.service
%if %{with mesh}
%{_unitdir}/bluetooth-mesh.service
%endif
%{_userunitdir}/mpris-proxy.service
%{_datadir}/dbus-1/system-services/org.bluez.service
# not packaged, boo#1151518
###%%{_datadir}/dbus-1/system-services/org.bluez.mesh.service
%config(noreplace) %{_sysconfdir}/bluetooth/input.conf
%config(noreplace) %{_sysconfdir}/bluetooth/mesh-main.conf
%config(noreplace) %{_sysconfdir}/bluetooth/network.conf

%files obexd
%{_libexecdir}/bluetooth/obexd
%{_datadir}/dbus-1/services/org.bluez.obex.service
%{_userunitdir}/obex.service
%{_userunitdir}/dbus-org.bluez.obex.service

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
%{_mandir}/man7/rfcomm.7%{?ext_man}
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
%dir %{_prefix}/lib/cups
%dir %{_prefix}/lib/cups/backend
%{_prefix}/lib/cups/backend/bluetooth

%files test
%{_bindir}/avinfo
#{_bindir}/hciemu
%{_bindir}/l2test
%{_bindir}/rctest
%{_bindir}/btgatt-client
%dir %{_libdir}/bluez
%{_libdir}/bluez/test
%{_mandir}/man7/l2cap.7%{?ext_man}

%files auto-enable-devices
%dir %{_sysconfdir}/bluetooth
%config(noreplace) %{_sysconfdir}/bluetooth/main.conf

%files zsh-completion
%{_datadir}/zsh/site-functions/_bluetoothctl

%changelog
