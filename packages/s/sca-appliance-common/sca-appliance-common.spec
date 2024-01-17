#
# spec file for package sca-appliance-common
#
# Copyright (c) 2021 SUSE LLC
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


%define sca_common sca
%define sca_libdir /usr/lib/%{sca_common}
%define sca_webdir /srv/www/htdocs/%{sca_common}
%define sca_configdir %{_sysconfdir}/%{sca_common}

Name:           sca-appliance-common
Version:        1.3
Release:        0
Summary:        Supportconfig Analysis Appliance Common Files
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            https://github.com/g23guy/sca-appliance-common
Source:         %{name}-%{version}.tar.gz
Requires:       curl
Recommends:     php, php-bz2, php-mbstring, php-mcrypt, php-mysql, php-zip, php-zlib
Recommends:     mod_php_any
Requires:       %{_bindir}/awk
Requires:       %{_bindir}/dos2unix
Requires:       %{_bindir}/sed
Requires:       %{_bindir}/ssh
Requires:       %{_bindir}/vmstat
Requires:       %{_sbindir}/mysqld
Requires:       /bin/logger
Requires:       /bin/ping
Requires:       apache2
BuildArch:      noarch

%description
Provides the common files needed by both the SCA Broker, Agent and pattern development.

%prep
%setup -q

%build

%install
pwd;ls -la
install -d %{buildroot}%{sca_libdir}
install -d %{buildroot}%{sca_configdir}
install -d %{buildroot}%{sca_webdir}
install -d %{buildroot}%{_docdir}/%{name}
install -d %{buildroot}/var/log/archives
install -m 444 docs/COPYING.GPLv2 %{buildroot}%{_docdir}/%{name}
install -m 644 websca/* %{buildroot}%{sca_webdir}
install -m 600 websca/web-config.php %{buildroot}%{sca_webdir}

%files
%defattr(-,root,root)
%dir %{sca_configdir}
%dir %{sca_libdir}
%dir %attr(-,wwwrun,www) %{sca_webdir}
%dir %{_docdir}/%{name}
%dir %attr(775,root,users) /var/log/archives
%attr(-,wwwrun,www) %{sca_webdir}/*
%doc %{_docdir}/%{name}/*

%changelog
