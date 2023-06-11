#
# spec file for package python-QtAwesome
#
# Copyright (c) 2022 SUSE LLC
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


%{?sle15_python_module_pythons}
%define skip_python2 1
Name:           python-QtAwesome
Version:        1.2.1
Release:        0
Summary:        FontAwesome icons in PyQt and PySide applications
License:        MIT
URL:            https://github.com/spyder-ide/qtawesome
Source:         https://files.pythonhosted.org/packages/source/Q/QtAwesome/QtAwesome-%{version}.tar.gz
BuildRequires:  %{python_module QtPy}
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module pytest-qt}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
# Choose one of the many backend options for pytest-qt,
# only PyQt5 available for all flavors and supported by QtPy
BuildRequires:  %{python_module qt5}
# /SECTION
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-QtPy
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
QtAwesome enables iconic fonts such as Font Awesome and
Elusive Icons in PyQt and PySide applications.

It is a port to Python - PyQt / PySide of the QtAwesome C++
library by Rick Blommers.

%prep
%setup -q -n QtAwesome-%{version}
dos2unix CHANGELOG.md README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/qta-browser

%check
%pytest -v qtawesome/tests

%post
%python_install_alternative qta-browser

%postun
%python_uninstall_alternative qta-browser

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG.md README.md
%{python_sitelib}/*
%python_alternative %{_bindir}/qta-browser

%changelog
