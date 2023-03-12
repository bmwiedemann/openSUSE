#
# spec file for package trytond_purchase
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014-2021 Dr. Axel Braun
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

%define majorver 6.0
Name:           trytond_purchase
Version:        %{majorver}.10
Release:        0
Summary:        The "purchase" module for the Tryton ERP system
License:        GPL-3.0
Group:          Productivity/Office/Management
Url:            http://www.tryton.org/
Source:         http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz
Source2:        http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz.asc
Source3:        https://keybase.io/cedrickrier/pgp_keys.asc?fingerprint=7C5A4360F6DF81ABA91FD54D6FF50AFE03489130#/%{name}.keyring
BuildRequires:  fdupes
BuildRequires:  python3-setuptools 
Requires:       trytond
Requires:       trytond_account 
Requires:       trytond_account_invoice
Requires:       trytond_account_product
Requires:       trytond_company 
Requires:       trytond_currency
Requires:       trytond_party
Requires:       trytond_product
Requires:       trytond_stock
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The purchase module defines the Purchase model in the Tryton
application platform. The purchase is mainly defined by a party from
which the products will be purchased and a list of purchase lines,
each one containing a product and a quantity.

%prep
%setup -q 

%build
%python3_build   

%install
%python3_install --prefix=%_prefix --root=%buildroot 
%fdupes -s %{buildroot}

%files 
%defattr(-,root,root)
%{python3_sitelib}/*

%changelog
