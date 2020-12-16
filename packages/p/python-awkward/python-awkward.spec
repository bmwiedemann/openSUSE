#
# spec file for package python-awkward
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global modname awkward
Name:           python-awkward
Version:        1.0.1
Release:        0
Summary:        Manipulate arrays of complex data structures as easily as Numpy
License:        BSD-3-Clause
URL:            https://github.com/scikit-hep/awkward-1.0
Source:         https://files.pythonhosted.org/packages/source/a/awkward/awkward-%{version}.tar.gz
# PATCH-FETAURE-OPENSUSE awkward-cmake-build-with-RelWithDebInfo.patch badshah400@gmail.com -- Set CMAKE_BUILD_TYPE to RelWithDebInfo by default instead of Release
Patch0:         awkward-cmake-build-with-RelWithDebInfo.patch
# PATCH-FEATURE-OPENSUSE awkward-correct-includedir.patch badshah400#gmail.com -- Make awkward.config return the correct includedir where we move the header files to
Patch1:         awkward-correct-includedir.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 1.13.1
Recommends:     python-numba
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module numpy >= 1.13.1}
BuildRequires:  %{python_module pandas}
BuildRequires:  %{python_module pytest}
%if 0%{?suse_version} >= 1550
BuildRequires:  %{python_module numba >= 0.50}
%endif
# /SECTION
%python_subpackages

%description
Awkward Array is a library for nested, variable-sized data, including
arbitrary-length lists, records, mixed types, and missing data, using
NumPy-like idioms.

Arrays are dynamically typed, but operations on them are compiled and fast.
Their behavior coincides with NumPy when array dimensions are regular and
generalizes when they're not.

%package -n awkward-devel
Summary:        Header files for using awkaward in C/C++ code
Requires:       python3-awkward = %{version}

%description -n awkward-devel
Awkward Array is a library for nested, variable-sized data, including
arbitrary-length lists, records, mixed types, and missing data, using
NumPy-like idioms.

This package provides the header files needed to compile C/C++ codes with
awkward.

%prep
%autosetup -p1 -n awkward-%{version}

%build
%python_build

%install
%python_install

# Remove static libs
%python_expand find %{buildroot}%{$python_sitearch}/%{modname}/ -name "*.a" -delete -print

mkdir -p %{buildroot}%{_includedir}/awkward
%{python_expand # Move headers to standard include dir for one python version and delete for the other
if [ $python_ = python3_ ]; then
mv %{buildroot}%{$python_sitearch}/%{modname}/include/* %{buildroot}%{_includedir}/awkward/
# Create a symlink to shared library in _libdir for the C/C++ devel pkg
ln -s %{$python_sitearch}/awkward/libawkward.so %{buildroot}%{_libdir}/
ln -s %{$python_sitearch}/awkward/libawkward-cpu-kernels.so %{buildroot}%{_libdir}/
else
rm -fr %{buildroot}%{$python_sitearch}/%{modname}/include
fi
}

%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Disable tests failing on 32-bit due to use of 64 data types
# https://github.com/scikit-hep/awkward-1.0/issues/600
%ifarch %ix86
%pytest_arch -k "not (test_0056-partitioned-array.py or test_0080-flatpandas-multiindex-rows-and-columns.py or test_0166-0167-0170-random-issues.py or test_0331-pandas-indexedarray.py)"
%else
%pytest_arch
%endif

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/%{modname}/
%{python_sitearch}/%{modname}-%{version}-py%{python_version}.egg-info/

%files -n awkward-devel
%license LICENSE
%{_includedir}/awkward/
%{_libdir}/*.so

%changelog
