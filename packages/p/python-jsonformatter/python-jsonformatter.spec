#
# spec file for package python-jsonformatter
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
Name:           python-jsonformatter
Version:        0.3.4
Release:        0
Summary:        Python log in json format
License:        BSD-2-Clause
URL:            https://github.com/MyColorfulDays/jsonformatter.git
Source:         https://files.pythonhosted.org/packages/source/j/jsonformatter/jsonformatter-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A formatter for python logging that outputs json log

%prep
%autosetup -p1 -n jsonformatter-%{version}
find . -type f -exec chmod -x {} \;
dos2unix README.md
sed -i '1{\,^#!%{_bindir}/env python,d}' src/jsonformatter/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_file_config' tests

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/jsonformatter
%{python_sitelib}/jsonformatter-%{version}.dist-info

%changelog
