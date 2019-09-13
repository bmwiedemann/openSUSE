#
# spec file for package acct
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


Name:           acct
Version:        6.6.4
Release:        0
Summary:        User-Specific Process Accounting
License:        GPL-2.0-or-later
Group:          System/Base
Url:            https://www.gnu.org/software/acct/
Source:         https://ftp.gnu.org/gnu/acct/%{name}-%{version}.tar.gz
Source1:        acct.service
Source2:        logrotate.acct
Source3:        https://ftp.gnu.org/gnu/acct/%{name}-%{version}.tar.gz.sig
Source4:        http://savannah.gnu.org/project/memberlist-gpgkeys.php?group=acct&download=1#/acct.keyring
Patch0:         acct-6.6.2-hz.patch
BuildRequires:  makeinfo
BuildRequires:  systemd-rpm-macros
Requires:       logrotate
Requires(post): %{install_info_prereq}
Requires(postun): %{install_info_prereq}
%{?systemd_ordering}

%description
This package contains the programs necessary for user-specific process
accounting: sa, accton, and lastcomm.

%prep
%setup -q
%patch0

%build
%configure
make %{?_smp_mflags}

%install
install -d -m 755 %{buildroot}%{_sysconfdir}/logrotate.d
install -d -m 755 %{buildroot}/%{_unitdir}
install -d -m 755 %{buildroot}%{_localstatedir}/account/
install -d -m 755 %{buildroot}%{_libexecdir}/account
install -d -m 755 %{buildroot}%{_sbindir}
install -d -m 755 %{buildroot}%{_bindir}
%make_install

install -m 644 %{SOURCE1} %{buildroot}/%{_unitdir}/acct.service
ln -sf service %{buildroot}%{_sbindir}/rcacct

install -m 644 %{SOURCE2}  %{buildroot}%{_sysconfdir}/logrotate.d/acct
mkdir -p %{buildroot}%{_localstatedir}/log/account
touch %{buildroot}%{_localstatedir}/log/account/pacct

rm -f %{buildroot}%{_bindir}/last
rm -f %{buildroot}/%{_mandir}/man1/last.1*

%pre
%service_add_pre acct.service

%post
%install_info --info-dir=%{_infodir} %{_infodir}/accounting.info.gz
%service_add_post acct.service

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/accounting.info.gz
%service_del_preun acct.service

%postun
%service_del_postun acct.service

%files
%doc README NEWS
%{_infodir}/*.info%{ext_info}
%{_mandir}/man1/ac*
%{_mandir}/man1/lastcomm*
%{_mandir}/man8/*
%config %{_sysconfdir}/logrotate.d/acct
%dir %{_localstatedir}/log/account
%{_localstatedir}/log/account/pacct
%{_bindir}/ac
%{_bindir}/lastcomm
%{_sbindir}/*
%{_unitdir}/acct.service

%changelog
