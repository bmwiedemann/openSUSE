#
# spec file for package python-positional
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-positional
Version:        1.2.1
Release:        0
Summary:        Library to enforce positional or key-word arguments
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/morganfainberg/positional
Source:         https://files.pythonhosted.org/packages/source/p/positional/positional-%{version}.tar.gz
BuildRequires:  %{python_module dbm}
BuildRequires:  %{python_module pbr}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dbm
Requires:       python-wrapt
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module testrepository >= 0.0.18}
BuildRequires:  %{python_module testresources >= 0.2.4}
BuildRequires:  %{python_module testtools >= 1.4.0}
BuildRequires:  %{python_module wrapt}
# /SECTION
%python_subpackages

%description
`positional` provides a decorator which enforces only some args may be passed
positionally. The idea and some of the code was taken from the oauth2 client
of the google-api client.

%prep
%setup -q -n positional-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v positional/tests/

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/positional
%{python_sitelib}/positional*egg-info

%changelog
