#
# spec file for package python-nose-timer
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
Name:           python-nose-timer
Version:        0.7.5
Release:        0
Summary:        A timer plugin for nosetests
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/mahmoudimus/nose-timer
Source:         https://github.com/mahmoudimus/nose-timer/archive/v%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module parameterized}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-nose
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module nose}
# /SECTION
%python_subpackages

%description
A timer plugin for nosetests that answers the question:
how much time does every test take?

%prep
%setup -q -n nose-timer-%{version}
rm -rf nose_timer.egg-info

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand nosetests-%$python_bin_suffix 

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
