#
# spec file for package trytond_party
#
# Copyright (c) 2021 SUSE LLC
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


%define majorver 5.0
Name:           trytond_party
Version:        %{majorver}.4
Release:        0
Summary:        The "party" module for the Tryton ERP system
License:        GPL-3.0-only
Group:          Productivity/Office/Management
URL:            http://www.tryton.org/
Source:         http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz
Source2:        http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz.asc
Source3:        https://keybase.io/cedrickrier/pgp_keys.asc?fingerprint=7C5A4360F6DF81ABA91FD54D6FF50AFE03489130#/%{name}.keyring
# List of additional build dependencies
BuildRequires:  fdupes
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-python-stdnum
Requires:       trytond
Requires:       trytond_country
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
The party module defines the concepts of party, category and contact
mechanism in the Tryton application platform. It also comes with
reports to print labels and letters and a "Check VIES" wizard.

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
