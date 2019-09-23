#
# spec file for package Ne10
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


%define         sover 10
Name:           Ne10
Version:        1.2.1
Release:        0
Summary:        A library of common math and DSP functions optimized for ARM NEON
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://projectne10.github.com/Ne10/
Source:         https://github.com/projectNe10/Ne10/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  armv7hl aarch64

%description
The library provides some of the fastest implementations of key
operations available for the ARM v7-A and v8-A architectures,
particularly focusing on math, signal processing, image processing,
and physics functions.

%package -n libNE10-%{sover}
Summary:        A library of common math and DSP functions optimized for ARM NEON
Group:          Development/Libraries/C and C++

%description -n libNE10-%{sover}
Ne10 is a library of common functions that have been
optimised for ARM-based CPUs equipped with NEON SIMD capabilities.

The library provides some of the fastest implementations of key
operations available for the ARM v7-A and v8-A architectures,
particularly focusing on math, signal processing, image processing,
and physics functions.

This package contains the shared library.

%package -n libNE10_test%{sover}
Summary:        A library of common math and DSP functions optimized for ARM NEON
Group:          Development/Libraries/C and C++

%description -n libNE10_test%{sover}
The library provides some of the fastest implementations of key
operations available for the ARM v7-A and v8-A architectures,
particularly focusing on math, signal processing, image processing,
and physics functions.

This package contains the shared library with tests.

%package devel
Summary:        Development files for Ne10, a math/DSP library for ARM NEON
Group:          Development/Libraries/C and C++
Requires:       libNE10-%{sover} = %{version}
Requires:       libNE10_test%{sover} = %{version}

%description devel
The library provides some of the fastest implementations of key
operations available for the ARM v7-A and v8-A architectures,
particularly focusing on math, signal processing, image processing,
and physics functions.

This package contains the development files.

%prep
%setup -q

%build
%cmake \
  -DNE10_BUILD_STATIC=OFF \
  -DNE10_BUILD_SHARED=ON  \
  -DGNULINUX_PLATFORM=ON  \
  %ifarch aarch64
  -DNE10_LINUX_TARGET_ARCH=aarch64 \
  %else
  -DNE10_LINUX_TARGET_ARCH=armv7 \
  %endif
  -DCMAKE_BUILD_TYPE=RelWithDebInfo
make %{?_smp_mflags}

%install
for i in inc/*.h; do
    install -p -D -m 0644 $i %{buildroot}/%{_includedir}/$(basename $i)
done

for i in build/modules/libNE*so.%{sover}; do
    install -p -D -m 0755 $i %{buildroot}/%{_libdir}/$(basename $i)
    ln -s -r %{buildroot}/%{_libdir}/$(basename $i) %{buildroot}/%{_libdir}/$(basename $i .so.%{sover}).so
done

%post -n libNE10-%{sover} -p /sbin/ldconfig
%post -n libNE10_test%{sover} -p /sbin/ldconfig
%postun -n libNE10-%{sover} -p /sbin/ldconfig
%postun -n libNE10_test%{sover} -p /sbin/ldconfig

%files -n libNE10-%{sover}
%defattr(-,root,root)
%doc LICENSE
%{_libdir}/libNE10.so.%{sover}*

%files -n libNE10_test%{sover}
%defattr(-,root,root)
%doc LICENSE
%{_libdir}/libNE10_test.so.%{sover}*

%files devel
%defattr(-,root,root)
%doc LICENSE
%{_includedir}/*.h
%{_libdir}/libNE10.so
%{_libdir}/libNE10_test.so

%changelog
