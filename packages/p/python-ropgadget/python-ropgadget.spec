#
# spec file for package python-ROPGadget
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


Name:           python-ropgadget
Version:        7.6
Release:        0
Summary:        This tool lets you search your gadgets on your binaries to facilitate your ROP exploitation
License:        BSD-3-Clause
URL:            https://github.com/JonathanSalwan/ROPgadget
Source:         https://files.pythonhosted.org/packages/source/r/ropgadget/ropgadget-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
# SECTION test requirements
BuildRequires:  python3-capstone >= 5.0.1
# /SECTION
BuildRequires:  fdupes
Requires:       python3-capstone >= 5.0.1
BuildArch:      noarch
%python_subpackages

%description
This tool lets you search your gadgets on your binaries to facilitate your ROP exploitation.

%prep
%autosetup -p1 -n ropgadget-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ROPgadget
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative ROPgadget

%postun
%python_uninstall_alternative ROPgadget

%files %{python_files}
%doc AUTHORS README.md
%license LICENSE_BSD.txt
%python_alternative %{_bindir}/ROPgadget
%{python_sitelib}/ropgadget
%{python_sitelib}/ropgadget-%{version}.dist-info

%changelog
