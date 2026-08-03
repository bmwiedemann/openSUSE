#
# spec file for package python-pyedbglib
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


%{?sle15_python_module_pythons}
Name:           python-pyedbglib
Version:        2.24.2.18
Release:        0
Summary:        Python EDBG protocol library
License:        MIT
URL:            https://github.com/microchip-pic-avr-tools/pyedbglib
Source:         https://github.com/microchip-pic-avr-tools/pyedbglib/archive/refs/tags/%{version}.tar.gz#/pyedbglib-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Cython
Requires:       python-base >= 3.8
Requires:       python-hidapi
Requires:       python-pyserial
BuildArch:      noarch
%if "%{python_provides}" == "python3"
Provides:       pyedbglib
%endif
# SECTION test requirements
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pyserial}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Low-level protocol library for communicating with Microchip CMSIS-DAP based debuggers.

%prep
%autosetup -p1 -n pyedbglib-%{version}
find -type f | xargs sed -i 's/import mock/from unittest import mock/'
find -type f | xargs sed -i 's/from mock import /from unittest.mock import /'

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/pyedbglib
%{python_sitelib}/pyedbglib-%{version}.dist-info

%changelog
