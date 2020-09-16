#
# spec file for package python-zeroconf
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
Name:           python-zeroconf
Version:        0.28.3
Release:        0
Summary:        Pure Python Multicast DNS Service Discovery Library (Bonjour/Avahi compatible)
License:        LGPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/jstasiak/python-zeroconf
Source:         https://github.com/jstasiak/python-zeroconf/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module ifaddr >= 0.1.7}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ifaddr >= 0.1.7
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

%build
%python_build

%install
%python_install
%python_expand rm -f %{buildroot}%{$python_sitelib}/zeroconf/test.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest zeroconf/test.py -k 'not (test_integration_with_listener_ipv6 or test_launch)'

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitelib}/zeroconf*

%changelog
