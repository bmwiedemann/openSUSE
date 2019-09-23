#
# spec file for package telepathy-mission-control
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           telepathy-mission-control
Version:        5.16.3
Release:        0
Summary:        Telepathy Mission Control instant messaging connection manager
License:        LGPL-2.1-only
Group:          System/Libraries
URL:            http://mission-control.sourceforge.net/
Source:         http://telepathy.freedesktop.org/releases/telepathy-mission-control/%{name}-%{version}.tar.gz
# PATCH-NEEDS-REBASE lockdown-protocols.patch fdo21699 vuntz@novell.com -- Sent upstream for discussion, it will need a rewrite for MC5 WAS: PATCH-FEATURE-UPSTREAM
Patch1:         lockdown-protocols.patch
BuildRequires:  dbus-1-glib-devel >= 0.73
BuildRequires:  fdupes
BuildRequires:  libxslt-devel
BuildRequires:  pkgconfig
BuildRequires:  python-xml
BuildRequires:  telepathy-glib-devel >= 0.19.0
Requires:       dbus-1-glib >= 0.73
%glib2_gsettings_schema_requires

%description
Mission Control, or MC, is a Telepathy component providing a way for
"end-user" applications to abstract some of the details of connection
managers, to provide a simple way to manipulate a bunch of connection
managers at once, to remove the need to have in each program the
account definitions and credentials, to manage channel handling/request
and to manage presence statuses.

%package -n libmission-control-plugins0
Summary:        Telepathy Mission Control instant messaging connection manager
Group:          Development/Libraries/C and C++
Recommends:     %{name} = %{version}

%description -n libmission-control-plugins0
Mission Control, or MC, is a Telepathy component providing a way for
"end-user" applications to abstract some of the details of connection
managers, to provide a simple way to manipulate a bunch of connection
managers at once, to remove the need to have in each program the
account definitions and credentials, to manage channel handling/request
and to manage presence statuses.

%package devel
Summary:        Telepathy Mission Control instant messaging connection manager
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libmission-control-plugins0 = %{version}

%description devel
Mission Control, or MC, is a Telepathy component providing a way for
"end-user" applications to abstract some of the details of connection
managers, to provide a simple way to manipulate a bunch of connection
managers at once, to remove the need to have in each program the
account definitions and credentials, to manage channel handling/request
and to manage presence statuses.

%prep
%setup -q
# NEEDS REBASE
# %patch1

%build
%configure --disable-static --with-pic
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# Create directory that will contain the plugins (fail if it exists, so we can remove this hack)
PLUGINDIR=`PKG_CONFIG_PATH=%{buildroot}%{_libdir}/pkgconfig pkg-config --variable=plugindir mission-control-plugins`
test ! -d %{buildroot}${PLUGINDIR}
install -d %{buildroot}${PLUGINDIR}
# create symlinks for man pages
%fdupes -s %{buildroot}%{_mandir}
# create hardlinks for the rest
%fdupes %{buildroot}

%post
%glib2_gsettings_schema_post

%postun
%glib2_gsettings_schema_postun

%post -n libmission-control-plugins0 -p /sbin/ldconfig
%postun -n libmission-control-plugins0 -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/mc-tool
%{_bindir}/mc-wait-for-name
%{_libexecdir}/mission-control-5
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.AccountManager.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.MissionControl5.service
%{_datadir}/glib-2.0/schemas/im.telepathy.MissionControl.FromEmpathy.gschema.xml
%{_mandir}/man1/mc-tool.1%{?ext_man}
%{_mandir}/man1/mc-wait-for-name.1%{?ext_man}
%{_mandir}/man8/mission-control-5.8%{?ext_man}

%files -n libmission-control-plugins0
%{_libdir}/libmission-control-plugins.so.*
# Directory containing the plugins
%dir %{_libdir}/mission-control-plugins.0

%files devel
%doc %{_datadir}/gtk-doc/html/mission-control-plugins/
%{_includedir}/mission-control-5.5/
%{_libdir}/libmission-control-plugins.so
%{_libdir}/pkgconfig/mission-control-plugins.pc

%changelog
