#
# spec file for package python-aiodns
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


# DNS tests won't work in OBS
%bcond_with tests

%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-aiodns
Version:        3.2.0
Release:        0
Summary:        Simple DNS resolver for asyncio
License:        MIT
Group:          Development/Libraries/Python
URL:            https://github.com/saghul/aiodns/releases
Source0:        https://github.com/saghul/aiodns/archive/refs/tags/v%{version}.tar.gz#/aiodns-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
Requires:       python-pycares >= 4.0.0
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with tests}
BuildRequires:  %{python_module pycares}
BuildRequires:  python-typing
%endif
BuildArch:      noarch

%python_subpackages

%description
Simple DNS resolver for asyncio module.

%prep
%autosetup -p1 -n aiodns-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}/aiodns/

%if %{with tests}
%check
%python_exec ./tests.py
%endif

%files %{python_files}
%doc ChangeLog README.rst
%license LICENSE
%{python_sitelib}/aiodns*

%changelog
