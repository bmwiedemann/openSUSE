#
# spec file for package agama-yast
#
# Copyright (c) 2025 SUSE LLC
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


Name:           agama-yast
Version:        16
Release:        0
%define mod_name agama-yast
%define mod_full_name %{mod_name}-%{version}
BuildRequires:  dbus-1-common
# "msgfmt" tool
BuildRequires:  gettext-runtime
Requires:       dbus-1-common
Requires:       rubygem(agama-yast)

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5

URL:            https://github.com/agama-project/agama
Source:         %{mod_full_name}.gem
Source1:        po.tar.bz2
Source2:        install_translations.sh
Summary:        YaST integration service for Agama - common files
License:        GPL-2.0-only
Group:          Development/Languages/Ruby

%description
D-Bus service exposing some YaST features that are useful for Agama.

%prep
%{gem_unpack}

%build

%install
echo MODFULLNAME is %{mod_full_name}
env \
  SRCDIR=%{mod_full_name} \
  DESTDIR=%{buildroot} \
  datadir=%{_datadir} \
  unitdir=%{_unitdir} \
  %{mod_full_name}/install.sh

# run a script for installing the translations
sh "%{SOURCE2}" "%{SOURCE1}"

%pre
%service_add_pre agama.service
%service_add_pre agama-dbus-monitor.service

%post
%service_add_post agama.service
%service_add_post agama-dbus-monitor.service

%preun
%service_del_preun agama.service
%service_del_preun agama-dbus-monitor.service

%postun
%service_del_postun_with_restart agama.service
%service_del_postun_with_restart agama-dbus-monitor.service

%files
%{_datadir}/dbus-1/agama.conf
%dir %{_datadir}/dbus-1/agama-services
%{_datadir}/dbus-1/agama-services/org.opensuse.Agama*.service
%{_unitdir}/agama.service
%{_unitdir}/agama-dbus-monitor.service
%{_unitdir}/agama-proxy-setup.service
%dir %{_datadir}/agama
%dir %{_datadir}/agama/conf.d
%{_datadir}/agama/conf.d
%dir /usr/share/YaST2
/usr/share/YaST2/locale

%changelog
