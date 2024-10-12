#
# spec file for package python-fasttext
#
# Copyright (c) 2024 SUSE LLC
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


%define modname fastText
%define sover 0
# Using annotation futures and dataclasses
%define skip_python36 1
%{?sle15_python_module_pythons}
Name:           python-fasttext
Version:        0.9.2
Release:        0
Summary:        Library for fast text representation and classification
License:        MIT
URL:            https://github.com/facebookresearch/fastText
Source:         https://github.com/facebookresearch/%{modname}/archive/refs/tags/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
Patch0:         reproducible.patch
Patch1:         gcc13-fix.patch
Patch2:         no-static-lib.patch
Patch3:         proper-lib-dir.patch
Patch4:         py-link-against-shared.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pybind11-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pybind11 >= 2.2}
BuildRequires:  %{python_module setuptools >= 0.7.0}
# /SECTION
BuildRequires:  fdupes
Requires:       fasttext
Requires:       python-numpy
Requires:       python-pybind11 >= 2.2
Requires:       python-setuptools >= 0.7.0
%python_subpackages

%description
fastText is a library for efficient learning of word
representations and sentence classification.

%package -n fasttext
Summary:        Fast text representation and classification

%description -n fasttext
fastText is a library for efficient learning of word
representations and sentence classification.

This package provides the fasttext binary.

%package -n fasttext-devel
Summary:        Development files for fasttext
Requires:       libfasttext%{sover}

%description -n fasttext-devel
fastText is a library for efficient learning of word
representations and sentence classification.

This package provides the fasttext library development files.

%package -n libfasttext%{sover}
Summary:        Library for fast text representation and classification

%description -n libfasttext%{sover}
fastText is a library for efficient learning of word
representations and sentence classification.

This package provides the fasttext library.

%prep
%autosetup -p1 -n %{modname}-%{version}

sed -Ei "1{/^#!\/usr\/bin\/env python/d}" \
    python/fasttext_module/fasttext/util/util.py

%build
pushd .
%define __builddir build-cmake
%define __builder ninja
%cmake
%cmake_build
popd

export LDFLAGS=-L%{__builddir}
%pyproject_wheel

%install
%cmake_install
%pyproject_install
%{python_expand :
%fdupes %{buildroot}%{$python_sitearch}
}

%check
# Tests require 300+MB test data

%ldconfig_scriptlets -n libfasttext%{sover}

%files %{python_files}
%license LICENSE
%{python_sitearch}/fasttext
%{python_sitearch}/fasttext-%{version}*-info
%{python_sitearch}/fasttext_pybind.*.so

%files -n fasttext
%doc README.md docs/
%license LICENSE
%{_bindir}/fasttext

%files -n fasttext-devel
%dir %{_includedir}/fasttext
%{_includedir}/fasttext/*.h
%{_libdir}/libfasttext.so
%{_libdir}/pkgconfig/fasttext.pc

%files -n libfasttext%{sover}
%{_libdir}/libfasttext.so.%{sover}

%changelog
