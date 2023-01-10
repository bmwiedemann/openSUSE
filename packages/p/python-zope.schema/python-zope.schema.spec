#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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
Name:           python-zope.schema%{psuffix}
Version:        7.0.1
Release:        0
Summary:        Zope interface extension for defining data schemas
License:        ZPL-2.1
URL:            https://pypi.python.org/pypi/zope.schema
Source:         https://files.pythonhosted.org/packages/source/z/zope.schema/zope.schema-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-zope.event
Requires:       python-zope.interface >= 5.0.0
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module zope.event}
BuildRequires:  %{python_module zope.i18nmessageid}
BuildRequires:  %{python_module zope.interface >= 3.6.0}
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
%setup -q -n zope.schema-%{version}
rm -rf zope.schema.egg-info

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
%doc COPYRIGHT.txt CHANGES.rst README.rst
%{python_sitelib}/*
%endif

%changelog
