#
# spec file for package python-pybind11-stubgen
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


%define pypiname pybind11-stubgen

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{pypiname}
Version:        0.12.0
Release:        0
Summary:        PEP 561 type stubs generator for pybind11 modules
License:        BSD-3-Clause
URL:            https://github.com/sizmailov/pybind11-stubgen
Source:         https://pypi.io/packages/source/p/%{pypiname}/%{pypiname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch

%python_subpackages

%description
Generate stubs for python modules.  There are several tweaks to target
specifically modules compiled using pybind11

%prep
%setup -q -n %{pypiname}-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pybind11-stubgen

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pybind11-stubgen

%postun
%python_uninstall_alternative pybind11-stubgen

%check
# pytest does not produce anything useful

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/pybind11-stubgen
%{python_sitelib}/pybind11_stubgen*

%changelog
