#
# spec file for package python-hardware
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
Name:           python-hardware
Version:        0.32.0
Release:        0
Summary:        Hardware detection and classification utilities
License:        Apache-2.0
URL:            https://github.com/redhat-cip/hardware
Source:         https://files.pythonhosted.org/packages/source/h/hardware/hardware-%{version}.tar.gz
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pbr >= 3.1.1}
BuildRequires:  %{python_module Babel >= 2.9.1}
BuildRequires:  %{python_module importlib-metadata >= 1.1.0}
BuildRequires:  %{python_module pexpect}
BuildRequires:  %{python_module stestr >= 2.0.0}
BuildRequires:  %{python_module stevedore}
BuildRequires:  %{python_module testtools >= 2.2.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pexpect
BuildArch:      noarch
%python_subpackages

%description
Hardware detection and classification utilities

%prep
%autosetup -p1 -n hardware-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/hardware-detect
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec -m stestr.cli run --test-path hardware/tests

%post
%python_install_alternative hardware-detect

%postun
%python_uninstall_alternative hardware-detect

%files %{python_files}
%doc AUTHORS ChangeLog README.rst
%license LICENSE
%python_alternative %{_bindir}/hardware-detect
%{python_sitelib}/hardware
%{python_sitelib}/hardware-%{version}.dist-info

%changelog
