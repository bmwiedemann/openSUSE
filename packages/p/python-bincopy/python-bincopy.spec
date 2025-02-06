#
# spec file for package python-bincopy
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


%{?sle15_python_module_pythons}
Name:           python-bincopy
Version:        20.1.0
Release:        0
Summary:        Mangling of various file formats that conveys binary information
License:        MIT
URL:            https://github.com/eerimoq/bincopy
Source:         https://files.pythonhosted.org/packages/source/b/bincopy/bincopy-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module argparse_addons}
BuildRequires:  %{python_module humanfriendly}
BuildRequires:  %{python_module pyelftools}
# /SECTION
Requires:       python-argparse_addons
Requires:       fdupes
Requires:       python-humanfriendly
Requires:       python-pyelftools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Mangling of various file formats that conveys binary information (Motorola S-Record, Intel HEX, TI-TXT, Verilog VMEM, ELF and binary files).

Project homepage: https://github.com/eerimoq/bincopy

Documentation: https://bincopy.readthedocs.io

%prep
%setup -q -n bincopy-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/bincopy

%check
%pytest

%post
%python_install_alternative bincopy

%postun
%python_uninstall_alternative bincopy

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/bincopy
%{python_sitelib}/bincopy*
%pycache_only %{python_sitelib}/__pycache__/*

%changelog
