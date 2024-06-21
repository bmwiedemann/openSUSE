#
# spec file for package vinagre
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


%bcond_with rdp

Name:           vinagre
Version:        3.22.0
Release:        0
Summary:        VNC client for GNOME
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other
URL:            http://www.gnome.org/projects/vinagre/
Source0:        http://download.gnome.org/sources/vinagre/3.22/%{name}-%{version}.tar.xz

# PATCH-FIX-UPSTREAM vinagre-freerdp2.patch bgo#765444 bgo#775616 mgorse@suse.com -- handle new "freerdp2" package name.
Patch1:         vinagre-freerdp2.patch
# PATCH-FIX-UPSTREAM vinagre-cert-validation-api.patch bgo#774473 boo#100235 fezhang@suse.com -- fix API incompatibilities with freerdp 1.2 that causes rdp connections abort
Patch2:         vinagre-cert-validation-api.patch
# The icon we rely on is from adwaita-icon-theme
# PATCH-FIX-UPSTREAM vinagre-invisible-fullscreen-toolbar.patch bgo#770484 boo#1008585 badshah400@opensuse.org -- Fix showing of toolbar as invisible in fullscreen mode; patch taken from upstream bug comment
Patch3:         vinagre-invisible-fullscreen-toolbar.patch

BuildRequires:  adwaita-icon-theme
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gdbm-devel
# Next two lines needed for Patch1
BuildRequires:  gnome-common
BuildRequires:  intltool >= 0.50.0
BuildRequires:  pkgconfig
# We need the %%mime_database_* macros
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(appstream-glib) >= 0.7.3
BuildRequires:  pkgconfig(avahi-gobject)
BuildRequires:  pkgconfig(avahi-ui-gtk3)
%if %{with rdp}
BuildRequires:  pkgconfig(freerdp2)
%endif
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.9.6
BuildRequires:  pkgconfig(gtk-vnc-2.0) >= 0.4.3
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.6.31
BuildRequires:  pkgconfig(spice-client-gtk-3.0) >= 0.5
# Disable telepathy support
#BuildRequires:  pkgconfig(telepathy-glib)
BuildRequires:  pkgconfig(vte-2.91)
BuildRequires:  pkgconfig(x11)

Obsoletes:      %{name}-devel < %{version}
%if 0%{?suse_version} < 1500
%glib2_gsettings_schema_requires
%endif

%description
Vinagre is a VNC client for GNOME that supports connecting to multiple
machines, browsing for VNC servers via avahi and password storage in
gnome-keyring.

%lang_package

%prep

# Work-around for boo#1225951, at least until vala is fixed.
%global optflags %{optflags} -fpermissive

%autosetup -p1

%build
# Needed for Patch1
autoreconf -fiv
export CFLAGS="%{optflags} -Wno-error=format-nonliteral -fcommon"
%configure \
	--disable-static \
%if %{with rdp}
	--enable-rdp \
%endif
	--enable-spice \
	--enable-ssh \
	--without-telepathy \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file -G "Remote Desktop Viewer" vinagre
%suse_update_desktop_file vinagre-file
%find_lang %{name} %{?no_lang_C}
for size in 8x8 16x16 22x22 24x24 32x32 48x48 256x256; do
        if test -f %{_datadir}/icons/Adwaita/$size/legacy/preferences-desktop-remote-desktop.png; then
                mkdir -p %{buildroot}%{_datadir}/icons/hicolor/$size/apps
                cp -a %{_datadir}/icons/Adwaita/$size/legacy/preferences-desktop-remote-desktop.png %{buildroot}%{_datadir}/icons/hicolor/$size/apps/preferences-desktop-remote-desktop.png
        fi
done

%fdupes %{buildroot}

%if 0%{?suse_version} < 1500
%post
%glib2_gsettings_schema_post
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%postun
%glib2_gsettings_schema_postun
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun
%endif

%files
%doc %{_datadir}/help/C/%{name}/
%{_mandir}/man1/*.1%{?ext_man}
%{_bindir}/vinagre
%{_datadir}/applications/vinagre.desktop
%{_datadir}/applications/vinagre-file.desktop
# Disable telepathy support
#%%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Vinagre.service
%dir %{_datadir}/GConf
%dir %{_datadir}/GConf/gsettings
%{_datadir}/GConf/gsettings/org.gnome.Vinagre.convert
%{_datadir}/glib-2.0/schemas/org.gnome.Vinagre.gschema.xml
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/metainfo/vinagre.appdata.xml
%{_datadir}/mime/packages/vinagre-mime.xml
%dir %{_datadir}/vinagre
%{_datadir}/vinagre/vinagre*
# Disable telepathy support
# Own directories that are not owned by anything else
#%%dir %%{_datadir}/telepathy
#%%dir %%{_datadir}/telepathy/clients
#%%{_datadir}/telepathy/clients/Vinagre.client

%files lang -f %{name}.lang

%changelog
