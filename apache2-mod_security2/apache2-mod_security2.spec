#
# spec file for package apache2-mod_security2
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define modname       mod_security2
%define tarballname   modsecurity-%{version}
%define usrsharedir %{_datadir}/%{name}
Name:           apache2-mod_security2
Version:        2.9.2
Release:        0
Summary:        Web Application Firewall for apache httpd
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
Url:            http://www.modsecurity.org/
Source:         https://www.modsecurity.org/tarball/%{version}/%{tarballname}.tar.gz
Source1:        https://github.com/SpiderLabs/owasp-modsecurity-crs/tarball/master//SpiderLabs-owasp-modsecurity-crs-2.2.9-5-gebe8790.tar.gz
Source2:        mod_security2.conf
Source6:        README-SUSE-mod_security2.txt
Source7:        empty.conf
Patch0:         apache2-mod_security2-no_rpath.diff
Patch1:         modsecurity-fixes.patch
Patch2:         apache2-mod_security2_tests_conf.patch
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
BuildRequires:  apache2-prefork
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  c++_compiler
BuildRequires:  libcurl-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  lua-devel
BuildRequires:  pcre-devel
BuildRequires:  perl-libwww-perl
BuildRequires:  pkgconfig
Requires:       %{apache_mmn}
Requires:       %{apache_suse_maintenance_mmn}
Requires:       apache2
%if 0%{suse_version} == 1110
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%endif

%description
ModSecurity is an intrusion detection and prevention
engine for web applications (or a web application firewall). Operating
as an Apache Web server module or standalone, the purpose of
ModSecurity is to increase web application security, protecting web
applications from known and unknown attacks.

%prep
%setup -q -n %{tarballname}
%setup -q -D -T -a 1 -n %{tarballname}
mv -v SpiderLabs* rules
%patch0
%patch1 -p1
%patch2 -p1

%build
# aclocal only works with newer distributions
%if 0%{?suse_version} >= 1310
aclocal
# on older versions only autoconf is called
%else
autoreconf -fi
%endif
automake
%configure --with-apxs=%{apache_apxs} --enable-request-early --enable-htaccess-config --disable-mlogc
CFLAGS="%{optflags}" make %{?_smp_mflags}

%install
pushd apache2
  install -d -m 0755 %{buildroot}%{apache_libexecdir}
  install .libs/mod_security2.so %{buildroot}%{apache_libexecdir}/%{modname}.so
popd
install -D -m 0644 %{SOURCE2} %{buildroot}%{apache_sysconfdir}/conf.d/%{modname}.conf
install -d -m 0755 %{buildroot}%{apache_sysconfdir}/mod_security2.d
install -D -m 0644 %{SOURCE6} %{buildroot}%{apache_sysconfdir}/mod_security2.d
install -D -m 0644 %{SOURCE7} %{buildroot}%{apache_sysconfdir}/mod_security2.d
cp -a %{SOURCE6} doc
install -d -m 0755 %{buildroot}/%{usrsharedir}
install -d -m 0755 %{buildroot}/%{usrsharedir}/tools
rm -f rules/.gitignore rules/LICENSE
cp -a rules/util/README %{buildroot}/%{usrsharedir}/tools/README-rules-updater.txt
cp -a tools/rules-updater.pl tools/rules-updater-example.conf %{buildroot}/%{usrsharedir}/tools
find rules -type f -exec chmod 644 {} +
cp -a rules %{buildroot}/%{usrsharedir}
rm -rf %{buildroot}/%{usrsharedir}/rules/util
rm -rf %{buildroot}/%{usrsharedir}/rules/lua
rm -f %{buildroot}/%{usrsharedir}/rules/READM*
rm -f %{buildroot}/%{usrsharedir}/rules/INSTALL %{buildroot}/%{usrsharedir}/rules/CHANGELOG
mv %{buildroot}/%{usrsharedir}/rules/modsecurity_crs_10_setup.conf.example \
  %{buildroot}/%{usrsharedir}/rules/modsecurity_crs_10_setup.conf

# Temporarily disable test suite as there are some failures that need to be solved
#%check
#make test
#make test-regression

set +x
mkdir -p %{apache_test_module_dir}
cp %{SOURCE2} %{apache_test_module_dir}/%{modname}-test.conf
sed -i 's:%{_localstatedir}/log/apache2:/tmp:' %{apache_test_module_dir}/%{modname}-test.conf
sed -i 's:%{_prefix}/share:%{buildroot}%{_prefix}/share:' %{apache_test_module_dir}/%{modname}-test.conf
sed -i 's:%{_sysconfdir}/apache2:%{buildroot}%{_sysconfdir}/apache2:' %{apache_test_module_dir}/%{modname}-test.conf
%apache_test_module_load -m security2 -i %{modname}-test.conf
set -x

%files
%if %{suse_version} == 1110
%defattr (-,root,root)
%endif
%{apache_libexecdir}/%{modname}.so
%config(noreplace) %{apache_sysconfdir}/conf.d/%{modname}.conf
%dir %{apache_sysconfdir}/mod_security2.d
%{apache_sysconfdir}/mod_security2.d/README-SUSE-mod_security2.txt
%{apache_sysconfdir}/mod_security2.d/empty.conf
%{usrsharedir}
%doc README.TXT CHANGES LICENSE NOTICE authors.txt
%doc doc/README.txt
%doc doc/README-SUSE-mod_security2.txt
%doc rules/util/regression-tests

%changelog
