#
# spec file for package python-w3lib
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-w3lib
Version:        1.20.0
Release:        0
Summary:        Library of Web-Related Functions
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            http://github.com/scrapy/w3lib
Source:         https://files.pythonhosted.org/packages/source/w/w3lib/w3lib-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six} >= 1.4.1
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
%setup -q -n w3lib-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
