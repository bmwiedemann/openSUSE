#
# spec file for package python-daemonize
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
Name:           python-daemonize
Version:        2.5.0
Release:        0
Summary:        Python module to launch code as a daemon process
License:        MIT
URL:            https://github.com/thesharp/daemonize
Source:         https://github.com/thesharp/daemonize/archive/v%{version}.tar.gz
Patch0:         no-python2.patch
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  procps
BuildRequires:  python-rpm-macros
BuildRequires:  user(nobody)
BuildArch:      noarch
%python_subpackages

%description
daemonize is a library for writing system daemons in Python.

%prep
%setup -q -n daemonize-%{version}
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/test.py

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
