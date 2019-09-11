#
# spec file for package python-osmviz
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-osmviz
Version:        1.1.0
Release:        0
Summary:        An OpenStreetMap Visualization Toolkit for Python
License:        MIT
Group:          Development/Languages/Python
Url:            http://cbick.github.com/osmviz
Source:         https://files.pythonhosted.org/packages/source/o/osmviz/osmviz-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/hugovk/osmviz/%{version}/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pygame
Recommends:     python-Pillow
BuildArch:      noarch

%python_subpackages

%description
OSMViz is a small set of Python tools for retrieving and using Mapnik
tiles from a Slippy Map server (you may know these as OpenStreetMap
images).

%prep
%setup -q -n osmviz-%{version}
cp %{SOURCE10} .

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
