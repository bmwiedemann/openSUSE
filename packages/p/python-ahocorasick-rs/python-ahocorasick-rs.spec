#
# spec file for package python-ahocorasick-rs
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-ahocorasick-rs
Version:        1.0.3
Release:        0
Summary:        Search a string for multiple substrings at once
License:        Apache-2.0
URL:            https://github.com/G-Research/ahocorasick_rs
Source:         https://files.pythonhosted.org/packages/source/a/ahocorasick_rs/ahocorasick_rs-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  %{python_module maturin >= 1.0}
BuildRequires:  %{python_module pip}
BuildRequires:  cargo-packaging
BuildRequires:  python-rpm-macros
BuildRequires:  zstd
# SECTION test requirements
BuildRequires:  %{python_module typing_extensions >= 4.6.0 if %python-base < 3.12}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pyahocorasick}
BuildRequires:  %{python_module pytest-benchmark}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
%python_subpackages

%description
ahocorasick_rs allows you to search for multiple substrings ("patterns") in a given string ("haystack") using variations of the Aho-Corasick algorithm.

In particular, it's implemented as a wrapper of the Rust aho-corasick library, and provides a faster alternative to the pyahocorasick library.

%prep
%autosetup -a1 -p1 -n ahocorasick_rs-%{version}
rm -v Cargo.lock

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE
%{python_sitearch}/ahocorasick_rs
%{python_sitearch}/ahocorasick_rs-%{version}.dist-info

%changelog
