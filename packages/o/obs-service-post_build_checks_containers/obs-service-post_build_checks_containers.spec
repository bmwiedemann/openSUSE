#
# spec file for package obs-service-post_build_checks_container
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           obs-service-post_build_checks_containers
Version:        1.0
Release:        0
Summary:        Pulls in post-build-checks-containers BRP script
License:        GPL-2.0-only
Group:          Development/Tools/Building
URL:            http://www.suse.com/
Source0:        post_build_checks_containers
Source1:        post_build_checks_containers.service
BuildArch:      noarch
Requires:       post-build-checks-containers

%description
An OBS service that pulls in the post-build-checks-containers package
which uses brp scripts to scan containers.

%prep

%build

%install
install -d -m 0755 %{buildroot}%{_prefix}/lib/obs/service
install -D -m 0755 %{_sourcedir}/post_build_checks_containers \
    %{buildroot}%{_prefix}/lib/obs/service
install -D -m 0644 %{_sourcedir}/post_build_checks_containers.service \
    %{buildroot}%{_prefix}/lib/obs/service

%files
%dir %{_prefix}/lib/obs
%dir %{_prefix}/lib/obs/service
%{_prefix}/lib/obs/service/post_build_checks_containers
%{_prefix}/lib/obs/service/post_build_checks_containers.service

%changelog
