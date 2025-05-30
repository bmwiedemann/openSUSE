#
# spec file for package python-hyperlink
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
Name:           python-hyperlink
Version:        21.0.0
Release:        0
Summary:        Immutable URL support for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/python-hyper/hyperlink
Source:         https://files.pythonhosted.org/packages/source/h/hyperlink/hyperlink-%{version}.tar.gz
BuildRequires:  %{python_module idna >= 2.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-idna >= 2.5
BuildArch:      noarch
%python_subpackages

%description
Hyperlink provides a pure-Python implementation of immutable URLs
based on RFC 3986 and 3987.

%prep
%setup -q -n hyperlink-%{version}

%build

%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGELOG.md README.md docs/*.rst
%{python_sitelib}/hyperlink
%{python_sitelib}/hyperlink-%{version}*-info

%changelog
