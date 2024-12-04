#
# spec file for package python-getkey
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
Name:           python-getkey
Version:        0.6.5
Release:        0
Summary:        Read single characters and key-strokes
License:        MIT
URL:            https://github.com/kcsaff/getkey
Source:         https://files.pythonhosted.org/packages/source/g/getkey/getkey-%{version}.tar.gz
# PATCH-FIX-OPENSUSE remove coverage report from tests
Patch0:         remove-coverage.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# test dependencies
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Read single characters and key-strokes

%prep
%autosetup -p1 -n getkey-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%{python_sitelib}/getkey
%{python_sitelib}/getkey-%{version}.dist-info

%changelog
