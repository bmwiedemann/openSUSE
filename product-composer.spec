#
# spec file for package product-composer
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


Name:           product-composer
Version:        0.4.7
Release:        0
Summary:        Product Composer
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/product-composer
Source:         %name-%{version}.tar.xz
BuildRequires:  python3-pip
BuildRequires:  python3-poetry-core
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
Requires:       python3-PyYAML
Requires:       python3-pydantic
Requires:       python3-rpm
Requires:       python3-zstandard
# build for signdummy
Requires:       build
Requires:       checkmedia
Requires:       createrepo
Requires:       inst-source-utils
Requires:       mkisofs
BuildArch:      noarch

%description
The new product builder for ALP family and beyond.
WARNING: please be aware that the code is still on the move and is
         likely to break with productcompose file syntax changes.

%prep
%autosetup -n %name-%version -p1

%build
%python3_pyproject_wheel

%install
%python3_pyproject_install
mv %buildroot/usr/bin/productcomposer %buildroot%_bindir/product-composer

%files
%doc README.rst docs examples
%_bindir/product-composer
%{python3_sitelib}/*

%changelog
