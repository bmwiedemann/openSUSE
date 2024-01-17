#
# spec file for package python-pypng
#
# Copyright (c) 2023 SUSE LLC
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


%define binaries prichunkpng priforgepng prigreypng pripalpng pripamtopng pripnglsch pripngtopam priweavepng pricolpng priditherpng priplan9topng prirowpng
%{?sle15_python_module_pythons}
Name:           python-pypng
Version:        0.20220715.0
Release:        0
Summary:        Pure Python PNG image encoder/decoder
License:        MIT
Group:          Development/Languages/Python
URL:            https://gitlab.com/drj11/pypng
Source:         https://files.pythonhosted.org/packages/source/p/pypng/pypng-%{version}.tar.gz
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module base >= 3.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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
%setup 1 -q -n pypng-%{version}
sed -i -e '/^#!\//, 1d' code/{exnumpy,iccp,mkiccp,png,pngsuite,texttopng}.py
sed -i 's|license_file = |license_files = |' setup.cfg

%build
%pyproject_wheel

%install
%pyproject_install
for b in %{binaries}; do
  %python_clone -a %{buildroot}%{_bindir}/$b
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%{lua: for b in rpm.expand("%{binaries}"):gmatch("%S+") do
  print(rpm.expand("%python_install_alternative " .. b .. "\n"))
end}

%postun
%{lua: for b in rpm.expand("%{binaries}"):gmatch("%S+") do
  print(rpm.expand("%python_uninstall_alternative " .. b .. "\n"))
end}

%files %{python_files}
%license LICENCE
%{python_sitelib}/png.py*
%{python_sitelib}/pypng-%{version}*-info
%pycache_only %{python_sitelib}/__pycache__/png.*.pyc
%{lua: for b in rpm.expand("%{binaries}"):gmatch("%S+") do
  print(rpm.expand("%python_alternative %{_bindir}/" .. b .. "\n"))
end}

%changelog
