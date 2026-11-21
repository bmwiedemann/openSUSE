#
# spec file for package python-array-api-strict
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


Name:           python-array-api-strict
Version:        2.6.1
Release:        0
Summary:        A strict, minimal implementation of the Python array API standard
License:        BSD-3-Clause
URL:            https://data-apis.org/array-api-strict/
Source:         https://files.pythonhosted.org/packages/source/a/array-api-strict/array_api_strict-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-numpy
BuildArch:      noarch
%python_subpackages

%description
A strict, minimal implementation of the Python array API standard.

%prep
%autosetup -p1 -n array_api_strict-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Failures on 32 bit
if [ "$(getconf LONG_BIT)" = "32" ]; then
    donttest="test_sum_prod_trace_2022_12 or test_sum_prod_trace_2023_12"
fi
%pytest ${donttest:+-k "not ($donttest)"}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/array_api_strict
%{python_sitelib}/array_api_strict-%{version}.dist-info

%changelog
