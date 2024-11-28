#
# spec file for package python-zxcvbn-rs-py
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


Name:           python-zxcvbn-rs-py
Version:        0.1.1+5
Release:        0
Summary:        Python bindings for zxcvbn-rs, the Rust implementation of zxcvbn
License:        MIT
URL:            https://github.com/fief-dev/zxcvbn-rs-py
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  %{python_module maturin >= 1.4.0}
BuildRequires:  %{python_module pip}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  zstd
%python_subpackages

%description
Python bindings for zxcvbn-rs, the Rust implementation of zxcvbn
Zxcvbn is a password strength estimator inspired by password crackers.
Through pattern matching and conservative estimation, it recognizes and
weighs 30k common passwords, common names and surnames according to US
census data, popular English words from Wikipedia and US television and movies,
and other common patterns like dates, repeats (aaa), sequences (abcd), keyboard
patterns (qwertyuiop), and l33t speak.

%prep
%autosetup -a1 -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/zxcvbn_rs_py
%{python_sitearch}/zxcvbn_rs_py-0.1.1.dist-info
%pycache_only %{python_sitearch}/zxcvbn_rs_py/__pycache__

%changelog
