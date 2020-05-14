#
# spec file for package oddjob
#
# Copyright (c) 2020 Stasiek Michalski <stasiek@michalski.cc>.
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


Name:           oddjob
Version:        0.34.5
Release:        0
Summary:        A D-Bus service which runs odd jobs on behalf of client applications
License:        BSD-3-Clause

URL:            https://pagure.io/oddjob
Source0:        https://releases.pagure.org/oddjob/oddjob-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  dbus-1-devel >= 0.22
BuildRequires:  dbus-1-x11
BuildRequires:  libselinux-devel
BuildRequires:  libxml2-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:  cyrus-sasl-devel
BuildRequires:  pkgconfig(krb5)
BuildRequires:  openldap2-devel
BuildRequires:  docbook
BuildRequires:  xmlto
BuildRequires:  pkgconfig(systemd)
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
Requires(post): psmisc
Requires:       dbus-1

%description
oddjob is a D-Bus service which performs particular tasks for clients which
connect to it and issue requests using the system-wide message bus.

%package mkhomedir
Summary:        An oddjob helper which creates and populates home directories
Requires:       %{name} = %{version}
Requires(post): dbus-1
Requires(post): grep
Requires(post): sed
Requires(post): psmisc

%description mkhomedir
This package contains the oddjob helper which can be used by the
pam_oddjob_mkhomedir module to create a home directory for a user
at login-time.

%prep
%autosetup

%build
%configure \
    --disable-static \
    --enable-pie --enable-now \
    --with-selinux-acls \
    --with-selinux-labels \
    --without-python --enable-xml-docs --enable-compat-dtd \
    --disable-dependency-tracking \
    --enable-systemd --disable-sysvinit
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/security/*.la
rm -f %{buildroot}%{_libdir}/security/*.a

mkdir -p %{buildroot}/%{_lib}/security
mv %{buildroot}%{_libdir}/security/*.so %{buildroot}/%{_lib}/security/

rm -f %{buildroot}%{_libdir}/*.la

mkdir -p sample-install-root/sample/{%{_sysconfdir}/{dbus-1/system.d,%{name}d.conf.d},%{_libdir}/%{name}}
install -m644 sample/oddjobd-sample.conf	sample-install-root/sample/%{_sysconfdir}/%{name}d.conf.d/
install -m644 sample/oddjob-sample.conf		sample-install-root/sample/%{_sysconfdir}/dbus-1/system.d/
install -m755 sample/oddjob-sample.sh		sample-install-root/sample/%{_libdir}/%{name}/

# Make sure we don't needlessly make these docs executable.
chmod -x src/reload src/mkhomedirfor src/mkmyhomedir

# Make sure the datestamps match in multilib pairs.
touch -r src/oddjobd-mkhomedir.conf.in %{buildroot}%{_sysconfdir}/oddjobd.conf.d/oddjobd-mkhomedir.conf
touch -r src/oddjob-mkhomedir.conf.in  %{buildroot}%{_sysconfdir}/dbus-1/system.d/oddjob-mkhomedir.conf

%files
%doc *.dtd COPYING NEWS QUICKSTART doc/oddjob.html src/reload
%doc sample-install-root/sample
%{_unitdir}/oddjobd.service
%{_bindir}/*
%{_sbindir}/*
%config(noreplace) %{_sysconfdir}/dbus-*/system.d/oddjob.conf
%config(noreplace) %{_sysconfdir}/oddjobd.conf
%dir %{_sysconfdir}/oddjobd.conf.d
%config(noreplace) %{_sysconfdir}/oddjobd.conf.d/oddjobd-introspection.conf
%dir %{_sysconfdir}/%{name}
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/sanity.sh
%{_mandir}/*/oddjob.*
%{_mandir}/*/oddjob_request.*
%{_mandir}/*/oddjobd.*
%{_mandir}/*/oddjobd-introspection.*

%files mkhomedir
%doc src/mkhomedirfor src/mkmyhomedir
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/mkhomedir
/%{_lib}/security/pam_oddjob_mkhomedir.so
%{_mandir}/*/pam_oddjob_mkhomedir.*
%{_mandir}/*/oddjob-mkhomedir.*
%{_mandir}/*/oddjobd-mkhomedir.*
%config(noreplace) %{_sysconfdir}/dbus-*/system.d/oddjob-mkhomedir.conf
%config(noreplace) %{_sysconfdir}/oddjobd.conf.d/oddjobd-mkhomedir.conf

%pre
%service_add_pre oddjobd.service

%post
if test $1 -eq 1 ; then
	killall -HUP dbus-daemon 2>&1 > /dev/null
fi
%service_add_post oddjobd.service

%postun
%service_del_postun oddjobd.service

%preun
%service_del_preun oddjobd.service

%post mkhomedir
if test $1 -eq 1 ; then
	killall -HUP dbus-daemon 2>&1 > /dev/null
fi
if [ -f /var/lock/subsys/oddjobd ] ; then
	/bin/dbus-send --system --dest=com.redhat.oddjob /com/redhat/oddjob com.redhat.oddjob.reload
fi

%changelog