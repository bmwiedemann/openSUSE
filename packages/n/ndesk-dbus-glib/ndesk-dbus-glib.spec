#
# spec file for package ndesk-dbus-glib
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           ndesk-dbus-glib
Version:        0.4.1
Release:        0
Summary:        Ndesk-dbus-glib provides glib integration for NDesk.DBus
License:        MIT
Group:          Development/Libraries/Other
Url:            http://www.ndesk.org/DBusSharp
Source:         http://ndesk.org/archive/ndesk-dbus/ndesk-dbus-glib-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
BuildRequires:  mono-devel
BuildRequires:  ndesk-dbus
Requires:       ndesk-dbus

%description
Ndesk-dbus-glibl provides glib integration for NDesk.DBus



%package devel
Summary:        Ndesk-dbus-glib provides glib integration for NDesk.DBus
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel 
Ndesk-dbus-glibl provides glib integration for NDesk.DBus



%prep
%setup

%build
./configure --prefix=%_prefix
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
# move .pc to usr/share
mkdir -p $RPM_BUILD_ROOT%_datadir/pkgconfig
mv $RPM_BUILD_ROOT/usr/lib/pkgconfig/ndesk-dbus-glib-1.0.pc $RPM_BUILD_ROOT%_datadir/pkgconfig

%files devel
%defattr(-,root,root)
%{_datadir}/pkgconfig/ndesk-dbus-glib-1.0.pc

%files
%defattr(-,root,root)
%doc COPYING README
%{_prefix}/lib/mono/gac/NDesk.DBus.GLib
%{_prefix}/lib/mono/ndesk-dbus-glib-1.0

%changelog
