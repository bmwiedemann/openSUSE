#
# spec file for package python-GooseMPL
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


Name:           python-GooseMPL
Version:        0.12.1
Release:        0
Summary:        Style and extension functions for matplotlib
License:        MIT
URL:            https://github.com/tdegeus/GooseMPL
Source:         https://files.pythonhosted.org/packages/source/G/GooseMPL/GooseMPL-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-PyYAML
Requires:       python-deprecation
Requires:       python-matplotlib
Requires:       python-matplotlib-latex
Requires:       python-numpy
Requires:       python-scipy
# \usepackage{amsmath, amsfonts, amssymb, bm}
Requires:       texlive-amsmath
Requires:       texlive-amsfonts
Requires:       texlive-tools
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module matplotlib-latex}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module deprecation}
BuildRequires:  %{python_module matplotlib}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy}
BuildRequires:  texlive-amsfonts
BuildRequires:  texlive-amsmath
BuildRequires:  texlive-tools
# /SECTION
%python_subpackages

%description
GooseMPL provides a style and several style extensions for matplotlib, some custom
functions that extend matplotlib, and several examples to make professional plot
using matplotlib.

%prep
%setup -q -n GooseMPL-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest test/main.py

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/GooseMPL
%{python_sitelib}/GooseMPL-%{version}.dist-info

%changelog
