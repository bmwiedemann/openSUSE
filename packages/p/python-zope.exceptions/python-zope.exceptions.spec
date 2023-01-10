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
Name:           python-zope.exceptions%{psuffix}
Version:        4.6
Release:        0
Summary:        Zope Exceptions
License:        ZPL-2.1
Group:          Development/Languages/Python
URL:            https://cheeseshop.python.org/pypi/zope.exceptions
Source:         https://files.pythonhosted.org/packages/source/z/zope.exceptions/zope.exceptions-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-zope.interface
Obsoletes:      %{name}-doc
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module zope.exceptions}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  %{python_module zope.testrunner}
%endif
%python_subpackages

%description
This package contains exception interfaces and implementations which are so
general purpose that they don't belong in Zope application-specific packages.

%prep
%autosetup -p1 -n zope.exceptions-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%python_expand %{_bindir}/zope-testrunner-%{$python_bin_suffix} -vvv --test-path src
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst COPYRIGHT.txt README.rst
%dir %{python_sitelib}/zope/
%{python_sitelib}/zope/exceptions
%{python_sitelib}/zope.exceptions-%{version}*-info
%{python_sitelib}/zope.exceptions-%{version}*-nspkg.pth
%endif

%changelog
