#
# spec file for package python-sas7bdat
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-sas7bdat
Version:        2.2.3
Release:        0
Summary:        A sas7bdat file reader for Python
License:        MIT
Group:          Development/Languages/Python
Url:            https://bitbucket.org/jaredhobbs/sas7bdat
Source:         https://files.pythonhosted.org/packages/source/s/sas7bdat/sas7bdat-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.8.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six >= 1.8.0
BuildArch:      noarch

%python_subpackages

%description
This module will read sas7bdat files using pure Python (2.6+, 3+). No SAS software
required! The module started out as a port of the R script of the same name
found here: <https://github.com/BioStatMatt/sas7bdat> but has since been
completely rewritten.

Also included with this library is a simple command line script,
`sas7bdat_to_csv`, which converts sas7bdat files to csv files. It will also
print out header information and meta data using the `--header` option and it
will batch convert files as well. Use the `--help` option for more information.

%prep
%setup -q -n sas7bdat-%{version}
sed -i 's/\r$//' README.md

%build
%python_build

%install
%python_install

%{python_expand sed -i "s|^#!/usr/bin/env python$|#!%__$python|" %{buildroot}%{$python_sitelib}/sas7bdat.py
chmod a+x %{buildroot}%{$python_sitelib}/sas7bdat.py
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{$python_sitelib}
}

%files %{python_files}
%doc README.md
%license LICENSE
%python3_only %{_bindir}/sas7bdat_to_csv
%{python_sitelib}/*

%changelog
