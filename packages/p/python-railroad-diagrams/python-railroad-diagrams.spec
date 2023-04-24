#
# spec file for package python-railroad-diagrams
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


%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-railroad-diagrams
Version:        1.1.1
Release:        0
Summary:        Railroad-Diagram Generator
License:        CC0-1.0
URL:            https://github.com/tabatkins/railroad-diagrams
Source0:        https://files.pythonhosted.org/packages/source/r/railroad-diagrams/railroad-diagrams-1.1.1.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This is a small library for generating railroad diagrams (like what JSON.org uses)
using SVG, with both JS and Python ports.

Railroad diagrams are a way of visually representing a grammar in a form that is more
readable than using regular expressions or BNF. They can easily represent any
context-free grammar, and some more powerful grammars. There are several railroad-diagram
generators out there, but none of them had the visual appeal I wanted, so I wrote my own.

%prep
%setup -q -n railroad-diagrams-%{version}

%build
%python_build

%install
%python_install

%files %{python_files}
%doc README.md
# For noarch packages: sitelib
%{python_sitelib}/*

%changelog
