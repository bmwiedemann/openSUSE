#
# spec file for package trytond_purchase_request
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2017-2024 Dr. Axel Braun
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


%if 0%{?suse_version} >= 1550
%define pythons python3
%define mypython python3
%define mysitelib %python3_sitelib
%else
%{?sle15_python_module_pythons}
%define mypython %pythons
%define mysitelib %{expand:%%%{mypython}_sitelib}
%endif

%define majorver 7.0
Name:           trytond_purchase_request
Version:        %{majorver}.1
Release:        0

URL:            http://www.tryton.org/
Source:         http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz
## Source2:        http://downloads.tryton.org/%{majorver}/%{name}-%{version}.tar.gz.asc
## Source3:        https://keybase.io/cedrickrier/pgp_keys.asc?fingerprint=7C5A4360F6DF81ABA91FD54D6FF50AFE03489130#/%{name}.keyring
Summary:        Tryton module for purchase requests
License:        GPL-3.0-only
Group:          Productivity/Office/Management

BuildRequires:  %{mypython}-devel
BuildRequires:  %{mypython}-pip
BuildRequires:  %{mypython}-setuptools
BuildRequires:  %{mypython}-wheel
BuildRequires:  fdupes
BuildRequires:  python-rpm-generators
BuildRequires:  python-rpm-macros

Requires:       trytond
Requires:       trytond_product
Requires:       trytond_purchase

BuildArch:      noarch

%description
The purchase_request module of the Tryton application platform allows you to create a purchase request as pre-step for a purchase

%prep
%setup -q

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{mysitelib}

%files
%defattr(-,root,root)
%{mysitelib}/tryton*

%changelog
