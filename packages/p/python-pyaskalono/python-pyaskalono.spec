#
# spec file for package python-pyaskalono
#
# Copyright (c) 2026 SUSE LLC
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


%define pythons python3
Name:           python-pyaskalono
Version:        0.2.0
Release:        0
Summary:        Python bindings for askalono - rust library to detect license texts
License:        Apache-2.0
URL:            https://github.com/kumekay/pyaskalono
Source:         https://files.pythonhosted.org/packages/source/p/pyaskalono/pyaskalono-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module maturin >= 1.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  cargo
BuildRequires:  fdupes
BuildRequires:  zstd
Suggests:       python-maturin >= 1.0
Suggests:       python-pytest >= 7.0
%python_subpackages

%description
Python bindings for askalono - rust library to detect license texts.

%prep
%autosetup -a1 -p1 -n pyaskalono-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pytest_arch

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/askalono
%{python_sitearch}/pyaskalono-%{version}.dist-info

%changelog
