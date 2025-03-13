#
# spec file for package python-py-deviceid
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

%{?sle15_python_module_pythons}
Name:           python-py-deviceid
Version:        0.1.1
Release:        0
Summary:        A simple library to get or create a unique device id for a device in Python
License:        MIT
URL:            https://github.com/microsoft/py-deviceid
Source:         https://files.pythonhosted.org/packages/source/p/py-deviceid/py_deviceid-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
A simple library to get or create a unique device id for a device in Python.

%prep
%autosetup -p1 -n py_deviceid-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%{python_sitelib}/deviceid
%{python_sitelib}/py_deviceid-%{version}.dist-info

%changelog
