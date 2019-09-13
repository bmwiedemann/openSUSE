#
# spec file for package libevtlog
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libevtlog
Version:        0.2.13
Release:        0
Summary:        Syslog-ng event logger library source
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://www.balabit.com/products/syslog_ng/
Source0:        http://www.balabit.com/downloads/files/syslog-ng/open-source-edition/3.4.4/source/eventlog_%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  pkg-config

%description
The EventLog library aims to be a replacement of the simple syslog()
API provided on UNIX systems. The major difference between EventLog and
syslog is that EventLog tries to add structure to messages.

Where you had a simple non-structrured string in syslog() you have a
combination of description and tag/value pairs.

EventLog provides an interface to build, format and output an event
record. The exact format and output method can be customized by the
administrator via a configuration file.

This package provides the source files.

The package may contain Novell/SUSE specific modifications/extensions,
please report problems using Bugzilla at https://bugzilla.novell.com/
before you contact the authors.

The official home page of syslog-ng is:
http://www.balabit.com/network-security/syslog-ng/

%package -n libevtlog0
Summary:        Syslog-ng event logger library runtime
Group:          System/Libraries

%description -n libevtlog0
The EventLog library aims to be a replacement of the simple syslog()
API provided on UNIX systems. The major difference between EventLog and
syslog is that EventLog tries to add structure to messages.

EventLog provides an interface to build, format and output an event
record. The exact format and output method can be customized by the
administrator via a configuration file.

This package provides the runtime part of the library.

The package may contain Novell/SUSE specific modifications/extensions,
please report problems using Bugzilla at https://bugzilla.novell.com/
before you contact the authors.

The official home page of syslog-ng is:
http://www.balabit.com/network-security/syslog-ng/

%package devel
Summary:        Syslog-ng event logger library development files
Group:          Development/Libraries/C and C++
Requires:       %{name}0 = %{version}
Requires:       glibc-devel

%description devel
The EventLog library aims to be a replacement of the simple syslog()
API provided on UNIX systems. The major difference between EventLog and
syslog is that EventLog tries to add structure to messages.

EventLog provides an interface to build, format and output an event
record. The exact format and output method can be customized by the
administrator via a configuration file.

This package provides the development files. The package may contain
Novell/SUSE specific modifications/extensions, please report problems
using Bugzilla at https://bugzilla.novell.com/ before you contact the
authors.

The official home page of syslog-ng is:
http://www.balabit.com/network-security/syslog-ng/

%prep
%setup -q -n eventlog-%{version}

%build
%configure --disable-static
%{__make} %{?_smp_mflags}

%check
make check

%install
make DESTDIR=%{buildroot} install
rm -vf %{buildroot}/%{_libdir}/%{name}.la

%post -n libevtlog0 -p /sbin/ldconfig

%postun -n libevtlog0 -p /sbin/ldconfig

%files -n libevtlog0
%defattr(-,root,root)
%{_libdir}/libevtlog*.so.0*

%files devel
%defattr(-,root,root)
%doc AUTHORS COPYING CREDITS NEWS PORTS README VERSION
%doc ChangeLog doc/*.txt
%dir %_includedir/eventlog
%_includedir/eventlog/*.h
%_libdir/libevtlog*.so
%_libdir/pkgconfig/eventlog.pc

%changelog
