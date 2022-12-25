#
# spec file for package thunar-volman
#
# Copyright (c) 2020-2022 SUSE LLC
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


%bcond_with git
Name:           thunar-volman
Version:        4.18.0
Release:        0
Summary:        Thunar Volume Manager
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://goodies.xfce.org/projects/thunar-plugins/thunar-volman
Source0:        https://archive.xfce.org/src/xfce/thunar-volman/4.18/%{name}-%{version}.tar.bz2
Source1:        thunar-volman.xml
# PATCH-FIX-OPENSUSE thunar-volman-use-udisks-hints.diff bnc#949808 -- seife+dev@b1-systems.com
Patch0:         thunar-volman-use-udisks-hints.diff
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(exo-2) >= 0.10.0
BuildRequires:  pkgconfig(gio-2.0) >= 2.66.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gthread-2.0) >= 2.66.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.24.0
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.12
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.12
BuildRequires:  pkgconfig(libxfconf-0) >= 4.12
%if %{with git}
BuildRequires:  xfce4-dev-tools
%endif
Recommends:     %{name}-lang = %{version}

%description
The Thunar Volume Manager is an extension for the Thunar file manager,
which enables automatic management of removable drives and media. For
example, if thunar-volman is installed and configured properly, and you
plug in your digital camera, it will automatically launch your
preferred photo application and import the new pictures from the camera
into your photo collection.

%package branding-upstream
Summary:        Upstream Branding of thunar-volman
Group:          System/GUI/XFCE
Supplements:    packageand(%{name}:branding-upstream)
Conflicts:      otherproviders(%{name}-branding)
Provides:       %{name}-branding = %{version}
#BRAND: xfce4.xml: Determines a whether to automatically mount hotpluggable
#BRAND: drives and removable median and whether to open what applications
#BRAND: automatically.
BuildArch:      noarch

%description branding-upstream
This package provides the upstream look and feel for the Thunar Volume Manager.

%lang_package

%prep
%autosetup -p1

%build
%if %{with git}
NOCONFIGURE=1 ./autogen.sh
%configure --enable-maintainer-mode
%else
%configure
%endif
%make_build

%install
%make_install

install -D -p -m 644 %{SOURCE1} \
    %{buildroot}%{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/thunar-volman.xml

%suse_update_desktop_file thunar-volman-settings Settings DesktopSettings

rm -rf %{buildroot}%{_datadir}/locale/{ast,kk,tl_PH,ur_PK}

%find_lang %{name} %{?no_lang_C}

%files
%doc AUTHORS NEWS README.md THANKS
%license COPYING
%{_bindir}/thunar-volman
%{_bindir}/thunar-volman-settings
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/*/*

%files lang -f %{name}.lang

%files branding-upstream
%dir %{_sysconfdir}/xdg/xfce4
%dir %{_sysconfdir}/xdg/xfce4/xfconf
%dir %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml
%config %{_sysconfdir}/xdg/xfce4/xfconf/xfce-perchannel-xml/thunar-volman.xml

%changelog
