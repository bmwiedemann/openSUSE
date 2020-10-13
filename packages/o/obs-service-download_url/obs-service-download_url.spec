#
# spec file for package obs-service-download_url
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


Name:           obs-service-download_url
Summary:        An OBS source service: curl download tool
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            http://openbuildservice.org
Version:        0.1.3
Release:        0
Source:         %name-%version.tar.gz
Requires:       wget
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

It supports downloading files from given URLs via curl

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/lib/obs/service
install -m 0755 download_url         %{buildroot}/usr/lib/obs/service
install -m 0644 download_url.service %{buildroot}/usr/lib/obs/service

%files
%defattr(-,root,root)
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
