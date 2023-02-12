#
# spec file for package python-cached-property
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-cached-property
Version:        1.5.2
Release:        0
Summary:        A decorator for caching properties in classes
License:        BSD-3-Clause
Group:          Development/Libraries/Python
URL:            https://github.com/pydanny/cached-property
Source:         https://files.pythonhosted.org/packages/source/c/cached-property/cached-property-%{version}.tar.gz
# PATCH-FIX-UPSTREAM skip test that rely on wrong freezegun behaviour
# https://github.com/pydanny/cached-property/pull/125
Patch0:         freezegun-skip.patch
# PATCH-FIX-UPSTREAM Don't use asyncio.coroutine if it's not available -- https://github.com/pydanny/cached-property/pull/267
Patch1:         python311.patch
BuildRequires:  %{python_module freezegun}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A decorator for caching properties in classes. It makes caching of time or
computational expensive properties quick and easy and it works in Python 2
and 3.

%prep
%autosetup -p1 -n cached-property-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc AUTHORS.rst README.rst HISTORY.rst
%{python_sitelib}/*

%changelog
