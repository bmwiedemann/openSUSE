#
# spec file for package python-crashtest
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
%define skip_python2 1
Name:           python-crashtest
Version:        0.3.1
Release:        0
Summary:        Manage Python errors with ease
License:        MIT
Group:          Development/Languages/Python
URL:            https://pypi.org/project/crashtest
Source:         https://github.com/sdispater/crashtest/archive/%{version}.tar.gz#/crashtest-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-dephell-rpm-macros
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Manage Python errors with ease.

%prep
%setup -q -n crashtest-%{version}
%dephell_gensetup

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
