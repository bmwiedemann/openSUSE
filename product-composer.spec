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


%if "%{?sle_version}" == "150600"
%define used_python python311
%else
%define used_python python3
%endif

Name:           product-composer
Version:        0.4.12
Release:        0
Summary:        Product Composer
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/product-composer
Source:         %name-%{version}.tar.xz
# Should become a build option
Patch1:         sle-15-defaults.patch
BuildRequires:  %{used_python}-pip
BuildRequires:  %{used_python}-poetry-core
BuildRequires:  %{used_python}-setuptools
BuildRequires:  %{used_python}-wheel
Requires:       %{used_python}-PyYAML
Requires:       %{used_python}-pydantic
Requires:       %{used_python}-rpm
Requires:       %{used_python}-zstandard
# build for signdummy
Requires:       build
Requires:       checkmedia
Requires:       createrepo_c
Requires:       inst-source-utils
Requires:       mkisofs
BuildArch:      noarch

%description
The new product builder for ALP family and beyond.
WARNING: please be aware that the code is still on the move and is
         likely to break with productcompose file syntax changes.

%prep
%setup -q -n %name-%version
%if "%{?sle_version}" == "150600"
%patch -P 1 -p1
%endif

%build
%if "%{?sle_version}" == "150600"
%python311_pyproject_wheel
%else
%python3_pyproject_wheel
%endif

%install
%if "%{?sle_version}" == "150600"
%python311_pyproject_install
%else
%python3_pyproject_install
%endif
mv %buildroot/usr/bin/productcomposer %buildroot%_bindir/product-composer

%files
%doc README.rst docs examples
%_bindir/product-composer
%if "%{?sle_version}" == "150600"
%{python311_sitelib}/*
%else
%{python3_sitelib}/*
%endif

%changelog
