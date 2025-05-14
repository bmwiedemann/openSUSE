#
# spec file for package python-PyRect
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-PyRect
Version:        0.2.0
Release:        0
Summary:        Rect class for Pygame-like rectangular areas
License:        BSD-3-Clause
URL:            https://github.com/asweigart/pyrect
Source:         https://files.pythonhosted.org/packages/source/P/PyRect/PyRect-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/asweigart/PyRect/master/LICENSE.txt
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pygame}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/pyrect
%{python_sitelib}/[Pp]y[Rr]ect-%{version}*-info

%changelog
