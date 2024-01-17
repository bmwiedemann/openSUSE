#
# spec file for package ypbind
#
# Copyright (c) 2018, 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           ypbind
Version:        2.7.2
Release:        0
Summary:        NIS client daemon
License:        GPL-2.0-only
Group:          Productivity/Networking/NIS
URL:            https://github.com/thkukuk/ypbind-mt/
Source:         %{name}-mt-%{version}.tar.xz
Source2:        ypbind.service
Source3:        ypbind-systemd-pre
Source4:        ypbind.conf
Source5:        ypbind.default
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libnsl) >= 1.0.1
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libtirpc) >= 1.0.1
Requires:       libnss_nis2
Requires:       rpcbind
Requires:       yp-tools
Requires(post): /usr/bin/grep

%description
This package provides the ypbind daemon. The ypbind daemon binds NIS
clients to an NIS domain and searches a new NIS server if the old one
goes down.

Ypbind must be running on any machines which are running NIS client
programs.

%prep
%setup -q -n ypbind-mt-%{version}

%build
%configure --disable-dbus-nm
make  %{?_smp_mflags}

%install
%make_install
# Install default/ypbind
install -D -m 644 %{SOURCE5}  %{buildroot}%{_prefix}/etc/default/ypbind
# Create dummy yp.conf
mkdir -p %{buildroot}%{_sysconfdir}
touch %{buildroot}%{_sysconfdir}/yp.conf
# Create filelist with translatins
%find_lang ypbind-mt
# Install systemd stuff
install -D -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/ypbind.service
mkdir -p %{buildroot}%{_libexecdir}/ypbind
install -m 755 %{SOURCE3} %{buildroot}%{_libexecdir}/ypbind/ypbind-systemd-pre
# create symlink for rcypbind
ln -s /sbin/service %{buildroot}%{_sbindir}/rcypbind
mkdir -p %{buildroot}%{_prefix}/lib/tmpfiles.d
install -m 644 %{SOURCE4} %{buildroot}%{_prefix}/lib/tmpfiles.d/

%pre
%service_add_pre ypbind.service

%post
%service_add_post ypbind.service
%tmpfiles_create ypbind.conf
if [ -f /etc/sysconfig/ypbind ]; then
    # migrate variables from sysconfig to default
    grep ^YPBIND_OPTIONS= /etc/sysconfig/ypbind > /etc/default/ypbind
    mv /etc/sysconfig/ypbind /etc/sysconfig/ypbind.rpmsave
fi

%preun
%service_del_preun ypbind.service

%postun
%service_del_postun ypbind.service
if [ "$1" = "0" ]; then
   test -d %{_localstatedir}/yp/binding && rm -rf %{_localstatedir}/yp/binding ||:
fi

%files -f ypbind-mt.lang
%license COPYING
%doc NEWS README
%ghost %config(noreplace) %{_sysconfdir}/yp.conf
%{_prefix}/etc/default/
%{_mandir}/man5/yp.conf.5%{ext_man}
%{_mandir}/man8/ypbind.8%{ext_man}
%{_sbindir}/ypbind
%{_sbindir}/rcypbind
%{_unitdir}/ypbind.service
%dir %{_libexecdir}/ypbind
%{_libexecdir}/ypbind/*
%{_prefix}/lib/tmpfiles.d/ypbind.conf

%changelog
