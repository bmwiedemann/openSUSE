#
# spec file for package python-testresources
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


%{?sle15_python_module_pythons}
Name:           python-testresources
Version:        2.0.1
Release:        0
Summary:        A pyunit extension for managing expensive test resources
License:        (Apache-2.0 OR BSD-3-Clause) AND GPL-2.0-or-later
URL:            https://github.com/testing-cabal/testresources
Source:         https://files.pythonhosted.org/packages/source/t/testresources/testresources-%{version}.tar.gz
Patch0:         testresources-flaky-tests.patch
# PATCH-FIX-UPSTREAM gh#testing-cabal/testresources#15
Patch1:         use-correct-assertions.patch
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pbr
BuildArch:      noarch
%python_subpackages

%description
testresources: extensions to python unittest to allow declarative use
of resources by test cases.

%prep
%autosetup -p1 -n testresources-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest

%files %{python_files}
%license BSD Apache-2.0 COPYING
%doc README.rst
%{python_sitelib}/testresources
%{python_sitelib}/testresources-%{version}.dist-info

%changelog
