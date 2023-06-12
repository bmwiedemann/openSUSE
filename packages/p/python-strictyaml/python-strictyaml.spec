#
# spec file for package python-strictyaml
#
# Copyright (c) 2022 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-strictyaml
Version:        1.6.2
Release:        0
Summary:        Strict, typed YAML parser
License:        MIT
URL:            https://hitchdev.com/strictyaml
Source:         https://files.pythonhosted.org/packages/source/s/strictyaml/strictyaml-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-dateutil >= 2.6.0
BuildArch:      noarch
# SECTION test requirements
# BuildRequires:  %{python_module pytest}
# BuildRequires:  %{python_module python-dateutil >= 2.6.0}
# /SECTION
%python_subpackages

%description
StrictYAML is a type-safe YAML parser that parses and validates a
restricted subset of the YAML specification.

Priorities:

 * No parsing of hard to read and insecure features of YAML like the
   Norway problem.
 * Strict validation of markup and straightforward type casting.
 * Acting as a near-drop in replacement for pyyaml, ruamel.yaml or poyo.
 * Comment preservation across a read-write cycle
 * Speed is not a key concern

%prep
%setup -q -n strictyaml-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

#%%check
# Not feasible due to extensive number of test dependencies
# and they are not suited for rpmbuild
# https://github.com/hitchdev/hitchkey/issues/2

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/*

%changelog
