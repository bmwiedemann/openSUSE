#
# spec file for package python-PyRect
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python36 1
Name:           python-PyRect
Version:        0.1.4
Release:        0
Summary:        Rect class for Pygame-like rectangular areas
License:        BSD-3-Clause
URL:            https://github.com/asweigart/pyrect
Source:         https://files.pythonhosted.org/packages/source/P/PyRect/PyRect-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/asweigart/PyRect/master/LICENSE.txt
BuildRequires:  %{python_module pygame}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
PyRect is a simple module with a Rect class for Pygame-like rectangular areas.

%prep
%setup -q -n PyRect-%{version}
cp %{SOURCE1} .
dos2unix README.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
