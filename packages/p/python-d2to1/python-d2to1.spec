#
# spec file for package python-d2to1
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-d2to1
Version:        0.2.12.post1
Release:        0
Summary:        Allows using distutils2-like setup.cfg with a distribute/setuptools
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://pypi.python.org/pypi/d2to1
Source0:        https://files.pythonhosted.org/packages/source/d/d2to1/d2to1-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
d2to1 (the 'd' is for 'distutils') allows using distutils2-like setup.cfg
files for a package's metadata with a distribute/setuptools setup.py script.
It works by providing a distutils2-formatted setup.cfg file containing all of
a package's metadata, and a very minimal setup.py which will slurp its arguments from the setup.cfg.

%prep
%setup -q -n d2to1-%{version}
rm -rf d2to1.egg-info

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%doc CHANGES.rst README.rst
%{python_sitelib}/d2to1/
%{python_sitelib}/d2to1-%{version}-py%{py_ver}.egg-info

%changelog
