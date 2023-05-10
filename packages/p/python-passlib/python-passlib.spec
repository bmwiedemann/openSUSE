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


%define skip_python2 1
%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif

%{?sle15_python_module_pythons}
Name:           python-passlib%{psuffix}
Version:        1.7.4
Release:        0
Summary:        Password hashing framework supporting over 20 schemes
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://foss.heptapod.net/python-libs/passlib
Source:         https://files.pythonhosted.org/packages/source/p/passlib/passlib-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module argon2_cffi}
BuildRequires:  %{python_module bcrypt}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module pytest}
%if 0%{?suse_version} >= 1550 || 0%{?is_opensuse}
BuildRequires:  %{python_module Django}
BuildRequires:  %{python_module scrypt}
%endif
BuildRequires:  apache2-utils
%endif
Recommends:     python-argon2_cffi
Recommends:     python-bcrypt
Recommends:     python-cryptography
Recommends:     python-scrypt
BuildArch:      noarch
%python_subpackages

%description
Passlib is a password hashing library for Python 2 & 3. It provides
implementations of over 20 password hashing algorithms, as well as a
framework for managing existing password hashes. It can verify hashes
found in %{_sysconfdir}/shadow, and provide password hashing for
applications.

%prep
%setup -q -n passlib-%{version}

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%check
%if %{with test}
# https://foss.heptapod.net/python-libs/passlib/-/issues/135 for the
# skipped tests.
%pytest -rs -k 'not (test_available_schemes or test_available_schemes or test_default_algorithm or test_empty_hash_value or test_empty_password or test_extension_config or test_invalid_hash_values or test_none_hash_value or test_unusable_flag or test_00_patch_control or test_01_overwrite_detection or test_12_config_presets or test_13_config_defaults or test_21_category_setting or test_02_handler_wrapper)'
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE
%doc README
%{python_sitelib}/passlib
%{python_sitelib}/passlib-%{version}-py%{python_version}.egg-info
%endif

%changelog
