#
# spec file for package python-zeroconf
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


%{?sle15_python_module_pythons}
Name:           python-zeroconf
Version:        0.136.0
Release:        0
Summary:        Pure Python Multicast DNS Service Discovery Library (Bonjour/Avahi compatible)
License:        LGPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/jstasiak/python-zeroconf
Source:         https://github.com/python-zeroconf/python-zeroconf/archive/refs/tags/%{version}.tar.gz
BuildRequires:  %{python_module async_timeout >= 4.0.1}
BuildRequires:  %{python_module ifaddr >= 0.1.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-async_timeout >= 4.0.1
Requires:       python-ifaddr >= 0.1.7
%python_subpackages

%description
This is a fork of pyzeroconf, a Multicast DNS Service Discovery for Python.
It is compatible with Bonjour and Avahi.
Compared to some other Zeroconf/Bonjour/Avahi Python packages, python-zeroconf
is not tied to Bonjour or Avahi, does not use D-Bus and
does not force you to use a particular event loop or python-twisted.

%prep
%autosetup -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand rm -f %{buildroot}%{$python_sitearch}/zeroconf/test.py
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
# Skip tests:
# - test_integration_with_listener_ipv6: Requires network access
# - test_launch*: Require network access
# - test_close_multiple_times: Requires network access
%pytest tests -k 'not (test_integration_with_listener_ipv6 or test_launch or test_close_multiple_times)'

%files %{python_files}
%doc README.rst
%license COPYING
%{python_sitearch}/zeroconf
%{python_sitearch}/zeroconf-%{version}.dist-info

%changelog
