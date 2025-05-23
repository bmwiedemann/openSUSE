#
# spec file for package python-tinyrecord
#
# Copyright (c) 2025 SUSE LLC
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


%global skip_python2 1
Name:           python-tinyrecord
Version:        0.2.0
Release:        0
Summary:        Atomic transactions for TinyDB
License:        MIT
URL:            https://github.com/eugene-eeo/tinyrecord
Source:         https://github.com/eugene-eeo/tinyrecord/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module tinydb}
BuildRequires:  %{python_module wheel}
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/tinyrecord
%{python_sitelib}/tinyrecord-%{version}.dist-info

%changelog
