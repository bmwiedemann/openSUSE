#
# spec file for package icewm-theme-branding
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


%define _name   icewm-config-openSUSE
Name:           icewm-theme-branding
Version:        1.2.4
Release:        0
Summary:        Icewm theme branding for SLES or openSUSE
License:        LGPL-2.1-or-later AND GPL-3.0-or-later
URL:            https://github.com/openSUSE/icewm-config-openSUSE
Source:         https://github.com/openSUSE/%{_name}/archive/%{_name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM add-adwaita-legacy-iconpath-to-preference.patch bsc#1157930 gh#openSUSE/icewm-config-openSUSE!8 yfjiang@suse.com -- Add the adwaita legacy path to the IconPath
Patch0:         add-adwaita-legacy-iconpath-to-preference.patch
Requires:       icewm
Conflicts:      icewm < 1.3.11
Conflicts:      icewm-configuration-files
Provides:       icewm-configuration-files = %{version}
BuildArch:      noarch

%description
This package is made for SLE or openSUSE customization of icewm, including
the system default theme,background etc.

%prep
%setup -q -n %{_name}-%{_name}-%{version}
%patch0 -p1

%build
%if 0%{?is_opensuse}
sed -i -e 's:SLEdefault:openSUSEdefault:g' preferences
%endif

%install
make DESTDIR=%{buildroot} prefix=%{_prefix} install
# move preferences to prefoverride to take preference over themes
mv %{buildroot}/%{_sysconfdir}/icewm/preferences \
   %{buildroot}/%{_sysconfdir}/icewm/prefoverride

%files
%license LICENSE.GPL-2.0 LICENSE.LGPL-2.1 LICENSE.MIT
%dir %{_sysconfdir}/icewm
%config %{_sysconfdir}/icewm/keys
%config %{_sysconfdir}/icewm/menu
%config %{_sysconfdir}/icewm/prefoverride
%config %{_sysconfdir}/icewm/startup
%config %{_sysconfdir}/icewm/theme
%config %{_sysconfdir}/icewm/toolbar
%config %{_sysconfdir}/icewm/winoptions
%dir %{_datadir}/icewm/
%dir %{_datadir}/icewm/themes/
%dir %{_datadir}/icewm/themes/zpaker/
%{_datadir}/icewm/themes/zpaker/*

%changelog
