#
# spec file for package python-rfc3987
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


%{?sle15_python_module_pythons}
Name:           python-rfc3987
Version:        1.3.8
Release:        0
Summary:        Module for parsing and validation of URIs (RFC 3986) and IRIs (RFC 3987)
License:        GPL-3.0-or-later
URL:            https://codeberg.org/atufi/rfc3987
Source:         https://files.pythonhosted.org/packages/source/r/rfc3987/rfc3987-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This module provides regular expressions according to `RFC 3986 "Uniform
Resource Identifier (URI): Generic Syntax"
<http://tools.ietf.org/html/rfc3986>`_ and `RFC 3987 "Internationalized
Resource Identifiers (IRIs)" <http://tools.ietf.org/html/rfc3987>`_, and
utilities for composition and relative resolution of references.

%prep
%setup -q -n rfc3987-%{version}
sed -i '1{/^#!/d}' rfc3987.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest --doctest-modules

%files %{python_files}
%license COPYING.txt
%doc README.txt
%{python_sitelib}/rfc3987.py
%pycache_only %{python_sitelib}/__pycache__/rfc3987.*.pyc
%{python_sitelib}/rfc3987-%{version}.dist-info

%changelog
