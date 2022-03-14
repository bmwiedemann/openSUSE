#
# spec file for package python-sphinxcontrib-httpdomain
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-sphinxcontrib-httpdomain
Version:        1.8.0
Release:        0
Summary:        Sphinx domain for HTTP APIs
License:        BSD-2-Clause
URL:            https://github.com/sphinx-contrib/httpdomain
Source:         https://github.com/sphinx-contrib/httpdomain/archive/%{version}.tar.gz
BuildRequires:  %{python_module Flask >= 0.11}
BuildRequires:  %{python_module Sphinx >= 1.5}
BuildRequires:  %{python_module bottle >= 0.11.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx >= 1.5
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
This contrib extension, sphinxcontrib.httpdomain provides a Sphinx
domain for describing RESTful HTTP APIs.

You can find the documentation from the following URL:

https://sphinxcontrib-httpdomain.readthedocs.io/en/stable/

%prep
%autosetup -p1 -n httpdomain-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/sphinxcontrib/autohttp/
%{python_sitelib}/sphinxcontrib/httpdomain.py*
%pycache_only %{python_sitelib}/sphinxcontrib/__pycache__
%{python_sitelib}/sphinxcontrib_httpdomain-%{version}-py*-nspkg.pth
%{python_sitelib}/sphinxcontrib_httpdomain-%{version}-py*.egg-info

%changelog
