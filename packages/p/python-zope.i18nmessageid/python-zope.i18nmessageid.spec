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
Name:           python-zope.i18nmessageid%{psuffix}
Version:        5.1.1
Release:        0
Summary:        Zope Location
License:        ZPL-2.1
URL:            https://www.python.org/pypi/zope.i18nmessageid
Source:         https://files.pythonhosted.org/packages/source/z/zope.i18nmessageid/zope.i18nmessageid-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION documentation requirements
BuildRequires:  %{python_module Sphinx}
Requires:       python-six
# /SECTION
# SECTION testing requirements
%if %{with test}
BuildRequires:  %{python_module zope.i18nmessageid}
%endif
%python_subpackages

%description
In Zope3, i18nmessageid are special objects that has a structural i18nmessageid.

%package     -n %{name}-doc
Summary:        Zope Location
Provides:       %{python_module zope.i18nmessageid-doc = %{version}}
BuildArch:      noarch

%description -n %{name}-doc
This package contains documentation files for %{name}.

%prep
%setup -q -n zope.i18nmessageid-%{version}
rm -rf zope.i18nmessageid.egg-info

%build
%if !%{with test}
%python_build
python3 setup.py build_sphinx && rm build/sphinx/html/.buildinfo build/sphinx/html/objects.inv
%endif

%install
%if !%{with test}
%python_install
# don't bother with development files
%{python_expand rm -f %{buildroot}%{$python_sitearch}/zope/i18nmessageid/_zope_i18nmessageid_message.c
  %fdupes %{buildroot}%{$python_sitearch}
}
%endif

%check
%if %{with test}
%pyunittest 'zope.i18nmessageid.tests.test_suite'
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst COPYRIGHT.txt README.rst
%dir %{python_sitearch}/zope
%{python_sitearch}/zope/i18nmessageid
%{python_sitearch}/zope.i18nmessageid-%{version}*-info
%{python_sitearch}/zope.i18nmessageid-%{version}*-nspkg.pth
%endif

%if !%{with test}
%files -n %{name}-doc
%doc build/sphinx/html/
%endif

%changelog
