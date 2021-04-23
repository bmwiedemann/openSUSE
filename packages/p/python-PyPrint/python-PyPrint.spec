#
# spec file for package python-PyPrint
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
%define         skip_python2 1
Name:           python-PyPrint
Version:        0.2.6
Release:        0
Summary:        A printer library for Python
License:        GPL-3.0-only
URL:            https://gitlab.com/coala/PyPrint/
Source:         https://files.pythonhosted.org/packages/source/P/PyPrint/PyPrint-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-colorama >= 0.3.7
Requires:       python-termcolor >= 1.1.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module colorama >= 0.3.7}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module termcolor >= 1.1.0}
# /SECTION
%python_subpackages

%description
A library providing printing facilities for python applications.

%prep
%setup -q -n PyPrint-%{version}
chmod a-x LICENSE

%build
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
export LANG=en_US.UTF-8
%python_exec setup.py test
%endif

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
