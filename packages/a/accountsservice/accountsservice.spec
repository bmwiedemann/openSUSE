#
# spec file for package accountsservice
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           accountsservice
Version:        0.6.55
Release:        0
Summary:        D-Bus Service to Manipulate User Account Information
License:        GPL-3.0-or-later
Group:          System/Daemons
URL:            https://www.freedesktop.org/wiki/Software/AccountsService/
Source0:        https://www.freedesktop.org/software/accountsservice/%{name}-%{version}.tar.xz

# WARNING: do not remove/significantly change patch0 without updating the relevant patch in gdm too
# PATCH-FIX-OPENSUSE accountsservice-sysconfig.patch bnc#688071 vuntz@opensuse.org -- Read/write autologin configuration from sysconfig, like gdm (see gdm-sysconfig-settings.patch) WAS PATCH-FIX-OPENSUSE
Patch0:         accountsservice-sysconfig.patch
# PATCH-FIX-OPENSUSE accountsservice-filter-suse-accounts.patch vuntz@opensuse.org -- Filter out some system users that are specific to openSUSE
Patch1:         accountsservice-filter-suse-accounts.patch
# PATCH-FIX-UPSTREAM accountsservice-read-root-user-cache.patch bsc#1114292 glfo#accountsservice/accountsservice#65 xwang@suse.com-- read root user cache file WAS PATCH-FIX-UPSTREAM
Patch2:         accountsservice-read-root-user-cache.patch

## SLE-only patches start at 1000
# PATCH-FEATURE-SLE as-fate318433-prevent-same-account-multi-logins.patch fate#318433 cxiong@suse.com -- prevent multiple simultaneous login.
Patch1000:      as-fate318433-prevent-same-account-multi-logins.patch

BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gio-2.0) >= 2.37.3
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(libsystemd) >= 186
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(systemd)
Recommends:     %{name}-lang
%{?systemd_ordering}

%description
The accountsservice server provides a set of D-Bus interfaces for
querying and manipulating user account information.

The implementation is based on the useradd, usermod and userdel
commands.

%package -n libaccountsservice0
Summary:        Client library for the user account information manipulation D-Bus service
# Clients do need the server to do something useful
Group:          System/Libraries
Requires:       %{name}

%description -n libaccountsservice0
The accountsservice server provides a set of D-Bus interfaces for
querying and manipulating user account information.

This package provides a client library for the service.

%package -n typelib-1_0-AccountsService-1_0
Summary:        Introspection bindings for the user account information manipulation service
Group:          System/Libraries

%description -n typelib-1_0-AccountsService-1_0
The accountsservice server provides a set of D-Bus interfaces for
querying and manipulating user account information.

This package provides the GObject Introspection bindings for the
client library.

%package devel
Summary:        Header files for the user account information manipulation service
Group:          Development/Libraries/C and C++
Requires:       libaccountsservice0 = %{version}
Requires:       typelib-1_0-AccountsService-1_0 = %{version}

%description devel
The accountsservice server provides a set of D-Bus interfaces for
querying and manipulating user account information.

%lang_package

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

# Sle-only patches start at 1000
%if !0%{?is_opensuse}
%patch1000 -p1
%endif

%build
%meson \
	-Duser-heuristics=true \
	-Dsystemd=true \
	-Dintrospection=true \
	-Dgtk_doc=true \
	%{nil}
%meson_build

%install
%meson_install
%find_lang accounts-service

%pre
%service_add_pre accounts-daemon.service

%post
%service_add_post accounts-daemon.service

%preun
%service_del_preun accounts-daemon.service

%postun
%service_del_postun accounts-daemon.service

%post -n libaccountsservice0 -p /sbin/ldconfig
%postun -n libaccountsservice0 -p /sbin/ldconfig

%files
%license COPYING
%doc NEWS README.md
%{_unitdir}/accounts-daemon.service
%{_sysconfdir}/dbus-1/system.d/org.freedesktop.Accounts.conf
%{_libexecdir}/accounts-daemon
%{_datadir}/dbus-1/interfaces/org.freedesktop.Accounts.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.Accounts.User.xml
%{_datadir}/dbus-1/system-services/org.freedesktop.Accounts.service
%{_datadir}/polkit-1/actions/org.freedesktop.accounts.policy
# Directories where the server stores user data
%dir %{_localstatedir}/lib/AccountsService
%dir %{_localstatedir}/lib/AccountsService/users
%dir %{_localstatedir}/lib/AccountsService/icons

%files -n libaccountsservice0
%{_libdir}/*.so.0*

%files -n typelib-1_0-AccountsService-1_0
%{_libdir}/girepository-1.0/AccountsService-1.0.typelib

%files devel
%doc AUTHORS TODO
%doc %{_datadir}/gtk-doc/html/lib%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/accountsservice.pc
%{_includedir}/accountsservice-1.0/
%{_datadir}/gir-1.0/AccountsService-1.0.gir

%files lang -f accounts-service.lang

%changelog
