#
# spec file for package python-grab
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-grab
Version:        0.6.41
Release:        0
Summary:        A mock implementation of python-ldap
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/lorien/grab
Source:         https://pypi.io/packages/source/g/grab/grab-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/lorien/grab/master/LICENSE
BuildRequires:  %{python_module defusedxml}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pycurl}
BuildRequires:  %{python_module selection}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module user_agent}
BuildRequires:  %{python_module weblib >= 0.1.23}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-defusedxml
Requires:       python-lxml
Requires:       python-pycurl
Requires:       python-selection
Requires:       python-six
Requires:       python-user_agent
Requires:       python-weblib
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%python_subpackages

%description
Grab is a Python web scraping framework. Grab provides a number of
methods to perform network requests, scrape web sites and process the scraped
content.

%prep
%setup -q -n grab-%{version}
cp %{SOURCE99} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/grab

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
