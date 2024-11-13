#
# spec file for package python-RPi.GPIO
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


%define modname RPi.GPIO
Name:           python-%{modname}
Version:        0.7.1
Release:        0
Summary:        A module to control Raspberry Pi GPIO channels
# FIXME: Select a correct license from https://github.com/openSUSE/spec-cleaner#spdx-licenses
License:        MIT
URL:            https://sourceforge.net/projects/raspberry-gpio-python/
Source:         https://files.pythonhosted.org/packages/source/R/RPi.GPIO/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
ExclusiveArch:  %{arm} aarch64
%python_subpackages

%description
This package provides a Python module to control the GPIO on a Raspberry Pi.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%{python_sitearch}/RPi/
%{python_sitearch}/%{modname}-%{version}*-info/

%changelog
