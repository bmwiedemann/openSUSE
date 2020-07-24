#
# spec file for package telepathy-gabble
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


Name:           telepathy-gabble
Version:        0.18.4
Release:        0
Summary:        XMPP connection manager for Telepathy
License:        LGPL-2.1-or-later
URL:            https://telepathy.freedesktop.org/wiki/
Source:         http://telepathy.freedesktop.org/releases/telepathy-gabble/%{name}-%{version}.tar.gz
Patch0:         telepathy-gabble-0.18.4-python3.patch
Patch1:         0001-xmpp-console-Explicitly-state-python-in-the-shebang.patch
# PATCH-FIX-OPENSUSE telepathy-gabble-SNI.patch bsc#1136781 sckang@suse.com -- Add SNI support
Patch2:         telepathy-gabble-SNI.patch
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libexslt)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(nice) >= 0.0.11
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(telepathy-glib) >= 0.19.7
Recommends:     ca-certificates
# doc subpackage removed during 12.2 development
Provides:       %{name}-doc = %{version}
Obsoletes:      %{name}-doc < %{version}

%description
Gabble is a Jabber/XMPP connection manager for the Telepathy framework,
currently supporting single user chats, multi user chats and
voice/video calls. Install this package to use Telepathy instant
messaging clients with Jabber/XMPP servers, including Google Talk.

%package xmpp-console
Summary:        XMPP connection manager for Telepathy -- XMPP Console
Requires:       %{name} = %{version}
Requires:       python3-gobject

%description xmpp-console
This utility is a XMPP console user interface, for telepathy-gabble.

%prep
%autosetup -p1

%build
%configure \
        --disable-static \
        --docdir=%{_docdir}/%{name} \
        --with-ca-certificates=%{_sysconfdir}/ssl/ca-bundle.pem
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
cp AUTHORS ChangeLog %{buildroot}%{_docdir}/%{name}

%check
# the test code is py2 only :(
#%%make_build check

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%doc %{_docdir}/%{name}/*.html
%dir %{_datadir}/telepathy
%dir %{_datadir}/telepathy/managers
%dir %{_libdir}/telepathy
%dir %{_libdir}/telepathy/gabble-0
%dir %{_libdir}/telepathy/gabble-0/plugins
%{_libexecdir}/telepathy-gabble
%{_libdir}/telepathy/gabble-0/lib/
%{_libdir}/telepathy/gabble-0/plugins/libgateways.so
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.gabble.service
%{_datadir}/telepathy/managers/gabble.manager
%{_mandir}/man8/telepathy-gabble.8%{?ext_man}

%files xmpp-console
%{_bindir}/telepathy-gabble-xmpp-console
%{_libdir}/telepathy/gabble-0/plugins/libconsole.so

%changelog
