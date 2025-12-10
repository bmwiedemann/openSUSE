#
# spec file for package python-argon2-cffi
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


%{?sle15_python_module_pythons}
Name:           python-argon2-cffi
Version:        25.1.0
Release:        0
Summary:        The Argon2 password hashing algorithm for Python
License:        MIT
URL:            https://github.com/hynek/argon2_cffi
Source:         https://files.pythonhosted.org/packages/source/a/argon2-cffi/argon2_cffi-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# For test
BuildRequires:  %{python_module argon2-cffi-bindings}
Requires:       python-argon2-cffi-bindings
Provides:       python-argon2_cffi = %{version}
Obsoletes:      python-argon2_cffi < %{version}
BuildArch:      noarch
%python_subpackages

%description
A Python module that uses CFFI to access the Argon2 password hashing
C library.

%prep
%autosetup -p1 -n argon2_cffi-%{version}

# FIXME: make it compatible with the older version of setuptools.
# make sure to remove this hack once we have a newer version of setuptools.
sed -i '/.*Programming Language :: Python :: 3\.14.*/d' pyproject.toml

%build
export ARGON2_CFFI_USE_SYSTEM=1
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md FAQ.md README.md
%license LICENSE
%{python_sitelib}/argon2
%{python_sitelib}/argon2_cffi-%{version}.dist-info

%changelog
