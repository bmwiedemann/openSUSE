#
# spec file for package python-asciimatics
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
Name:           python-asciimatics
Version:        1.11.0
Release:        0
Summary:        Package to replace curses and create ASCII animations
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/peterbrittain/asciimatics
Source:         https://files.pythonhosted.org/packages/source/a/asciimatics/asciimatics-%{version}.tar.gz
# isatty test skips see https://github.com/peterbrittain/asciimatics/issues/216
Patch0:         pr_200.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow >= 2.7.0
Requires:       python-curses
Requires:       python-future
Requires:       python-pyfiglet >= 0.7.2
Requires:       python-wcwidth
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Pillow >= 2.7.0}
BuildRequires:  %{python_module curses}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pyfiglet >= 0.7.2}
BuildRequires:  %{python_module wcwidth}
# /SECTION
%python_subpackages

%description
Asciimatics is a package to help people create full-screen text UIs
(from interactive forms to ASCII animations) on any platform.

%prep
%setup -q -n asciimatics-%{version}
%autopatch -p1
sed -i '/setup_requires/d' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_image_files requires specific version of Pillow
%python_exec -m nose -v -e test_image_files

%files %{python_files}
%doc CHANGES.rst README.rst doc/source/*.rst doc/source/*.png
%license LICENSE
%{python_sitelib}/*

%changelog
