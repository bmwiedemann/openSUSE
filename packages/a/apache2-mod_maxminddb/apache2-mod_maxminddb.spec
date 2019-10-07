#
# spec file for package apache2-mod_maxminddb
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


%define modname mod_maxminddb
Name:           apache2-mod_maxminddb
Version:        1.1.0
Release:        0
Summary:        MaxMind DB Apache Module
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
URL:            https://maxmind.github.io/mod_maxminddb/
Source:         https://github.com/maxmind/mod_maxminddb/releases/download/%{version}/mod_maxminddb-%{version}.tar.gz
Source2:        %{modname}.conf
# PATCH-FIX-OPENSUSE apache2-mod_maxminddb-build.patch -- Fix built on factory versions
Patch1:         apache2-mod_maxminddb-build.patch
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
BuildRequires:  automake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libmaxminddb)
Requires:       %{apache_mmn}
Requires:       %{apache_suse_maintenance_mmn}
Requires:       apache2

%description
This module allows you to query MaxMind DB files from Apache 2.2+ using the libmaxminddb library.

%prep
%setup -q -n %{modname}-%{version}
%patch1 -p1
# This config file is used for loading the module without
# enabling any databases which are not available on OBS
echo "MaxMindDBEnable On" > test-enable-module.conf

%build
autoreconf
%configure
make %{?_smp_mflags}

%check
set +x
%apache_test_module_load -m maxminddb -i test-enable-module.conf
set -x

%install
mkdir -p %{buildroot}/%{apache_libexecdir}
cp -p src/.libs/%{modname}.so %{buildroot}/%{apache_libexecdir}

mkdir -p %{buildroot}/%{apache_sysconfdir}/conf.d
cp %{SOURCE2} %{buildroot}/%{apache_sysconfdir}/conf.d

%files
%doc Changes.md README.md
%license LICENSE
%{apache_libexecdir}/%{modname}.so
%config(noreplace) %{apache_sysconfdir}/conf.d/%{modname}.conf

%changelog
