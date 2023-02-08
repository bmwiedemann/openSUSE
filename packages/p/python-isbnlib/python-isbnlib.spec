#
# spec file for package python-isbnlib
#
# Copyright (c) 2023 SUSE LLC
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


%define modname isbnlib
Name:           python-isbnlib
Version:        3.10.12
Release:        0
Summary:        Extract, clean, transform, hyphenate and metadata for ISBNs
License:        LGPL-3.0-only
URL:            https://github.com/xlcnd/isbnlib
Source:         https://github.com/xlcnd/%{modname}/archive/refs/tags/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM mark-network-tests.patch gh#xlcnd/isbnlib#121 mcepl@suse.com
# mark tests requiring network access so they may be skipped
Patch0:         mark-network-tests.patch
BuildRequires:  %{python_module anyio}
BuildRequires:  %{python_module flaky}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest-forked}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Extract, clean, transform, hyphenate and metadata for ISBNs
(International Standard Book Number).

%prep
%autosetup -p1 -n isbnlib-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTEST_ADDOPTS="--ignore=isbnlib/test/test_classify.py"
%pytest -k 'not network'

%files %{python_files}
%doc README.rst
%license LICENSE-LGPL-3.0.txt
%{python_sitelib}/isbnlib
%{python_sitelib}/isbnlib-%{version}*-info

%changelog
