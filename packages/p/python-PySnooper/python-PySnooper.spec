#
# spec file for package python-PySnooper
#
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/

%define modname pysnooper
Name:           python-PySnooper
Version:        1.2.3
Release:        0
Summary:        A poor man's debugger for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/cool-RR/PySnooper
Source:         https://files.pythonhosted.org/packages/source/p/%{modname}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-base
BuildArch:      noarch
%python_subpackages

%description
A poor man's debugger for Python.

%prep
%setup -q -n %{modname}-%{version}
sed -i -e 's/\r//' README.md

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/%{modname}
%{python_sitelib}/%{modname}-%{version}*-info

%changelog
