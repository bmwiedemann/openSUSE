#
# spec file
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


%define mod_name rjsmin
%{?sle15_python_module_pythons}
Name:           python-%{mod_name}
Version:        1.2.2
Release:        0
Summary:        A JavaScript minifier written in Python
License:        Apache-2.0
URL:            http://opensource.perlig.de/rjsmin/
Source:         https://github.com/ndparker/rjsmin/archive/refs/tags/%{version}.tar.gz#/rjsmin-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Obsoletes:      %{name}-doc
%python_subpackages

%description
rJSmin is a Javascript minifier written in Python.

The minifier is based on the semantics of jsmin.c by Douglas Crockford.

The module is a re-implementation targeting speed, so it can be used
at runtime (rather than during a preprocessing step).

%prep
%autosetup -p1 -n %{mod_name}-%{version}

%build
export CFLAGS="%optflags" # must be defined to build without -ftest-coverage instrumentation
%pyproject_wheel

%install
%pyproject_install
rm -rf %{buildroot}%{_datadir}/doc/rjsmin

%check
%pytest_arch

%files %{python_files}
%license LICENSE
%doc README.md docs/CHANGES
%{python_sitearch}/rjsmin.py
%{python_sitearch}/_rjsmin*
%pycache_only %{python_sitearch}/__pycache__/rjsmin*
%{python_sitearch}/rjsmin-%{version}.dist-info

%changelog
