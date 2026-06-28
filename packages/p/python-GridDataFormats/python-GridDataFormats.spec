#
# spec file for package python-GridDataFormats
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


Name:           python-GridDataFormats
Version:        1.2.0
Release:        0
Summary:        Python Tools for Reading and writing of data on regular grids
License:        LGPL-3.0-or-later
URL:            https://github.com/MDAnalysis/GridDataFormats/
Source0:        https://files.pythonhosted.org/packages/source/G/GridDataFormats/griddataformats-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 40.9.0}
BuildRequires:  %{python_module versioningit}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-mrcfile
Requires:       python-numpy >= 1.21
Requires:       python-scipy
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mrcfile}
BuildRequires:  %{python_module numpy >= 1.21}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
# /SECTION
%python_subpackages

%description
The *gridDataFormats* package provides classes to unify reading and
writing n-dimensional datasets. One can read grid data from files,
make them available as a :class:`Grid` object, and allows one to
write out the data again.

%prep
%autosetup -p1 -n griddataformats-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG README.rst
%license COPYING*
%{python_sitelib}/gridData
%{python_sitelib}/[Gg]rid[Dd]ata[Ff]ormats-%{version}.dist-info

%changelog
