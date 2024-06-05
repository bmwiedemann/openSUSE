#
# spec file for package python-nocaselist
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
Name:           python-nocaselist
Version:        2.0.2
Release:        0
Summary:        A case-insensitive list for Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/pywbem/nocaselist
Source:         https://files.pythonhosted.org/packages/source/n/nocaselist/nocaselist-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module typing-extensions}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-typing-extensions
BuildArch:      noarch
%python_subpackages

%description
Class `NocaseList`_ is a case-insensitive list that preserves the lexical case
of its items.

%prep
%setup -q -n nocaselist-%{version}

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
%{python_sitelib}/nocaselist
%{python_sitelib}/nocaselist-%{version}.dist-info

%changelog
