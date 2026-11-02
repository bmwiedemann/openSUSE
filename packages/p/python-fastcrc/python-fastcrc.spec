#
# spec file for package python-fastcrc
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


Name:           python-fastcrc
Version:        0.5.0
Release:        0
Summary:        A hyper-fast Python module for computing CRC(8, 16, 32, 64) checksum
License:        MIT
URL:            https://github.com/overcat/fastcrc
Source0:        https://files.pythonhosted.org/packages/source/f/fastcrc/fastcrc-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  %{python_module maturin >= 1.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  cargo
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
A hyper-fast Python module for computing CRC(8, 16, 32, 64) checksum.

%prep
%autosetup -p1 -n fastcrc-%{version} -a1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE LICENSE
%{python_sitearch}/fastcrc
%{python_sitearch}/fastcrc-%{version}.dist-info

%changelog
