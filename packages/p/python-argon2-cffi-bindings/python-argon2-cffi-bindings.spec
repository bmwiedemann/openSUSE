#
# spec file for package python-argon2-cffi-bindings
#
# Copyright (c) 2022 SUSE LLC
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
%define skip_python2 1
Name:           python-argon2-cffi-bindings
Version:        21.2.0
Release:        0
Summary:        Low-level Python CFFI Bindings for Argon2
License:        MIT
URL:            https://github.com/hynek/argon2-cffi-bindings
Source:         https://files.pythonhosted.org/packages/source/a/argon2-cffi-bindings/argon2-cffi-bindings-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.0.1}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 45}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(libargon2)
Requires:       python-cffi >= 1.0.1
Provides:       python-argon2_cffi_bindings
Obsoletes:      python-argon2_cffi_bindings
%python_subpackages

%description
argon2-cffi-bindings provides low-level CFFI bindings
to the Argon2 password hashing algorithm.

%prep
%setup -q -n argon2-cffi-bindings-%{version}

%build
export ARGON2_CFFI_USE_SYSTEM=1
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch -v

%files %{python_files}
%doc README.md CHANGELOG.md
%license LICENSE
%{python_sitearch}/_argon2_cffi_bindings
%{python_sitearch}/argon2_cffi_bindings-%{version}*-info

%changelog
