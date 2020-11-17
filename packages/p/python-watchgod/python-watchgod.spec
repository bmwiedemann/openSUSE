#
# spec file for package python-watchgod
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
Name:           python-watchgod
Version:        0.6
Release:        0
Summary:        Python file watching and code reload
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/samuelcolvin/watchgod
Source:         https://github.com/samuelcolvin/watchgod/archive/v%{version}.tar.gz#/watchgod-%{version}.tar.gz
BuildRequires:  %{python_module pytest-aiohttp >= 0.3.0}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest-toolbox}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Simple, modern file watching and code reload in Python.

watchgod is inspired by watchdog, hence the name, but tries to fix
29-some of the frustrations I found with watchdog, namely: separate
approaches for each OS, an inelegant approach to 30-concurrency using
threading, challenges around debouncing changes and bugs which weren't
being fixed.

%prep
%setup -q -n watchgod-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/watchgod
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative watchgod

%postun
%python_uninstall_alternative watchgod

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*
%python_alternative %{_bindir}/watchgod

%changelog
