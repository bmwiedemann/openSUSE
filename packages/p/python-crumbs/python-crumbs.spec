#
# spec file for package python-crumbs
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
# Tests are executable-dependent
%bcond_with     test
Name:           python-crumbs
Version:        2.1.0
Release:        0
Summary:        Generalized all-in-one parameters module
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/alunduil/crumbs
Source:         https://files.pythonhosted.org/packages/source/c/crumbs/crumbs-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pyinotify}
%endif
Suggests:       python-pyinotify
BuildArch:      noarch

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

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# we will put this in the right place ourselves
rm -rf %{buildroot}/%{_datadir}/doc/crumbs-*

%if %{with test}
%check
%python_expand nosetests-%{$python_bin_suffix}
%endif

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
