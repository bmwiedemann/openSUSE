#
# spec file for package proteus
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017-2018 Dr. Axel Braun
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


%define majorver 4.6
Name:           proteus
Version:        %{majorver}.6
Release:        0
Summary:        A library to access Tryton's modules like a client
License:        GPL-3.0-or-later
Group:          Productivity/Office/Management
Url:            http://www.tryton.org/
Source0:        http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz
# List of additional build dependencies
BuildRequires:  fdupes
BuildRequires:  python-devel
BuildRequires:  python-lxml
BuildRequires:  python-psycopg2
BuildRequires:  python-pydot
BuildRequires:  python-setuptools
Requires:       python-cdecimal
Requires:       python-dateutil
Requires:       python-simplejson
Requires:       trytond
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Proteus allows you to access Tryton's modules like a client. Useful for automation, data load etc.

%prep
%setup -q 

%build 
python setup.py build

%install
python setup.py install --prefix=%_prefix --root=%buildroot 
%fdupes -s %{buildroot}

%files 
%defattr(-,root,root)
%doc README 
%license LICENSE
%{python_sitelib}/*

%changelog
