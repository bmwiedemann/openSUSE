#
# spec file for package python-warlock
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


Name:           python-warlock
Version:        2.0.1
Release:        0
Summary:        Python object model built on top of JSON schema
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/bcwaldon/warlock
Source:         https://github.com/bcwaldon/warlock/archive/%{version}.tar.gz#/warlock-%{version}.tar.gz
BuildRequires:  %{python_module jsonpatch >= 1}
BuildRequires:  %{python_module jsonschema >= 4}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jsonpatch >= 1
Requires:       python-jsonschema >= 4
BuildArch:      noarch
%python_subpackages

%description
Build self-validating python objects using JSON schemas.

%prep
%setup -q -n warlock-%{version}
rm pytest.ini

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/warlock
%{python_sitelib}/warlock-%{version}.dist-info

%changelog
