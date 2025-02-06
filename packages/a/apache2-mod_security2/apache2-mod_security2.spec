#
# spec file for package apache2-mod_security2
#
# Copyright (c) 2025 SUSE LLC
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


Name:           apache2-mod_security2
Version:        2.9.8
Release:        0
Summary:        Web Application Firewall for Apache httpd
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
URL:            https://www.modsecurity.org/
Source0:        https://github.com/owasp-modsecurity/ModSecurity/releases/download/v%{version}/modsecurity-v%{version}.tar.gz
Source1:        https://github.com/owasp-modsecurity/ModSecurity/releases/download/v%{version}/modsecurity-v%{version}.tar.gz.asc
Source2:        apache2-mod_security2.keyring
Source3:        mod_security2.conf
Source4:        README_SUSE
Patch0:         apache2-mod_security2-no_rpath.diff
Patch1:         modsecurity-fixes.patch
Patch2:         apache2-mod_security2_tests_conf.patch
# https://github.com/SpiderLabs/ModSecurity/issues/2514
Patch3:         modsecurity-2.9.3-input_filtering_errors.patch
# fix build with gcc14
Patch4:         apache2-mod_security2-gcc14.patch
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
BuildRequires:  apache2-prefork
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  c++_compiler
BuildRequires:  libcurl-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  lua53-devel
BuildRequires:  pcre-devel
BuildRequires:  perl-libwww-perl
BuildRequires:  pkgconfig
Requires:       %{apache_mmn}
Requires:       %{apache_suse_maintenance_mmn}
Requires:       apache2
Recommends:     owasp-modsecurity-crs-apache2

%description
ModSecurity is an intrusion detection and prevention
engine for web applications (or a web application firewall). Operating
as an Apache Web server module or standalone, the purpose of
ModSecurity is to increase web application security, protecting web
applications from known and unknown attacks.

%prep
%autosetup -p1 -n modsecurity-v%{version}
cp %{SOURCE4} .

%build
aclocal
automake
%configure --with-apxs=%{apache_apxs} --enable-request-early --enable-htaccess-config --disable-mlogc
CFLAGS="%{optflags}" make %{?_smp_mflags}

%install
pushd apache2
  install -d -m 0755 %{buildroot}%{apache_libexecdir}
  install .libs/mod_security2.so %{buildroot}%{apache_libexecdir}/mod_security2.so
popd
mkdir -p %{buildroot}%{apache_sysconfdir}/mod_security2.d
mkdir -p %{buildroot}%{apache_sysconfdir}/mod_security2.d/rules
mkdir -p %{buildroot}%{apache_sysconfdir}/conf.d/
cp -a %{SOURCE3} %{buildroot}%{apache_sysconfdir}/conf.d/

%check
make test

%files
%{apache_libexecdir}/mod_security2.so
%license LICENSE
%dir %{apache_sysconfdir}/mod_security2.d
%dir %{apache_sysconfdir}/mod_security2.d/rules
%dir %{apache_sysconfdir}/conf.d/
%config(noreplace) %{apache_sysconfdir}/conf.d/mod_security2.conf
%doc README.md CHANGES NOTICE authors.txt README_SUSE

%changelog
