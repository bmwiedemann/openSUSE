#
# spec file for package python-pypng
#
# Copyright (c) 2021 SUSE LLC
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
%{?!python_module:%define python_module() python3-%{**}}
Name:           python-pypng
Version:        0.0.20
Release:        0
Summary:        Pure Python PNG image encoder/decoder
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/drj11/pypng
Source:         https://files.pythonhosted.org/packages/source/p/pypng/pypng-%{version}.tar.gz
# PATCH-FIX-UPSTREAM pr_106 -- gh#drj11/pypng#106 remove test modules
Patch0:         pr_106.patch
# PATCH-FIX-UPSTREAM pypng-pr104-py39.patch -- gh#drj11/pypng#104 -- python 3.9 compat
Patch1:         https://github.com/drj11/pypng/pull/104.patch#/pypng-pr104-py39.patch
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module numpy if (%python-base without python36-base)}
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
PyPNG allows PNG image files to be read and written using pure Python.

%prep
%setup -q -n pypng-%{version}
%patch0 -p1
%if 0%{suse_version} >= 1550
# The patch for Python 3.9 compatibility breaks Python 2
%patch1 -p1
%endif
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
%{lua: for b in rpm.expand("%{binaries}"):gmatch("%S+") do
  print(rpm.expand("%python_install_alternative " .. b))
end}

%postun
%{lua: for b in rpm.expand("%{binaries}"):gmatch("%S+") do
  print(rpm.expand("%python_uninstall_alternative " .. b))
end}

%files %{python_files}
%license LICENCE
%{python_sitelib}/png.py*
%{python_sitelib}/pypng-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/png.*.pyc
%{lua: for b in rpm.expand("%{binaries}"):gmatch("%S+") do
  print(rpm.expand("%python_alternative %{_bindir}/" .. b))
end}

%changelog
