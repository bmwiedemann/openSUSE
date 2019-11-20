#
# spec file for package python-palettable
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
%bcond_without  test
Name:           python-palettable
Version:        3.3.0
Release:        0
Summary:        Color palettes for Python
License:        MIT
URL:            https://jiffyclub.github.io/palettable/
Source:         https://files.pythonhosted.org/packages/source/p/palettable/palettable-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Palettable (formerly brewer2mpl) is a library of color palettes for Python.
It's written in pure Python with no dependencies, but it can supply color maps
for matplotlib. You can use Palettable to customize matplotlib plots or supply
colors for a web application.

%prep
%setup -q -n palettable-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license license.txt
%{python_sitelib}/*

%changelog
