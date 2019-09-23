#
# spec file for package libatasmart
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


Name:           libatasmart
Version:        0.19
Release:        0
Summary:        ATA S.M.A.R.T. Disk Health Monitoring Library
License:        LGPL-2.1+
Group:          System/Libraries
Url:            http://git.0pointer.net/libatasmart.git/
Source:         http://0pointer.de/public/%{name}-%{version}.tar.xz
Patch0:         libatasmart-0.19-wd-fix.patch

BuildRequires:  libudev-devel
BuildRequires:  pkgconfig
BuildRequires:  xz

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A small and lightweight parser library for ATA S.M.A.R.T. hard disk
health monitoring.

As the name suggests libatasmart only does ATA S.M.A.R.T.,
there is no support for SCSI harddisks. SCSI S.M.A.R.T. is a
very different system, support for it should be implemented in
a separate library "libscsismart" if there should ever be
demand for it.

This library is supposed to be lean and small and thus
supports only a subset of the S.M.A.R.T. functionality.
However, I claim that it implements the relevant part of it.
If you need full control over all S.M.A.R.T. functionality of
your hardware please refer to Buce Allen's smartmontools.

%package -n libatasmart4
Summary:        ATA S.M.A.R.T. Disk Health Monitoring Library
Group:          System/Libraries

%description -n libatasmart4
A small and lightweight parser library for ATA S.M.A.R.T. hard disk
health monitoring.

%package utils
Summary:        ATA S.M.A.R.T. Disk Health Monitoring Library - Utilities
Group:          Hardware/Other
Requires:       libatasmart4 = %{version}

%description utils
A small and lightweight parser library for ATA S.M.A.R.T. hard disk
health monitoring.

%package devel
Summary:        ATA S.M.A.R.T. Disk Health Monitoring Library - Development Files
Group:          Development/Libraries/C and C++
Requires:       libatasmart4 = %{version}

%description devel
A small and lightweight parser library for ATA S.M.A.R.T. hard disk
health monitoring.

%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%makeinstall
rm -f %{buildroot}%{_libdir}/*.la
# We already package this
rm %{buildroot}%{_datadir}/doc/libatasmart/README

%clean
rm -rf %{buildroot}

%post -n libatasmart4 -p /sbin/ldconfig

%postun -n libatasmart4 -p /sbin/ldconfig

%files -n libatasmart4
%defattr(-,root,root)
%doc README LGPL
%{_libdir}/libatasmart.so.*

%files utils
%defattr(-,root,root)
%{_sbindir}/sk*

%files devel
%defattr(-,root,root)
%doc blob-examples/
%{_includedir}/atasmart.h
%{_libdir}/libatasmart.so
%{_libdir}/pkgconfig/libatasmart.pc
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/*.vapi

%changelog
