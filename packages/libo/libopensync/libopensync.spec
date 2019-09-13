#
# spec file for package libopensync
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


Name:           libopensync
Version:        0.22
Release:        0
Summary:        A Platform and Distribution Independent Synchronization Framework
License:        LGPL-2.1+
Group:          Productivity/Networking/Other
Url:            http://www.opensync.org
Source:         %{name}-%{version}.tar.bz2
Patch0:         libopensync-wrapper-wno_uninitialized.diff
Patch1:         libopensync-fix-vcal-reminder.diff
Patch2:         libopensync-vformat-infinite-loop.diff
Patch3:         libopensync-sqlite-buildfix.diff
Patch4:         libopensync-swig-fix.diff
Patch5:         libopensync-fixed-unused-variables.diff
Patch6:         libopensync-swig-2x.patch
Patch7:         libopensync-wrong-memset.patch
#PATCH-FIX-UPSTREAM fix misleading indentation
Patch8:         libopensync-0.22-gcc6.patch
BuildRequires:  glib2-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  python-devel
BuildRequires:  sqlite3-devel
BuildRequires:  swig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
OpenSync is a synchronization framework that is platform and
distribution independent. It consists of several plug-ins that can be
used to connect to devices, a powerful sync engine, and the framework
itself. The synchronization framework is kept very flexible and is
capable of synchronizing any type of data, including contacts,
calendar, tasks, notes, and files.

To sync various sources, additionally install the plug-ins.

%package devel
Summary:        Header files, libraries and development documentation for libopensync
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glib2-devel
Requires:       libxml2-devel
Requires:       python-devel
Requires:       sqlite3-devel

%description devel
This package contains the header files, static libraries and
development documentation for libopensync. If you like to develop
programs using libopensync, you will need to install this package.

%package tools
Summary:        Tools for libopensync
Group:          Productivity/Networking/Other
Requires:       %{name} = %{version}

%description tools
OpenSync is a synchronization framework that is platform and
distribution independent. This package contains some tools needed for
testing and debugging it.

%package -n python-opensync
Summary:        Python bindings for OpenSync
Group:          Development/Languages/Python
Requires:       %{name} = %{version}

%description -n python-opensync
OpenSync is a synchronization framework that is platform and
distribution independent. It consists of several plug-ins that can be
used to connect to devices, a powerful sync engine, and the framework
itself. The synchronization framework is kept very flexible and is
capable of synchronizing any type of data, including contacts,
calendar, tasks, notes, and files.

To sync various sources, additionally install the plug-ins.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3
%patch4 -p1
%patch5 -p1
%patch6
%patch7
%patch8 -p1

%build
autoreconf -sif
# -fno-strict-aliasing needed for python wrapper
CFLAGS="%{optflags} -fno-strict-aliasing -Wno-error=deprecated-declarations"
%configure --disable-static --libexecdir=%{_libdir}/opensync/ --enable-tools --disable-profiling --disable-unit-tests
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install
mkdir -p %{buildroot}/%{_libdir}/opensync/plugins
mkdir -p %{buildroot}/%{_datadir}/opensync/defaults
find %{buildroot} -type f -name "*.la" -delete -print

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPYING INSTALL NEWS README TODO
%{_libdir}/libopensync-xml.so.*
%{_libdir}/libopensync.so.*
%{_libdir}/libosengine.so.*
%dir %{_libdir}/opensync
%dir %{_libdir}/opensync/formats
%dir %{_libdir}/opensync/plugins
%{_libdir}/opensync/osplugin
%{_libdir}/opensync/formats/*.so
%dir %{_datadir}/opensync
%dir %{_datadir}/opensync/defaults

%files -n python-opensync
%defattr(-, root, root)
%{py_sitedir}/_opensync.so*
%{py_sitedir}/opensync.py*

%files devel
%defattr(-,root,root)
%{_libdir}/libopensync-xml.so
%{_libdir}/libopensync.so
%{_libdir}/libosengine.so
%dir %{_includedir}/opensync-1.0
%dir %{_includedir}/opensync-1.0/opensync
%{_includedir}/opensync-1.0/opensync/*
%dir %{_includedir}/opensync-1.0/osengine
%{_includedir}/opensync-1.0/osengine/*
%{_libdir}/pkgconfig/opensync-1.0.pc
%{_libdir}/pkgconfig/osengine-1.0.pc

%files tools
%defattr(-,root,root)
%{_bindir}/osyncdump
%{_bindir}/osyncplugin
%{_bindir}/osyncstress
%{_bindir}/osyncbinary
%{_bindir}/osynctest

%changelog
