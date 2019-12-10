#
# spec file for package python-GooseMPL
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
Name:           python-GooseMPL
Version:        0.2.26
Release:        0
Summary:        Style and extension functions for matplotlib
License:        MIT
URL:            https://github.com/tdegeus/GooseMPL
Source:         https://github.com/tdegeus/GooseMPL/archive/v%{version}.tar.gz#/GooseMPL-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-matplotlib
Requires:       python-matplotlib-latex
Requires:       python-numpy
Requires:       tex(type1cm.sty)
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module matplotlib-latex}
BuildRequires:  %{python_module numpy}
BuildRequires:  tex(type1cm.sty)
# /SECTION
%python_subpackages

%description
GooseMPL provides a style and several style extensions for matplotlib, some custom
functions that extend matplotlib, and several examples to make professional plot
using matplotlib.

%prep
%setup -q -n GooseMPL-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand export PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -c "import GooseMPL; GooseMPL.copy_style()"
$python -B docs/examples/*/*.py
}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
