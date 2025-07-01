#
# spec file for package python-gitdb
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


%{?sle15_python_module_pythons}
Name:           python-gitdb
Version:        4.0.12
Release:        0
Summary:        Git Object Database
License:        BSD-3-Clause
URL:            https://github.com/gitpython-developers/gitdb
Source:         https://files.pythonhosted.org/packages/source/g/gitdb/gitdb-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module smmap >= 3.0.1}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-smmap >= 3.0.1
Provides:       python-gitdb2 = %{version}
Obsoletes:      python-gitdb2 < %{version}
BuildArch:      noarch
%python_subpackages

%description
GitDB is a pure-Python git object database

%prep
%setup -q -n gitdb-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
donttest="test_reading or test_writing or test_correctness or test_base"
donttest+=" or test_loose_correctness or test_pack_random_access"
donttest+=" or test_pack_writing or test_stream_reading"
%pytest -k "not ($donttest)"

%files %{python_files}
%license LICENSE
%doc AUTHORS
%{python_sitelib}/gitdb
%{python_sitelib}/gitdb-%{version}.dist-info

%changelog
