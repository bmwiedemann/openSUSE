#
# spec file for package python-PyExecJS
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
Name:           python-PyExecJS
Version:        1.5.1
Release:        0
Summary:        Python module to run JavaScript
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/doloopwhile/PyExecJS
Source:         https://files.pythonhosted.org/packages/source/P/PyExecJS/PyExecJS-%{version}.tar.gz
# PATCH: Not all runtimes are available in openSUSE, hence only test the default instead of failing.
Patch0:         PyExecJS-test-default-runtime-only.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  nodejs
BuildRequires:  python-rpm-macros
Requires:       nodejs
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
PyExecJS is a port of ExecJS for Ruby.
It allows running JavaScript code from Python.

%prep
%setup -q -n PyExecJS-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test assumes Unicode environment
export LC_ALL=C.UTF-8
%python_exec ./test_execjs.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
