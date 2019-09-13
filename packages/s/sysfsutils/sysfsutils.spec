#
# spec file for package sysfsutils
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           sysfsutils
Summary:        System Utilities Package / Libsysfs
License:        LGPL-2.1+
Group:          System/Libraries
Version:        2.1.0
Release:        0
Url:            http://linux-diag.sourceforge.net
Source:         http://aleron.dl.sourceforge.net/sourceforge/linux-diag/%{name}-%{version}.tar.gz
Source2:        baselibs.conf
Provides:       libsysfs
# bug437293
%ifarch ppc64
Obsoletes:      sysfsutils-64bit
%endif
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package's purpose is to provide a library for interfacing with the
kernel's sys filesystem mounted at /sys. The library was an attempt to
create a stable interface to sysfs, but it failed. It is still provided
for the current users, but no new software should use this library.



Authors:
--------
    Ananth Mavinakayanahalli <ananth@in.ibm.com>
    Daniel Stekloff <dsteklof@us.ibm.com>
    Mohan Kumar <mohan@in.ibm.com>

%package devel
Summary:        Development files for libsysfs
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Libsysfs' purpose is to provide a library for interfacing with the
kernel's sys filesystem mounted at /sys. The library was an attempt to
create a stable interface to sysfs, but it failed. It is still provided
for the current users, but no new software should use this library.

This package contains the development files for libsysfs.

%prep
%setup -q

%build
%configure --disable-static --with-pic
%{__make} %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
%{__rm} -v %{buildroot}/%{_libdir}/libsysfs.la
# don't install the tools
rm -f %{buildroot}/%{_bindir}/dlist_test
rm -f %{buildroot}/%{_bindir}/get_device
rm -f %{buildroot}/%{_bindir}/get_driver
rm -f %{buildroot}/%{_bindir}/get_module
rm -f %{buildroot}/%{_bindir}/testlibsysfs

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/systool
%{_mandir}/man1/systool.1.gz
%{_libdir}/libsysfs.so.*
%doc README ChangeLog

%files devel
%defattr(-,root,root)
%dir %{_includedir}/sysfs
%{_includedir}/sysfs/libsysfs.h
%{_includedir}/sysfs/dlist.h
%{_libdir}/libsysfs.so

%changelog
