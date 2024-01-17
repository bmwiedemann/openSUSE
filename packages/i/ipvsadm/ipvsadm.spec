#
# spec file for package ipvsadm
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           ipvsadm
BuildRequires:  kernel-source
BuildRequires:  pkgconfig
BuildRequires:  popt-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
Summary:        A Utility for Administering the Linux Virtual Server
License:        GPL-2.0-or-later
Group:          Productivity/Networking/System
Version:        1.31
Release:        0
URL:            http://www.linuxvirtualserver.org/
Source0:        https://www.kernel.org/pub/linux/utils/kernel/ipvsadm/%{name}-%{version}.tar.xz
Source1:        ipvsadm.service
Patch0:         ipvsadm-makefile.patch
Patch1:         ipvsadm-print_largenum.patch
Provides:       %{name}-%{version}
Requires:       grep
Requires(pre):  %fillup_prereq
%{?systemd_requires}

%description
ipvsadm is a utility for administering the IP virtual server services
offered by the Linux kernel with Linux Virtual Server support.

%prep
%autosetup
# This files are embedded here instead of being another source in order
# to the prefix directory
cat >sysconfig.ipvsadm <<EOFF
## Path:           Network/IPVS
## Description:    Linux Virtual Server Configuration
## ServiceRestart: ipvsadm
## Type:           string
## Default:        /etc/ipvsadm.rules
#
# Where to find the IPVSADM config-file
#
IPVSADM_CONFIG="/etc/ipvsadm.rules"
EOFF
cat >ipvsadm.rules <<EOFF
#
# Please insert your ipvs-rules here
#
EOFF

%build
make POPT_LIB="-lpopt" CFLAGS="%{optflags} -fPIC -DHAVE_POPT -DLIBIPVS_USE_NL -I%{_includedir}/libnl3"

%install
mkdir -p %{buildroot}/{sbin,%{_sbindir},%{_mandir}/man8,%{_unitdir},%{_fillupdir}}
make BUILD_ROOT=%{buildroot} MANDIR=%{_mandir} SBINDIR=%{_sbindir} install
%if 0%{?suse_version} < 1550
for binary in ipvsadm ipvsadm-save ipvsadm-restore ; do
  ln -sf %{_sbindir}/$binary            %{buildroot}/sbin/$binary ;
done
%endif
# Sysvinit support dropping
rm -rf %{buildroot}/etc/init.d
# install SuSE init script
install -m 644 %{S:1}           	%{buildroot}%{_unitdir}/%{name}.service
ln -sf %_sbindir/service	        %{buildroot}%{_sbindir}/rc%{name}
install -m 644 sysconfig.ipvsadm	%{buildroot}%{_fillupdir}/sysconfig.%{name}
install -m 644 ipvsadm.rules		%{buildroot}%{_sysconfdir}/%{name}.rules

%post
%{fillup_only}
%service_add_post ipvsadm.service

%postun
%service_del_postun ipvsadm.service

%pre
%service_add_pre ipvsadm.service

%preun
%service_del_preun ipvsadm.service

%files
%defattr(-,root,root)
%doc README
%config %{_sysconfdir}/%{name}.rules
%{_unitdir}/%{name}.service
%if 0%{?suse_version} < 1550
/sbin/ipvsadm*
%endif
%{_sbindir}/ipvsadm*
%{_sbindir}/rcipvsadm*
/%{_mandir}/man*/ipvsadm*
%{_fillupdir}/sysconfig.%{name}

%changelog
