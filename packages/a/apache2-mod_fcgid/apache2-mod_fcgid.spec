#
# spec file for package apache2-mod_fcgid
#
# Copyright (c) 2024 SUSE LLC
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


Name:           apache2-mod_fcgid
Version:        2.3.9
Release:        0
Summary:        Alternative FastCGI module for Apache2
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Servers
URL:            http://httpd.apache.org/mod_fcgid/
Source:         http://mirror.synyx.de/apache/httpd/mod_fcgid/mod_fcgid-%{version}.tar.bz2
Source1:        apache2-mod_fcgid.conf
Patch0:         mod_fcgid-2.3.5_suse_paths.patch
# PATCH-FIX-UPSTREAM bsc#988492 kstreitova@suse.com -- don't allow setting the HTTP_PROXY variable
Patch1:         mod_fcgid-2.3.9-CVE-2016-1000104.patch
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
BuildRequires:  perl-FastCGI
Requires:       %{apache_mmn}
Requires:       %{apache_suse_maintenance_mmn}
Requires:       apache2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A binary compatibile alternative to the Apache module mod_fastcgi.

The module implements an efficient process pool management for external
CGI program invocation. The pool of CGI programs is mapped against the
pool of apache workers in such way that there is always a weighted number
of programs waiting for requests in the pool.

To load the module into Apache, run the command "a2enmod fcgid" as
root.

See %{_sysconfdir}/apache2/conf.d/mod_fcgid.conf and
%{_docdir}/apache2-mod_fcgid for configuration.

%prep
%setup -q -n mod_fcgid-%{version}
%patch -P 0
%patch -P 1 -p1

%build
APXS="%{apache_apxs}" ./configure.apxs
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
install -D -m 0644 %{SOURCE1} %{buildroot}%{apache_sysconfdir}/conf.d/mod_fcgid.conf
install -d -m 0755 %{buildroot}%{_localstatedir}/lib/apache2/fcgid/

%files
%defattr(-,root,root)
%{apache_libexecdir}/mod_fcgid.so
%config(noreplace) %{apache_sysconfdir}/conf.d/mod_fcgid.conf
%doc CHANGES-FCGID LICENSE-FCGID NOTICE-FCGID README-FCGID STATUS-FCGID
%dir %{_datadir}/apache2/manual/
%dir %{_datadir}/apache2/manual/mod/
%{_datadir}/apache2/manual/mod/mod_fcgid*
%attr(750,wwwrun,www) %{_localstatedir}/lib/apache2/fcgid/

%changelog
