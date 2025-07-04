#
# spec file for package python-pamela
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


Name:           python-pamela
Version:        1.2.0
Release:        0
Summary:        PAM interface using ctypes
License:        MIT
URL:            https://github.com/minrk/pamela
Source:         https://github.com/minrk/pamela/archive/%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
PAM interface using ctypes.

%prep
%setup -q -n pamela-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_session seems to need root
%pytest -k 'not test_session'

%files %{python_files}
%doc README.md
%license COPYING
%{python_sitelib}/pamela.py
%pycache_only %{python_sitelib}/__pycache__/pamela.*.pyc
%{python_sitelib}/pamela-%{version}.dist-info

%changelog
