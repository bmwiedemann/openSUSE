#
# spec file for package python-pgmagick
#
# Copyright (c) 2026 SUSE LLC and contributors
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


# Building for primary python only due to Boost only being built for the
# primary python, and exporting all symbols. We can revisit after Python
# 3.13 is the lowest version we build for.
%define pythons python3
%{?sle15_python_module_pythons}
Name:           python-pgmagick
Version:        0.8
Release:        0
Summary:        Yet Another Python wrapper for GraphicsMagick
License:        MIT
URL:            https://github.com/hhatto/pgmagick/
Source:         https://files.pythonhosted.org/packages/source/p/pgmagick/pgmagick-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/hhatto/pgmagick/master/test/Makefile
Source2:        https://raw.githubusercontent.com/hhatto/pgmagick/master/test/utils.py
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  ghostscript-fonts-std
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(GraphicsMagick++)
%if 0%{?suse_version} >= 1500
BuildRequires:  libboost_python3-devel
%else
BuildRequires:  boost-devel
%endif
%python_subpackages

%description
The pgmagick package is a yet another boost.python based
wrapper for GraphicsMagick.

%prep
%autosetup -p1 -n pgmagick-%{version}
cp %{SOURCE1} test

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
export PYTHONDONTWRITEBYTECODE=1
%python_expand cp -v %{SOURCE2} %{buildroot}%{$python_sitearch}
mv pgmagick do-not-use-pgmagick
%python_expand PYTHON=$python PYTHONPATH=%{buildroot}%{$python_sitearch} make -C test all clean
mv do-not-use-pgmagick pgmagick
%python_expand rm -v %{buildroot}%{$python_sitearch}/utils.py

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/pgmagick
%{python_sitearch}/pgmagick-%{version}.dist-info

%changelog
