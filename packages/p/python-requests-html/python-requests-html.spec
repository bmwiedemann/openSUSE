#
# spec file for package python-requests-html
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-requests-html
Version:        0.10.0
Release:        0
License:        MIT
Summary:        HTML Parsing package for requests
Url:            https://github.com/kennethreitz/requests-html
Group:          Development/Languages/Python
Source:         https://github.com/kennethreitz/requests-html/archive/v%{version}.tar.gz#/requests-html-%{version}.tar.gz
# PATCH-FIX-UPSTREAM expand_bs4_dependency.patch gh#kennethreitz/requests-html#296
Patch0:         expand_bs4_dependency.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module fake-useragent}
BuildRequires:  %{python_module parse}
BuildRequires:  %{python_module psutil}
BuildRequires:  %{python_module pyppeteer >= 0.0.14}
BuildRequires:  %{python_module pyquery}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module requests-file}
BuildRequires:  %{python_module w3lib}
# /SECTION
BuildRequires:  fdupes
Requires:       python-beautifulsoup4
Requires:       python-fake-useragent
Requires:       python-parse
Requires:       python-pyppeteer >= 0.0.14
Requires:       python-pyquery
Requires:       python-requests
Requires:       python-w3lib
BuildArch:      noarch

%python_subpackages

%description
HTML parsing built on top of requests.

 * Full JavaScript support
 * CSS Selectors
 * XPath Selectors
 * Mocked user-agent
 * Automatic following of redirects.
 * Connection–pooling and cookie persistence.
 * Async Support

%prep
%setup -q -n requests-html-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests require a network connection
# %%check
# %%{python_expand export PYTHONPATH=%%{buildroot}%%{$python_sitelib}
# pytest-%%{$python_bin_suffix} -v -m ok
# %}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
