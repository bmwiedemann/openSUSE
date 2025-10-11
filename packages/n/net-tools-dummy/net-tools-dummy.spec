#
# spec file for package net-tools-dummy
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           net-tools-dummy
%define _name net-tools-dummy-rootless
Version:        0.1
Release:        0
Summary:        Dummy implementation for obsolete network commands
License:        CC0-1.0
Source:         %{name}-rpmlintrc
Conflicts:      net-tools-deprecated
Conflicts:      busybox-net-tools
Recommends:     %{name}-ether-wake
Recommends:     bridge-utils-dummy
BuildArch:      noarch

%description
As many people are still trying to use deprecated net-tools utilities
without realizing its obsolete status, this package provides a useful
feedback how to proceed.

%package ether-wake
Summary:        Dummy implementation for obsolete network commands
Conflicts:      busybox-ether-wake
# Up to net-tools-2.10, ether-wake was part of the downstream package
Conflicts:      net-tools < 2.10+1

%description ether-wake
As many people are still trying to use deprecated net-tools utilities
without realizing its obsolete status, this package provides a useful
feedback how to proceed.

%package -n bridge-utils-dummy
Summary:        Dummy implementation for obsolete network commands
Conflicts:      bridge-utils
Conflicts:      busybox-iproute2

%description -n bridge-utils-dummy
As many people are still trying to use deprecated net-tools utilities
without realizing its obsolete status, this package provides a useful
feedback how to proceed.

%prep
%autosetup -Tc

%build
dummy() {
	cat >$1 <<EOFF
#!/bin/sh
if test -z "\$*" ; then
	$3
	echo >&2
fi
if test "\`id -u\`" -eq 0 ; then
	SUDO=""
else
	SUDO="sudo "
fi
cat >&2 <<EOF
$1 is deprecated and should not be used. Please migrate to iproute2:
$2
If you still depend on the deprecated tool, install net-tools-deprecated.
\${SUDO}zypper install net-tools-deprecated
EOF
exit 1
EOFF
}
dummy arp "ip [-r] neigh" "ip neigh"
dummy ifconfig "ip addr" "ip addr"
dummy "ipmaddr" "ip maddress" "ip maddress"
dummy iptunnel "ip tunnel" "ip tunnel"
dummy netstat "ss [-r]" "ss"
dummy route "ip route" "ip route"
	cat >ether-wake <<EOFF
#!/bin/sh
if test "\`id -u\`" -eq 0 ; then
	SUDO=""
else
	SUDO="sudo "
fi
if test -x %{_bindir}/wol ; then
	INSTALL_WOL=""
else
	INSTALL_WOL="\${SUDO}zypper install wol
"
fi

cat >&2 <<EOF
ether-wake was removed from net-tools. Please migrate to wol:
\${INSTALL_WOL}wol [options]
or use busybox-ether-wake:
\${SUDO}zypper install busybox-ether-wake
EOF
exit 1
EOFF

cat >brctl <<EOFF
#!/bin/sh
if test "\`id -u\`" -eq 0 ; then
	SUDO=""
else
	SUDO="sudo "
fi
cat >&2 <<EOF
brctl is deprecated and should not be used. Please migrate to iproute2:
ip link add type bridge / ip --brief link show
If you still depend on the deprecated tool, install bridge-utils.
\${SUDO}zypper install bridge-utils
EOF
exit 1
EOFF

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_sbindir}
install ifconfig netstat route %{buildroot}%{_bindir}/
install arp brctl ether-wake ipmaddr iptunnel %{buildroot}%{_sbindir}/

%check

%files
%{_bindir}/ifconfig
%{_bindir}/netstat
%{_bindir}/route
%{_sbindir}/arp
%{_sbindir}/ipmaddr
%{_sbindir}/iptunnel

%files ether-wake
%{_sbindir}/ether-wake

%files -n bridge-utils-dummy
%{_sbindir}/brctl

%changelog
