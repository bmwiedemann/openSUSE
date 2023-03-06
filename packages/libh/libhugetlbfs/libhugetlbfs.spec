#
# spec file for package libhugetlbfs
#
# Copyright (c) 2021 SUSE LLC
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


%define my_make_flags V=1 CFLAGS="%{optflags} -fPIC" LDFLAGS="-pie" BUILDTYPE=NATIVEONLY PREFIX=%{_prefix} LIBDIR32=%{_libdir} DESTDIR=%{buildroot}
Name:           libhugetlbfs
Version:        2.23.0.g6b126a4
Release:        0
Summary:        Helper library for the Huge Translation Lookaside Buffer Filesystem
License:        LGPL-2.1-or-later
Group:          System/Libraries
URL:            https://github.com/libhugetlbfs/libhugetlbfs
Source0:        libhugetlbfs-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         libhugetlbfs.tests-malloc.patch
Patch1:         libhugetlbfs_ia64_fix_missing_test.patch
Patch2:         disable-rw-on-non-ldscripts.diff
Patch3:         zero_filesize_segment.patch
Patch4:         glibc-2.34-fix.patch
BuildRequires:  doxygen
BuildRequires:  glibc-devel-static
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# bug437293
%ifarch ppc64
Obsoletes:      libhugetlbfs-64bit
%endif

%description
The libhugetlbfs package interacts with the Linux hugetlbfs to
make large pages available to applications in a transparent manner.

%package devel
Summary:        Development files for libhugetlbfs
Group:          Development/Libraries/C and C++
Requires:       libhugetlbfs

%description devel
Devel package, header and static library, of libhugetlbfs.

%package tests
Summary:        Tests for package libhugetlbfs
Group:          Development/Tools/Other

%description tests
The testsuite for libhugetlbfs. Binaries can be found in
%{_libdir}/libhugetlbfs/tests.

%prep
%autosetup -p1

%build
echo %{version} > version
make %{my_make_flags}

%install
make %{my_make_flags} PMDIR="%{perl_vendorlib}/TLBC" \
	install install-tests
mkdir -p %{buildroot}%{_prefix}/include
cp -avL hugetlbfs.h %{buildroot}%{_prefix}/include
chmod 644 %{buildroot}%{_libdir}/*.a
if [ -f %{buildroot}%{_libdir}/libhugetlbfs/tests/obj64/dummy.ldscript ]; then
	chmod -f a-x %{buildroot}%{_libdir}/libhugetlbfs/tests/obj64/dummy.ldscript
fi
rm -r %{buildroot}%{_libdir}/libhugetlbfs/tests

%files
%defattr(-, root, root)
%doc LGPL-2.1 HOWTO README NEWS
%{_datadir}/libhugetlbfs
%{_bindir}/*
%{_mandir}/man[178]/*%{?ext_man}
%{_libdir}/libhugetlbfs_privutils.so
%{_libdir}/libhugetlbfs.so

%files devel
%defattr(-, root, root)
%{_includedir}/hugetlbfs.h
%{_libdir}/libhugetlbfs.a
%{_mandir}/man3/*%{?ext_man}

%files tests
%defattr(-,root,root)
%{_libdir}/libhugetlbfs/

%changelog
