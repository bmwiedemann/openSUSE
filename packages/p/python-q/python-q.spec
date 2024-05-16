#
# spec file for package python-q
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-q
Version:        2.7
Release:        0
Summary:        Quick-and-dirty debugging output for tired programmers
License:        Apache-2.0
URL:            https://github.com/zestyping/q
Source:         https://files.pythonhosted.org/packages/source/q/q/q-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Quick-and-dirty debugging output for tired programmers.

%prep
%setup -q -n q-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec test/test_basic.py

%files %{python_files}
%doc README.md
%{python_sitelib}/q.py
%pycache_only %{python_sitelib}/__pycache__/q.*.pyc
%{python_sitelib}/q-%{version}.dist-info

%changelog
