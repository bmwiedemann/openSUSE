#
# spec file for package python-python-json-logger
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
Name:           python-python-json-logger
Version:        2.0.7
Release:        0
Summary:        A python library adding a json log formatter
License:        BSD-2-Clause
URL:            https://github.com/madzak/python-json-logger
Source:         https://files.pythonhosted.org/packages/source/p/python-json-logger/python-json-logger-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#madzak/python-json-logger#183
Patch0:         support-python312.patch
# PATCH-FIX-UPSTREAM gh#madzak/python-json-logger#192
Patch1:         support-python313.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A python library adding a json log formatter.

%prep
%autosetup -p1 -n python-json-logger-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/pythonjsonlogger
%{python_sitelib}/python_json_logger-%{version}.dist-info

%changelog
