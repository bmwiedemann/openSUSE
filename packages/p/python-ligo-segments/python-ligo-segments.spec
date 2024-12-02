#
# spec file for package python-ligo-segments
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


# Disable tests for 32-bit archs as lal is not supported there
%ifarch %ix86
%bcond_with tests
%else
# Disable tests for all other archs since they are broken for Python 3.13 anyway
# https://git.ligo.org/lscsoft/ligo-segments/-/issues/22
%bcond_with tests
%endif

%define skip_python2 1
Name:           python-ligo-segments
Version:        1.4.0
Release:        0
Summary:        Representations of semi-open intervals
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://git.ligo.org/lscsoft/ligo-segments
Source:         https://files.pythonhosted.org/packages/source/l/ligo-segments/ligo-segments-%{version}.tar.gz
# PATCH-FIX-UPSTREAM ligo-segments-python312-compat.patch badshah400@gmail.com -- Initialize PyTypeObjects with PyVarObject_HEAD_INIT for python 3.12 compatibility; upstream commit
Patch0:         ligo-segments-python312-compat.patch
# PATCH-FIX-UPSTREAM python-3.13-compat.patch badshah400@gmail.com -- Compatibility for python 3.13
Patch1:         python-3.13-compat.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION For tests
%if %{with tests}
BuildRequires:  %{python_module lal}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
%endif
# /SECTION
Requires:       python-six

%python_subpackages

%description
ligo-segments defines the segment, segmentlist, and segmentlistdict objects for
manipulating semi-open intervals.

%prep
%autosetup -p1 -n ligo-segments-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%if %{with tests}
%check
%{python_expand export PYTHON=$python
export PYTHONDONTWRITEBYTECODE=1
export PYTHONPATH=%{buildroot}%{$python_sitearch}
cp -r test test-%{$python_bin_suffix}
pushd test-%{$python_bin_suffix}
%make_build check
popd
}
%endif

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/ligo/
%{python_sitearch}/ligo_segments-%{version}*.*-info
%if 0%{?suse_version} >= 1550
%{python_sitearch}/ligo_segments-%{version}-py%{python_version}-nspkg.pth
%endif

%changelog
