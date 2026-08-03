#
# spec file for package python-parsel
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        1.11.0
Release:        0
Summary:        Library to extract data from HTML and XML using XPath and CSS selectors
License:        BSD-3-Clause
URL:            https://github.com/scrapy/parsel
Source:         https://files.pythonhosted.org/packages/source/p/parsel/parsel-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module hatchling >= 1.27}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cssselect >= 1.2.0
Requires:       python-jmespath >= 1.0.0
Requires:       python-lxml >= 5.1
Requires:       python-packaging >= 23
Requires:       python-w3lib >= 1.19.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module cssselect >= 1.2.0}
BuildRequires:  %{python_module jmespath >= 1.0.0}
BuildRequires:  %{python_module lxml >= 5.1}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module sybil}
BuildRequires:  %{python_module w3lib >= 1.19.0}
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
%python_exec -Bm pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/parsel
%{python_sitelib}/parsel-%{version}.dist-info

%changelog
