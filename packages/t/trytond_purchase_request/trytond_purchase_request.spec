#
# spec file for package trytond_purchase_request
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 Dr. Axel Braun
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

Name:           trytond_purchase_request
Version:        %{majorver}.1
Release:        0

Url:            http://www.tryton.org/
Source:         http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz
Summary:        Tryton is an OpenSource ERP system
License:        GPL-3.0-only
Group:          Productivity/Office/Management

BuildRequires:  python3-setuptools

BuildArch:      noarch

Requires:       trytond
Requires:       trytond_product
Requires:       trytond_purchase

%description
The purchase_request module of the Tryton application platform allows you to create a purchase request as pre-step for a purchase

%prep
%setup -q -n %{name}-%version

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%_prefix --root=%buildroot 

%files 
%defattr(-,root,root)
%{python3_sitelib}/*

%changelog
