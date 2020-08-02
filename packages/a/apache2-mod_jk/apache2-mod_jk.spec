#
# spec file for package apache2-mod_jk
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


%define connectors_root    tomcat-connectors-%{version}-src
Name:           apache2-mod_jk
Version:        1.2.48
Release:        0
Summary:        Connectors between Apache and Tomcat Servlet Container
License:        Apache-2.0
Group:          Productivity/Networking/Web/Frontends
URL:            https://tomcat.apache.org/connectors-doc/
Source0:        https://www.apache.org/dist/tomcat/tomcat-connectors/jk/tomcat-connectors-%{version}-src.tar.gz
Source1:        jk.conf
Source2:        README.SUSE
Source3:        https://www.apache.org/dist/tomcat/tomcat-connectors/jk/tomcat-connectors-%{version}-src.tar.gz.asc
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
BuildRequires:  java-devel
BuildRequires:  pcre-devel
Requires:       %{apache_mmn}
Requires:       %{apache_suse_maintenance_mmn}
Requires:       apache2
Provides:       mod_jk = %{version}
Provides:       mod_jk-ap20 = %{version}
Provides:       tomcat-mod = %{version}
Obsoletes:      mod_jk-ap20 < %{version}
Obsoletes:      tomcat-mod < %{version}

%description
This package provides modules for Apache to invisibly integrate Tomcat
capabilities into an existing Apache installation.

To load the module into Apache, run the command "a2enmod jk" as root.

%prep
%setup -q -n %{connectors_root}

%build
# prepare apr
export APACHE2_CFLAGS="%{apache_cflags}"
cd native
%configure \
	--with-pic \
	--with-apxs=%{apache_apxs}
make %{?_smp_mflags}

%install
# AJP Connector jk
install -d -m 755 %{buildroot}%{apache_libexecdir}
install -m 755 native/apache-2.0/.libs/mod_jk.so %{buildroot}%{apache_libexecdir}/
cp %{SOURCE1} .
cp %{SOURCE2} .

%files
%license LICENSE
%doc README.SUSE
%doc conf/workers.properties
%doc jk.conf
%{apache_libexecdir}/*

%changelog
