#
# spec file for package python-pytest-qt-app
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
Name:           python-pytest-qt-app
Version:        1.0.1
Release:        0
Summary:        QT app fixture for py.test
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/manahl/pytest-plugins
Source:         https://files.pythonhosted.org/packages/source/p/pytest-qt-app/pytest-qt-app-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/manahl/pytest-plugins/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest-server-fixtures
Requires:       python-pytest-shutil
Requires:       xauth
Requires:       xorg-x11-server
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module qt4}
BuildRequires:  %{python_module pytest-server-fixtures}
BuildRequires:  %{python_module pytest-shutil}
BuildRequires:  xauth
BuildRequires:  xorg-x11-server
# /SECTION
%python_subpackages

%description
QT app fixture for py.test.

%prep
%setup -q -n pytest-qt-app-%{version}
cp %{SOURCE1} .
rm -f setup.cfg pytest.ini tox.ini

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGES.md README.md
%license LICENSE
%{python_sitelib}/*

%changelog
