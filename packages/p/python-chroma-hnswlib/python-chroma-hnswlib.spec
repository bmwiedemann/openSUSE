#
# spec file for package python-chroma-hnswlib
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


%{?sle15_python_module_pythons}
Name:           python-chroma-hnswlib
Version:        0.7.6
Release:        0
Summary:        Chromas fork of hnswlib
License:        Apache-2.0
URL:            https://github.com/chroma-core/hnswlib
Source:         https://github.com/chroma-core/hnswlib/archive/refs/tags/%{version}.tar.gz#/chroma_hnswlib-%{version}.tar.gz
Group:          Development/Languages/Python
BuildRequires:  %{python_module numpy >= 1.10.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pybind11-devel >= 2.10.0}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module wheel}
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-numpy >= 1.10.0
%python_subpackages

%description
Chroma-Hnswlib - fast approximate nearest neighbor search

%prep
%autosetup -p1 -n hnswlib-%{version}

%build
export HNSWLIB_NO_NATIVE=1
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_expand rm -f %{buildroot}%{$python_sitearch}/chroma_hnswlib-0.7.5.dist-info/REQUESTED

%check
%python_expand export PYTHONPATH=$PYTHONPATH:%{buildroot}%{$python_sitelib}:%{buildroot}%{$python_sitearch}
# class method
donttest="test_space_main"
%pytest -v tests/python/bindings_test*.py -k "not ($donttest)"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/hnswlib.*.so
%{python_sitearch}/chroma_hnswlib-%{version}.dist-info

%changelog
