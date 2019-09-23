#
# spec file for package python-ws4py
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
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-ws4py%{psuffix}
Version:        0.5.1
Release:        0
Summary:        WebSocket client and server library for Python
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Lawouach/WebSocket-for-Python
Source:         https://files.pythonhosted.org/packages/source/w/ws4py/ws4py-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module gevent}
BuildRequires:  %{python_module greenlet}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tornado}
BuildRequires:  %{python_module ws4py = %{version}}
%endif
%python_subpackages

%description
Python library providing an implementation of the WebSocket protocol
defined in RFC 6455.

%prep
%setup -q -n ws4py-%{version}
# CherryPy is python3 only to ease the testing just skip it here
rm test/test_cherrypy.py

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%pytest
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*
%endif

%changelog
