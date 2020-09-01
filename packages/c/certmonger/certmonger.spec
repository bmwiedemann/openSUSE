#
# spec file for package certmonger
#
# Copyright (c) 2020 SUSE LLC
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


Name:           certmonger
Version:        0.79.11
Release:        0
Summary:        Certificate status monitor and PKI enrollment client
License:        GPL-3.0-or-later

URL:            http://pagure.io/certmonger/
Source0:        http://releases.pagure.org/certmonger/certmonger-%{version}.tar.gz
Patch0002:      0002-certmonger-return-type.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dbus-1
BuildRequires:  dbus-1-devel
BuildRequires:  diffutils
BuildRequires:  dos2unix
BuildRequires:  expect
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  krb5-devel
BuildRequires:  libcurl-devel
BuildRequires:  libfreebl3-hmac
BuildRequires:  libidn2-devel
BuildRequires:  libsoftokn3-hmac
BuildRequires:  libtalloc-devel
BuildRequires:  libtevent-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
BuildRequires:  mozilla-nspr-devel
BuildRequires:  mozilla-nss-devel
BuildRequires:  mozilla-nss-sysinit
BuildRequires:  mozilla-nss-tools
BuildRequires:  openldap2-devel
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  popt-devel
BuildRequires:  python3-dbus-python
BuildRequires:  which
BuildRequires:  xmlrpc-c-devel

Requires:       dbus-1
Requires(post): dbus-1
Requires(preun): dbus-1
Requires(preun): sed

BuildRequires:  systemd-rpm-macros
%{?systemd_requires}

%description
Certmonger is a service which is primarily concerned with getting your
system enrolled with a certificate authority (CA) and keeping it enrolled.

%prep
%autosetup -p1

%build
autoreconf -i -f
%configure \
    --enable-systemd \
    --enable-tmpfiles \
    --with-homedir=/run/certmonger \
    --with-tmpdir=/run/certmonger --enable-pie --enable-now

%make_build

%install
%make_install
mkdir -p %{buildroot}/%{_localstatedir}/lib/certmonger/{cas,requests}
%{find_lang} %{name}

%check
make check

%pre
%service_add_pre certmonger.service

%post
if test $1 -eq 1 ; then
  %{_bindir}/dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig 2>&1 || :
fi
%service_add_post certmonger.service
%tmpfiles_create certmonger.conf

%preun
%service_del_preun certmonger.service

%postun
%service_del_postun certmonger.service

%files -f %{name}.lang
%doc README.md LICENSE STATUS doc/*.txt
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/*
%{_datadir}/dbus-1/services/*
%dir %{_sysconfdir}/certmonger
%config(noreplace) %{_sysconfdir}/certmonger/certmonger.conf
%ghost /run/certmonger
%{_bindir}/*
%{_sbindir}/certmonger
%{_mandir}/man*/*
%{_libexecdir}/%{name}
%{_localstatedir}/lib/certmonger
%{_tmpfilesdir}/certmonger.conf
%{_datadir}/dbus-1/system-services/*

%changelog
