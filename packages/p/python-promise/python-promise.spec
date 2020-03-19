#
# spec file for package python-promise
#
# Copyright (c) 2020 SUSE LLC
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
%bcond_without python2
%bcond_without python3
Name:           python-promise
Version:        2.3.0
Release:        0
Summary:        Promises/A+ implementation for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/syrusakbary/promise
Source:         https://github.com/syrusakbary/promise/archive/v%{version}.tar.gz#/promise-%{version}.tar.gz
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
%if %{with python2}
BuildRequires:  python2-futures
BuildRequires:  python2-typing
%endif
%if %{with python3}
BuildRequires:  python3-pytest-asyncio
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
%ifpython2
Requires:       python-typing
%endif
%python_subpackages

%description
This is an implementation of Promises in Python

%prep
%setup -q -n promise-%{version}

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
%{python_sitelib}/*

%changelog
