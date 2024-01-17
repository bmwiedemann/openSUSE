#
# spec file for package obs-service-replace_using_env
#
# Copyright (c) 2021 SUSE LLC
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


Name:           obs-service-replace_using_env
Version:        0.1
Release:        0
Summary:        Service for variables substitution
License:        GPL-2.0-or-later
URL:            https://build.opensuse.org/
Source0:        replace_using_env
Source1:        replace_using_env.service
Source2:        README
Source3:        LICENSE
Requires:       bash
Requires:       sed
BuildArch:      noarch

%description
This service can be enabled to run during buildtime to replace the placeholders
in the specified files with the values from the build environment.

%prep
cp %{SOURCE2} .
cp %{SOURCE3} .

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 %{SOURCE0} %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/obs/service

%files
%license LICENSE
%doc README
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service

%changelog
