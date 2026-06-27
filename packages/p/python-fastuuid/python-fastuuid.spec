#
# spec file for package python-fastuuid
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


Name:           python-fastuuid
Version:        0.14.0
Release:        0
Summary:        Python bindings to Rust's UUID library
License:        BSD-3-Clause
URL:            https://github.com/thedrow/fastuuid/
Source:         https://files.pythonhosted.org/packages/source/f/fastuuid/fastuuid-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  %{python_module maturin >= 1.0}
BuildRequires:  %{python_module pip}
BuildRequires:  cargo
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
FastUUID is a library which provides CPython bindings to Rust's UUID library.
Why?
It is much faster than Python's pure-python implementation and it is stricter
when parsing hexadecimal representation of UUIDs.
If you need to generate a lot of random UUIDs we also provide the uuid4_bulk()
function which releases the GIL for the entire duration of the generation. This
allows other threads to run while the library generates UUIDs.

%prep
%autosetup -a1 -p1 -n fastuuid-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

# tests would need uuid7 package which isn't available

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/fastuuid
%{python_sitearch}/fastuuid-%{version}.dist-info

%changelog
