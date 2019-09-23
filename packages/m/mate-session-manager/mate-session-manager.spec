#
# spec file for package mate-session-manager
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _version 1.23
Name:           mate-session-manager
Version:        1.23.0
Release:        0
Summary:        MATE Session Manager
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
# Not an upstream file. Only proposes upstream packages:
Source1:        mate-session-manager-upstream-mate_defaults.conf
# Some documentation for people writing branding packages, shipped in the branding-upstream package.
Source2:        README.Gsettings-overrides
# PATCH-FIX-OPENSUSE mate-session-manager-qt-5.7-styleoverride.patch sor.alexei@meowr.ru -- On Qt 5.7+ use Gtk2 Platform Theme.
Patch0:         mate-session-manager-qt-5.7-styleoverride.patch
BuildRequires:  hicolor-icon-theme
# set to _version when mate-common has an equal release
BuildRequires:  mate-common >= 1.22
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0) >= 2.50
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtrans)
Requires:       %{name}-branding >= %{_version}
Requires:       %{name}-gschemas >= %{version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     %{name}-lang
%glib2_gsettings_schema_requires
%if 0%{?suse_version} >= 1500
# Make native styling in Qt5 happen.
Requires:       libqt5-qtstyleplugins-platformtheme-gtk2
%endif

%description
This package contains a session that can be started from a display
manager such as LightDM. It will load all necessary applications
for a full-featured user session.

%lang_package

%package branding-upstream
Summary:        Upstream definitions of default settings and applications
Group:          System/Libraries
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:branding-upstream)
Conflicts:      otherproviders(%{name}-branding)
Provides:       %{name}-branding = %{version}
BuildArch:      noarch
#BRAND: The /etc/mate_defaults.conf allows to define arbitrary
#BRAND: applications as preferred defaults.
#BRAND: A /usr/share/glib-2.0/schemas/$NAME.gschema.override file can
#BRAND: be used to override the default value for GSettings keys. See
#BRAND: README.Gsettings-overrides for more details. The branding
#BRAND: package should then have proper Requires for features changed
#BRAND: with such an override file.

%description -n mate-session-manager-branding-upstream
This package provides upstream defaults for settings stored with
GSettings and applications used by the MIME system.

%package gschemas
Summary:        MATE Session Manager GSchemas
Group:          System/Libraries
%glib2_gsettings_schema_requires

%description gschemas
This package provides the GSettings schemas for
MATE Session Manager.

%prep
%autosetup -p1

cp -a %{SOURCE2} .
cp -a %{SOURCE1} mate_defaults.conf

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-static             \
  --enable-ipv6                \
  --with-default-wm=marco      \
%if 0%{?suse_version} >= 1500
  --enable-qt57-theme-support  \
%else
  --disable-qt57-theme-support \
%endif
  --with-systemd=yes
make %{?_smp_mflags} V=1

%install
%make_install
install -Dpm 0644 mate_defaults.conf \
  %{buildroot}%{_sysconfdir}/mate_defaults.conf

mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop \
  %{buildroot}%{_datadir}/xsessions/default.desktop

%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file mate-session-properties
%suse_update_desktop_file %{buildroot}%{_datadir}/xsessions/mate.desktop

%post
%if 0%{?suse_version} < 1500
%icon_theme_cache_post
%endif
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/mate.desktop 20

%postun
%if 0%{?suse_version} < 1500
%icon_theme_cache_postun
%endif
if [ ! -f %{_datadir}/xsessions/mate.desktop ]; then
    %{_sbindir}/update-alternatives --remove default-xsession.desktop \
      %{_datadir}/xsessions/mate.desktop
fi

%if 0%{?suse_version} < 1500
%post gschemas
%glib2_gsettings_schema_post

%postun gschemas
%glib2_gsettings_schema_postun
%endif

%files
%license COPYING
%doc NEWS README
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop
%{_bindir}/mate-*
%{_datadir}/%{name}/
%{_datadir}/xsessions/*.desktop
%{_datadir}/applications/mate-session-properties.desktop
%{_datadir}/icons/hicolor/*/apps/mate-session-properties.*
%{_mandir}/man?/mate-*.?%{?ext_man}
%{_libexecdir}/mate-*

%files lang -f %{name}.lang

%files branding-upstream
%doc README.Gsettings-overrides
%config(noreplace) %{_sysconfdir}/mate_defaults.conf

%files gschemas
%{_datadir}/glib-2.0/schemas/*.xml

%changelog
