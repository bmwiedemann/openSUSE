#
# spec file for package python-extras
#
# Copyright (c) 2020 SUSE LLC
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
# A build cycle exists between python-extras and python-testtools.
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
Name:           python-extras%{psuffix}
Version:        1.0.0
Release:        0
Summary:        Extra bits for Python
License:        MIT
URL:            https://github.com/testing-cabal/extras
Source:         https://files.pythonhosted.org/packages/source/e/extras/extras-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Break cycle
#!BuildIgnore:  python-extras
BuildArch:      noarch
# Test requirements:
%if %{with test}
BuildRequires:  %{python_module testtools}
%endif
%python_subpackages

%description
extras is a set of extensions to the Python standard library, originally
written to make the code within testtools cleaner, but now split out for
general use outside of a testing context.

%prep
%setup -q -n extras-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%python_exec -m unittest discover
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc NEWS README.rst
%{python_sitelib}/extras
%{python_sitelib}/extras-%{version}-py%{python_version}.egg-info/
%endif

%changelog
