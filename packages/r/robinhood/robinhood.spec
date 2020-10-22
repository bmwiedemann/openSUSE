#
# spec file for package robinhood
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


#
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

%define installdir_www %{_localstatedir}/lib/
%define githash 1ca39f131bb35f120f458faf4e70779d5621e8cd

Name:           robinhood
Version:        3.1.6
Release:        0
Summary:        Policy engine and reporting tool for large filesystems
License:        CECILL-C
Group:          System/Monitoring
URL:            https://github.com/cea-hpc/robinhood
Source0:        https://github.com/cea-hpc/robinhood/archive/%{githash}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         web-gui.patch
Patch2:         rbh-config.patch
Patch3:         avoid-version.patch
Patch4:         make-test_confparam-depend-on-lustre.patch
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  glib2-devel
BuildRequires:  glibc-devel
BuildRequires:  jemalloc-devel
BuildRequires:  libmysqlclient-devel
BuildRequires:  libtool
BuildRequires:  mailx
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
Requires:       which
Recommends:     mysql-server
Recommends:     mysql-server-devel
Provides:       robinhood = %{version}-%{release}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{?systemd_requires}
Requires(post): %fillup_prereq
ExcludeArch:    i586

%description
The Robinhood Policy Engine is a tool to manage contents of large
file systems. It maintains a replicate of filesystem medatada in a
database that can be queried at will. It makes it possible to
schedule mass action on filesystem entries by defining
attribute-based policies, provides fast 'find' and 'du' enhanced
clones, gives to administrators an overall view of filesystem
contents through its web UI and command line tools.

It supports any POSIX filesystem and implements advanced features for
Lustre filesystems (list/purge files per OST or pool, read MDT
changelogs...)

%package webgui
Summary:        Web interface to vizualize filesystems stats
Group:          System/Monitoring
Requires:       apache2
Requires:       php
Requires:       php-mysql
Requires:       php-pdo
BuildRequires:  apache2
Requires:       mod_php_any

%description webgui
Web interface to vizualize filesystems stats. This uses robinhood database
to display miscelancous user and group stats.

%package tools
Summary:        Tools for accessing the statistics
Group:          System/Monitoring

%description tools
The commanline tools for extracting the information out of the
robinhood database. Commands work like du or df and find. Be careful 
as robinhood_find does not always honor the file permissions.

%package tests
Summary:        Internal tests for robinhood
Group:          System/Monitoring

%description tests
Tests and examples for the robinhood policy engine.

%prep

%setup -q -n %{name}-%{githash}
%patch1
# the macro {installdir_www} is not known in the patch
sed -i 's,WWWROOT,%{installdir_www}robinhood,g' web_gui/robinhood.conf
%patch2
%patch3
%patch4 -p1 
# remove spurious executeable bits
find ./doc/templates -type f -executable -exec chmod 644 {} +

# manual call for autobuild
autoreconf -fi

%build
%configure \
  --enable-lustre \
  --disable-static \
  --enable-dependency-tracking \
  %{nil}
make %{?_smp_mflags}

%install
%make_install
# remove static linking for libraries
find %{buildroot} -regex '.*\.[la]*' -print -delete
# move architecture dependend test file library location to trick rpmlint
mv %{buildroot}%{_datadir}/robinhood/tests/create-random %{buildroot}%{_libdir}/robinhood/
ln -s %{_libdir}/robinhood/create-random %{buildroot}%{_datadir}/robinhood/tests/create-random 
# get the web config
mkdir -p %{buildroot}/%{installdir_www}/robinhood
mkdir -p %{buildroot}/%{_sysconfdir}/apache2/conf.d/
cp -r web_gui/gui_v3/* %{buildroot}/%{installdir_www}/robinhood/.
#fix executeable bits
chmod 0644  %{buildroot}/%{installdir_www}/robinhood/js/*.js
cp    web_gui/gui_v3/api/.htaccess %{buildroot}/%{installdir_www}/robinhood/api/.
install -m 644 web_gui/robinhood.conf %{buildroot}/%{_sysconfdir}/apache2/conf.d/.
# install systemd
mkdir -p  %{buildroot}/%{_unitdir}
install -m 644 scripts/robinhood.service %{buildroot}/%{_unitdir}/robinhood.service
install -m 644 scripts/robinhood@.service %{buildroot}/%{_unitdir}/robinhood@.service
ln -s /usr/sbin/service %{buildroot}%{_sbindir}/rcrobinhood 
mkdir -p %{buildroot}/%{_fillupdir}/
install -m 644 scripts/sysconfig_robinhood %{buildroot}/%{_fillupdir}/sysconfig.%{name}
# remove duplicates in tests
%fdupes -s  %{buildroot}/%{_datadir}/robinhood/tests
# Ugly fix to add right shebang line
for file in $(find %{buildroot}%{_datadir}/robinhood/tests/ -name \*.sh) ; do grep '#!/bin/bash' $file || sed -i '1s,^,#!/bin/bash\n,' $file ;done  
# created config dir
mkdir -p %{buildroot}/%{_sysconfdir}/robinhood.d/
#service files for systemd
%pre
%service_add_pre robinhood.service robinhood@.service 

%post
%{fillup_only}
%service_add_post robinhood.service robinhood@.service

%preun
%service_del_preun robinhood.service robinhood@.service

%postun
%service_del_postun robinhood.service robinhood@.service 

%files
%defattr(-,root,root)
%license LICENSE.en.txt LICENSE.fr.txt
%doc ChangeLog README.md
%doc ./doc/templates/

%{_mandir}/man1/robinhood*

%{_sbindir}/rbh-undelete
%{_sbindir}/rbh_cksum.sh
%{_sbindir}/rbh-config
%{_sbindir}/rbh-rebind
%{_sbindir}/robinhood
%{_sbindir}/rcrobinhood

%dir %{_libdir}/robinhood
%{_libdir}/robinhood/librbh_mod_*.so*

%{_unitdir}/robinhood.service
%{_unitdir}/robinhood@.service
%{_fillupdir}/sysconfig.%{name}

%dir %{_sysconfdir}/robinhood.d/

%files tools
%{_bindir}/rbh-du
%{_bindir}/rbh-find
%{_sbindir}/rbh-report
%{_sbindir}/rbh-diff
%{_mandir}/man1/rbh-*

%dir %{_sysconfdir}/robinhood.d/

%files webgui
%defattr(-,wwwrun,www)
%{installdir_www}/robinhood
%config(noreplace) %{_sysconfdir}/apache2/conf.d/robinhood.conf
%config(noreplace) %{installdir_www}/robinhood/config.php
%attr(640,-,-) %{installdir_www}/robinhood/config.php

%files tests
%defattr(-,root,root,-)
%{_datadir}/robinhood/tests/
%{_libdir}/robinhood/create-random 
%dir %{_datadir}/robinhood

%changelog
