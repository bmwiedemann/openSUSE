#
# spec file for package libpathrs
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


%define somajor 0
%define libname %{name}%{somajor}
%define devname %{name}-devel
%define pyname  pathrs

Name:           libpathrs
Version:        0.2.2
Release:        0
Summary:        Safe path resolution library for Linux
Group:          Productivity/Security
License:        MPL-2.0 OR LGPL-3.0-or-later
URL:            https://github.com/cyphar/%{name}
Source0:        https://github.com/cyphar/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
Patch1:         https://github.com/cyphar/libpathrs/commit/3b5c7817bdc54adb47fb9e10e0e02176c7fa41b8.patch#/0001-fd-fix-f_flags-fdinfo-test-on-other-architectures.patch
BuildRequires:  rust >= 1.63
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  zstd
BuildRequires:  fdupes
# We need to use lld in order to avoid issues with our version scripts.
BuildRequires:  lld
BuildRequires:  clang
ExclusiveArch:  %{rust_arches}

%description
libpathrs implements a set of C-friendly APIs (written in Rust) to make path
resolution within a potentially-untrusted directory safe on GNU/Linux. There
are countless examples of security vulnerabilities caused by bad handling of
paths (symlinks make the issue significantly worse).

%package -n %{libname}
Summary:        Shared library for %{name}
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}

%description -n %{libname}
libpathrs implements a set of C-friendly APIs (written in Rust) to make path
resolution within a potentially-untrusted directory safe on GNU/Linux. There
are countless examples of security vulnerabilities caused by bad handling of
paths (symlinks make the issue significantly worse).

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}-%{release}
Requires:       glibc-devel

%description devel
libpathrs implements a set of C-friendly APIs (written in Rust) to make path
resolution within a potentially-untrusted directory safe on GNU/Linux. There
are countless examples of security vulnerabilities caused by bad handling of
paths (symlinks make the issue significantly worse).

This subpackage provides the development headers for %{name}.

%package devel-static
Summary:        Static library for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-devel:%{_libdir}/%{name}.a

%description devel-static
libpathrs implements a set of C-friendly APIs (written in Rust) to make path
resolution within a potentially-untrusted directory safe on GNU/Linux. There
are countless examples of security vulnerabilities caused by bad handling of
paths (symlinks make the issue significantly worse).

This subpackage contains the static version of %{name} used for development.

%package -n python-%{pyname}
Summary:        Python3 bindings for %{name}
Group:          Development/Libraries/Python
URL:            https://pypi.org/p/pathrs
BuildRequires:  %{python_module cffi >= 1.10.0}
BuildRequires:  %{python_module setuptools >= 44}
BuildRequires:  %{python_module toml if %python-base < 3.11}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module devel}
BuildRequires:  python-rpm-macros
Requires:       %{libname} = %{version}-%{release}
%define python_subpackage_only 1
%{?python_enable_dependency_generator}
%python_subpackages

%description -n python-%{pyname}
libpathrs implements a set of C-friendly APIs (written in Rust) to make path
resolution within a potentially-untrusted directory safe on GNU/Linux. There
are countless examples of security vulnerabilities caused by bad handling of
paths (symlinks make the issue significantly worse).

This subpackage provides the Python bindings for %{name}.

%prep
%autosetup -a1 -p1

%build
# We need to use lld.
%define __rustflags -C linker=clang -C link-arg=-fuse-ld=lld

# Build libpathrs.so.
make CARGO='%{__cargo}' release

# Used for building bindings against our not-yet-installed libs.
export PATHRS_SRC_ROOT="$PWD"

# Build python3-pathrs.
pushd contrib/bindings/python
%{pyproject_wheel}
popd

%install
# Install libpathrs.so.
./install.sh \
	DESTDIR=%{buildroot} \
	--prefix=%{_prefix} \
	--exec-prefix=%{_exec_prefix} \
	--includedir=%{_includedir} \
	--libdir=%{_libdir}

# Install python3-pathrs.
pushd contrib/bindings/python
%{pyproject_install}
popd

%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# We do not do --all-features because we _test_as_root won't work in OBS. Note
# that these tests *do not* use the shared library we installed, they are pure
# Rust-only tests!
%{cargo_test} --features capi

# TODO: Run tests that actually use the cdylib (at least the Python ones...).

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license COPYING.md LICENSE.*
%doc README.md CHANGELOG.md
%{_libdir}/libpathrs.so.*

%files %{python_files %{pyname}}
%{python_sitearch}/%{pyname}
%{python_sitearch}/%{pyname}-%{version}.dist-info

%files devel
%{_includedir}/pathrs.h
%{_libdir}/libpathrs.so
%{_libdir}/pkgconfig/pathrs.pc

%files devel-static
%{_libdir}/libpathrs.a

%changelog
