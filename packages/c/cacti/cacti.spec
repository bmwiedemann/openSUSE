#
# spec file for package cacti
#
# Copyright (c) 2023 SUSE LLC
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


%{!?make_build: %define make_build make %{?_smp_mflags}}
%if 0%{?suse_version} <= 1210
%define cacti_dir %{_datadir}/cacti
%else
%define cacti_dir %{apache_datadir}/cacti
%endif
%if 0%{?suse_version} >= 01230
%bcond_without systemd
%else
%bcond_with systemd
%endif
Name:           cacti
Version:        1.2.23
Release:        0
Summary:        Web Front-End to Monitor System Data via RRDtool
License:        GPL-2.0-or-later
Group:          System/Monitoring
URL:            https://www.cacti.net/
Source0:        https://www.cacti.net/downloads/%{name}-%{version}.tar.gz
Source1:        %{name}.cron
Source2:        %{name}-httpd.conf
Source3:        %{name}.logrotate
Source4:        %{name}-httpd.conf.default
Source5:        %{name}-cron.service
Source6:        %{name}-cron.timer
Source10:       cacti-rpmlintrc
# PATCH-FIX-UPSTREAM cacti-config.patch
Patch0:         %{name}-config.patch
BuildRequires:  apache-rpm-macros
Requires:       httpd
Requires:       logrotate
Requires:       net-snmp
Requires:       php-ctype
Requires:       php-gd
Requires:       php-gmp
Requires:       php-json
Requires:       php-ldap
Requires:       php-mbstring
Requires:       php-openssl
Requires:       php-posix
Requires:       php-snmp >= 7.0
Requires:       php-zlib
Requires:       rrdtool
Conflicts:      cacti-spine < %{version}
Conflicts:      cacti-spine > %{version}
Provides:       cacti-system = %{version}-%{release}
Obsoletes:      cacti-PA < %{version}-%{release}
Provides:       cacti-PA = %{version}-%{release}
BuildArch:      noarch
%if 0%{?suse_version}
BuildRequires:  apache2-devel
%else
BuildRequires:  httpd-devel
%endif
%if 0%{?suse_version}
BuildRequires:  fdupes
Requires:       mod_php_any >= 7.0
Requires:       php-sockets >= 7.0
%if %{with systemd}
BuildRequires:  pkgconfig(systemd)
%{?systemd_requires}
%else
BuildRequires:  cron
Requires:       cron
%endif
%endif
%if 0%{?fedora_version}
Requires:       php-mysqlnd >= 7.0
%else
Requires:       php-mysql >= 7.0
%endif

%description
Cacti is a complete front-end to RRDtool: it stores all necessary
information for creating graphs and populates them with data from a
MySQL database. The front-end is completely PHP driven. Along with
being ableto maintain graphs, data sources, and round robin archives
ina database, Cacti also handles data gathering. There exists an SNMP
support for those accustomed to creating traffic graphs with MRTG as
well.

%package doc
Summary:        Documentation for Cacti
Group:          System/Monitoring
Requires:       %{name} = %{version}

%description doc
Cacti is a complete front-end to RRDtool: it stores all necessary
information for creating graphs and populates them with data from a
MySQL database. The front-end is completely PHP driven. Along with
being ableto maintain graphs, data sources, and round robin archives
ina database, Cacti also handles data gathering. There exists an SNMP
support for those accustomed to creating traffic graphs with MRTG as
well.

This package contains the HTML documentation for Cacti.

%prep
%setup -q
%patch0 -p1

#delete some files
find . -type f -name "*\.orig" -exec rm {} \;
find . -type f -name .gitignore -delete
find . -type f -name .gitattributes -delete
find . -type f -name .htaccess -delete

# fix env interpreter lines
sed -i 's|%{_bindir}/env perl|%{_bindir}/perl|g' scripts/*.pl
sed -i 's|%{_bindir}/env php|%{_bindir}/php|g' include/vendor/cldr-to-gettext-plural-rules/bin/export-plural-rules

%build
#nothing to build

%install
install -d -m 0755 %{buildroot}%{cacti_dir}
install -d -m 0755 %{buildroot}%{_localstatedir}/lib/%{name}
install -d -m 0755 %{buildroot}%{_localstatedir}/log/%{name}

cp *.php        %{buildroot}%{cacti_dir}
cp -pr cache    %{buildroot}%{cacti_dir}
cp -pr cli      %{buildroot}%{cacti_dir}
cp -pr formats  %{buildroot}%{cacti_dir}
cp -pr images   %{buildroot}%{cacti_dir}
cp -pr include  %{buildroot}%{cacti_dir}
cp -pr install  %{buildroot}%{cacti_dir}
cp -pr lib      %{buildroot}%{cacti_dir}
cp -pr locales  %{buildroot}%{cacti_dir}
cp -pr mibs     %{buildroot}%{cacti_dir}
cp -pr plugins  %{buildroot}%{cacti_dir}
cp -pr resource %{buildroot}%{cacti_dir}
cp -pr rra      %{buildroot}%{cacti_dir}
cp -pr scripts  %{buildroot}%{cacti_dir}

install -d -m 0755 scripts %{buildroot}%{cacti_dir}/scripts
install -m 0755 scripts/* %{buildroot}%{cacti_dir}/scripts
install -d -m 0755 cli %{buildroot}%{cacti_dir}/cli
install -m 0755 cli/* %{buildroot}%{cacti_dir}/cli
install -m 0644 *.sql %{buildroot}%{cacti_dir}

%if %{with systemd}
install -Dm644 %{SOURCE6} %{buildroot}%{_unitdir}/%{name}-cron.timer
sed -e "s;__CACTIDIR__;%{cacti_dir};g" \
	-e "s;__APACHEUSER__;%{apache_user};g" \
    %{SOURCE5} > %{buildroot}%{_unitdir}/%{name}-cron.service
%else
# cron task
install -d -m 0755 %{buildroot}%{_sysconfdir}/cron.d
sed -e "s;__CACTIDIR__;%{cacti_dir};g" -e "s;__APACHEUSER__;%{apache_user};g" \
    %{SOURCE1} > %{buildroot}%{_sysconfdir}/cron.d/%{name}
%endif

# apache2 config
%if 0%{?suse_version}
%if 0%{?suse_version} > 1210
install -d -m 0755 %{buildroot}%{apache_sysconfdir}/conf.d
sed -e "s;__CACTIDIR__;%{cacti_dir};g" %{SOURCE4} > %{buildroot}%{apache_sysconfdir}/conf.d/%{name}.conf
install -d -m 0755 %{buildroot}%{apache_sysconfdir}/vhosts.d/conf.d
sed -e "s;__CACTIDIR__;%{cacti_dir};g" -e "s;<IfDefine CACTI>;<IfDefine CACTIVHOST>;g" \
    %{SOURCE4} > %{buildroot}%{apache_sysconfdir}/vhosts.d/conf.d/%{name}.conf
%endif
%if 0%{?suse_version} <= 1210
install -d -m 0755 %{buildroot}%{apache_sysconfdir}/conf.d
sed -e "s;__CACTIDIR__;%{cacti_dir};g" %{SOURCE2} > %{buildroot}%{apache_sysconfdir}/conf.d/%{name}.conf
%endif
%else
install -d -m 0755 %{buildroot}%{apache_sysconfdir}/../conf.d
sed -e "s;__CACTIDIR__;%{cacti_dir};g" %{SOURCE2} > %{buildroot}%{apache_sysconfdir}/../conf.d/%{name}.conf
%endif

# logrotate config
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
sed -e "s;__APACHEUSER__;%{apache_user};g" -e "s;__APACHEGROUP__;%{apache_group};g" \
    %{SOURCE3} > %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Set the correct permissions for pl and sh files
#find %%{buildroot}%%{cacti_dir} -type f -name "*.sh" -o -name "*.pl" -exec chmod ugo+x {} \;
# compute files list without config file
find %{buildroot}%{cacti_dir} -type d | sed -e 's|'%{buildroot}'|%dir |' >> %{name}.list
find %{buildroot}%{cacti_dir} -type f ! -name config.php | sed -e 's|'%{buildroot}'||' >> %{name}.list
ln -sf %{_localstatedir}/log/%{name} %{buildroot}%{cacti_dir}/log

%if 0%{?suse_version}
%fdupes %{buildroot}
%endif

%if %{with systemd}
%post
%service_add_post %{name}-cron.timer

%pre
%service_add_pre %{name}-cron.timer

%preun
%service_del_preun %{name}-cron.timer

%postun
%service_del_postun  %{name}-cron.timer
%endif

%files -f %{name}.list
%license LICENSE
%doc README.md
%attr(-,%{apache_user},%{apache_group}) %dir %{_localstatedir}/lib/%{name}
%attr(-,%{apache_user},%{apache_group}) %dir %{_localstatedir}/log/%{name}
%attr(-,%{apache_user},%{apache_group}) %{cacti_dir}/rra
%attr(-,%{apache_user},%{apache_group}) %{cacti_dir}/log
%config(noreplace) %{cacti_dir}/include/config.php
%if %{with systemd}
%{_unitdir}/%{name}-cron.service
%{_unitdir}/%{name}-cron.timer
%else
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%endif
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%if 0%{?suse_version}
%if 0%{?suse_version} <= 1210
%dir %{apache_sysconfdir}/conf.d
%config(noreplace) %{apache_sysconfdir}/conf.d/%{name}.conf
%endif
%if 0%{?suse_version} > 1210
%dir %{apache_sysconfdir}/conf.d
%config(noreplace) %{apache_sysconfdir}/conf.d/%{name}.conf
%dir %{apache_sysconfdir}/vhosts.d/conf.d
%config(noreplace) %{apache_sysconfdir}/vhosts.d/conf.d/%{name}.conf
%endif
%else
%dir %{apache_sysconfdir}/../conf.d
%config(noreplace) %{apache_sysconfdir}/../conf.d/%{name}.conf
%endif

%changelog
