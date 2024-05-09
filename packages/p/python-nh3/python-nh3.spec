#
# spec file for package python-nh3
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


%{?sle15_python_module_pythons}
Name:           python-nh3
Version:        0.2.17
Release:        0
Summary:        Ammonia HTML sanitizer Python binding
License:        MIT
URL:            https://github.com/messense/nh3
Source:         https://files.pythonhosted.org/packages/source/n/nh3/nh3-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  %{python_module maturin >= 1.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  cargo
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  zstd
%python_subpackages

%description
Ammonia HTML sanitizer Python binding

%prep
%autosetup -a1 -p1 -n nh3-%{version}
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
%doc README.md
%license LICENSE
%{python_sitearch}/nh3
%{python_sitearch}/nh3-%{version}.dist-info

%changelog
