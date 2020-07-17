#
# spec file for package python-spyder-unittest
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-spyder-unittest
Version:        0.4.1
Release:        0
Summary:        Plugin to run tests from within the Spyder IDE
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/spyder-ide/spyder-unittest
Source:         https://files.pythonhosted.org/packages/source/s/spyder_unittest/spyder_unittest-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-lxml
Requires:       spyder >= 3
Provides:       spyder3-unittest = %{version}-%{release}
Obsoletes:      spyder3-unittest < %{version}-%{release}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module QtPy}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pytest-qt}
BuildRequires:  %{python_module pytest-xvfb}
BuildRequires:  %{python_module pytest}
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc CHANGELOG.md README.md
%license LICENSE.txt
%{python_sitelib}/*

%changelog
