#
# spec file for package monitoring-plugins-mysql_health
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define         realname check_mysql_health
Name:           monitoring-plugins-mysql_health
Version:        3.0.0.5
Release:        0
Summary:        Check various parameters of a MySQL database
License:        GPL-2.0+
Group:          System/Monitoring
Url:            http://labs.consol.de/lang/en/nagios/check_mysql_health/
Source0:        https://labs.consol.de/assets/downloads/nagios/%{realname}-%{version}.tar.gz
BuildRequires:  nagios-rpm-macros
Requires:       mysql-client
Recommends:     perl(DBD::mysql)
Recommends:     perl(DBI)
Provides:       nagios-plugins-mysql_health = %{version}-%{release}
Obsoletes:      nagios-plugins-mysql_health < %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
When using a database that are business critical it can be a good idea to
monitor the internals.

This Nagios plugin allows you to monitor the internal details of your
MySQL database.

%prep
%setup -q -n %{realname}-%{version}

%build
%configure \
	--libexecdir=%{nagios_plugindir} \
	--with-nagios-user=%{nagios_user} \
	--with-nagios-group=%{nagios_group} \
	--with-mymodules-dyn-dir=%{nagios_plugindir} \
 	--with-mymodules-dir=%{nagios_plugindir} \
	--with-perl=%{_bindir}/perl

%install
mkdir -p %{buildroot}/%{nagios_plugindir}
mkdir -p %{buildroot}/%{pnp4nagios_templatedir}
make %{?_smp_mflags} DESTDIR=%{buildroot} install
mv contrib/check_mysql_health.php %{buildroot}/%{pnp4nagios_templatedir}/check_mysql_health.php

%files
%defattr(-,root,root)
%attr(0644,root,root) %doc README TODO NEWS ChangeLog AUTHORS COPYING contrib
# avoid build dependecy of nagios - own the dirs
%dir %{nagios_libdir}
%{nagios_plugindir}/
%dir %{pnp4nagios_datadir}
%dir %{pnp4nagios_templatedir}
%attr(0644,root,root) %{pnp4nagios_templatedir}/check_mysql_health.php

%changelog
