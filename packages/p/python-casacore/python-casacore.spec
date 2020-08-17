#
# spec file for package python-casacore
#
# Copyright (c) 2020 SUSE LLC
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
%define skip_python2 1
%global modname casacore
Name:           python-casacore
Version:        3.3.1
Release:        0
Summary:        A wrapper around CASACORE, the radio astronomy library
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/casacore/python-casacore
Source:         https://files.pythonhosted.org/packages/source/p/python-casacore/python-casacore-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  casacore-devel pkgconfig(cfitsio)
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libboost_python3-devel
BuildRequires:  python-rpm-macros
Requires:       python-configargparse
Requires:       python-future
Requires:       python-numpy
Requires:       python-six
%python_subpackages

%description
A python wrapper around CASACORE, the radio astronomy library

%prep
%setup -q -n python-casacore-%{version}

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

# No tests defined
#%%check

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitearch}/%{modname}/
%{python_sitearch}/pyrap/
%{python_sitearch}/python_%{modname}-%{version}-py%{python_version}.egg-info/

%changelog
