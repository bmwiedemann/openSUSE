#
# spec file for package python-zope.copy
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-zope.copy
Version:        4.2
Release:        0
License:        ZPL-2.1
Summary:        Pluggable object copying mechanism
Url:            http://github.com/zopefoundation/zope.copy
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/z/zope.copy/zope.copy-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-zope.interface
%if %{with test}
BuildRequires:  %{python_module zope.component}
BuildRequires:  %{python_module zope.location}
BuildRequires:  %{python_module zope.testing}
BuildRequires:  %{python_module zope.testrunner}
%endif
BuildArch:      noarch

%python_subpackages

%description
This package provides a pluggable mechanism for copying persistent objects.

Documentation is hosted at https://zopecopy.readthedocs.io/en/latest/

%prep
%setup -q -n zope.copy-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%python_expand PYTHONPATH=src %{_bindir}/zope-testrunner-%{$python_bin_suffix} -vvv --test-path src
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*
%endif

%changelog
