#
# spec file for package python-warlock
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
Name:           python-warlock
Version:        1.3.3
Release:        0
Summary:        Python object model built on top of JSON schema
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            http://github.com/bcwaldon/warlock
Source:         https://files.pythonhosted.org/packages/source/w/warlock/warlock-%{version}.tar.gz
BuildRequires:  %{python_module jsonpatch >= 0.7}
BuildRequires:  %{python_module jsonschema >= 0.10}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jsonpatch >= 0.7
Requires:       python-jsonschema >= 0.10
Requires:       python-six
BuildArch:      noarch
%python_subpackages

%description
Build self-validating python objects using JSON schemas

%prep
%setup -q -n warlock-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests are not distributed by upstream and github does not
# use setuptools anymore

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
