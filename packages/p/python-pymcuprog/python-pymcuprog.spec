#
# spec file for package python-pymcuprog
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-pymcuprog
Version:        3.19.4.61
Release:        0
Summary:        Python MCU programmer
License:        MIT
URL:            https://github.com/microchip-pic-avr-tools/pymcuprog
Source:         https://github.com/microchip-pic-avr-tools/pymcuprog/archive/refs/tags/%{version}.tar.gz#/pymcuprog-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-appdirs
Requires:       python-intelhex
Requires:       python-pyserial
Requires:       python-base >= 3.8
BuildArch:      noarch
%if "%{python_provides}" == "python3"
Provides:       pymcuprog
%endif
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module appdirs}
BuildRequires:  %{python_module intelhex}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module pyedbglib}
BuildRequires:  %{python_module pyserial}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Python utility for programming various Microchip MCU devices using Microchip CMSIS-DAP based debuggers.

%prep
%autosetup -p1 -n pymcuprog-%{version}
find -type f | xargs sed -i 's/import mock/from unittest import mock/'
find -type f | xargs sed -i 's/from mock import /from unittest.mock import /'

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pymcuprog
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
%python_libalternatives_reset_alternative pymcuprog

%post
%python_install_alternative pymcuprog

%postun
%python_uninstall_alternative pymcuprog

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%python_alternative %{_bindir}/pymcuprog
%{python_sitelib}/pymcuprog
%{python_sitelib}/pymcuprog-%{version}.dist-info

%changelog
