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
Version:        0.3.2
Release:        0
Summary:        Python log in json format
License:        BSD-2-Clause
URL:            https://github.com/MyColorfulDays/jsonformatter.git
Source:         https://files.pythonhosted.org/packages/source/j/jsonformatter/jsonformatter-%{version}.tar.gz
Patch0:         remove-failing-test.py
BuildRequires:  dos2unix
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
A formatter for python logging that outputs json log

%prep
%autosetup -p1 -n jsonformatter-%{version}
find . -type f -exec chmod -x {} \;
dos2unix jsonformatter/__init__.py
sed -i '1{\,^#!%{_bindir}/env python,d}' jsonformatter/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand  #
export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python test/test.py
}

%files %{python_files}
%doc README.md
%{python_sitelib}/jsonformatter
%{python_sitelib}/jsonformatter-%{version}.dist-info

%changelog
