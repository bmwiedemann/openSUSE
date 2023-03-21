#
# spec file for package rubygem-d-installer
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-d-installer
Version:        0.8
Release:        0
%define mod_name d-installer
%define mod_full_name %{mod_name}-%{version}
# MANUAL
%global rb_build_versions %{rb_default_ruby}
BuildRequires:  dbus-1-common
Requires:       dbus-1-common
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.5.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            https://github.com/yast/d-installer
Source:         %{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        D-Installer Service
License:        GPL-2.0-only
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
System service for D-Installer, an experimental YaST-based installer.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  -f
# MANUAL
install -D -m 0644 %{buildroot}%{gem_base}/gems/%{mod_full_name}/share/dbus.conf %{buildroot}%{_datadir}/dbus-1/d-installer.conf
install --directory %{buildroot}%{_datadir}/dbus-1/d-installer-services
install -m 0644 --target-directory=%{buildroot}%{_datadir}/dbus-1/d-installer-services %{buildroot}%{gem_base}/gems/%{mod_full_name}/share/org.opensuse.DInstaller*.service
install -D -m 0644 %{buildroot}%{gem_base}/gems/%{mod_full_name}/share/systemd.service %{buildroot}%{_unitdir}/d-installer.service
install -D -m 0644 %{buildroot}%{gem_base}/gems/%{mod_full_name}/etc/d-installer.yaml %{buildroot}%{_sysconfdir}/d-installer.yaml
# /MANUAL

%gem_packages

%changelog
