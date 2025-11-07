#
# spec file for package leancrypto
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2022 - 2025 Stephan Mueller <smueller@chronox.de
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "kmp"
%define psuffix -kmp
%bcond_without kmp
%else
%define psuffix %{nil}
%bcond_with kmp
%endif

%define pkgname leancrypto
%define libname lib%{pkgname}
Name:           %{pkgname}%{psuffix}
Version:        1.6.0
Release:        0
%if %{with kmp}
Summary:        leancrypto Kernel Module Package
%else
Summary:        Cryptographic library with stack-only support and PQC-safe algorithms
%endif
License:        BSD-3-Clause OR GPL-2.0-only
URL:            https://www.leancrypto.org
Source0:        https://www.leancrypto.org/%{pkgname}/releases/%{pkgname}-%{version}/%{pkgname}-%{version}.tar.xz
Source1:        https://www.leancrypto.org/%{pkgname}/releases/%{pkgname}-%{version}/%{pkgname}-%{version}.tar.xz.asc
Source2:        https://leancrypto.org/about/smuellerDD-2024.asc#/leancrypto.keyring
Source3:        baselibs.conf
# PATCH-FIX-UPSTREAM - https://github.com/smuellerDD/leancrypto/commit/fe9751f2b
Patch1:         fe9751f2.patch
BuildRequires:  clang
BuildRequires:  meson
%if %{with kmp}
BuildRequires:  %kernel_module_package_buildreqs
%kernel_module_package -n %{pkgname}
%endif

%description
Leancrypto provides a general-purpose cryptographic library with PQC-safe
algorithms. Further it only has POSIX dependencies, and allows all algorithms
to be used on stack as well as on heap. Accelerated algorithms are transparently
enabled if possible.

%if %{without kmp}
%package -n %{libname}1
Summary:        Cryptographic library with stack-only support and PQC-safe algorithms

%description -n %{libname}1
Leancrypto provides a general-purpose cryptographic library with PQC-safe
algorithms. Further it only has POSIX dependencies, and allows all algorithms
to be used on stack as well as on heap. Accelerated algorithms are transparently
enabled if possible.

%package devel
Summary:        Development files for leancrypto, a cryptographic library
Requires:       %{libname}1 = %{version}
Requires:       glibc-devel

%description devel
Leancrypto provides a general-purpose cryptographic library with PQC-safe
algorithms. Further it only has POSIX dependencies, and allows all algorithms
to be used on stack as well as on heap. Accelerated algorithms are transparently
enabled if possible.

This subpackage holds the development headers for the library.

%package devel-static
Summary:        Static library for leancrypto
Requires:       %{name}-devel = %{version}
Provides:       %{name}-devel:%{_libdir}/%{libname}.a

%description devel-static
Leancrypto provides a general-purpose cryptographic library with PQC-safe
algorithms. Further it only has POSIX dependencies, and allows all algorithms
to be used on stack as well as on heap. Accelerated algorithms are transparently
enabled if possible.

This subpackage contains the static version of the library
used for development.

%package -n %{libname}-fips1
Summary:        Cryptographic library with stack-only support and PQC-safe algorithms

%description -n %{libname}-fips1
Leancrypto provides a general-purpose cryptographic library with PQC-safe
algorithms. Further it only has POSIX dependencies, and allows all algorithms
to be used on stack as well as on heap. Accelerated algorithms are transparently
enabled if possible.

This subpackage contains the FIPS 140 compliant version of the library.

%package -n %{name}-tools
Summary:        Applications provided by leancrypto

%description -n %{name}-tools
Leancrypto provides a general-purpose cryptographic library with PQC-safe
algorithms. Further it only has POSIX dependencies, and allows all algorithms
to be used on stack as well as on heap. Accelerated algorithms are transparently
enabled if possible.

This subpackage holds the tools provided by the library, such as sha*sum.
%else

%package KMP
Summary:        leancrypto Kernel Module Package
Group:          System/Kernel

%description KMP
Leancrypto for the Linux Kernel. The leancrypto library is intended to provide
the identical services for user space as well as Linux kernel space. This shall
allow developers to only have one crypto provider which they need to maintain
and learn to develop with.

The user space and kernel space versions of leancrypto are fully independent of
each other. Neither requires the presence of the other for full operation.
%endif

%prep
%autosetup -p1 -n %{pkgname}-%{version}

%if %{with kmp}
set -- *
mkdir source
cp -ar "$@" source/
# broken symlink
rm source/linux_kernel/kyber768/armv8/kyber_poly_armv8.c
mkdir obj
%endif

%build
%meson -Dseedsource=esdm -Dstrip=false
# Only build the lib when we need it, if building the kernel module, just build
# the kernel module.
%if %{without kmp}
%meson_build
%else
for flavor in %flavors_to_build; do
	KERNELRELEASE=`make -j${RPM_BUILD_NCPUS} -s -C /%{_prefix}/src/linux-obj/%{_target_cpu}/$flavor kernelrelease`
	rm -rf obj/$flavor
	cp -r source obj/$flavor
	make -j${RPM_BUILD_NCPUS} -C $PWD/obj/$flavor/linux_kernel KERNELRELEASE=$KERNELRELEASE
done
%endif

%check
%if %{without kmp}
%meson_test --suite regression
%endif

%install
%if %{without kmp}
%meson_install
%else
export INSTALL_MOD_PATH=$RPM_BUILD_ROOT
export INSTALL_MOD_DIR=updates
for flavor in %flavors_to_build; do
	KERNELRELEASE=`make -s -C /%{_prefix}/src/linux-obj/%{_target_cpu}/$flavor kernelrelease`
	make -C obj/$flavor/linux_kernel modules_install M=$PWD/obj/$flavor KERNELRELEASE=$KERNELRELEASE
done
%endif

%if %{without kmp}
%ldconfig_scriptlets -n %{libname}1
%ldconfig_scriptlets -n %{libname}-fips1

%files -n %{libname}1
%license LICENSE LICENSE.bsd LICENSE.gplv2
%{_libdir}/%{libname}.so.*

%files devel
%doc README.md CHANGES.md
%{_includedir}/%{name}.h
%{_includedir}/%{name}
%{_libdir}/%{libname}.so
%{_libdir}/%{libname}-fips.so
%{_libdir}/pkgconfig/%{name}-fips.pc
%{_libdir}/pkgconfig/%{name}.pc

%files devel-static
%{_libdir}/%{libname}.a
%{_libdir}/%{libname}-fips.a

%files -n %{libname}-fips1
%{_libdir}/%{libname}-fips.so.*

%files -n %{name}-tools
%{_libexecdir}/%{name}
%{_libexecdir}/%{name}/sha256sum
%{_libexecdir}/%{name}/sha384sum
%{_libexecdir}/%{name}/sha512sum
%{_libexecdir}/%{name}/sha3-256sum
%{_libexecdir}/%{name}/sha3-384sum
%{_libexecdir}/%{name}/sha3-512sum
%{_libexecdir}/%{name}/ascon256-sum
%{_bindir}/lc_pkcs7_generator
%{_bindir}/lc_x509_generator
%endif

%changelog
