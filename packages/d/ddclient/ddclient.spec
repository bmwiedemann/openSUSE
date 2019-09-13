#
# spec file for package ddclient
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           ddclient
Summary:        A Perl Client to Update Dynamic DNS Entries
License:        GPL-2.0-or-later
Group:          Productivity/Networking/DNS/Utilities
Version:        3.9.0
Release:        0
Url:            http://ddclient.sourceforge.net/
Source0:        http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.sysconfig
Source3:        %{name}-tmpfiles.conf
Source4:        rc.%{name}
Patch0:         %{name}-3.8.1-config.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires(pre):  %fillup_prereq
Requires(pre):  pwdutils
Requires:       perl-Data-Validate-IP

%if 0%{?suse_version} >= 1230
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%define has_systemd 1
%endif

Requires:       perl >= 5.004
Recommends:     perl-IO-Socket-SSL

%description
ddclient is a client requiring only Perl. Supported
features include daemon operation, manual and automatic updates, static
and dynamic updates, optimized updates for multiple addresses, MX, wild
cards, abuse avoidance, retry for failed updates, and status updates to
syslog and through e-mail. ddclient can obtain the IP address from any
interface, through a Web-based IP detection service, and for multiple
routers using custom FW definitions. It also provides full support for
DynDNS.org's NIC2 protocol. Support is also included for other dynamic
DNS services. Comes with sample scripts for use with DHCP, PPP, and
cron.

%prep
%setup
%patch0
rm -f sample-etc_ddclient.conf.orig
chmod a-x sample-*
mkdir examples
mv sample-* examples

%build
#%%configure
#make
# If the package provides automatic testing
#make test
# nothing to do here (yet)

%install
#%%make_install
install -D -m 755 %{name} %{buildroot}%{_sbindir}/%{name}
install -D -m 600 examples/sample-etc_ddclient.conf %{buildroot}%{_sysconfdir}/%{name}.conf
%if 0%{?has_systemd}
sed -i -e "s,/var/run/,/run/%{name}/," %{buildroot}%{_sysconfdir}/%{name}.conf
%else
sed -i -e "s,/var/run/,/var/run/%{name}/," %{buildroot}%{_sysconfdir}/%{name}.conf
%endif
# init script and config file
%if 0%{?has_systemd}
install -D -m 644 %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}.service
install -D -m 644 %{SOURCE3} %{buildroot}%{_libexecdir}/tmpfiles.d/%{name}.conf
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}
%else
install -D -m 755 %{SOURCE4} %{buildroot}%{_sysconfdir}/init.d/%{name}
ln -s %{_sysconfdir}/init.d/%{name} %{buildroot}%{_sbindir}/rc%{name}
%endif
install -d -m 755 %{buildroot}%{_fillupdir}
install -m 644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -d -m 755 %{buildroot}/var/cache/%{name}
%if 0%{?has_systemd}
install -d -m 755 %{buildroot}/run/%{name}
%else
install -d -m 755 %{buildroot}%{_localstatedir}/run/%{name}
%endif

%pre
getent group %{name} >/dev/null || %{_sbindir}/groupadd -r %{name}
getent passwd %{name} >/dev/null || \
  %{_sbindir}/useradd -c "DDClient User" -d %{_localstatedir}/cache/%{name} \
    -g %{name} -r -s /bin/false %{name}
%if 0%{?has_systemd}
%service_add_pre %{name}.service
install -d -m 755 -o %{name} -g root /run/%{name}
%else
install -d -m 755 -o %{name} -g root %{_localstatedir}/run/%{name}
%endif

%post
%{fillup_only}
%if 0%{?has_systemd}
%service_add_post %{name}.service
%endif

%preun
%if 0%{?has_systemd}
%service_del_preun %{name}.service
%else
%stop_on_removal ddclient
%endif

%postun
%if 0%{?has_systemd}
%service_del_postun %{name}.service
%else
%restart_on_update ddclient
%insserv_cleanup
%endif

%files
%defattr(-, root, root)
%doc COPY* README* examples
%config(noreplace) %attr(600,%{name},root) %{_sysconfdir}/%{name}.conf
%if 0%{?has_systemd}
%{_unitdir}/%{name}.service
%{_libexecdir}/tmpfiles.d/ddclient.conf
%ghost %dir %attr(755,%{name},%{name}) /run/%{name}
%else
/etc/init.d/%{name}
%ghost %dir %attr(755,%{name},%{name}) %{_localstatedir}/run/%{name}
%endif
%{_sbindir}/%{name}
%{_sbindir}/rc%{name}
%{_fillupdir}/sysconfig.%{name}
%dir %attr(700,%{name},root) %{_localstatedir}/cache/%{name}

%changelog
