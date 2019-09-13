#
# spec file for package libcpuset
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


%define debug_package_requires libcpuset1 = %{version}-%{release}
Name:           libcpuset
Version:        1.0
Release:        0
Summary:        cpuset processor and memory placement library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://oss.sgi.com/projects/cpusets/
Source:         ftp://oss.sgi.com/projects/cpusets/download/libcpuset-%{version}.tar.bz2
Patch0:         libcpuset-fix-missing-syscall.diff
Patch1:         libcpuset-rm-cpuonline.diff
Patch2:         bug-514127_libcpuset-cpuset_set_iopt-adds.patch
Patch3:         libcpuset-agnostic-mountpoint.diff
Patch4:         libcpuset-handle-cgroup-mount.diff
Patch5:         libcpuset-robustify-cpuset_pin-cpuset_size-cpuset_where-error-handling.diff
Patch6:         libcpuset-init-buf-2.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libbitmask-devel
BuildRequires:  libtool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Cpuset System is a processor and memory placement mechanism that
enables a system administrator to confine tasks to running certain
CPUs, and to allocating memory on certain Memory Nodes.  The libcpuset
library provides a convenient 'C' API to cpusets.

%package -n libcpuset1
Summary:        cpuset processor and memory placement library
Group:          Development/Libraries/C and C++

%description -n libcpuset1
The Cpuset System is a processor and memory placement mechanism that
enables a system administrator to confine tasks to running certain
CPUs, and to allocating memory on certain Memory Nodes.  The libcpuset
library provides a convenient 'C' API to cpusets.

%package -n libcpuset-devel
Summary:        cpuset processor and memory placement library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libcpuset1 = %{version}

%description -n libcpuset-devel
The Cpuset System is a processor and memory placement mechanism that
enables a system administrator to confine tasks to running certain
CPUs, and to allocating memory on certain Memory Nodes.  The libcpuset
library provides a convenient 'C' API to cpusets.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
sed -i -e 's@-Werror@@g' configure.in
autoreconf -fiv
%configure \
  --disable-static \
  --with-pic
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libcpuset1 -p /sbin/ldconfig

%postun -n libcpuset1 -p /sbin/ldconfig

%files -n libcpuset1
%defattr(-,root,root)
%{_libdir}/lib*so.*

%files -n libcpuset-devel
%defattr(-,root,root)
%{_mandir}/man3/*
%{_mandir}/man4/*
%{_includedir}/*
%{_libdir}/lib*so
%{_docdir}/libcpuset/libcpuset.*
%dir %{_docdir}/libcpuset

%changelog
