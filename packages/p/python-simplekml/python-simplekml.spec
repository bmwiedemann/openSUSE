#
# spec file for package python-simplekml
#
# Copyright (c) 2016-2019, Martin Hauke <mardnh@gmx.de>
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
Name:           python-simplekml
Version:        1.3.1
Release:        0
Summary:        A Simple KML creator
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
#HG-Clone:      https://bitbucket.org/KyleLancaster/simplekml
URL:            http://readthedocs.org/projects/simplekml/
Source:         https://files.pythonhosted.org/packages/source/s/simplekml/simplekml-%{version}.tar.gz
Source1:        https://bitbucket.org/KyleLancaster/simplekml/raw/76ac20169865b793aa0ed574f12651e96562570d/LICENSE.txt
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
The python package simplekml was created to generate kml (or kmz).
It was designed to alleviate the burden of having to study KML in order to
achieve anything worthwhile with it.
If you have a simple understanding of the structure of KML, then simplekml
is easy to run with and create usable KML.

%prep
%setup -q -n simplekml-%{version}
sed -i 's/\r$//' README.txt
cp %{SOURCE1} .
 
%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
#Upstream does not have any checks

%files %{python_files}
%license LICENSE.txt
%doc README.txt
%{python_sitelib}/simplekml
%{python_sitelib}/simplekml-%{version}-py%{py_ver}.egg-info

%changelog
