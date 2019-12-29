#
# spec file for package python-zeroconf
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
%define skip_python2 1
Name:           python-zeroconf
Version:        0.24.3
Release:        0
Summary:        Pure Python Multicast DNS Service Discovery Library (Bonjour/Avahi compatible)
License:        LGPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/jstasiak/python-zeroconf
Source:         https://github.com/jstasiak/python-zeroconf/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         python-zeroconf-disable-some-tests.patch
BuildRequires:  %{python_module ifaddr}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ifaddr
BuildArch:      noarch
%python_subpackages

%description
This is a fork of pyzeroconf, a Multicast DNS Service Discovery for Python.
It is compatible with Bonjour and Avahi.
Compared to some other Zeroconf/Bonjour/Avahi Python packages, python-zeroconf
is not tied to Bonjour or Avahi, does not use D-Bus and
does not force you to use a particular event loop or python-twisted.

%prep
%setup -q
%patch0 -p1

%build
%python_build

%install
%python_install
%python_expand rm -f %{buildroot}%{$python_sitelib}/zeroconf/test.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests that do not run in an OBS chroot are disabled via python-zeroconf-disable-some-tests.patch
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} %python_exec -m unittest discover -v

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitelib}/zeroconf*

%changelog
