#
# spec file for package python-pandocfilters
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
Name:           python-pandocfilters
Version:        1.4.2
Release:        0
Summary:        Python module for writing pandoc filters
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            http://github.com/jgm/pandocfilters
Source:         https://pypi.io/packages/source/p/pandocfilters/pandocfilters-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Recommends:     pandoc >= 1.16
BuildArch:      noarch

%python_subpackages

%description
Pandoc filters are pipes that read a JSON serialization of the 
Pandoc AST from stdin, transform it in some way, and write it 
to stdout. They can be used with pandoc (>= 1.12) either using
pipes.
pandoc -t json -s | ./caps.py | pandoc -f json
or using the --filter (or -F) command-line option.

%prep
%setup -q -n pandocfilters-%{version}
# Fix usr/bin/env call in example
sed -i 's/^#\!\/.*//g' examples/*.py

%build
%python_build

%install
%python_install

%files %{python_files}
%defattr(-,root,root,-)
%doc README README.rst 
%doc examples/
%license LICENSE
%{python_sitelib}/*

%changelog
