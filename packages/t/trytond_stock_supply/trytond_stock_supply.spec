#
# spec file for package trytond_stock_supply
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2014-2017 Dr. Axel Braun
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


%define 		majorver 5.0
Name:           trytond_stock_supply
Version:        %{majorver}.6
Release:        0
Summary:        The Stock Supply module for the Tryton ERP system
License:        GPL-3.0-only
Group:          Productivity/Office/Management
URL:            http://www.tryton.org/
Source:         http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz
# List of additional build dependencies
BuildRequires:  fdupes
BuildRequires:  python3-setuptools
Requires:       trytond
Requires:       trytond_account
Requires:       trytond_party
Requires:       trytond_product
Requires:       trytond_purchase
Requires:       trytond_stock
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The Stock Supply module adds automatic supply mechanisms and
introduce the concepts of order point and purchase request into the
Tryton application platform.

%prep
%setup -q 

%build
python3 setup.py build   

%install
python3 setup.py install --prefix=%_prefix --root=%buildroot 
%fdupes -s %{buildroot}

%files 
%defattr(-,root,root)
%{python3_sitelib}/*

%changelog
