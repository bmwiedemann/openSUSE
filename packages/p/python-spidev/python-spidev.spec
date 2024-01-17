#
# spec file for package python-spidev
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-spidev
Version:        3.6
Release:        0
Summary:        Python module for interfacing with SPI devices
License:        MIT
URL:            https://pypi.org/project/spidev/
Source0:        https://files.pythonhosted.org/packages/source/s/spidev/spidev-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This package contains the python module for interfacing with SPI devices from user space via the spidev linux kernel driver.

%prep
%setup -q -n spidev-%{version}

%build
%python_build

%install
%python_install -O1 --skip-build

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitearch}/*.so
%{python_sitearch}/*.egg-info

%changelog
