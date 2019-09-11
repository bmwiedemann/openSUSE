#
# spec file for package obs-service-refresh_patches
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define service refresh_patches

Name:           obs-service-%{service}
Version:        0.3.9+git.1537184752.d624424
Release:        0
Summary:        An OBS source service: Refreshs local patches
License:        Apache-2.0
Group:          Development/Tools/Building
Url:            https://github.com/openSUSE/obs-service-%{service}
Source:         %{name}-%{version}.tar.gz
#NOTE(saschpe): Any Python will do:
Requires:       python
Requires:       quilt
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

It refreshes locals patches by using quilt.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 refresh_patches %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 refresh_patches.service %{buildroot}%{_prefix}/lib/obs/service

%files
%defattr(-,root,root)
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
