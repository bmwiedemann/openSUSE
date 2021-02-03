#
# spec file for package python-spyder-unittest
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


# Not really singlespec: Spyder is an app only for the primary python3 interpreter
# But we need the python3-spyder-unittest name, provided by the python_subpackages rewrite
%define pythons python3
Name:           python-spyder-unittest
Version:        0.4.1
Release:        0
Summary:        Plugin to run tests from within the Spyder IDE
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/spyder-ide/spyder-unittest
Source:         https://files.pythonhosted.org/packages/source/s/spyder_unittest/spyder_unittest-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       python-lxml
Requires:       spyder >= 3
Provides:       spyder-unittest = %{version}-%{release}
Obsoletes:      spyder-unittest < %{version}-%{release}
Provides:       spyder3-unittest = %{version}-%{release}
Obsoletes:      spyder3-unittest < %{version}-%{release}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  python3-QtPy
BuildRequires:  python3-lxml
# Tests that it can run nose tests
BuildRequires:  python3-nose
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-qt
BuildRequires:  python3-pytest-xvfb
BuildRequires:  spyder >= 3
BuildRequires:  xdpyinfo
# /SECTION
%python_subpackages

%description
Spyder, the Scientific Python Development Environment, is an
IDE for researchers, engineers and data analysts.

This is a plugin for the Spyder IDE that integrates unit test
frameworks. It allows running tests and viewing the results.

%prep
%setup -q -n spyder_unittest-%{version}

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/spyder_unittest
%{python_sitelib}/spyder_unittest-%{version}*-info

%changelog
