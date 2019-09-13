#
# spec file for package python-pypng
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-pypng
Version:        0.0.20
Release:        0
Summary:        Pure Python PNG image encoder/decoder
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/drj11/pypng
Source:         https://files.pythonhosted.org/packages/source/p/pypng/pypng-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
PyPNG allows PNG image files to be read and written using pure Python.

%prep
%setup -q -n pypng-%{version}
sed -i -e '/^#!\//, 1d' code/png.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib}:code $python code/test_png.py

%files %{python_files}
%license LICENCE
%{python_sitelib}/*
%python3_only %{_bindir}/*

%changelog
