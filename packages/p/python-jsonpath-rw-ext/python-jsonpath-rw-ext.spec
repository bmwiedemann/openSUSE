#
# spec file for package python-jsonpath-rw-ext
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-jsonpath-rw-ext
Version:        1.2.2
Release:        0
Summary:        Extensions for JSONPath RW
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/sileht/python-jsonpath-rw-ext
Source:         https://files.pythonhosted.org/packages/source/j/jsonpath-rw-ext/jsonpath-rw-ext-%{version}.tar.gz
BuildRequires:  %{python_module jsonpath-rw >= 1.2.0}
BuildRequires:  %{python_module oslotest >= 1.10.0}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testscenarios >= 0.4}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jsonpath-rw >= 1.2.0
Requires:       python-pbr >= 1.4
BuildArch:      noarch
%python_subpackages

%description
Extensions for JSONPath RW

This extensions will be proposed `upstream <https://github.com/kennknowles/python-jsonpath-rw>`__
and will stay here only if they are refused.

%prep
%setup -q -n jsonpath-rw-ext-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m unittest discover -v

%files %{python_files}
%license LICENSE
%doc ChangeLog AUTHORS README.rst
%{python_sitelib}/*

%changelog
