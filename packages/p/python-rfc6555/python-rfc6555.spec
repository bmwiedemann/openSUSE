#
# spec file for package python-rfc6555
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
%bcond_without python2
Name:           python-rfc6555
Version:        0.1.0
Release:        0
Summary:        Python implementation of the Happy Eyeballs Algorithm described in RFC 6555
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/sethmlarson/rfc6555
Source:         https://github.com/sethmlarson/rfc6555/archive/refs/tags/v%{version}.tar.gz#/rfc6555-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with python2}
BuildRequires:  python-mock
BuildRequires:  python-selectors2
%endif
%ifpython2
Requires:       python-selectors2
%endif
%python_subpackages

%description
This module provided with a single file and dead-simple API for RFC 6555
"Happy Eyeballs: Success with Dual-Stack Hosts"
<https://tools.ietf.org/html/rfc6555> to allow easy vendoring and
integration into other projects.

%prep
%setup -q -n rfc6555-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_create_connection_has_proper_timeout - online tests
%pytest -k 'not test_create_connection_has_proper_timeout'

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
