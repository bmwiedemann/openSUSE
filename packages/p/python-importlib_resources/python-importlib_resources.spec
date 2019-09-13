#
# spec file for package python-importlib_resources
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%if %{python3_version_nodots} >= 37
%define skip_python3 1
%endif
Name:           python-importlib_resources
Version:        1.0.2
Release:        0
Summary:        Python package resource reader
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://gitlab.com/python-devs/importlib_resources
Source:         https://files.pythonhosted.org/packages/source/i/importlib_resources/importlib_resources-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python2-pathlib2
BuildArch:      noarch
Requires:       python-typing
%ifpython2
Requires:       python-pathlib2
%endif
%python_subpackages

%description
importlib_resources is a backport of Python 3.7's standard library
importlib.resources module for Python 2.7, and 3.4 through 3.6.

%prep
%setup -q -n importlib_resources-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest discover

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
