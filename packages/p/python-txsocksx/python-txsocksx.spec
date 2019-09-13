#
# spec file for package python-txsocksx
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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
#


%define oname   txsocksx

Name:           python-txsocksx
Version:        1.15.0.2
Release:        0
Summary:        Twisted client endpoints for SOCKS{4,4a,5}
License:        ISC
Group:          Productivity/Networking/Security
Url:            https://github.com/habnabit/txsocksx
Source0:        https://pypi.python.org/packages/source/t/%{oname}/%{oname}-%{version}.tar.gz
BuildRequires:  python-Parsley
BuildRequires:  python-Twisted
BuildRequires:  python-devel
BuildRequires:  python-setuptools
BuildRequires:  python-vcversioner
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif

%description
txsocksx is SOCKS4/4a and SOCKS5 client endpoints for Twisted 10.1
or greater.

%prep
%setup -q -n %{oname}-%{version}

# Remove not needed files
sed -i "s|, 'txsocksx.test'||" setup.py

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%defattr(-,root,root,-)
%doc examples COPYING README.rst
%{python_sitelib}/%{oname}
%{python_sitelib}/%{oname}-%{version}-py%{py_ver}.egg-info

%changelog
