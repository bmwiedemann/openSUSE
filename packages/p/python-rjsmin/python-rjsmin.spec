#
# spec file for package python-rjsmin
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
%define mod_name rjsmin
%define release_sha 53a0848b2372c1b49c03326bc8209ea39e889c47
Name:           python-%{mod_name}
Version:        1.1.0
Release:        0
Summary:        A JavaScript minifier written in Python
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://opensource.perlig.de/rjsmin/
Source:         https://github.com/ndparker/rjsmin/archive/%{release_sha}.tar.gz#/%{mod_name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE -- build without profiling
Patch0:         reproducible.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-mock
BuildRequires:  python-rpm-macros
Obsoletes:      %{name}-doc
%python_subpackages

%description
rJSmin is a Javascript minifier written in Python.

The minifier is based on the semantics of jsmin.c by Douglas Crockford.

The module is a re-implementation targeting speed, so it can be used
at runtime (rather than during a preprocessing step).

%prep
%setup -q -n %{mod_name}-%{release_sha}
%autopatch -p1

%build
%python_build

%install
%python_install
rm -rf %{buildroot}%{_datadir}/doc/rjsmin

%check
%pytest_arch

%files %{python_files}
%license LICENSE
%doc README.md docs/CHANGES
%{python_sitearch}/*

%changelog
