#
# spec file for package python-tinycss2
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
Name:           python-tinycss2
Version:        1.0.2
Release:        0
Summary:        Low-level CSS parser for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/Kozea/tinycss2
Source:         https://files.pythonhosted.org/packages/source/t/tinycss2/tinycss2-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest-isort}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module webencodings >= 0.4}
# /SECTION
Requires:       python-webencodings >= 0.4
BuildArch:      noarch

%python_subpackages

%description
TinyCSS2 is a rewrite of tinycss with a simpler API, based on the
more recent CSS Syntax Level 3 specification.

%prep
%setup -q -n tinycss2-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# remove pytest default args --flake8 and --isort
rm setup.cfg
%pytest --isort

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/tinycss2
%{python_sitelib}/tinycss2-%{version}-*.egg-info

%changelog
