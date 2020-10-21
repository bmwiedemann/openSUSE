#
# spec file for package trytond_account
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016 Dr. Axel Braun
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


%define majorver 5.0
Name:           trytond_account
Version:        %{majorver}.15
Release:        0
Summary:        The "account" module for the Tryton ERP system
License:        GPL-3.0+
Group:          Productivity/Office/Management
Url:            http://www.tryton.org/
Source:         http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:	python3-setuptools 
Requires:       trytond 
Requires:       trytond_company 
Requires:	trytond_currency 
Requires:	trytond_party
BuildArch:      noarch

%description
The accounting module of the Tryton application platform.
It defines fundamentals for most of accounting needs, such as fiscal year,
period, account type, journal, tax code and more.

%prep
%setup -q 

%build
python3 setup.py build
    
%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%fdupes -s %{buildroot}

%files 
%defattr(-,root,root)
%{python3_sitelib}/*

%changelog
