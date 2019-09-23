#
# spec file for package libsmi
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


Name:           libsmi
Version:        0.4.8
Release:        0
Url:            http://www.ibr.cs.tu-bs.de/projects/libsmi
Summary:        A Library to Access SMI MIB Information
License:        MIT
Group:          System/Libraries
Source:         https://www.ibr.cs.tu-bs.de/projects/%{name}/download/%{name}-%{version}.tar.gz
Patch0:         libsmi-0.4.8-parser.patch
Patch1:         libsmi-0.4.8-gnu-source.patch
Patch2:         libsmi-CVE-2010-2891.patch
Patch3:         libsmi-flex.patch
Patch4:         libsmi-bison-3.0.patch
Patch5:         libsmi-exports.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libtool
BuildRequires:  pkg-config

%description
The purpose of libsmi is to

* Give network management applications a concise programmer-friendly
   interface to access MIB module information

* Separate the knowledge on SMI from the main parts of management
   applications

* Allow addition of new kinds of MIB repositories without the need to
adapt applications that make use of libsmi

%package devel
Summary:        Libsmi Header Files And Static Libraries
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       glibc-devel

%package -n libsmi2
Summary:        Libsmi Shared Libraries
Group:          System/Libraries  
Requires:       %{name} = %{version}

%description -n libsmi2
The purpose of libsmi is to

* Give network management applications a concise programmer-friendly
   interface to access MIB module information

* Separate the knowledge on SMI from the main parts of management
   applications

* Allow addition of new kinds of MIB repositories without the need to
adapt applications that make use of libsmi

%description devel
This package contains the header files and static libraries of package
libsmi.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2
%if 0%{?suse_version} > 1220 && 0%{?suse_version} < 1321
%patch3 -p1
%endif
%patch4 -p1
%patch5 -p1

%build
autoreconf --force --install
%configure --disable-static \
           --with-pic --enable-smi \
	       --enable-sming \
	       --with-mibdir=%{_datadir}/mibs
# Parallel build disabled
make #%{?_smp_mflags}

%install
make install DESTDIR=%buildroot
rm -f %{buildroot}%{_libdir}/*.la

%check
make check || cat test/test-suite.log && exit 0

%post -n libsmi2 -p /sbin/ldconfig

%postun -n libsmi2 -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc ANNOUNCE COPYING ChangeLog README THANKS TODO doc/*.txt
%doc %{_mandir}/man?/*
%{_bindir}/*
%{_datadir}/mibs
%{_datadir}/pibs

%files -n libsmi2
%defattr(-, root, root)
%{_libdir}/libsmi.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/libsmi.so
%{_libdir}/pkgconfig/libsmi.pc
%{_datadir}/aclocal/libsmi.m4

%changelog
