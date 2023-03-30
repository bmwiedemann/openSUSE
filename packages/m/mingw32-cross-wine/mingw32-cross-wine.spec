#
# spec file for package mingw32-cross-wine
#
# Copyright (c) 2020 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define _with_dns 0

%define _rpm_macros_dir %{_rpmconfigdir}/macros.d

Name:           mingw32-cross-wine
Version:        1.3.2
Release:        0
Summary:        Wine cross runtime
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Url:            http://www.winehq.org/
Source1:        macros
Source2:        wine.sh
%if %{?_with_dns}
# nslookup
Requires:       bind-utils
# dns server
Requires:       dnsmasq
BuildRequires:  NetworkManager
# netupdate for regenerating /etc/resolv.conf
Requires:       sysconfig
%endif
# i686-w64-mingw32-objdump
BuildRequires:  mingw32-cross-binutils
BuildRequires:  mingw32-filesystem
Requires:       mingw32-filesystem
Requires:       wine-binfmt-standalone
Requires:       wget
Requires:       winetricks
# Xvfb for x display
Requires:       xorg-x11-server
Requires:       xvfb-run
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%_mingw32_package_header
BuildArch:      noarch
#!BuildIgnore: post-build-checks

%description
This package contains a ready to use wine prefix for
running cross compiled applications while building 
packages, for example cross compiled test 

%prep
%setup -c -T

%build

%install
mkdir -p %{buildroot}%{_rpm_macros_dir}
cp %{_sourcedir}/macros %{buildroot}%{_rpm_macros_dir}/macros.mingw32-cross-wine
cp %{_sourcedir}/wine.sh %{buildroot}%{_rpmconfigdir}/mingw32-cross-wine-wine.sh
mkdir -p %{buildroot}%{_bindir}
ln -s ../lib/mingw32-scripts %{buildroot}%{_bindir}/mingw32-cross-wine-init
ln -s ../lib/mingw32-scripts %{buildroot}%{_bindir}/mingw32-cross-wine-run
ln -s ../lib/mingw32-scripts %{buildroot}%{_bindir}/mingw32-cross-wine-start-session

%if %{?_with_dns}
%post
# setup dns config
set -x
# add dnsmasq as local dns server
sed -i '/^NETCONFIG_DNS_FORWARDER=/ s,"resolver","dnsmasq",g' /etc/sysconfig/network/config 
sed -i '/^NETCONFIG_DNS_STATIC_SERVERS=/ s,"","127.0.0.1",g' /etc/sysconfig/network/config
sed -i '/^DEBUG=/ s,"no","yes",g' /etc/sysconfig/network/config
sed -i '/^NETCONFIG_VERBOSE=/ s,"no","yes",g' /etc/sysconfig/network/config

cat /etc/sysconfig/network/config


# update /etc/resolv.conf
netconfig update -f
cat /etc/resolv.conf

cat /var/run/dnsmasq-forwarders.conf

#  setup dns server
cat << EOF >> /etc/dnsmasq.conf
listen-address=127.0.0.1
port=53
domain-needed
bogus-priv
resolv-file=/var/run/dnsmasq-forwarders.conf
EOF

# start local dns server
/usr/sbin/dnsmasq -u root &

sleep 2

netstat -alnp

# check dns
dig 127.0.0.1
%endif

%if %{?_with_dns}
%preun
killall -9 dnsmasq
%endif

%files
%defattr(-,root,root)
%dir %{_rpmconfigdir}
%dir %{_rpm_macros_dir}
%{_rpm_macros_dir}/macros.mingw32-cross-wine
%{_rpmconfigdir}/mingw32-cross-wine-wine.sh
%{_bindir}/mingw32-*

%changelog
