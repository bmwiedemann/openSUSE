#
# spec file for package python-tinyarray
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


Name:           python-tinyarray
Version:        1.2.3
Release:        0
Summary:        Arrays of numbers for Python, optimized for small sizes
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://gitlab.kwant-project.org/kwant/tinyarray
Source:         https://files.pythonhosted.org/packages/source/t/tinyarray/tinyarray-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  python-rpm-macros
Requires:       python-numpy
# SECTION FOR TESTS
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Tinyarrays are similar to NumPy arrays, but optimized for small sizes.
Tinyarrays support mathematical operations like element-wise addition
and matrix multiplication. Tinyarrays can be used as dictionary keys
because they are hashable and immutable. Tinyarrays are useful if you
need many small arrays of numbers, and cannot combine them into a few
large ones. Common operations on very small arrays are faster than
with NumPy, and less memory is used to store them.

%prep
%setup -q -n tinyarray-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Disable conversion test on non x86 systems; see https://gitlab.kwant-project.org/kwant/tinyarray/-/issues/19
%ifarch %ix86 x86_64
%pytest_arch
%else
%pytest_arch -k 'not test_conversion'
%endif

%files %{python_files}
%doc README.rst
%license LICENSE.rst
%{python_sitearch}/*

%changelog
