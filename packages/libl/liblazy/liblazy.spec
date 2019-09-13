#
# spec file for package liblazy
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           liblazy
Version:        0.2
Release:        0
Summary:        Liblazy - D-Bus methods provided for convenience
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://freedesktop.org/wiki/Software/liblazy/

#Git-Clone:	git://anongit.freedesktop.org/git/liblazy
Source:         %{name}-%{version}.tar.bz2
Source2:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  dbus-1-devel
BuildRequires:  pkg-config

%description
Liblazy is a simple and easy to use library that provides convenient
functions for sending messages over the D-Bus daemon, querying
information from HAL or asking PolicyKit for a privilege.

%package -n liblazy1
Summary:        Liblazy - D-Bus methods provided for convenience
Group:          System/Libraries

%description -n liblazy1
Liblazy is a simple and easy to use library that provides convenient
functions for sending messages over the D-Bus daemon, querying
information from HAL or asking PolicyKit for a privilege.

%package devel
Summary:        Liblazy - D-Bus methods provided for convenience
Group:          Development/Libraries/C and C++
Requires:       liblazy1 = %{version}-%{release} dbus-1-devel

%description devel
Liblazy is a simple and easy to use library that provides convenient
functions for sending messages over the D-Bus daemon, querying
information from HAL or asking PolicyKit for a privilege.

%prep
%setup

%build
%configure --disable-static 
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm $RPM_BUILD_ROOT/usr/lib*/liblazy.la

%post -n liblazy1 -p /sbin/ldconfig

%postun -n liblazy1 -p /sbin/ldconfig

%files -n liblazy1
%defattr(-,root,root)
%doc COPYING
%_libdir/liblazy.so.*

%files devel
%defattr(-,root,root)
%_includedir/liblazy.h
%_libdir/pkgconfig/*.pc
%_libdir/liblazy.so

%changelog
