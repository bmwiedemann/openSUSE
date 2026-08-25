#
# spec file for package python-edk2toollib
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-edk2toollib
Version:        0.23.16
Release:        0
Summary:        Tianocore Edk2 PyTool Library
License:        BSD-2-Clause-Patent
URL:            https://github.com/tianocore/edk2-pytool-library
Source:         https://github.com/tianocore/edk2-pytool-library/archive/refs/tags/v%{version}.tar.gz#/edk2-pytool-library-%{version}.tar.gz
# PATCH-FIX-OPENSUSE include submodules when building wheels
Patch0:         include-submodules.patch
BuildRequires:  %{python_module GitPython >= 3.1.30}
BuildRequires:  %{python_module SQLAlchemy >= 2.0.0}
BuildRequires:  %{python_module base >= 3.11}
BuildRequires:  %{python_module cryptography >= 39.0.1}
BuildRequires:  %{python_module joblib >= 1.3.2}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyasn1 >= 0.4.8}
BuildRequires:  %{python_module pyasn1-modules >= 0.2.8}
BuildRequires:  %{python_module pygount >= 1.6.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
Requires:       python-GitPython >= 3.1.30
Requires:       python-SQLAlchemy >= 2.0.0
Requires:       python-cryptography >= 39.0.1
Requires:       python-joblib >= 1.3.2
Requires:       python-pyasn1 >= 0.4.8
Requires:       python-pyasn1-modules >= 0.2.8
Requires:       python-pygount >= 1.6.1
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This is a Tianocore maintained project consisting of a python library supporting UEFI firmware development. This package's intent is to provide an easy way to organize and share python code to facilitate reuse across environments, tools, and scripts.

%prep
%autosetup -p1 -n edk2-pytool-library-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Requires network
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -Bm pytest -k 'not test_basic_parse'
}

%files %{python_files}
%license LICENSE
%doc readme.md
%{python_sitelib}/edk2toollib
%{python_sitelib}/edk2_pytool_library-%{version}.dist-info

%changelog
