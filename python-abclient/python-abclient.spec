#
# spec file for package python-abclient
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
Name:           python-abclient
Version:        0.2.3
Release:        0
Summary:        Python client library for EISOO AnyBackup API
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://global.eisoo.com/
Source:         https://files.pythonhosted.org/packages/source/a/abclient/abclient-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-oslo.log >= 1.14.0
Requires:       python-oslo.utils >= 3.16.0
Requires:       python-requests >= 2.10.0
BuildArch:      noarch
%python_subpackages

%description
abclient: Python library for EISOO AnyBackup APIs

%prep
%setup -q -n abclient-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no testsuite found

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
