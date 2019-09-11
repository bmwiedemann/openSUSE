#
# spec file for package python-python-sofa
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-python-sofa
Version:        0.1.0
Release:        0
License:        MIT
Summary:        Spatially Oriented Format for Acoustics (SOFA) API for Python
Url:            http://github.com/spatialaudio/python-sofa/
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/python-sofa/python-sofa-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module netCDF4}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module scipy >= 1.2.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-netCDF4
Requires:       python-numpy
Requires:       python-scipy >= 1.2.0
BuildArch:      noarch

%python_subpackages

%description
A Python API for reading, writing and creating SOFA files as defined
by the SOFA conventions (version 1.0).

%prep
%setup -q -n python-sofa-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
