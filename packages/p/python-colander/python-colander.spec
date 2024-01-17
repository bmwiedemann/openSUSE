#
# spec file for package python-colander
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2013-2019 LISA GmbH, Bingen, Germany.
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
Name:           python-colander
Version:        2.0
Release:        0
Summary:        A schema-based serialization and deserialization library
License:        BSD-4-Clause AND ZPL-2.1 AND MIT
URL:            https://github.com/Pylons/colander
Source:         https://files.pythonhosted.org/packages/source/c/colander/colander-%{version}.tar.gz
BuildRequires:  %{python_module Babel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module translationstring}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-iso8601
Requires:       python-translationstring
Obsoletes:      python2-colander-doc
Obsoletes:      python2-colander-lang
Obsoletes:      python3-colander-doc
Obsoletes:      python3-colander-lang
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module hupper}
BuildRequires:  %{python_module iso8601}
BuildRequires:  %{python_module plaster-pastedeploy}
BuildRequires:  %{python_module plaster}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
An extensible package which can be used to:

- deserialize and validate a data structure composed of strings,
  mappings, and lists.

- serialize an arbitrary data structure to a data structure composed
  of strings, mappings, and lists.

%prep
%autosetup -p1 -n colander-%{version}

%build
%python_build

%install
%python_install
%find_lang colander
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst README.rst
%{python_sitelib}/colander*

%changelog
