#
# spec file for package python-libpass
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


Name:           python-libpass
Version:        1.9.3
Release:        0
Summary:        Fork of passlib, a comprehensive password hashing framework
License:        BSD-3-Clause
URL:            https://github.com/notypecheck/passlib
Source:         https://files.pythonhosted.org/packages/source/l/libpass/libpass-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
# Test requirements
BuildRequires:  %{python_module bcrypt}
BuildRequires:  %{python_module argon2-cffi}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module pytest}
# endof test requirements
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-argon2-cffi >= 18.2.0
Suggests:       python-bcrypt >= 3.1.0
Suggests:       python-cryptography >= 43.0.1
Conflicts:      python-passlib
BuildArch:      noarch
%python_subpackages

%description
This is a fork of https://foss.heptapod.net/python-libs/passlib

Passlib is a password hashing library for Python 3, which provides
cross-platform implementations of over 30 password hashing algorithms, as well
as a framework for managing existing password hashes. It's designed to be useful
for a wide range of tasks, from verifying a hash found in /etc/shadow, to
providing full-strength password hashing for multi-user application.

%prep
%autosetup -p1 -n libpass-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# do not run bcrypt tests, there's an issue with bcrypt >= 5.0.0
# https://github.com/notypecheck/passlib/issues/27
donttest="test_77_fuzz_input or test_secret_w_truncate_size"
%pytest --ignore tests/test_handlers_bcrypt.py -k "not ($donttest)"

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE LICENSE
%{python_sitelib}/passlib
%{python_sitelib}/libpass-%{version}.dist-info

%changelog
