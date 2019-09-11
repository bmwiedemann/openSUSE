#
# spec file for package python-svgwrite
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
Name:           python-svgwrite
Version:        1.3.1
Release:        0
Summary:        Python module for creating SVG drawings
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/mozman/svgwrite
Source:         https://files.pythonhosted.org/packages/source/s/svgwrite/svgwrite-%{version}.zip
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-pyparsing >= 2.0.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pyparsing >= 2.0.1}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A Python library to create SVG drawings.

%prep
%setup -q -n svgwrite-%{version}
find svgwrite -name "*.py" -exec sed -i -e '/^#!\//, 1d' {} \; -exec sed -i 's/\r$//' {} \;
sed -i 's/\r$//' LICENSE.TXT NEWS.rst README.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_embed_google_web_font - asks google for data
%pytest -k 'not test_embed_google_web_font'

%files %{python_files}
%doc NEWS.rst README.rst
%license LICENSE.TXT
%{python_sitelib}/*

%changelog
