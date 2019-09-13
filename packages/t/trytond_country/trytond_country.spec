#
# spec file for package trytond_country
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014-2016 Dr. Axel Braun
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
Name:           trytond_country
Version:        %{majorver}.0
Release:        0
Summary:        The "country" module for the Tryton ERP system
License:        GPL-3.0-only
Group:          Productivity/Office/Management
Url:            http://www.tryton.org/
Source:         http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz
# List of additional build dependencies
BuildRequires:  fdupes
BuildRequires:  python3-setuptools
Requires:       proteus
Requires:       trytond
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
%description
The country module defines the concepts of country and subdivision in
the Tryton application platform. The module comes preloaded with the
ISO 3166 list of countries and subdivisions thanks to the pycountry
module.

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
%{_bindir}/trytond_import_zip

%changelog
