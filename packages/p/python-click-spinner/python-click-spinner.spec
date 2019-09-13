#
# spec file for package python-click-spinner
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-click-spinner
# tests and LICENSE included in sdist 0.1.9 not yet released
Version:        0.1.8
Release:        0
License:        MIT
Summary:        Spinner for Click
Url:            https://github.com/click-contrib/click-spinner
Group:          Development/Languages/Python
Source:         https://github.com/click-contrib/click-spinner/archive/v%{version}.tar.gz#/click-spinner-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/click-contrib/click-spinner/master/LICENSE
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  fdupes
Requires:       python-click
BuildArch:      noarch

%python_subpackages

%description
Spinner for Click.

%prep
%setup -q -n click-spinner-%{version}
cp %{SOURCE1} .

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%python_exec setup.py pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
