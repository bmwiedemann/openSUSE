#
# spec file for package liboqs
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define         liboqs_sover 9
Name:           liboqs
Version:        0.15.0
Release:        0
Summary:        C library for quantum-resistant cryptographic algorithms
License:        MIT
Group:          Productivity/Security
URL:            https://github.com/open-quantum-safe/liboqs/
Source:         https://github.com/open-quantum-safe/liboqs/archive/refs/tags/%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         liboqs-fix-build.patch
Patch1:         liboqs-fix-prototypemismatch.patch
#PATCH-FIX-OPENSUSE boo#1101107 Do not embed the buildhost's kernel version
Patch2:         reproducible.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  libopenssl-devel
# for tests
BuildRequires:  python3-pytest
BuildRequires:  python3-PyYAML
BuildRequires:  python3-pytest-xdist

%description
liboqs is a C library for quantum-resistant cryptographic algorithms.
See the bundled README.md for particular limitations on intended use.

%package -n liboqs%{liboqs_sover}
Summary:        C library for quantum-resistant cryptographic algorithms
Group:          System/Libraries

%description -n liboqs%{liboqs_sover}
liboqs is a C library for quantum-resistant cryptographic algorithms.
See the bundled README.md for particular limitations on intended use.

%package devel
Summary:        Headers for liboqs, a library for quantum-resistant cryptography
Group:          Development/Languages/C and C++
Requires:       liboqs%{liboqs_sover} = %{version}

%description devel
liboqs is a C library for quantum-resistant cryptographic algorithms.
See the bundled README.md for particular limitations on intended use.

%prep
%autosetup -p1

%build
export RPM_OPT_FLAGS="%{optflags} -std=gnu11"

# 20220702: The %%cmake macro can't be used because a 'CMakeLists.txt' folder
# exists
cmake -S . -B build -DBUILD_SHARED_LIBS:BOOL=ON -DOQS_DIST_BUILD:BOOL=ON -DOQS_ENABLE_KEM_HQC=ON

pushd build
%cmake_build
popd

%install
%cmake_install

# need to find out what cmake option is needed
mv %{buildroot}%{_prefix}/local/* %{buildroot}%{_prefix}

#if [ "%%{_lib}" != "lib" ]; then
  # mv %%{buildroot}%%{_prefix}/lib %%{buildroot}%%{_libdir}
#fi

rmdir %{buildroot}%{_prefix}/local/

%check
pushd build
make run_tests
popd

%post -n liboqs%{liboqs_sover} -p /sbin/ldconfig
%postun -n liboqs%{liboqs_sover} -p /sbin/ldconfig

%files -n liboqs%{liboqs_sover}
%license LICENSE.txt
%{_libdir}/liboqs.so.%{version}
%{_libdir}/liboqs.so.%{liboqs_sover}
%doc README.md

%files devel
%license LICENSE.txt
%dir %{_includedir}/oqs
%{_includedir}/oqs/*
%{_libdir}/liboqs.so
%{_libdir}/pkgconfig/liboqs.pc
%dir %{_libdir}/cmake/
%dir %{_libdir}/cmake/liboqs/
%{_libdir}/cmake/liboqs/liboqsTargets-noconfig.cmake
%{_libdir}/cmake/liboqs/liboqsTargets.cmake
%{_libdir}/cmake/liboqs/liboqsConfig.cmake
%{_libdir}/cmake/liboqs/liboqsConfigVersion.cmake

%changelog
