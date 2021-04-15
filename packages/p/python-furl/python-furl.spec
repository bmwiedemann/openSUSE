#
# spec file for package python-furl
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-furl
Version:        2.1.0
Release:        0
Summary:        A Python URL manipulation library
License:        Unlicense
Group:          Development/Languages/Python
URL:            https://github.com/gruns/furl
Source:         https://files.pythonhosted.org/packages/source/f/furl/furl-%{version}.tar.gz
# PATCH-FIX-UPSTREAM tests_overcome_bpo42967.patch gh#gruns/furl#135 mcepl@suse.com
# With fix for bpo#42967, it is not possible to separate
# parameters of URL query with semicolon
Patch0:         tests_overcome_bpo42967.patch
# PATCH-FIX-UPSTREAM furl-py39-join.patch -- gh#gruns/furl#139
Patch1:         furl-py39-join.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-orderedmultidict >= 1.0
Requires:       python-six >= 1.8.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module orderedmultidict >= 1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six >= 1.8.0}
# /SECTION
%python_subpackages

%description
furl is a Python library for parsing and manipulating URLs.

%prep
%autosetup -p1 -n furl-%{version}

chmod -x *.md

%build
%python_build

%install
%python_install
%{python_expand #
chmod -x %{buildroot}%{$python_sitelib}/furl-%{version}*-info/*
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/furl
%{python_sitelib}/furl-%{version}*-info

%changelog
