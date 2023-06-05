#
# spec file for package obs-service-download_assets
#
# Copyright (c) 2023 SUSE LLC
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


Name:           obs-service-download_assets
Version:        0.2
Release:        0
Summary:        An OBS source service: Wrapper for download_assets
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            http://build.opensuse.org/
Requires:       build >= 20220221
Source1:        download_assets
Source2:        download_assets.service
Source3:        download_assets.rc
Source4:        clean_assets
Source5:        clean_assets.service
Source10:       COPYING
Source11:       README.md
BuildArch:      noarch

%description
A small wrapper to make download_assets from the build script usable
via a source service.

%prep
%setup -n %_sourcedir -D -T 0

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 %{S:1} %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 %{S:2} %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 %{S:4} %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 %{S:5} %{buildroot}%{_prefix}/lib/obs/service

mkdir -p %{buildroot}%{_sysconfdir}/obs/services
install -m 0644 %{S:3} %{buildroot}%{_sysconfdir}/obs/services

%files
%license COPYING
%doc README.md
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service
%dir %{_sysconfdir}/obs
%dir %{_sysconfdir}/obs/services
%config(noreplace) %{_sysconfdir}/obs/services/*

%changelog
