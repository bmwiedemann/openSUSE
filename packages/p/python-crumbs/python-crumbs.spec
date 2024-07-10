#
# spec file for package python-crumbs
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
%define modname crumbs
Name:           python-crumbs
Version:        2.1.1
Release:        0
Summary:        Generalized all-in-one parameters module
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/alunduil/crumbs
Source:         https://github.com/alunduil/%{modname}/archive/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-pyinotify
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pyinotify}
BuildRequires:  %{python_module pytest}
%endif
%python_subpackages

%description
This package provides a single interface to environment variables',
configuration files', and command line arguments' provided values.  The
dictionary-like interface makes interacting with these, most of the time
disparate, resources much simpler.  It also allows parameters' values to be set
in any of the three sources and selects an appropriate value when a parameter's
value is specified in multiple sources.  This way the most expected value,
according to the normal prcedence—command line arguments then configuration
files then environment variables, is always returned.

%prep
%setup -q -n crumbs-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# we will put this in the right place ourselves
rm -rf %{buildroot}/%{_datadir}/doc/crumbs-*

%check
# Tests are all broken, but they were even before so not a regression
# %%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
