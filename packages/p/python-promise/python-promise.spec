#
# spec file for package python-promise
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


Name:           python-promise
Version:        2.3.0
Release:        0
Summary:        Promises/A+ implementation for Python
License:        MIT
URL:            https://github.com/syrusakbary/promise
Source:         https://github.com/syrusakbary/promise/archive/v%{version}.tar.gz#/promise-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#syrusakbary/promise#96
Patch0:         pytest-7-support.patch
# PATCH-FIX-UPSTREAM python-311.patch gh#syrusakbary/promise#99
Patch1:         python-311.patch
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
This is an implementation of Promises in Python

%prep
%autosetup -p1 -n promise-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/promise*

%changelog
