#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?sle15_python_module_pythons}
%define         X_display         ":98"
Name:           python-QDarkStyle%{psuffix}
Version:        3.2.1
Release:        0
Summary:        A dark stylesheet for Python and Qt applications
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ColinDuquesnoy/QDarkStyleSheet
Source:         https://github.com/ColinDuquesnoy/QDarkStyleSheet/archive/v%{version}.tar.gz#/QDarkStyle-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-QtPy >= 2
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module QDarkStyle = %{version}}
BuildRequires:  %{python_module QtPy >= 2}
BuildRequires:  %{python_module qt5-devel}
# pyside2 is for primary python3 flavor only
# but the exception was in Leap 15.6 has both built with 3.6 and 3.11
%if 0%{?suse_version} == 1500 && 0%{?sle_version} > 150500
BuildRequires:  %{python_module pyside2}
%else
BuildRequires:  python3-pyside2
%endif
BuildRequires:  xvfb-run
%endif
%python_subpackages

%description
QDarkStyle is a dark stylesheet for Python and Qt applications.

%prep
%autosetup -p1 -n QDarkStyleSheet-%{version}
sed -i '1{\,^#!%{_bindir}/env python,d}' qdarkstyle/*.py qdarkstyle/*/*.py

%build
%if !%{with test}
%python_build
%endif

%install
%if !%{with test}
%python_install
%python_clone -a %{buildroot}%{_bindir}/qdarkstyle
%python_clone -a %{buildroot}%{_bindir}/qdarkstyle.example
%python_clone -a %{buildroot}%{_bindir}/qdarkstyle.utils
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
export LANG=C.UTF-8
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} xvfb-run $python -B -m qdarkstyle.example --qt_from=pyqt5 --test
# pyside2 is for primary python3 flavor only
PYTHONPATH=%{buildroot}%{python3_sitelib} xvfb-run python%{python_bin_suffix} -B -m qdarkstyle.example --qt_from=pyside2 --test
# no qtsass compiler (extras_require 'develop')
#%%pytest
%endif

%post
%python_install_alternative qdarkstyle qdarkstyle.example qdarkstyle.utils

%postun
%python_uninstall_alternative qdarkstyle

%if !%{with test}
%files %{python_files}
%doc AUTHORS.rst CHANGES.rst README.rst
%license LICENSE.rst
%python_alternative %{_bindir}/qdarkstyle
%python_alternative %{_bindir}/qdarkstyle.example
%python_alternative %{_bindir}/qdarkstyle.utils
%{python_sitelib}/qdarkstyle
%{python_sitelib}/QDarkStyle-%{version}*-info
%endif

%changelog
