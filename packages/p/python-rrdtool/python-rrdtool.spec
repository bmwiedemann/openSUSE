#
# spec file for package python-rrdtool
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
Name:           python-rrdtool
Version:        0.1.15
Release:        0
Summary:        Python bindings for rrdtool
License:        LGPL-2.1-or-later
Group:          Development/Languages/Python
URL:            https://github.com/commx/python-rrdtool
Source:         https://github.com/commx/python-rrdtool/archive/v%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(librrd)
Requires:       rrdtool
%python_subpackages

%description
This package contains Python bindings for rrdtool.

%prep
%setup -q

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# test do not work on py2
python3 setup.py test

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/*

%changelog
