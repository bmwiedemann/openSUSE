#
# spec file for package python-hidapi
#
# Copyright (c) 2023 SUSE LLC
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

Name:           python-hidapi
Version:        0.14.0.post2
Release:        0
Summary:        A Cython interface to the hidapi from https://githubcom/libusb/hidapi
License:        BSD-3-Clause AND GPL-3.0
URL:            https://github.com/trezor/cython-hidapi
# osc service runall download_files
Source:         https://files.pythonhosted.org/packages/source/h/hidapi/hidapi-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module poetry}
BuildRequires:  %{python_module Cython0}
# SECTION test requirements
BuildRequires:  %{python_module setuptools >= 19.0}
# /SECTION
BuildRequires:  fdupes
BuildRequires:  libusb-1_0-devel
BuildRequires:  libgudev-1_0-devel
BuildRequires:  pkgconfig(hidapi-hidraw)
Requires:       python-Cython0

%python_subpackages

%description
A Cython interface to the hidapi from https://github.com/libusb/hidapi

%prep
%setup -q -n hidapi-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE-bsd.txt LICENSE-gpl3.txt LICENSE-orig.txt LICENSE.txt
%{python_sitearch}/hid.*
%{python_sitearch}/hidapi-%{version}*

%changelog
