#
# spec file for package python-pylzma
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


%define oname   pylzma
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pylzma
Version:        0.5.0
Release:        0
Summary:        Python bindings for the LZMA compression library
License:        LGPL-2.1-only
Group:          Development/Languages/Python
URL:            https://github.com/fancycode/pylzma
Source0:        https://github.com/fancycode/pylzma/archive/v%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
PyLZMA provides a platform independent way to read and write data
that has been compressed or can be decompressed by the LZMA library.

%prep
%setup -q -n %{oname}-%{version}

# Remove Shebang
sed -i '1d' py7zlib.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitearch}/*
%{python_sitearch}/%{oname}*

%changelog
