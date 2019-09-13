#
# spec file for package python-python-qdatamatrix
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
Name:           python-python-qdatamatrix
Version:        0.1.18
Release:        0
License:        GPL-3.0-or-later
Summary:        A PyQt4/PyQt5 widget for viewing and editing a DataMatrix object
Url:            https://github.com/smathot/python-qdatamatrix
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/python-qdatamatrix/python-qdatamatrix-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/smathot/python-qdatamatrix/master/copyright
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module QtPy}
BuildRequires:  %{python_module python-datamatrix}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-QtPy
Requires:       python-python-datamatrix
BuildArch:      noarch

%python_subpackages

%description
The qdatamatrix package provides a graphical PyQt4/PyQt5 widget to
view and edit a DataMatrix object.

%prep
%setup -q -n python-qdatamatrix-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license copyright
%{python_sitelib}/*

%changelog
