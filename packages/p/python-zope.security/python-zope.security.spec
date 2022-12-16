#
# spec file
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2013-2022 LISA GmbH, Bingen, Germany.
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
Version:        5.8
Release:        0
Summary:        Zope Security Framework
License:        ZPL-2.1
Group:          Development/Languages/Python
URL:            https://www.python.org/pypi/zope.security
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
Requires:       python-zope.schema >= 4.2.0
%if %{with test}
BuildRequires:  %{python_module BTrees}
BuildRequires:  %{python_module zope.component}
BuildRequires:  %{python_module zope.configuration}
BuildRequires:  %{python_module zope.location}
BuildRequires:  %{python_module zope.proxy >= 4.3.0}
BuildRequires:  %{python_module zope.schema >= 4.2.0}
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

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%python_expand rm %{buildroot}%{$python_sitearch}/zope/security/*.c
%endif

%if %{with test}
%check
%python_expand %{_bindir}/zope-testrunner-%{$python_bin_suffix} -vvv --test-path src
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc README.rst
%dir %{python_sitearch}/zope
%{python_sitearch}/zope/security
%{python_sitearch}/zope.security-%{version}*-info
%{python_sitearch}/zope.security-%{version}*-nspkg.pth
%endif

%changelog
