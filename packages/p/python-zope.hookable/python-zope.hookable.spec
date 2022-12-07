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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-zope.hookable%{psuffix}
Version:        5.4
Release:        0
Summary:        Zope hookable
License:        ZPL-2.1
URL:            https://www.python.org/pypi/zope.hookable
Source:         https://files.pythonhosted.org/packages/source/z/zope.hookable/zope.hookable-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION documentation requirements
BuildRequires:  %{python_module Sphinx}
# /SECTION
# SECTION testing requirements
%if %{with test}
BuildRequires:  %{python_module zope.hookable}
BuildRequires:  %{python_module zope.testing}
%endif
# /SECTION
%python_subpackages

%description
Hookable object support.

Support the efficient creation of hookable objects, which are callable objects
that are meant to be replaced by other callables, at least optionally.

The idea is you create a function that does some default thing and make it
hookable. Later, someone can modify what it does by calling its sethook method
and changing its implementation. All users of the function, including those
that imported it, will see the change.

%package     -n %{name}-doc
Summary:        Zope hookable
Provides:       %{python_module zope.hookable-doc = %{version}}
BuildArch:      noarch

%description -n %{name}-doc
This package contains documentation files for %{name}.

%prep
%setup -q -n zope.hookable-%{version}
rm -rf zope.hookable.egg-info

%build
%if !%{with test}
%python_build
python3 setup.py build_sphinx && rm build/sphinx/html/.buildinfo build/sphinx/html/objects.inv
%endif

%install
%if !%{with test}
%python_install
%{python_expand rm -f %{buildroot}%{$python_sitearch}/zope/hookable/_zope_hookable.c
  %fdupes %{buildroot}%{$python_sitearch}
}
%endif

%check
%if %{with test}
pushd src
%pyunittest 'zope.hookable.tests.test_hookable.test_suite'
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst COPYRIGHT.txt README.rst
%dir %{python_sitearch}/zope
%{python_sitearch}/zope/hookable
%{python_sitearch}/zope.hookable-%{version}*-info
%{python_sitearch}/zope.hookable-%{version}*-nspkg.pth
%endif

%if !%{with test}
%files -n %{name}-doc
%doc build/sphinx/html/
%endif

%changelog
