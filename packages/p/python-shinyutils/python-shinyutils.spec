#
# spec file for package python-shinyutils
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
Name:           python-shinyutils
Version:        3.1.0
Release:        0
Summary:        Various utilities for Python
License:        MIT
URL:            https://github.com/jayanthkoushik/shinyutils
Source:         https://files.pythonhosted.org/packages/source/s/shinyutils/shinyutils-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-crayons
Requires:       python-matplotlib
Requires:       python-seaborn
Recommends:     python-black
Recommends:     python-isort
Recommends:     python-twine
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module black}
BuildRequires:  %{python_module crayons}
BuildRequires:  %{python_module isort}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module pylint}
BuildRequires:  %{python_module seaborn}
BuildRequires:  %{python_module twine}
BuildRequires:  %{python_module wheel}
# /SECTION
%python_subpackages

%description
This package contains utilities for tasks in Python, including
matplotlib, subclasses, argument parsing, and logging.

%prep
%setup -q -n shinyutils-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
