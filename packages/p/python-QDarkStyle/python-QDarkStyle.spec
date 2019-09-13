#
# spec file for package python-QDarkStyle
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
Name:           python-QDarkStyle
Version:        2.6.8
Release:        0
Summary:        A dark stylesheet for Python and Qt applications
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/ColinDuquesnoy/QDarkStyleSheet
Source:         https://github.com/ColinDuquesnoy/QDarkStyleSheet/archive/%{version}.tar.gz#/QDarkStyle-%{version}.tar.gz
BuildRequires:  %{python_module QtPy}
BuildRequires:  %{python_module pytest-qt}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module qt5-devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-pyside2
Requires:       python-setuptools
BuildArch:      noarch

%python_subpackages

%description
QDarkStyle is a dark stylesheet for Python and Qt applications.

%prep
%setup -q -n QDarkStyleSheet-%{version}
sed -i '1{\,^#!%{_bindir}/env python,d}' qdarkstyle/*.py

%build
%python_build

%check
pushd script
export LANG=C.UTF-8
python3 process_ui.py
python3 process_qrc.py

python3 ../example/example.py --qt_from=pyqt5 --test
python3 ../example/example.py --qt_from=pyqt5 --test --no_dark

python3 ../example/example.py --qt_from=pyside2 --test
python3 ../example/example.py --qt_from=pyside2 --test --no_dark
popd

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc AUTHORS.md CHANGES.md README.md
%license LICENSE.md
%python3_only %{_bindir}/qdarkstyle
%{python_sitelib}/qdarkstyle
%{python_sitelib}/QDarkStyle-%{version}-py%{py_ver}.egg-info

%changelog
