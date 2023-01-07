#
# spec file for package python-entrypoint2
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%global skip_python2 1
Name:           python-entrypoint2
Version:        1.1
Release:        0
Summary:        Command-line interface for python modules
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ponty/entrypoint2
Source:         https://github.com/ponty/entrypoint2/archive/%{version}.tar.gz#/entrypoint2-%{version}-gh.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-EasyProcess
Requires:       python-decorator
Requires:       python-path.py
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module EasyProcess}
BuildRequires:  %{python_module decorator}
BuildRequires:  %{python_module entrypoint2 = %{version}}
BuildRequires:  %{python_module path.py}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
entrypoint2 is a command-line interface for python modules, forked
off entrypoint.

%prep
%setup -q -n entrypoint2-%{version}

%if !%{with test}
%build
%python_build
%endif

%if !%{with test}
%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest tests/test_all.py
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/*
%endif

%changelog
