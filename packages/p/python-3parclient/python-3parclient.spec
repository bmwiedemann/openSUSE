#
# spec file for package python-3parclient
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           python-3parclient
Version:        4.2.5
Release:        0
Summary:        3PAR HTTP REST Client
License:        Apache-2.0
Group:          Development/Languages/Python
Url:            http://pypi.python.org/pypi/3parclient
Source:         https://files.pythonhosted.org/packages/source/p/python-3parclient/python-3parclient-%{version}.tar.gz
BuildRequires:  python-devel
BuildRequires:  python-eventlet
BuildRequires:  python-paramiko
BuildRequires:  python-requests
BuildRequires:  python-setuptools
#BuildRequires:  python-nose
Requires:       python-eventlet
Requires:       python-paramiko
Requires:       python-requests
Provides:       python-hp3parclient = %version
Obsoletes:      python-hp3parclient < %version
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif

%description
This is a Client library that can talk to the HP 3PAR Storage array.  The 3PAR
storage array has a REST web service interface and a command line interface.
This client library implements a simple interface for talking with either
interface, as needed.  The python httplib2 library is used to communicate
with the REST interface.  The python paramiko library is used to communicate
with the command line interface over an SSH connection.

This branch requires 3.1.3 version MU1 of the 3PAR firmware.
File Persona capabilities require 3PAR firmware 3.2.1 Build 46 or later.

%prep
%setup -q -n python-3parclient-%{version}

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}
rm -rf %{buildroot}/%{python_sitelib}/test/

%files
%defattr(-,root,root,-)
%doc README.rst
%{python_sitelib}/*

%changelog
