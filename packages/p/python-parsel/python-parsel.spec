#
# spec file for package python-parsel
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
Name:           python-parsel
Version:        1.9.1
Release:        0
Summary:        Library to extract data from HTML and XML using XPath and CSS selectors
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/scrapy/parsel
Source:         https://files.pythonhosted.org/packages/source/p/parsel/parsel-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module cssselect >= 1.2.0}
BuildRequires:  %{python_module jmespath}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing-extensions}
BuildRequires:  %{python_module w3lib >= 1.19.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cssselect >= 1.2.0
Requires:       python-jmespath
Requires:       python-lxml
Requires:       python-typing-extensions
Requires:       python-w3lib >= 1.19.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Parsel is a library to extract data from HTML and XML using XPath and CSS
selectors.

%prep
%autosetup -p1 -n parsel-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/parsel
%{python_sitelib}/parsel-%{version}.dist-info

%changelog
