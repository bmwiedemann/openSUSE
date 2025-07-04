#
# spec file for package python-netifaces
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2011 Novell
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
Name:           python-netifaces
Version:        0.11.0
Release:        0
Summary:        Portable network interface information
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/al45tair/netifaces
Source0:        https://files.pythonhosted.org/packages/source/n/netifaces/netifaces-%{version}.tar.gz
Source2:        https://raw.githubusercontent.com/al45tair/netifaces/master/test.py
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
%python_subpackages

%description
netifaces provides a (hopefully portable-ish) way for Python programmers to
get access to a list of the network interfaces on the local machine, and to
obtain the addresses of those network interfaces.

The package has been tested on Mac OS X, Windows XP, Windows Vista, Linux and
Solaris. On Windows, it is currently not able to retrieve IPv6 addresses,
owing to shortcomings of the Windows API.

It should work on other UNIX-like systems provided they implement either
getifaddrs() or support the SIOCGIFxxx socket options, although the data
provided by the socket options is normally less complete.

%prep
%setup -q -n netifaces-%{version}
cp %{SOURCE2} .

%build
%pyproject_wheel

%install
%pyproject_install

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python test.py | grep 'Interface lo'

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/netifaces.cpython*
%{python_sitearch}/netifaces-%{version}*-info

%changelog
