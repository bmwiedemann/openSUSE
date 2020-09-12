#
# spec file for package python3-susepubliccloudinfo
#
# Copyright (c) 2020 SUSE LLC
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


%define upstream_name susepubliccloudinfo
Name:           python3-susepubliccloudinfo
Version:        1.2.2
Release:        0
Summary:        Query SUSE Public Cloud Info Service
License:        GPL-3.0-or-later
Group:          System/Management
URL:            https://github.com/SUSE-Enceladus/public-cloud-info-client
Source0:        %{upstream_name}-%{version}.tar.bz2
Requires:       python3
Requires:       python3-docopt
Requires:       python3-lxml
Requires:       python3-requests
BuildRequires:  python3-setuptools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

Provides:       python-susepubliccloudinfo = %{version}
Obsoletes:      python-susepubliccloudinfo < %{version}

%description
Query the SUSE Public Cloud Information Service REST API

%prep
%setup -q -n %{upstream_name}-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
install -d -m 755 %{buildroot}/%{_mandir}/man1
install -m 644 man/man1/pint.1 %{buildroot}/%{_mandir}/man1
gzip %{buildroot}/%{_mandir}/man1/pint.1

%files
%defattr(-,root,root,-)
%license LICENSE
%{_mandir}/man1/*
%dir %{python3_sitelib}/susepubliccloudinfoclient
%{python3_sitelib}/*
%{_bindir}/pint

%changelog
