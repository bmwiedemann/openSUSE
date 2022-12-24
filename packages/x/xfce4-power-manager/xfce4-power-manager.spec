#
# spec file for package xfce4-power-manager
#
# Copyright (c) 2022 SUSE LLC
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


%define panel_version 4.12.0
%bcond_with git
Name:           xfce4-power-manager
Version:        4.18.0
Release:        0
Summary:        Power Management for the Xfce Desktop Environment
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/xfce/xfce4-power-manager/start
Source0:        https://archive.xfce.org/src/xfce/xfce4-power-manager/4.18/%{name}-%{version}.tar.bz2
Source1:        xfce4-power-manager.xml
BuildRequires:  appstream-glib
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  libxslt-tools
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0) >= 2.66
BuildRequires:  pkgconfig(glib-2.0) >= 2.66
BuildRequires:  pkgconfig(gmodule-2.0) >= 2.66
BuildRequires:  pkgconfig(gobject-2.0) >= 2.66
BuildRequires:  pkgconfig(gthread-2.0) >= 2.66
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24
BuildRequires:  pkgconfig(libnotify) >= 0.4.1
BuildRequires:  pkgconfig(libxfce4panel-2.0) >= %{panel_version}
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.12.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.12.0
BuildRequires:  pkgconfig(libxfconf-0) >= 4.12.0
BuildRequires:  pkgconfig(polkit-gobject-1) >= 0.100
BuildRequires:  pkgconfig(upower-glib) >= 0.99.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrandr) >= 1.2.0
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
Requires:       /usr/bin/pkexec
Requires:       systemd
Requires:       upower
Recommends:     %{name}-lang = %{version}
Provides:       xfce4-power-manager-doc = %{version}
Obsoletes:      xfce4-power-manager-doc <= 1.2.0

%description
The Xfce Power Manager is a tool for the Xfce desktop environment for managing
profiles of policies which affect power consumption, such as the display
brightness level, display sleep times, or CPU frequency scaling. It can also
trigger actions on certain events such as closing the lid or reaching low
battery levels and provides a set of interfaces to inform other applications
about current power level so that they can adjust their power consumption.
Furthermore, it provides a standardized inhibit interface which allows
applications to prevent automatic sleep actions via the power manager.

%package -n xfce4-power-manager-plugin
Summary:        Xfce Panel Plugin for Monitoring Batteries and Changing the Display Brightness
Group:          System/GUI/XFCE
Requires:       %{name} = %{version}
Requires:       xfce4-panel >= %{panel_version}
Provides:       xfce4-panel-plugin-brightness = %{version}
Obsoletes:      xfce4-panel-plugin-brightness <= 1.3.0
Provides:       xfce4-panel-plugin-xfce4battery = %{version}
Obsoletes:      xfce4-panel-plugin-xfce4battery <= 1.3.1
# package was renamed in 2019 after Leap 15.1
Obsoletes:      xfce4-panel-plugin-power-manager < %{version}-%{release}
Provides:       xfce4-panel-plugin-power-manager = %{version}-%{release}

%description -n xfce4-power-manager-plugin
This package provides a plugin for the Xfce panel for monitoring battery and
device charge levels and to regulate display brightness.

%package branding-upstream
Summary:        Upstream Branding of xfce4-power-manager
Group:          System/GUI/XFCE
Supplements:    packageand(%{name}:branding-upstream)
Conflicts:      otherproviders(%{name}-branding)
Provides:       %{name}-branding = %{version}
#BRAND: xfce4-power-manager.xml: Determines power management policy and related
#BRAND: event actions.
BuildArch:      noarch

%description branding-upstream
This package provides the openSUSE look and feel for the Xfce Power Manager.

%lang_package

%prep
%autosetup -p1

# xfce4-pm-helper is only needed on non-systemd systems
xsltproc --nonet - ./src/org.xfce.power.policy.in2 <<'EOF' \
    > ./src/org.xfce.power.policy.in2.new && \
    mv ./src/org.xfce.power.policy.in2.new ./src/org.xfce.power.policy.in2
<?xml version="1.0"?>
<xsl:stylesheet
  version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
  <xsl:output
  doctype-public="-//freedesktop//DTD PolicyKit Policy Configuration 1.0//EN"
  doctype-system="http://www.freedesktop.org/standards/PolicyKit/1.0/policyconfig.dtd"/>
  <xsl:template match="action[@id='org.xfce.power.xfce4-pm-helper']" />
  <xsl:template match="@*|node()">
    <xsl:copy>
      <xsl:apply-templates select="@*|node()"/>
    </xsl:copy>
  </xsl:template>
</xsl:stylesheet>
EOF

%build
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure \
    --enable-maintainer-mode
%else
%configure
%endif
%make_build

%install
%make_install

install -D -p -m 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml

%suse_update_desktop_file xfce4-power-manager-settings
%suse_update_desktop_file xfce4-power-manager

rm %{buildroot}%{_libdir}/xfce4/panel/plugins/libxfce4powermanager.la

# xfce4-pm-helper is only needed on non-systemd systems
rm %{buildroot}%{_sbindir}/xfce4-pm-helper

%find_lang %{name} %{?no_lang_C}

%fdupes %{buildroot}/%{_datadir}

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml

%files
%if %{with git}
%doc AUTHORS NEWS README.md
%else
%doc AUTHORS NEWS README.md ChangeLog
%endif
%license COPYING
%{_bindir}/xfce4-power-manager
%{_bindir}/xfce4-power-manager-settings
%{_sbindir}/xfpm-power-backlight-helper
%config %{_sysconfdir}/xdg/autostart/xfce4-power-manager.desktop
%{_mandir}/man1/xfce4-power-manager*.1*
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/org.xfce.power.policy
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/xfce4-power-manager.appdata.xml
%{_datadir}/applications/xfce4-power-manager-settings.desktop
%{_datadir}/icons/hicolor/*/*/*

%files lang -f %{name}.lang

%files -n xfce4-power-manager-plugin
%{_libdir}/xfce4/panel/plugins/libxfce4powermanager.so
%{_datadir}/xfce4/panel/plugins/power-manager-plugin.desktop

%files branding-upstream
%dir %{_sysconfdir}/xdg/xfce4
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%dir %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
%config %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/xfce4-power-manager.xml

%changelog
