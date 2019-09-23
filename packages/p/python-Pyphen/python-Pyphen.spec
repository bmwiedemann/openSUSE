#
# spec file for package python-Pyphen
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
Name:           python-Pyphen
Version:        0.9.5
Release:        0
Summary:        Pure Python module to hyphenate text
License:        GPL-2.0-or-later AND LGPL-2.1-or-later AND MPL-1.1
Group:          Development/Languages/Python
Url:            https://github.com/Kozea/Pyphen
Source:         https://github.com/Kozea/Pyphen/archive/%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch

%python_subpackages

%description
Pyphen is a pure Python module to hyphenate text using existing Hunspell
hyphenation dictionaries.

This module is a fork of python-hyphenator, written by Wilbert Berendsen.

%prep
%setup -q -n Pyphen-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -v test.py

%files %{python_files}
%doc README
%license COPYING COPYING.GPL COPYING.LGPL COPYING.MPL
%{python_sitelib}/*

%changelog
