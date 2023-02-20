#
# spec file for package trytond_purchase_request
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2017-2021 Dr. Axel Braun
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
Name:           trytond_purchase_request
Version:        %{majorver}.4
Release:        0

URL:            http://www.tryton.org/
Source:         http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz
Source2:        http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz.asc
Source3:        https://keybase.io/cedrickrier/pgp_keys.asc?fingerprint=7C5A4360F6DF81ABA91FD54D6FF50AFE03489130#/%{name}.keyring
Summary:        Tryton module for purchase requests
License:        GPL-3.0-only
Group:          Productivity/Office/Management

BuildRequires:  fdupes
BuildRequires:  python3-setuptools

Requires:       trytond
Requires:       trytond_product
Requires:       trytond_purchase

BuildArch:      noarch

%description
The purchase_request module of the Tryton application platform allows you to create a purchase request as pre-step for a purchase

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
