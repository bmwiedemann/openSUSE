#
# spec file for package python-lzallright
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


Name:           python-lzallright
Version:        0.2.6
Release:        0
Summary:        A Python 38+ binding for LZ👌(lzokay) library
License:        MIT
URL:            https://vlaci.github.io/lzallright
Source:         https://files.pythonhosted.org/packages/source/l/lzallright/lzallright-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  %{python_module maturin >= 1.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  c++_compiler
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  rust
BuildRequires:  zstd
%python_subpackages

%description
# lzallright

A Python 3.8+ binding for [LZ👌](https://github.com/jackoalan/lzokay) library which is

> A minimal, C++14 implementation of the
> [LZO compression format](http://www.oberhumer.com/opensource/lzo/).

Licensed under the friendly MIT license.

Wheels are built statically without any external dependencies.

%prep
%autosetup -p1 -a1 -n lzallright-%{version}

%build
export MATURIN_NO_INSTALL_RUST=1
%pyproject_wheel

%install
export MATURIN_NO_INSTALL_RUST=1
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest_arch

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/lzallright
%{python_sitearch}/lzallright-%{version}.dist-info

%changelog
