#
# spec file for package python-python-qdatamatrix
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-python-qdatamatrix
Version:        0.1.31
Release:        0
Summary:        A PyQt4/PyQt5 widget for viewing and editing a DataMatrix object
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/open-cogsci/python-qdatamatrix
Source:         https://files.pythonhosted.org/packages/source/p/python-qdatamatrix/python-qdatamatrix-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/open-cogsci/python-qdatamatrix/master/copyright
Source2:        https://raw.githubusercontent.com/open-cogsci/python-qdatamatrix/master/example.py
BuildRequires:  %{python_module QtPy}
BuildRequires:  %{python_module python-datamatrix}
# QtPy has a number of possible backends, none of them mandatory, use PyQt5 for the build
BuildRequires:  %{python_module qt5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION TEST REQUIREMENTS (recommendations by datamatrix)
BuildRequires:  xvfb-run
BuildRequires:  %{python_module fastnumbers}
BuildRequires:  %{python_module prettytable}
#/SECTION
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
# don't run the event loop on the example
sed '/app.exec_/ d' %{SOURCE2} > example.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
xvfb-run $python example.py
# wait before we start the next xvfb-run
sleep 5
}

%files %{python_files}
%license copyright
%{python_sitelib}/qdatamatrix
%{python_sitelib}/python_qdatamatrix-%{version}*-info

%changelog
