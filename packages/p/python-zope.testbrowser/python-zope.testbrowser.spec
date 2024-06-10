#
# spec file for package python-zope.testbrowser
#
# Copyright (c) 2024 SUSE LLC
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
Name:           python-zope.testbrowser%{psuffix}
Version:        7.0
Release:        0
Summary:        Programmable browser for functional black-box tests
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zope.testbrowser
Source:         https://files.pythonhosted.org/packages/source/z/zope.testbrowser/zope.testbrowser-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-WSGIProxy2
Requires:       python-WebTest >= 2.0.30
Requires:       python-beautifulsoup4
Requires:       python-pytz > dev
Requires:       python-setuptools
Requires:       python-soupsieve >= 1.9.0
Requires:       python-zope.cachedescriptors
Requires:       python-zope.interface
Requires:       python-zope.schema
Suggests:       python-mock
Suggests:       python-zope.testing
BuildArch:      noarch
# SECTION test requirements
%if %{with test}
BuildRequires:  %{python_module WSGIProxy2}
BuildRequires:  %{python_module WebTest >= 2.0.30}
BuildRequires:  %{python_module beautifulsoup4}
BuildRequires:  %{python_module pytz > dev}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module soupsieve >= 1.9.0}
BuildRequires:  %{python_module zope.cachedescriptors}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  %{python_module zope.schema}
BuildRequires:  %{python_module zope.testbrowser}
BuildRequires:  %{python_module zope.testing}
%endif
# /SECTION
%python_subpackages

%description
The zope.testbrowser package provides an programmable web browser
with special focus on testing.  It is used in Zope, but it's not Zope
specific.  It can be used to test or otherwise interact with any web
site.

%prep
%autosetup -p1 -n zope.testbrowser-%{version}

%build
%if !%{with test}
%pyproject_wheel
%endif

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
cd src
%pyunittest -v zope/testbrowser/tests/test_*.py
# TODO doctests
%endif

%files %{python_files}
%if !%{with test}
%doc CHANGES.rst README.rst
%license LICENSE.rst
%dir %{python_sitelib}/zope
%{python_sitelib}/zope/testbrowser
%{python_sitelib}/zope.testbrowser-%{version}-py*-nspkg.pth
%{python_sitelib}/zope.testbrowser-%{version}.dist-info
%endif

%changelog
