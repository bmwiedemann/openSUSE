#
# spec file for package startup-notification
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


Name:           startup-notification
Version:        0.12
Release:        0
Summary:        Reference Implementation for the Startup-Notification Protocol
License:        LGPL-2.1-or-later
Group:          System/X11/Utilities
URL:            http://www.freedesktop.org/wiki/Software/startup-notification
Source:         http://www.freedesktop.org/software/startup-notification/releases/startup-notification-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb) >= 1.6
BuildRequires:  pkgconfig(xcb-aux)
BuildRequires:  pkgconfig(xcb-event)

%description
Startup-notification contains a reference implementation of the
startup-notification protocol.

%package -n libstartup-notification-1-0
Summary:        Reference Implementation for the Startup-Notification Protocol
Group:          System/X11/Utilities
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
#

%description -n libstartup-notification-1-0
Startup-notification contains a reference implementation of the
startup-notification protocol.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/GNOME
Requires:       libstartup-notification-1-0 = %{version}
#

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libstartup-notification-1-0 -p /sbin/ldconfig
%postun -n libstartup-notification-1-0 -p /sbin/ldconfig

%files -n libstartup-notification-1-0
%license COPYING
%doc AUTHORS NEWS ChangeLog
%{_libdir}/*.so.*

%files devel
%{_includedir}/startup-notification-1.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
