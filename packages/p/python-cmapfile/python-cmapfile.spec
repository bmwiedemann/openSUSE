#
# spec file for package python-cmapfile
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
Name:           python-cmapfile
Version:        2025.1.1
Release:        0
Summary:        Write Chimera Map (CMAP) files
License:        BSD-3-Clause
URL:            https://github.com/cgohlke/cmapfile/
# SourceRepository: https://github.com/cgohlke/cmapfile
Source:         https://github.com/cgohlke/cmapfile/archive/v%{version}.tar.gz#/cmapfile-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module h5py >= 3.11}
BuildRequires:  %{python_module numpy >= 2.1.0}
BuildRequires:  %{python_module oiffile >= 2021.6.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module scipy >= 1.14.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tifffile >= 2024.5.24}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-h5py >= 3.11
Requires:       python-numpy >= 2.1.0
Requires:       python-oiffile >= 2021.6.6
Requires:       python-scipy >= 1.5
Requires:       python-tifffile >= 2024.5.24
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Create Chimera MAP files from various file formats containing volume data.

%prep
%setup -q -n cmapfile-%{version}
# Fix warning wrong-file-end-of-line-encoding
sed -i 's/\r//' README.rst

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/cmapfile
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative cmapfile

%postun
%python_uninstall_alternative cmapfile

%check
# No tests by upstream

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/cmapfile
%{python_sitelib}/cmapfile
%{python_sitelib}/cmapfile-%{version}.dist-info

%changelog
