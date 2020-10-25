#
# spec file for package libunwind
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


Name:           libunwind
Version:        1.4.0
Release:        0
Summary:        Call chain detection library
License:        MIT
Group:          System/Base
URL:            https://savannah.nongnu.org/projects/libunwind/
Source0:        https://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz
Source1:        https://download.savannah.gnu.org/releases/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        %{name}.keyring
Source3:        baselibs.conf
Patch0:         libunwind_U_dyn_info_list.patch
BuildRequires:  gcc-c++
BuildRequires:  lzma-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(atomic_ops)
ExclusiveArch:  %{ix86} ia64 x86_64 %{arm} ppc ppc64 ppc64le aarch64 s390x

%description
A C programming interface (API) to determine the call chain of a program.

%package devel
Summary:        Headers for the Unwind library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
A C programming interface (API) to determine the call chain of a program.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%configure \
    --enable-minidebuginfo
make %{?_smp_mflags}

%check
%if ! 0%{?qemu_user_space_build}
# run-coredump-unwind fails
make check %{?_smp_mflags} || :
%endif

%install
%make_install
find %{buildroot} -iregex '.*\.l?a$' -delete -print

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/lib*.so.*

%files devel
%{_includedir}/*
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/%{name}*.pc

%changelog
