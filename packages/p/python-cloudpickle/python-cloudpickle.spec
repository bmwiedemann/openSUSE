#
# spec file for package python-cloudpickle
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
Name:           python-cloudpickle
Version:        3.0.0
Release:        0
Summary:        Extended pickling support for Python objects
License:        BSD-3-Clause
URL:            https://github.com/cloudpipe/cloudpickle
Source:         https://github.com/cloudpipe/cloudpickle/archive/refs/tags/v{%version}.tar.gz#/cloudpickle-%{version}-gh.tar.gz
# PATCH-FIX-UPSTREAM gh/cloudpipe/cloudpickle#534 - Fix test_extract_class_dict for Python 3.13 beta 1
Patch:          Fix-test_extract_class_dict-for-Python-313.patch
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements. None of these are hard dependencies
BuildRequires:  %{python_module curses}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module py}
BuildRequires:  %{python_module setuptools if %python-base >= 3.12}
BuildRequires:  %{python_module tornado}
%if 0%{?suse_version} > 1600
BuildRequires:  %{python_module numpy >= 1.18.5}
BuildRequires:  %{python_module scipy}
%endif
# /SECTION
%python_subpackages

%description
The cloudpickle package makes it possible to serialize Python constructs
not supported by the default pickle module from the Python standard
library.

cloudpickle is especially useful for cluster computing where Python
expressions are shipped over the network to execute on remote hosts,
possibly close to the data.

Among other things, cloudpickle supports pickling for lambda expressions,
functions and classes defined interactively in the __main__ module.

%prep
%autosetup -p1 -n cloudpickle-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# make local source and testpkg importable
export PYTHONPATH=':./tests/cloudpickle_testpkg'
# -s: tests need direct print
%pytest -s

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/cloudpickle
%{python_sitelib}/cloudpickle-%{version}.dist-info

%changelog
