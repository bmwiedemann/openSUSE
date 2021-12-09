#
# spec file for package python-yarl
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
%define skip_python2 1
Name:           python-yarl
Version:        1.7.2
Release:        0
Summary:        Yet another URL library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/aio-libs/yarl/
Source:         https://files.pythonhosted.org/packages/source/y/yarl/yarl-%{version}.tar.gz
# PATCH-FIX-UPSTREAM tests_overcome_bpo42967.patch bsc#[0-9]+ mcepl@suse.com
# Overcome effects of bpo#42967, which forbade mixing amps and
# semicolons in query strings as separators.
Patch0:         tests_overcome_bpo42967.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module idna >= 2.0}
BuildRequires:  %{python_module typing_extensions >= 3.7.4 if %python-base < 3.8}
# test requirements
BuildRequires:  %{python_module multidict >= 4.0}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-idna >= 2.0
Requires:       python-multidict >= 4.0
%python_subpackages

%description
The module provides a URL class for url parsing and changing.

%prep
%autosetup -p1 -n yarl-%{version}

%build
export CFLAGS="%{optflags} -Wno-return-type"
%python_build

%install
%python_install
# devel file in non-devel-package
%python_expand rm %{buildroot}%{$python_sitearch}/yarl/_quoting_c.c
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitearch}/yarl
%{python_sitearch}/yarl-%{version}-py*.egg-info

%changelog
