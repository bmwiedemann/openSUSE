#
# spec file for package python-multipledispatch
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-multipledispatch
Version:        1.0.0
Release:        0
Summary:        Multiple dispatch in Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://multiple-dispatch.readthedocs.io/
Source:         https://github.com/mrocklin/multipledispatch/archive/%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A relatively sane approach to multiple dispatch in Python.

This implementation of multiple dispatch is mostly complete,
performs static analysis to avoid conflicts, and provides optional namespace
support.

%prep
%autosetup -n multipledispatch-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/multipledispatch*

%changelog
