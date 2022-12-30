#
# spec file for package python-rfc3986-validator
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


Name:           python-rfc3986-validator
Version:        0.1.1
Release:        0
Summary:        Pure python rfc3986 validator
License:        MIT
URL:            https://github.com/naimetti/rfc3986-validator
Source:         https://files.pythonhosted.org/packages/source/r/rfc3986_validator/rfc3986_validator-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module hypothesis >= 4.41.3}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rfc3987}
# /SECTION
Provides:       python-rfc3986_validator = %{version}-%{release}
%python_subpackages

%description
A pure python rfc3986 validator

Usage:
    >>> from rfc3986_validator import validate_rfc3986
    >>> validate_rfc3986('http://foo.bar?q=Spaces should be encoded')
    False
    
    >>> validate_rfc3986('http://foo.com/blah_blah_(wikipedia)')
    True

%prep
%setup -q -n rfc3986_validator-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/rfc3986_validator.py*
%pycache_only %{python_sitelib}/__pycache__/rfc3986_validator.*.pyc
%{python_sitelib}/rfc3986_validator-%{version}.dist-info

%changelog
