#
# spec file for package sblim-tools-libra
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


Name:           sblim-tools-libra
Version:        1.0
Release:        0
URL:            http://www.sblim.org
Source:         http://prdownloads.sourceforge.net/sblim/%{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}-docdir.patch
Patch1:         0001-declare-sys_errlist.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libtool
Summary:        SBLIM Common Resource Access Library for WBEM-SMT tasks
License:        EPL-1.0
Group:          System/Libraries
%define debug_package_requires libRaTools0 = %{version}-%{release}

%description
The tools-libra package provides common functionality required by 
the task-specific resource access layers of wbem-smt tasks such as 
cmpi-dns and cmpi-samba.

%package -n libRaTools0
%define libname libRaTools0
Summary:        SBLIM Common Resource Access Library for WBEM-SMT tasks
Group:          System/Libraries

%description -n %libname
The tools-libra package provides common functionality required by 
the task-specific resource access layers of wbem-smt tasks such as 
cmpi-dns and cmpi-samba.


%package devel
Summary:        Development files for libRaTools
Group:          Development/Libraries/C and C++
Provides:       libRaTools-devel = %version
Requires:       %libname = %{version}

%description devel
The tools-libra package provides common functionality required by 
the task-specific resource access layers of the wbem-smt tasks such as 
cmpi-dns and cmpi-samba.
This package includes the header files and link libraries for dependent 
provider packages.

%prep
%setup -q
%patch0
%patch1 -p1

%build
autoreconf -fi
%configure \
	--disable-static \
make

%clean
rm -rf %buildroot

%install
%if 0%{?suse_version}
make DESTDIR=%buildroot install
%else
make DESTDIR=%buildroot docdir=%_docdir/%name-%version install
%endif
rm %buildroot/%{_libdir}/*.la

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr(-,root,root) 
%{_libdir}/libRaTools.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/sblim
%{_libdir}/libRaTools.so
%if 0%{?suse_version}
%doc %_docdir/%name
%else
%doc %_docdir/%name-%version
%endif

%changelog
