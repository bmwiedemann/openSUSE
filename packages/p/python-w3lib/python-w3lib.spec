#
# spec file for package python-w3lib
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
Name:           python-w3lib
Version:        2.2.1
Release:        0
Summary:        Library of Web-Related Functions
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/scrapy/w3lib
Source:         https://files.pythonhosted.org/packages/source/w/w3lib/w3lib-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This is a Python library of web-related functions, such as:

* remove comments, or tags from HTML snippets

* extract base url from HTML snippets

* translate entites on HTML strings

* encoding mulitpart/form-data

* convert raw HTTP headers to dicts and vice-versa

* construct HTTP auth header

* converting HTML pages to unicode

* RFC-compliant url joining

* sanitize urls (like browsers do)

* extract arguments from urls

%prep
%autosetup -p1 -n w3lib-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/w3lib
%{python_sitelib}/w3lib-%{version}.dist-info

%changelog
