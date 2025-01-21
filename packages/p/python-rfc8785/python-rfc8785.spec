#
# spec file for package python-rfc8785
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


Name:           python-rfc8785
Version:        0.1.4
Release:        0
Summary:        A pure-Python implementation of RFC 8785
License:        Apache-2.0
URL:            https://github.com/trailofbits/rfc8785.py
Source:         https://github.com/trailofbits/rfc8785.py/archive/v%{version}.tar.gz#/rfc8785-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module flit-core >= 3.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-cov}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
A pure-Python, no-dependency implementation of RFC 8785, a.k.a. JSON
Canonicalization Scheme or JCS.

This implementation should be behaviorally comparable to Andrew
Rundgren's reference implementation, with the following added
constraints:

1. This implementation does not transparently convert non-`str`
   dictionary keys into strings. Users must explicitly perform this
   conversion.
2. No support for indentation, pretty-printing, etc. is provided. The
   output is always minimally encoded.
3. All APIs produce UTF-8-encoded `bytes` objects or `bytes` I/O.

%prep
%autosetup -p1 -n rfc8785.py-%{version}

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
%{python_sitelib}/rfc8785
%{python_sitelib}/rfc8785-%{version}.dist-info

%changelog
