#
# spec file for package python-multipledispatch
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-multipledispatch
Version:        0.6.0
Release:        0
Summary:        Multiple dispatch in Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            http://github.com/mrocklin/multipledispatch/
Source:         https://github.com/mrocklin/multipledispatch/archive/0.6.0.tar.gz
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%python_subpackages

%description
A relatively sane approach to multiple dispatch in Python.

This implementation of multiple dispatch is mostly complete,
performs static analysis to avoid conflicts, and provides optional namespace
support.

%prep
%setup -q -n multipledispatch-%{version}
rm multipledispatch/tests/test_dispatcher_3only.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
