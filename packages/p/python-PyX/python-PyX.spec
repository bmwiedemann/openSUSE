#
# spec file for package python-PyX
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
%bcond_without  test
Name:           python-PyX
Version:        0.15
Release:        0
Summary:        Python package for the generation of PostScript, PDF, and SVG files
License:        GPL-2.0-or-later
Group:          Development/Languages/Python
URL:            https://pyx-project.org/
Source:         https://github.com/pyx-project/pyx/archive/%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module testfixtures}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  texlive-latex-bin-bin
BuildRequires:  texlive-tex-bin
BuildRequires:  texlive-texware-bin
Obsoletes:      python3-pyx < %{version}
Provides:       python3-pyx = %{version}
BuildArch:      noarch
%python_subpackages

%description
PyX is a Python package for the creation of PostScript, PDF, and SVG files. It
combines an abstraction of the PostScript drawing model with a TeX/LaTeX
interface. Complex tasks like 2d and 3d plots in publication-ready quality are
built out of these primitives.

%prep
%setup -q -n pyx-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest test/unit

%files %{python_files}
%license LICENSE
%doc AUTHORS CHANGES README.md
%{python_sitelib}/*

%changelog
