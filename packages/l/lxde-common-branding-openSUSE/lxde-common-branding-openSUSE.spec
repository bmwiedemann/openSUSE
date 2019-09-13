#
# spec file for package lxde-common-branding-openSUSE
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define	upstream_ver 0.99.0
Name:           lxde-common-branding-openSUSE
Version:        12.1
Release:        0
Summary:        openSUSE branding for LXDE
License:        GPL-2.0
Group:          System/GUI/LXDE
Url:            http://www.opensuse.org
Source0:        lxde-common-%{upstream_ver}.tar.xz
Source1:        start-here-branding.svg
Source2:        suse-logout.png
Patch0:         lxde-common-0.99.0-pcmanfm-default.patch
Patch1:         lxde-common-0.99.0-openbox-menu.patch
Patch2:         lxde-common-0.99.0-lxpanel.patch
Patch3:         lxde-common-0.99.0-lxde-logout.patch
Patch4:         lxde-common-0.99.0-openbox-shortcut.patch
Patch5:			lxde-common-0.99.0-use-Adwaita-as-default-theme.patch
# Apply after lxde-common-0.99.0-use-Adwaita-as-default-theme.patch
Patch6:			lxde-common-0.99.0-openbox-titlebar-font.patch
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  update-desktop-files
Requires:       desktop-data-openSUSE
Requires:       wallpaper-branding-openSUSE
Requires:		gtk2-metatheme-adwaita
Requires:		gtk3-metatheme-adwaita
Requires:		openbox-adwaita-ob-theme
# asigned to C-A-Escape in lxde-common-0.5.5-openbox-shortcut.patch but not installed by default
Requires:		xkill
Supplements:    packageand(lxde-common:branding-openSUSE)
Provides:       lxde-common-branding = %{version}
BuildRoot:      %{tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Conflicts:      otherproviders(lxde-common-branding)

%description
This branding-style package sets openSUSE style improvements into LXDE.
You should always prefer branding-openSUSE packages to branding-upstream.

%prep
%setup -q -n lxde-common-%{upstream_ver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
# keep enable-man even if not needed or make will fail
%configure --enable-man
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
cp %{SOURCE1} %{buildroot}/%{_datadir}/lxde/images/
cp %{SOURCE2} %{buildroot}/%{_datadir}/lxde/images/

#delete not branding files
rm -rf %{buildroot}/%{_datadir}/xsessions
rm -rf %{buildroot}/%{_bindir}/openbox-lxde
rm -rf %{buildroot}/%{_bindir}/startlxde
rm -rf %{buildroot}/%{_datadir}/lxde/wallpapers
rm -rf %{buildroot}/%{_mandir}
rm -rf %{buildroot}/%{_datadir}/applications/*.desktop

%fdupes -s %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/lxde-logout
%dir %{_datadir}/lxde
%dir %{_datadir}/lxde/images
%{_datadir}/lxde/images/logout-banner.png
%{_datadir}/lxde/images/lxde-icon.png
%{_datadir}/lxde/images/suse-logout.png
%{_datadir}/lxde/images/start-here-branding.svg
%dir %{_sysconfdir}/xdg/lxsession
%dir %{_sysconfdir}/xdg/pcmanfm
%dir %{_sysconfdir}/xdg/lxsession/LXDE
%dir %{_sysconfdir}/xdg/pcmanfm/LXDE
%config %{_sysconfdir}/xdg/lxsession/LXDE/autostart
%config %{_sysconfdir}/xdg/lxsession/LXDE/desktop.conf
%config %{_sysconfdir}/xdg/pcmanfm/LXDE/pcmanfm.conf
%dir %{_sysconfdir}/xdg/lxpanel
%dir %{_sysconfdir}/xdg/lxpanel/LXDE
%dir %{_sysconfdir}/xdg/lxpanel/LXDE/panels
%dir %{_sysconfdir}/xdg/openbox
%dir %{_sysconfdir}/xdg/openbox/LXDE
%config %{_sysconfdir}/xdg/lxpanel/LXDE/config
%config %{_sysconfdir}/xdg/lxpanel/LXDE/panels/panel
%config %{_sysconfdir}/xdg/openbox/LXDE/menu.xml
%config %{_sysconfdir}/xdg/openbox/LXDE/rc.xml

%changelog
