#
# spec file for package python-compressed_rtf
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2021-2025, Martin Hauke <mardnh@gmx.de>
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
Name:           python-compressed_rtf
Version:        1.0.7
Release:        0
Summary:        Compressed Rich Text Format (RTF) compression and decompression package
License:        MIT
URL:            https://github.com/delimitry/compressed_rtf
Source:         compressed_rtf-%{version}.tar.xz
Patch0:         0001-fix-pyproject.toml-license-format.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Compressed Rich Text Format (RTF) compression and decompression package

%prep
%autosetup -p1 -n compressed_rtf-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/compressed_rtf
%{python_sitelib}/compressed_rtf-%{version}.dist-info

%changelog
