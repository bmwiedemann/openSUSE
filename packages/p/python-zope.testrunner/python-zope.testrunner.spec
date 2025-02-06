#
# spec file for package python-zope.testrunner
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-zope.testrunner%{psuffix}
Version:        6.6.1
Release:        0
Summary:        Zope testrunner script
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zope.testrunner
Source:         https://files.pythonhosted.org/packages/source/z/zope.testrunner/zope_testrunner-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module zope.exceptions}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires:       python-zope.exceptions
Requires:       python-zope.interface
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module zope.testing}
BuildRequires:  %{python_module zope.testrunner = %{version}}
BuildRequires:  %{pythons}
%endif
%python_subpackages

%description
This package provides a flexible test runner with layer support.

%prep
%autosetup -p1 -n zope_testrunner-%{version}
find -size 0 -delete

%build
%pyproject_wheel

%install
%if !%{with test}
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/zope-testrunner
%endif

%if %{with test}
%check
%{python_expand #
$python -m zope.testrunner --test-path=src -vv
}
%endif

%if !%{with test}
%post
%python_install_alternative zope-testrunner

%postun
%python_uninstall_alternative zope-testrunner

%files %{python_files}
%license LICENSE.md
%doc README.rst
%python_alternative %{_bindir}/zope-testrunner
%{python_sitelib}/zope/testrunner
%{python_sitelib}/zope.testrunner-%{version}-py*-nspkg.pth
%{python_sitelib}/zope.testrunner-%{version}.dist-info
%endif

%changelog
