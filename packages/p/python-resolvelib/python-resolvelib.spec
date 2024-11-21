#
# spec file for package python-resolvelib
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
Name:           python-resolvelib
# ansible-core 2.14.x is currently requiring < 0.9.0
Version:        1.1.0
Release:        0
Summary:        Module to resolve abstract dependencies into concrete ones
License:        ISC
Group:          Development/Languages/Python
URL:            https://github.com/sarugaku/resolvelib
Source:         https://github.com/sarugaku/resolvelib/archive/%{version}.tar.gz#/resolvelib-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A Python module to resolve abstract dependencies into concrete ones.

%prep
%autosetup -p1 -n resolvelib-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Ignoring some faulty tests because of python-packaging version:
# gh#sarugaku/resolvelib#114
%pytest --ignore tests/functional/cocoapods/test_resolvers_cocoapods.py --ignore tests/functional/python/test_resolvers_python.py

%files %{python_files}
%doc README.rst
%{python_sitelib}/resolvelib
%{python_sitelib}/resolvelib-%{version}*info

%changelog
