#
# spec file for package python-reedsolo
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-reedsolo
Version:        1.6.0
Release:        0
Summary:        Pure-Python Reed Solomon encoder/decoder
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/tomerfiliba/reedsolomon
Source:         https://files.pythonhosted.org/packages/source/r/reedsolo/reedsolo-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A pure-python universal errors-and-erasures Reed-Solomon Codec, based on the wonderful tutorial at Wikiversity,
written by "Bobmath" and "LRQ3000". If you are just starting with Reed-Solomon error correction codes,
the Wikiversity article is a good beginner's introduction. This is a burst-type implementation,
so that it supports any Galois field higher than 2^3, but not binary streams.

%prep
%setup -q -n reedsolo-%{version}
sed -i '/^#!/d' reedsolo.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst changelog.txt
%license LICENSE
%{python_sitelib}/*

%changelog
