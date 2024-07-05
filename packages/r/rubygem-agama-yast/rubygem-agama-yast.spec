#
# spec file for package rubygem-agama-yast
#
# Copyright (c) 2024 SUSE LLC
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

Name:           rubygem-agama-yast
Version:        9
Release:        0
%define mod_name agama-yast
%define mod_full_name %{mod_name}-%{version}
# MANUAL
%global rb_build_versions %{rb_default_ruby}
BuildRequires:  dbus-1-common
# "msgfmt" tool
BuildRequires:  gettext-runtime
Requires:       dbus-1-common
# /MANUAL
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.5.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
URL:            https://github.com/openSUSE/agama
Source:         %{mod_full_name}.gem
Source1:        po.tar.bz2
Source2:        install_translations.sh
Source3:        gem2rpm.yml
Summary:        YaST integration service for Agama
License:        GPL-2.0-only
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
D-Bus service exposing some YaST features that are useful for Agama.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  -f
# MANUAL
install -D -m 0644 %{buildroot}%{gem_base}/gems/%{mod_full_name}/share/dbus.conf %{buildroot}%{_datadir}/dbus-1/agama.conf
install --directory %{buildroot}%{_datadir}/dbus-1/agama-services
install -m 0644 --target-directory=%{buildroot}%{_datadir}/dbus-1/agama-services %{buildroot}%{gem_base}/gems/%{mod_full_name}/share/org.opensuse.Agama*.service
install -D -m 0644 %{buildroot}%{gem_base}/gems/%{mod_full_name}/share/agama.service %{buildroot}%{_unitdir}/agama.service
install -D -m 0644 %{buildroot}%{gem_base}/gems/%{mod_full_name}/share/agama-proxy-setup.service %{buildroot}%{_unitdir}/agama-proxy-setup.service
install --directory %{buildroot}/usr/share/agama/conf.d
install -D -m 0644 %{buildroot}%{gem_base}/gems/%{mod_full_name}/conf.d/*.yaml %{buildroot}/usr/share/agama/conf.d/
# run a script for installing the translations
sh "%{SOURCE2}" "%{SOURCE1}"
# /MANUAL

%pre
%service_add_pre agama.service

%post
%service_add_post agama.service

%preun
%service_del_preun agama.service

%postun
%service_del_postun_with_restart agama.service

%gem_packages

%changelog
