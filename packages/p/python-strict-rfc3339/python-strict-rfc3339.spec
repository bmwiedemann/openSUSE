#
# spec file for package python-strict-rfc3339
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-strict-rfc3339
Version:        0.7
Release:        0
Summary:        RFC 3339 functions
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/danielrichman/strict-rfc3339/
Source:         https://github.com/danielrichman/strict-rfc3339/archive/version-%{version}.tar.gz#/strict-rfc3339-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  timezone
Requires:       timezone
BuildArch:      noarch
%python_subpackages

%description
RFC 3339 functions.
 - Convert unix timestamps to and from RFC3339.
 - Either produce RFC3339 strings with a UTC offset (Z) or with the offset
   that the C time module reports is the local timezone offset.
 - Avoid timezones as much as possible.
 - Be very strict and follow RFC3339.

%prep
%setup -q -n strict-rfc3339-version-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# two 32bit failures https://github.com/danielrichman/strict-rfc3339/issues/10
%pytest -k 'not test_leap_year and not test_y2038'

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/strict_rfc3339.py
%pycache_only %{python_sitelib}/__pycache__/strict_rfc3339*
%{python_sitelib}/strict[-_]rfc3339-%{version}*-info

%changelog
