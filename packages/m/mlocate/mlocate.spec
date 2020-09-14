#
# spec file for package mlocate
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           mlocate
Version:        0.26
Release:        0
Summary:        A utility for finding files by name
License:        GPL-2.0-only
Group:          System/Monitoring
URL:            https://pagure.io/mlocate
Source0:        https://fedorahosted.org/releases/m/l/%{name}/%{name}-%{version}.tar.xz
Source1:        updatedb.conf
Source2:        sysconfig.locate
# apparmor profile
Source3:        usr.bin.locate
Source4:        usr.bin.updatedb
Source5:        mlocate.timer
Source6:        mlocate.service
BuildRequires:  gettext-tools
BuildRequires:  grep
BuildRequires:  sed
BuildRequires:  systemd-rpm-macros
BuildRequires:  xz
Requires:       apparmor-abstractions
Requires(post): %fillup_prereq
Recommends:     %{name}-lang = %{version}
Provides:       findutils:%{_bindir}/locate
# findutils is at version 4.5 so we need newer
# provides here to get it really obsoleted
Provides:       findutils-locate = 5.%{version}
Obsoletes:      findutils-locate < 5.%{version}
%if 0%{?suse_version} > 1320
Requires:       user(nobody)
%endif

%description
A new locate implementation. The m character
stands for merging, because updatedb reuses the
existing database to avoid re-reading most of the
file system.

%lang_package

%prep
%setup -q

# do not check for visibilty by default as we go with nobody
sed -i \
	-e 's:conf_check_visibility = true:conf_check_visibility = false:g' \
	src/conf.c

%build
export CFLAGS="%{optflags} -fPIE"
export LDFLAGS="-pie"
%configure \
	--localstatedir=%{_localstatedir}/lib \
	--enable-nls \
	--disable-rpath
make groupname=nobody %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} groupname=nobody install
%find_lang %{name} || echo -n >> %{name}.lang
# DB file
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
echo -n >> %{buildroot}%{_localstatedir}/lib/%{name}/%{name}.db
# Config
mkdir -p %{buildroot}%{_sysconfdir}
install -p -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}
# Sysconfig settings
install -D -m 644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.locate
# systemd units
install -D -m 644 %{SOURCE5} %{buildroot}%{_unitdir}/mlocate.timer
install -D -m 644 %{SOURCE6} %{buildroot}%{_unitdir}/mlocate.service
# rc symlink
mkdir -p %{buildroot}%{_sbindir}
ln -s /usr/sbin/service %{buildroot}/%{_sbindir}/rcmlocate
# apparmor
install -D -m 644 %{SOURCE3} %{buildroot}%{_sysconfdir}/apparmor.d/usr.bin.locate
install -D -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/apparmor.d/usr.bin.updatedb

%check
make check %{?_smp_mflags}

%pre
%service_add_pre mlocate.service mlocate.timer

%post
%{fillup_only -n locate}
%service_add_post mlocate.service mlocate.timer

%preun
%service_del_preun mlocate.service mlocate.timer

%postun
%service_del_postun mlocate.service mlocate.timer

%files
%license COPYING
%doc AUTHORS ChangeLog README NEWS
%config(noreplace) %{_sysconfdir}/updatedb.conf
%attr(0755,root,root) %{_bindir}/locate
%{_bindir}/updatedb
%{_mandir}/man*/*
%{_unitdir}/mlocate.timer
%{_unitdir}/mlocate.service
%dir %{_localstatedir}/lib/mlocate
%ghost %{_localstatedir}/lib/mlocate/mlocate.db
%{_fillupdir}/*
%dir %{_sysconfdir}/apparmor.d/
%{_sysconfdir}/apparmor.d/*
%{_sbindir}/rcmlocate

%files lang -f %{name}.lang

%changelog
