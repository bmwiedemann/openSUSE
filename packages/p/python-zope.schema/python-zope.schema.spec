#
# spec file for package python-zope.schema
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-zope.schema%{psuffix}
Version:        8.1
Release:        0
Summary:        Zope interface extension for defining data schemas
License:        ZPL-2.1
URL:            https://pypi.python.org/pypi/zope.schema
Source:         https://files.pythonhosted.org/packages/source/z/zope.schema/zope_schema-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-zope.event
Requires:       python-zope.interface >= 5.0.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module zope.i18nmessageid}
BuildRequires:  %{python_module zope.schema = %{version}}
BuildRequires:  %{python_module zope.testing}
BuildRequires:  %{python_module zope.testrunner}
%endif
%python_subpackages

%description
Schemas extend the notion of interfaces to detailed descriptions of
Attributes (but not methods).  Every schema is an interface and
specifies the public fields of an object.  A *field* roughly
corresponds to an attribute of a Python object.  But a Field provides
space for at least a title and a description.  It can also constrain
its value and provide a validation method.  Besides you can optionally
specify characteristics such as its value being read-only or not
required.

%prep
%setup -q -n zope_schema-%{version}
rm -rf zope.schema.egg-info

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
%license LICENSE.txt
%doc COPYRIGHT.txt CHANGES.rst README.rst
%dir %{python_sitelib}/zope
%{python_sitelib}/zope/schema
%{python_sitelib}/zope[_.]schema-%{version}.dist-info
%endif

%changelog
