#
# spec file for package proteus
#
# Copyright (c) 2019 SUSE LLC
# Copyright (c) 2019 Dr. Axel Braun
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


%define majorver 5.0
Name:           proteus
Version:        %{majorver}.7
Release:        0
Summary:        A library to access Tryton's modules like a client
License:        GPL-3.0-or-later
Group:          Productivity/Office/Management
URL:            http://www.tryton.org/
Source0:        http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz
# List of additional build dependencies
BuildRequires:  fdupes
BuildRequires:  python3-devel
BuildRequires:  python3-lxml
BuildRequires:  python3-psycopg2
BuildRequires:  python3-pydot
BuildRequires:  python3-setuptools
Requires:       python3-dateutil
##equires:	python3-cdecimal
##Requires:	python3-simplejson
Requires:       trytond
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Proteus allows you to access Tryton's modules like a client. Useful for automation, data load etc.

%prep
%setup -q 

%build 
python3 setup.py build

%install
python3 setup.py install --prefix=%_prefix --root=%buildroot 
%fdupes -s %{buildroot}

%files 
%defattr(-,root,root)
%doc README LICENSE
%{python_sitelib}/*

%changelog
