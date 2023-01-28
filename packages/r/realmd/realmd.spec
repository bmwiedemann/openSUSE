#
# spec file for package realmd
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


Name:           realmd
Version:        0.17.1
Release:        0
Summary:        AD integration detection
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
URL:            https://www.freedesktop.org/software/realmd/
Source:         https://gitlab.freedesktop.org/realmd/realmd/-/archive/%{version}/realmd-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-tools
BuildRequires:  glib2-devel >= 2.36
BuildRequires:  intltool
BuildRequires:  libpackagekit-glib2-devel
BuildRequires:  libtool
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  polkit-devel
BuildRequires:  xmlto
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(systemd)
Recommends:     %{name}-lang
%{?systemd_requires}

%description
This packages contains realmd.

Realmd is an on demand system DBus service, which allows
callers to configure network authentication and domain
membership in a standard way. realmd discovers information
about the domain or realm automatically and does not require
complicated configuration in order to join a domain or realm.

realmd configures sssd or winbind to do the actual network
authentication and user account lookups.

%lang_package

%prep
%setup -q

%build
NOCONFIGURE=1 sh ./autogen.sh
# krb5-config is hidden
PATH=$PATH:%{_prefix}/lib/mit/bin
%configure \
  --with-distro=suse \
  --with-systemd-journal=no \
  --with-systemd-unit-dir=%{_unitdir} \
  --with-private-dir=%{_libdir}/%{name}
%make_build

%install
%make_install

%find_lang %{name}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rc%{name}

%pre
if [ -f %{_localstatedir}/lib/systemd/migrated/%{name} ]; then
%service_add_pre %{name}.service
fi

%post
%service_add_post %{name}.service

%preun
%service_del_preun %{name}.service

%postun
%service_del_postun %{name}.service

%files
%{_sbindir}/realm
%{_sbindir}/rc%{name}
%{_unitdir}/realmd.service
%{_libexecdir}/%{name}
%{_libdir}/%{name}/
%config %{_sysconfdir}/dbus-1/system.d/org.freedesktop.realmd.conf
%{_datadir}/dbus-1/system-services/org.freedesktop.realmd.service
%{_datadir}/polkit-1/actions/org.freedesktop.realmd.policy

%{_datadir}/doc/realmd
%{_mandir}/man5/realmd.conf.5%{?ext_man}
%{_mandir}/man8/realm.8%{?ext_man}

%files lang -f %{name}.lang

%changelog
