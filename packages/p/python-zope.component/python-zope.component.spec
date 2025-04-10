#
# spec file for package python-zope.component
#
# Copyright (c) 2025 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
Name:           python-zope.component%{psuffix}
Version:        6.0
Release:        0
Summary:        Zope Component Architecture
License:        ZPL-2.1
Group:          Development/Languages/Python
URL:            https://github.com/zopefoundation/zope.component
Source:         https://files.pythonhosted.org/packages/source/z/zope.component/zope.component-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-zope.event
Requires:       python-zope.hookable >= 4.2.0
Requires:       python-zope.interface >= 5.3.0a1
#test requirements
%if %{with test}
BuildRequires:  %{python_module zope.component = %{version}}
BuildRequires:  %{python_module zope.configuration}
BuildRequires:  %{python_module zope.testing}
BuildRequires:  %{python_module zope.testrunner}
%if 0%{?suse_version} >= 1600
# run complete testsuite on Tumbleweed
BuildRequires:  %{python_module persistent}
BuildRequires:  %{python_module zope.location}
BuildRequires:  %{python_module zope.proxy}
BuildRequires:  %{python_module zope.security}
%endif
%endif
%python_subpackages

%description
This package is intended to be independently reusable in any Python project. It
is maintained by the Zope Toolkit project.

This package represents the core of the Zope Component Architecture. Together
with the 'zope.interface' package, it provides facilities for defining,
registering and looking up components.

Please see http://docs.zope.org/zope.component/ or doc package for the
documentation.

%prep
%setup -q -n zope.component-%{version}
rm -rf src/zope.component.egg-info

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%python_expand PYTHONPATH=src %{_bindir}/zope-testrunner-%{$python_bin_suffix} -vvv --test-path src
%endif

%if !%{with test}
%files %{python_files}
%defattr(-,root,root)
%license LICENSE.txt COPYRIGHT.txt
%doc CHANGES.rst README.rst
%dir %{python_sitelib}/zope
%{python_sitelib}/zope/component
%{python_sitelib}/zope.component-%{version}-py*-nspkg.pth
%{python_sitelib}/zope[_.]component-%{version}.dist-info
%endif

%changelog
