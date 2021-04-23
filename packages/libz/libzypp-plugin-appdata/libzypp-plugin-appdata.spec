#
# spec file for package libzypp-plugin-appdata
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


Name:           libzypp-plugin-appdata
Version:        1.0.1+git.20180426
Release:        0
Summary:        libzypp extension to handle AppStream metadata
License:        MIT AND CC0-1.0
Group:          System/Libraries
URL:            https://wiki.gnome.org/Design/Apps/Software
Source0:        openSUSE-appstream-%{version}.tar.xz
Source99:       libzypp-plugin-appdata-rpmlintrc
# appstreamcli is provided by the AppStream package. Let's pull it in when available, but ignore its absence
Recommends:     AppStream
# appstream-glib >= 0.3.6 is the first to correctly to appstream-util uninstall in /var/cache
Requires:       appstream-glib >= 0.3.6
# appdata hook was introduced in libzypp 14.29.4
Requires:       libzypp >= 14.29.4
# AsHelper is a python program with few dependencies
Requires:       python3-cmdln
Requires:       python3-createrepo_c
Requires(post): appstream-glib >= 0.3.6
# libzypp 16.13.1 was the version gaingin support for ZYPP_PLUGIN_APPDATA_FORCE_COLLECT
Requires(post): libzypp >= 16.13.1
Requires(post): python3-cmdln
Requires(post): python3-createrepo_c
Requires(post): zypper
# This is one way of providing valid appstream metadata to applications (currently the only implemented one)
Provides:       appstream-provider
BuildArch:      noarch

%description
This plugin extends libzypp to install AppStream metadata, as extracted from the
repository metadata, onto the file system in order to be picked up by
software centers.

%package -n openSUSE-appdata-extra
Summary:        Additional Appstream Metadata
License:        CC0-1.0
Group:          Metapackages

%description -n openSUSE-appdata-extra
This package contains extra appstream metadata to be used by appstream-builder

%prep
%setup -q -n openSUSE-appstream-%{version}

%build

%install
# install the additional appstream metadata
install -m 0755 -d %{buildroot}%{_datadir}/appdata-extra
cp appdata-extra/*/* %{buildroot}%{_datadir}/appdata-extra/

# Install AppData zypp plugin
install -Dm 0755 InstallAppdata.py %{buildroot}%{_prefix}/lib/zypp/plugins/appdata/InstallAppdata
install -Dm 0755 AsHelper.py %{buildroot}%{_prefix}/lib/AsHelper

# Install zypper helper command
install -Dm 0755 zypper-appstream-cache %{buildroot}%{_prefix}/lib/zypper/commands/zypper-appstream-cache

# Install the systemd service, which triggers when /var/cache/app-info/xmls does not yet exist during a boot
install -dm 0755 %{buildroot}%{_unitdir}
install -m 0644 appstream-sync-cache.service %{buildroot}%{_unitdir}

%preun
%service_del_preun appstream-sync-cache.service

%pre
%service_add_pre appstream-sync-cache.service

%post
%service_add_post appstream-sync-cache.service

%postun
%service_del_postun appstream-sync-cache.service

%files
# zypp plugin triggering AppData update on repo refresh
%dir %{_prefix}/lib/zypp
%dir %{_prefix}/lib/zypp/plugins
%dir %{_prefix}/lib/zypp/plugins/appdata/
%{_prefix}/lib/zypp/plugins/appdata/InstallAppdata
%dir %{_prefix}/lib/zypper
%dir %{_prefix}/lib/zypper/commands
%{_prefix}/lib/zypper/commands/zypper-appstream-cache
%{_prefix}/lib/AsHelper
%{_unitdir}/appstream-sync-cache.service

%files -n openSUSE-appdata-extra
%{_datadir}/appdata-extra/

%changelog
