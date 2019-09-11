#
# spec file for package python-GridDataFormats
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
#

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-GridDataFormats
Version:        0.5.0
Release:        0
Summary:        Python Tools for Reading and writing of data on regular grids
License:        GPL-3.0
Group:          Development/Libraries/Python
Url:            https://github.com/MDAnalysis/GridDataFormats/
Source0:        https://files.pythonhosted.org/packages/source/G/GridDataFormats/GridDataFormats-%{version}.tar.gz
BuildRequires:  %{python_module numpy >= 1.0.3}
BuildRequires:  %{python_module paramiko}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
Requires:       python-numpy >= 1.0.3
Requires:       python-six
Requires:       python-xml
Recommends:     python-scipy
BuildArch:      noarch
%python_subpackages

%description
The *gridDataFormats* package provides classes to unify reading and
writing n-dimensional datasets. One can read grid data from files,
make them available as a :class:`Grid` object, and allows one to
write out the data again.

%prep
%setup -n GridDataFormats-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS CHANGELOG README.rst
%license COPYING*
%{python_sitelib}/gridData
%{python_sitelib}/GridDataFormats-%{version}-py*.egg-info

%changelog
