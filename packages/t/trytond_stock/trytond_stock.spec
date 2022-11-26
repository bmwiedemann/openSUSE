#
# spec file for package trytond_stock
#
# Copyright (c) 2022 SUSE LLC
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define majorver 6.0
Name:           trytond_stock
Version:        %{majorver}.18
Release:        0
Summary:        The "stock" module for the Tryton ERP system
License:        GPL-3.0-only
Group:          Productivity/Office/Management
URL:            http://www.tryton.org/
Source:         http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz
Source2:        http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz.asc
Source3:        https://keybase.io/cedrickrier/pgp_keys.asc?fingerprint=7C5A4360F6DF81ABA91FD54D6FF50AFE03489130#/%{name}.keyring
BuildRequires:  fdupes
BuildRequires:  python3-setuptools
Requires:       trytond
Requires:       trytond_company
Requires:       trytond_currency
Requires:       trytond_party
Requires:       trytond_product

BuildArch:      noarch

%description
The stock module defines fundamentals for all stock management
situations: Locations where product are stored, moves between these
locations, shipments for product arrivals and departures and
inventory to control and update stock levels.

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
