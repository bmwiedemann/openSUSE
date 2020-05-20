#
# spec file for package netcfg
#
# Copyright (c) 2020 SUSE LLC
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


Name:           netcfg
Version:        11.6
Release:        0
Summary:        Network Configuration Files in /etc
License:        BSD-3-Clause
Group:          System/Base
Source0:        defaultdomain
Source1:        exports
Source2:        ftpusers
Source3:        host.conf
Source4:        hosts
Source5:        hosts.allow
Source6:        hosts.deny
Source7:        hosts.equiv
Source8:        hosts.lpd
Source9:        networks
Source10:       protocols
Source11:       services.bz2
Source12:       hostname
Source13:       aliases
Source14:       ethers
Source15:       netgroup
Source16:       COPYING
Source17:       ethertypes
Source100:      services-compare.pl
Source101:      services-compare.sh
Source102:      services-create.pl
Source103:      services_UPDATING
Patch0:         services-suse.diff
BuildRequires:  libnss_usrfiles2
Requires:       libnss_usrfiles2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
All of the basic configuration files for the network programs including
%{_sysconfdir}/aliases, %{_sysconfdir}/protocols, and %{_sysconfdir}/services.

These are often used by network routines in the C library and therefore
must be installed for all network programs.

%prep

%build
cp %{SOURCE16} .

%install
mkdir -p %{buildroot}%{_sysconfdir}
for i in hostname aliases defaultdomain exports ftpusers host.conf hosts hosts.allow hosts.deny hosts.equiv hosts.lpd netgroup ethertypes; do
  install $RPM_SOURCE_DIR/$i %{buildroot}/%{_sysconfdir}
done
mkdir -p %{buildroot}%{_prefix}%{_sysconfdir}
for i in networks protocols services.bz2 ethers; do
  install $RPM_SOURCE_DIR/$i %{buildroot}%{_prefix}%{_sysconfdir}
done
bunzip2 %{buildroot}%{_prefix}%{_sysconfdir}/services.bz2
patch -p0 %{buildroot}%{_prefix}%{_sysconfdir}/services < $RPM_SOURCE_DIR/services-suse.diff
rm -f %{buildroot}%{_prefix}%{_sysconfdir}/services.orig

install -d -m 0755 %{buildroot}/%{_sysconfdir}/exports.d

%files
%defattr(644,root,root,755)
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/hostname
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/aliases
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/defaultdomain
%verify(not md5 size mtime)                    %{_prefix}%{_sysconfdir}/ethers
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/exports
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/ftpusers
%config(noreplace) %{_sysconfdir}/host.conf
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/hosts
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/hosts.allow
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/hosts.deny
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/hosts.equiv
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/hosts.lpd
%config(noreplace) %{_sysconfdir}/netgroup
%{_prefix}%{_sysconfdir}/networks
%{_prefix}%{_sysconfdir}/protocols
%{_prefix}%{_sysconfdir}/services
%config(noreplace) %{_sysconfdir}/ethertypes
%dir %{_sysconfdir}/exports.d
%license COPYING

%changelog
