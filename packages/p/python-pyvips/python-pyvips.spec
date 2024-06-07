#
# spec file for package python-pyvips
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pyvips
Version:        2.2.3
Release:        0
Summary:        Python bindings for VIPS image processing library
License:        MIT
URL:            https://github.com/libvips/pyvips
Source0:        https://pypi.io/packages/source/p/pyvips/pyvips-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.0.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cffi >= 1.0.0
BuildArch:      noarch
%python_subpackages

%description
This package contains the Python bindings for the VIPS library.

%prep
%autosetup -n pyvips-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# NOTE: tests are not present in the pypi tarball

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/pyvips
%{python_sitelib}/pyvips-%{version}-py%{python_version}.egg-info

%changelog
