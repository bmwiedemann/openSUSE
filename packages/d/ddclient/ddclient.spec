#
# spec file for package ddclient
#
# Copyright (c) 2022 SUSE LLC
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


Name:           ddclient
Version:        3.10.0
Release:        0
Summary:        A Perl Client to Update Dynamic DNS Entries
License:        GPL-2.0-or-later
Group:          Productivity/Networking/DNS/Utilities
URL:            https://github.com/ddclient/ddclient
Source0:        https://github.com/ddclient/ddclient/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}.service
Source2:        %{name}.sysconfig
Source3:        %{name}-tmpfiles.conf
Patch0:         %{name}-config.patch
Patch1:         %{name}-delay-main-process-for-systemd.patch
Patch2:         fix-configure_ac.patch
Patch3:         disable-ip-test.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  perl(HTTP::Daemon)
BuildRequires:  perl(HTTP::Message::PSGI)
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Test::MockModule)
BuildRequires:  perl(Test::Warnings)
Requires:       perl >= 5.10.1
Requires(pre):  %fillup_prereq
Requires(pre):  shadow
Recommends:     perl-IO-Socket-SSL
BuildArch:      noarch
%{?systemd_requires}

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
%autosetup -p1
rm -f sample-etc_ddclient.conf.orig
chmod a-x sample-*
mkdir examples
mv sample-* examples

%build
./autogen
%configure
make

%install
%make_install
find examples -name *exe -delete
mkdir -p %{buildroot}%{_sbindir}/
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_sbindir}/%{name}
sed -i -e "s,%{_localstatedir}/run/,/run/%{name}/," %{buildroot}%{_sysconfdir}/%{name}.conf
install -D -m 644 %{SOURCE1} %{buildroot}/%{_unitdir}/%{name}.service
install -D -m 644 %{SOURCE3} %{buildroot}%{_tmpfilesdir}/%{name}.conf
ln -s service %{buildroot}%{_sbindir}/rc%{name}
install -d -m 755 %{buildroot}%{_fillupdir}
install -m 644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.%{name}
install -d -m 755 %{buildroot}%{_localstatedir}/cache/%{name}
install -d -m 755 %{buildroot}/run/%{name}

%check
make VERBOSE=1 check

%pre
getent group %{name} >/dev/null || %{_sbindir}/groupadd -r %{name}
getent passwd %{name} >/dev/null || \
  %{_sbindir}/useradd -c "DDClient User" -d %{_localstatedir}/cache/%{name} \
    -g %{name} -r -s /bin/false %{name}
%service_add_pre %{name}.service

%post
%fillup_only
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%doc COPY* README* examples
%config(noreplace) %attr(600,%{name},root) %{_sysconfdir}/%{name}.conf
%{_unitdir}/%{name}.service
%{_tmpfilesdir}/ddclient.conf
%ghost %dir %attr(755,%{name},%{name}) /run/%{name}
%{_sbindir}/%{name}
%{_sbindir}/rc%{name}
%{_fillupdir}/sysconfig.%{name}
%dir %attr(700,%{name},root) %{_localstatedir}/cache/%{name}

%changelog
