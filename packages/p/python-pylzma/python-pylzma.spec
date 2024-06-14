#
# spec file for package python-pylzma
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


%define oname   pylzma
Name:           python-pylzma
Version:        0.5.0
Release:        0
Summary:        Python bindings for the LZMA compression library
License:        LGPL-2.1-only
URL:            https://github.com/fancycode/pylzma
Source0:        https://github.com/fancycode/pylzma/archive/v%{version}.tar.gz
# PATCH-FIX-UPSTREAM python-pylzma-test-python3.patch gh#fancycode/pylzma#76 mcepl@suse.com
# use python3 syntax in test_usage.py
Patch0:         python-pylzma-test-python3.patch
# PATCH-FIX-UPSTREAM python-pylzma-gcc14.patch gh#fancycode/pylzma#81 glaubitz@suse.com
Patch1:         python-pylzma-gcc14.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
PyLZMA provides a platform independent way to read and write data
that has been compressed or can be decompressed by the LZMA library.

%prep
%autosetup -p1 -n %{oname}-%{version}
# No .dev0 builds please
rm -rf pylzma.egg-info setup.cfg

# Remove Shebang
sed -i '1d' py7zlib.py

%build
echo %{version} > RELEASE-VERSION
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%pyunittest_arch discover -v

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/py7zlib.py
%pycache_only %{python_sitearch}/__pycache__/py7zlib.*.py*
%{python_sitearch}/%{oname}.cpython-*.so
%{python_sitearch}/%{oname}-%{version}.dist-info

%changelog
