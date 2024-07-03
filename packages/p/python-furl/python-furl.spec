#
# spec file for package python-furl
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
%define skip_python2 1
Name:           python-furl
Version:        2.1.3
Release:        0
Summary:        A Python URL manipulation library
License:        Unlicense
Group:          Development/Languages/Python
URL:            https://github.com/gruns/furl
Source:         https://files.pythonhosted.org/packages/source/f/furl/furl-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 165-use-ipaddress-library.patch gh#gruns/furl#164 mcepl@suse.com
# use ipaddress to parse IP addresses
Patch0:         165-use-ipaddress-library.patch
Patch1:         netloc-tests.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-orderedmultidict >= 1.0.1
Requires:       python-six >= 1.8.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module orderedmultidict >= 1.0.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six >= 1.8.0}
# /SECTION
%python_subpackages

%description
furl is a Python library for parsing and manipulating URLs.

%prep
%autosetup -p1 -n furl-%{version}
chmod -x *.md furl.egg-info/*

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.md
%{python_sitelib}/furl
%{python_sitelib}/furl-%{version}*-info

%changelog
