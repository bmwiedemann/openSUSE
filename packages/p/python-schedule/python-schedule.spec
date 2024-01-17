#
# spec file for package python-schedule
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-schedule
Version:        1.1.0
Release:        0
Summary:        Job scheduling module for Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/dbader/schedule
Source:         https://files.pythonhosted.org/packages/source/s/schedule/schedule-%{version}.tar.gz
# https://github.com/dbader/schedule/issues/484
Patch0:         python-schedule-no-mock.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
An in-process scheduler for periodic jobs that uses the builder
pattern for configuration. Schedule lets the user run Python functions
(or any other callable) periodically at pre-determined intervals.

%prep
%autosetup -p1 -n schedule-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_until_time: https://github.com/dbader/schedule/issues/488
%pytest -k 'not test_until_time'

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
