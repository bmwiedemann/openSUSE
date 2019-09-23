#
# spec file for package python-netifaces
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-netifaces
Version:        0.10.9
Release:        0
Summary:        Portable network interface information
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/al45tair/netifaces
Source0:        https://pypi.io/packages/source/n/netifaces/netifaces-%{version}.tar.gz
# https://github.com/al45tair/netifaces/issues/40
Source1:        https://raw.githubusercontent.com/al45tair/netifaces/master/LICENSE
Source2:        https://raw.githubusercontent.com/al45tair/netifaces/master/test.py
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
cp %{SOURCE1} %{SOURCE2} .

%build
%python_build

%install
%python_install

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python test.py | grep 'Interface lo'

%files %{python_files}
%defattr(-,root,root,-)
%license LICENSE
%doc README.rst
%{python_sitearch}/*

%changelog
