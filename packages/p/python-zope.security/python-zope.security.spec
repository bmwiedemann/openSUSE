#
# spec file for package python-zope.security
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 LISA GmbH, Bingen, Germany.
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
Name:           python-zope.security%{psuffix}
Version:        4.3.1
Release:        0
Summary:        Zope Security Framework
License:        ZPL-2.1
Group:          Development/Languages/Python
Url:            http://www.python.org/pypi/zope.security
Source0:        https://files.pythonhosted.org/packages/source/z/zope.security/zope.security-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  %{python_module zope.proxy-devel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytz
Requires:       python-zope.component
Requires:       python-zope.configuration
Requires:       python-zope.i18nmessageid
Requires:       python-zope.interface
Requires:       python-zope.location
Requires:       python-zope.proxy >= 4.3.0
Requires:       python-zope.schema
%if %{with test}
BuildRequires:  %{python_module BTrees}
BuildRequires:  %{python_module zope.component}
BuildRequires:  %{python_module zope.configuration}
BuildRequires:  %{python_module zope.location}
BuildRequires:  %{python_module zope.proxy >= 4.3.0}
BuildRequires:  %{python_module zope.security = %{version}}
BuildRequires:  %{python_module zope.testing}
BuildRequires:  %{python_module zope.testrunner}
%endif
%python_subpackages

%description
The Security framework provides a generic mechanism to implement security
policies on Python objects.

%prep
%setup -q -n zope.security-%{version}
rm -rf *.egg-info

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with test}
%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} %{_bindir}/zope-testrunner-%{$python_bin_suffix} -vvv --test-path src
%endif

%if !%{with test}
%files %{python_files}
%defattr(-,root,root)
%license LICENSE.txt
%doc README.rst
%{python_sitearch}/*
%endif

%changelog
