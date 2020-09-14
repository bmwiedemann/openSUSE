#
# spec file for package efivar
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


%if 0%{?suse_version} <= 1320
  # Allow building on older products (SLE11SP4, SLES12, and Leap 42.2)
  %define gcc 5
  %define gcc_v %{gcc}
  %if 120200 <= 0%{?sle_version} && 0%{?sle_version} < 130000
    %define gcc 6
    %define gcc_v %{gcc}
  %endif
%endif
%define major 1

Name:           efivar
Version:        37
Release:        0
Summary:        Tools to manage UEFI variables
License:        LGPL-2.1-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/rhinstaller/efivar
Source:         https://github.com/rhinstaller/%{name}/releases/download/%{version}/%{name}-%{version}.tar.bz2
Patch0:         libefiboot-export-disk_get_partition_info.patch
# PATCH-FIX-UPSTREAM boo#1120862
Patch1:         efivar-make-format_guid-handle-misaligned-guid-pointer.patch
# PATCH-FIX-UPSTREAM boo#1120862
Patch2:         efivar-Fix-all-the-places-Werror-address-of-packed-member-c.patch
Patch3:         efivar-bsc1127544-fix-ucs2len.patch
Patch4:         efivar-fix-efidp_ipv4_addr-fields-assignment.patch
Patch5:         efivar-bsc1175989-handle-NULL-set-variable.patch
%if "0%{?buildroot}" == "0"
# set a sane value for buildroot, unless it's already there!
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%endif
BuildRequires:  fdupes
BuildRequires:  pkg-config
BuildRequires:  popt-devel
%if 0%{?gcc} != 0
BuildRequires:  gcc%{gcc}
%endif
Requires:       libefivar%{major} = %{version}-%{release}

%description
efivar provides a simple command line interface to the UEFI variable facility.

%package -n libefivar%{major}
Summary:        Library to manage UEFI variables
Group:          System/Libraries

%description -n libefivar%{major}
Library to allow for the simple manipulation of UEFI variables.

%package devel
Summary:        Development headers for libefivar
Group:          Development/Libraries/C and C++
Requires:       libefivar%{major} = %{version}-%{release}

%description devel
Development headers required to use libefivar.

%prep
%setup -q
%patch0 -p1
%if 0%{?suse_version} == 1110
# Instead of conditional patching:
# - 'popt.pc' missing in 'popt-devel' on SLE11
perl -pi -e 's{^.*PKGS=popt.*$}{}; s{^(efivar\S* : LIBS=.*)dl}{$1popt dl}' \
   src/Makefile
# - 'uchar.h' missing in both 'glibc-devel' and 'gcc-5' packages on SLE11
perl -pi -e 's{\#include \<uchar\.h\>}{typedef __CHAR16_TYPE__ char16_t;}' \
   src/export.c
%endif
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
CFLAGS="%{optflags} -Wno-nonnull -flto"
%ifarch ia64
  CFLAGS="${CFLAGS//-fstack-protector/}"
%endif
export CFLAGS
export LDFLAGS="-flto-partition=one"

make \
%if 0%{?gcc_v} != 0
  CC=gcc-%{gcc_v} \
  AR=gcc-ar-%{gcc_v} \
  NM=gcc-nm-%{gcc_v} \
  RANLIB=gcc-ranlib-%{gcc_v} \
%endif
  libdir=%{_libdir} \
  bindir=%{_bindir}

%install
make DESTDIR=%{buildroot} \
  libdir=%{_libdir} \
  bindir=%{_bindir} \
  install
%fdupes -s %{buildroot}

# fail on undercover ABI changes
file %{buildroot}/%{_libdir}/lib%{name}.so.%{major}*

%post -n libefivar%{major} -p /sbin/ldconfig

%postun -n libefivar%{major} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license COPYING
%{_bindir}/efivar
%{_mandir}/man1/*

%files devel
%defattr(-,root,root)
%{_mandir}/man3/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n libefivar%{major}
%defattr(-,root,root)
%{_libdir}/*.so.*

%changelog
