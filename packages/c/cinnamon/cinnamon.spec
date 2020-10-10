#
# spec file for package cinnamon
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


%define _version 4.0.0
Name:           cinnamon
Version:        4.6.7
Release:        0
Summary:        GNU/Linux Desktop featuring a traditional layout
License:        GPL-2.0-or-later AND LGPL-2.1-only
Group:          System/GUI/Other
URL:            https://github.com/linuxmint/cinnamon
Source:         https://github.com/linuxmint/cinnamon/archive/%{version}/%{name}-%{version}.tar.gz
# Some documentation for people writing branding packages, shipped in the branding-upstream package.
Source1:        README.Gsettings-overrides
# PATCH-FIX-OPENSUSE cinnamon-wheel-and-sbin-path sor.alexei@meowr.ru -- Make full sbin paths and use wheel as a sudo group.
Patch1:         %{name}-wheel-and-sbin-path.patch
# PATCH-FIX-OPENSUSE cinnamon-settings-native.patch andythe_great@pm.me -- Remove foreign configuration tools and add openSUSE's native.
Patch2:         %{name}-settings-native.patch
# PATCH-FIX-OPENSUSE cinnamon-settings-xscreensaver-path.patch boo#960165 sor.alexei@meowr.ru -- Fix xscreensaver configs path.
Patch3:         %{name}-settings-xscreensaver-path.patch
# PATCH-FEATURE-OPENSUSE cinnamon-favourite-applications.patch sor.alexei@meowr.ru -- Remove mintinstall from favourites and add YaST.
Patch4:         %{name}-favourite-applications.patch
# PATCH-FIX-OPENSUSE cinnamon-fix-cogl.patch sor.alexei@meowr.ru -- Fix compilation with Cogl.
Patch6:         %{name}-fix-cogl.patch
# PATCH-FEATURE-OPENSUSE cinnamon-fallback-icewm.patch sor.alexei@meowr.ru -- Use IceWM as fallback.
Patch7:         %{name}-fallback-icewm.patch
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
# For gnome-background-properties.
BuildRequires:  desktop-data-openSUSE-extra
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
# For distributor.svg.
BuildRequires:  hicolor-icon-theme-branding-openSUSE
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  python3-xml
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cinnamon-desktop) >= %{_version}
BuildRequires:  pkgconfig(cjs-1.0)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(libcinnamon-menu-3.0)
BuildRequires:  pkgconfig(libcroco-0.6)
BuildRequires:  pkgconfig(libmuffin) >= %{_version}
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(polkit-agent-1)
Requires:       %{name}-gschemas = %{version}
Requires:       adwaita-icon-theme
Requires:       cinnamon-control-center-common >= %{_version}
Requires:       cinnamon-screensaver >= %{_version}
Requires:       cinnamon-session >= %{_version}
Requires:       cinnamon-settings-daemon >= %{_version}
Requires:       cjs >= %{_version}
Requires:       cups-pk-helper
Requires:       dbus-1
Requires:       gettext-runtime
Requires:       glib2-tools
Requires:       iso-country-flags-png
Requires:       libcinnamon-desktop-data >= %{_version}
# gkbd-capplet / gkbd-keyboard-display.
Requires:       gnomekbd-tools
Requires:       libgnomekbd
Requires:       muffin >= %{_version}
Requires:       nemo
Requires:       pkgconfig
Requires:       polkit-gnome
Requires:       python3-Pillow
Requires:       python3-cairo
Requires:       python3-distro
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-gobject-cairo
Requires:       python3-pexpect
Requires:       python3-pyinotify
Requires:       python3-python-pam
# cinnamon-settings calendar module
Requires:       python3-pytz
# cinnamon-settings theme module
Requires:       python3-tinycss2
Requires:       v4l-tools
Requires:       wget
Requires:       xdg-user-dirs
Requires:       xdg-user-dirs-gtk
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     %{name}-lang
Recommends:     blueberry
Recommends:     cinnamon-themes
Recommends:     gnome-terminal
Recommends:     gnome-themes-standard
Recommends:     icewm
# cinnamon-2d was last used in openSUSE 13.2.
Provides:       %{name}-2d = %{version}
Obsoletes:      %{name}-2d < %{version}
# cinnamon-menu-editor was last used in openSUSE 13.2.
Provides:       %{name}-menu-editor = %{version}
Obsoletes:      %{name}-menu-editor < %{version}
# cinnamon-settings was last used in openSUSE 13.2.
Provides:       %{name}-settings = %{version}
Obsoletes:      %{name}-settings < %{version}
# typelib-1_0-Cinnamon-0_1 was last used in openSUSE Leap 42.1.
Provides:       typelib-1_0-Cinnamon-0_1 = %{version}
Obsoletes:      typelib-1_0-Cinnamon-0_1 < %{version}
%if 0%{?suse_version} >= 1500
BuildRequires:  pkgconfig(libnm)
Requires:       NetworkManager-applet
Requires:       python3-dbus-python
%else
BuildRequires:  pkgconfig(libnm-glib)
Requires:       NetworkManager-gnome
Requires:       dbus-1-python3
%endif

%description
Cinnamon is a modern Linux desktop which provides advanced innovative
features and a traditional user experience. It's easy to use,
powerful and flexible.

%package gschemas
Summary:        GNU/Linux Desktop featuring a traditional layout -- GSchemas
Group:          System/Libraries
Requires:       %{name}-gschemas-branding = %{version}
%glib2_gsettings_schema_requires

%description gschemas
This package provides GSettings schemas for
Cinnamon Desktop Environment.

%package gschemas-branding-upstream
Summary:        Upstream definitions of default settings and applications
Group:          System/Libraries
Requires:       %{name}-gschemas = %{version}
Requires:       libgnomesu
Supplements:    packageand(%{name}-gschemas:branding-upstream)
Conflicts:      otherproviders(%{name}-gschemas-branding)
Provides:       %{name}-gschemas-branding = %{version}
# cinnamon-branding-upstream was last used in openSUSE Leap 42.2.
Provides:       %{name}-branding-upstream = %{version}
Obsoletes:      %{name}-branding-upstream < %{version}
BuildArch:      noarch
#BRAND: A /usr/share/glib-2.0/schemas/$NAME.gschema.override file can
#BRAND: be used to override the default value for GSettings keys. See
#BRAND: README.Gsettings-overrides for more details. The branding
#BRAND: package should then have proper Requires for features changed
#BRAND: with such an override file.

%description gschemas-branding-upstream
This package provides upstream defaults for settings stored with
GSettings and applications used by the MIME system.

%package devel-doc
Summary:        Development Documentation files for Cinnamon
Group:          System/GUI/Other
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description devel-doc
This package contains the code documentation for various Cinnamon components.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p1
cp -a %{SOURCE1} .

for file in files%{_datadir}/%{name}/%{name}-settings/bin/*.py files%{_datadir}/%{name}/%{name}-looking-glass/*.py \
   files%{_datadir}/%{name}/%{name}-settings/modules/cs_{applets,desklets}.py; do
   chmod a+x $file
done
chmod a-x files%{_datadir}/%{name}/%{name}-settings/bin/__init__.py

sed -i -e 's!imports.gi.NMClient!imports_gi_NMClient!g' js/ui/extension.js

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
    --disable-static \
    --disable-schemas-compile \
    --disable-silent-rules \
    --enable-introspection=yes \
    --enable-compile-warnings=no \
    --with-ca-certificates=%{_sysconfdir}/ssl/ca-bundle.pem

%make_build

%install
%make_install

# Non-executable in /usr/bin/ is unacceptable.
chmod a+x %{buildroot}%{_bindir}/%{name}-file-dialog

# We should own this directory.
mkdir -p %{buildroot}%{_libdir}/%{name}/extensions/

# Provide all GNOME compatible backgrounds (including openSUSE branding) to Cinnamon.
ln -s gnome-background-properties \
  %{buildroot}%{_datadir}/cinnamon-background-properties

dirname $(find %{buildroot}%{_datadir} -type f -name '*.py') | sort -u | while read dir; do
    # Compile Python bytecode.
    %py3_compile .
done

mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop \
  %{buildroot}%{_datadir}/xsessions/default.desktop

%{_bindir}/find %{buildroot}%{_libdir} -name '*.a' -print -delete
%{_bindir}/find %{buildroot}%{_libdir} -name '*.la' -print -delete
%fdupes %{buildroot}%{_datadir}/

%suse_update_desktop_file %{name}-settings
%suse_update_desktop_file %{name}-settings-users
%suse_update_desktop_file %{name}-menu-editor
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/%{name}2d.desktop
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/%{name}-killer-daemon.desktop
%suse_update_desktop_file %{buildroot}%{_datadir}/xsessions/%{name}.desktop
%suse_update_desktop_file %{buildroot}%{_datadir}/xsessions/%{name}2d.desktop

%post
/sbin/ldconfig
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/%{name}.desktop 20
%if 0%{?suse_version} < 1500
%desktop_database_post
%icon_theme_cache_post
%endif

%postun
/sbin/ldconfig
if [ ! -f %{_datadir}/xsessions/%{name}.desktop ]; then
    %{_sbindir}/update-alternatives --remove default-xsession.desktop \
      %{_datadir}/xsessions/%{name}.desktop
fi
%if 0%{?suse_version} < 1500
%desktop_database_postun
%icon_theme_cache_postun
%endif

%if 0%{?suse_version} < 1500
%post gschemas
%glib2_gsettings_schema_post

%postun gschemas
%glib2_gsettings_schema_postun
%endif

%files
%license COPYING
%doc AUTHORS README.rst debian/changelog
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/xdg/menus/*
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop
%ghost %{_sysconfdir}/alternatives/default.desktop
%{_datadir}/cinnamon-session
%{_datadir}/cinnamon-session/sessions
%{_datadir}/applications/*
%{_datadir}/dbus-1/services/org.Cinnamon.*.service
%{_datadir}/desktop-directories/*
%{_datadir}/%{name}-session/sessions/*
%exclude %{_datadir}/%{name}/theme/menu*.svg
%{_datadir}/icons/hicolor/*/*/*.svg
%{_datadir}/polkit-1/actions/org.%{name}.settings-users.policy
%{_datadir}/xsessions/*
%{_datadir}/%{name}/
%{_datadir}/%{name}-background-properties
%{_libdir}/%{name}/
%{_libexecdir}/%{name}/
%{_mandir}/man1/*

%files gschemas
%{_datadir}/glib-2.0/schemas/org.cinnamon.gschema.xml

%files gschemas-branding-upstream
%doc README.Gsettings-overrides
%{_datadir}/%{name}/theme/menu*.svg

%files devel-doc
%doc %{_datadir}/gtk-doc/html/*/

%changelog
