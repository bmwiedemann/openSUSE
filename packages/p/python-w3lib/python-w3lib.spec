#
# spec file for package python-w3lib
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-w3lib
Version:        1.22.0
Release:        0
Summary:        Library of Web-Related Functions
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/scrapy/w3lib
Source:         https://files.pythonhosted.org/packages/source/w/w3lib/w3lib-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 166-add-xfail-test_add_or_replace_parameter_fail.patch mcepl@suse.com
# Allow working with Python fixed CVE-2021-23336
Patch0:         166-add-xfail-test_add_or_replace_parameter_fail.patch
# https://github.com/scrapy/w3lib/commit/c16d7bac3af3148b7018c67ef7922a5da6b3e640
Patch1:         python-w3lib-no-six.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
