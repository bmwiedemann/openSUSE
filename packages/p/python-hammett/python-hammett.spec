#
# spec file for package python-hammett
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


Name:           python-hammett
Version:        0.10.0
Release:        0
Summary:        Fast python test runner
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/boxed/hammett
Source0:        https://github.com/boxed/hammett/archive/refs/tags/%{version}.tar.gz#/hammett-%{version}-gh.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-astunparse
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module astunparse}
# /SECTION
%python_subpackages

%description
Hammett is a fast python test runner that aims to be compatible with the parts
of pytest most people use (unless that conflicts with the goal of being fast).

%prep
%autosetup -p1 -n hammett-%{version}
echo "# Empty module" >> hammett/mark.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/hammett
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# the rest doesn't work: https://github.com/boxed/hammett/issues/12
testfiles="tests/test_di.py tests/test_misc.py"
%pyunittest $testfiles -v

%post
%python_install_alternative hammett

%postun
%python_uninstall_alternative hammett

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%python_alternative %{_bindir}/hammett
%{python_sitelib}/hammett
%{python_sitelib}/hammett-%{version}.dist-info

%changelog
