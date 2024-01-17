#
# spec file for package python-compressed_rtf
#
# Copyright (c) 2021, Martin Hauke <mardnh@gmx.de>
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-compressed_rtf
Version:        1.0.6
Release:        0
Summary:        Compressed Rich Text Format (RTF) compression and decompression package
License:        MIT
URL:            https://github.com/delimitry/compressed_rtf
Source:         compressed_rtf-%{version}.tar.xz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Compressed Rich Text Format (RTF) compression and decompression package

%prep
%setup -q -n compressed_rtf-%{version}
sed -i -e '/^#!\//, 1d' compressed_rtf/{compressed_rtf.py,crc32.py}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest -v

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/compressed_rtf*

%changelog
