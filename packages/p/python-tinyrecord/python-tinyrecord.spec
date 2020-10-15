#
# spec file for package python-tinyrecord
#
# Copyright (c) 2020 SUSE LLC
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
%global skip_python2 1
Name:           python-tinyrecord
Version:        0.2.0
Release:        0
Summary:        Atomic transactions for TinyDB
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/eugene-eeo/tinyrecord
Source:         https://github.com/eugene-eeo/tinyrecord/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tinydb}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-tinydb
BuildArch:      noarch

%python_subpackages

%description
Atomic transactions for TinyDB.

%prep
%setup -q -n tinyrecord-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
