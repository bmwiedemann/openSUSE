#
# spec file for package python-pypng
#
# Copyright (c) 2020 SUSE LLC
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


%define binaries prichunkpng priforgepng prigreypng pripalpng pripamtopng pripnglsch pripngtopam priweavepng
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pypng
Version:        0.0.20
Release:        0
Summary:        Pure Python PNG image encoder/decoder
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/drj11/pypng
Source:         https://files.pythonhosted.org/packages/source/p/pypng/pypng-%{version}.tar.gz
Patch0:         pr_106.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
PyPNG allows PNG image files to be read and written using pure Python.

%prep
%setup -q -n pypng-%{version}
%patch0 -p1
sed -i -e '/^#!\//, 1d' code/png.py

%build
%python_build

%install
%python_install
for b in %{binaries}; do
  %python_clone -a %{buildroot}%{_bindir}/$b
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib}:code $python code/test_png.py

%post
for b in %{binaries}; do
  %python_install_alternative $b
done

%postun
for b in %{binaries}; do
  %python_uninstall_alternative $b
done

%files %{python_files}
%license LICENCE
%{python_sitelib}/*
%python_alternative %{_bindir}/prichunkpng
%python_alternative %{_bindir}/priforgepng
%python_alternative %{_bindir}/prigreypng
%python_alternative %{_bindir}/pripalpng
%python_alternative %{_bindir}/pripamtopng
%python_alternative %{_bindir}/pripnglsch
%python_alternative %{_bindir}/pripngtopam
%python_alternative %{_bindir}/priweavepng

%changelog
