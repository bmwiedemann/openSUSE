#
# spec file for package python-textual-speedups
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


Name:           python-textual-speedups
Version:        0.2.1
Release:        0
Summary:        None
License:        MIT
URL:            https://github.com/willmcgugan/textual-speedups
Source0:        https://files.pythonhosted.org/packages/source/t/textual_speedups/textual_speedups-%{version}.tar.gz
Source9:        vendor.tar.gz
BuildRequires:  %{python_module maturin >= 1.8}
BuildRequires:  %{python_module pip}
BuildRequires:  cargo
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  rust
%python_subpackages

%description
None

%prep
%autosetup -p1 -a9 -n textual_speedups-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%doc README.md
%{python_sitearch}/textual_speedups
%{python_sitearch}/textual_speedups-%{version}.dist-info

%changelog
