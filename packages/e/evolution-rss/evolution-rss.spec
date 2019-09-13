#
# spec file for package evolution-rss
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


%define _eds_moduledir %(pkg-config --variable privlibdir libedataserver-1.2)/registry-modules
%define _evo_branch %(pkg-config --variable execversion evolution-shell-3.0)
%define _evo_plugindir %(pkg-config --variable privlibdir evolution-shell-3.0)/plugins
%define _evo_imagesdir %(pkg-config --variable imagesdir evolution-shell-3.0)
%define         _name evolution-plugin-rss
%define _evo_errordir %(pkg-config --variable errordir evolution-shell-3.0)

Name:           evolution-rss
Version:        0.3.95+git.20171129
Release:        0
Summary:        Evolution Plugin for RSS Feeds Support
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Email/Clients
URL:            http://gnome.eu.org/evo/index.php/Evolution_RSS_Reader_Plugin
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM evolution-rss-drop-gconf-for-good.patch -- Drop gconf2 for good.
Patch:          evolution-rss-drop-gconf-for-good.patch
# PATCH-FIX-UPSTREAM evolution-rss-use-unicode.patch -- Use Unicode in translatable strings, Remove markup from strings in UI files
Patch1:         evolution-rss-use-unicode.patch

BuildRequires:  gcc-c++
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(evolution-data-server-1.2)
BuildRequires:  pkgconfig(evolution-shell-3.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.26
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libebook-1.2)
BuildRequires:  pkgconfig(libemail-engine)
BuildRequires:  pkgconfig(libsoup-2.4)
Provides:       %{_name} = %{version}

%description
This plugin for Evolution adds RSS Feeds support and enables the use of
Evolution as a RSS Reader.

%package -n %{_name}
Summary:        Evolution Plugin for RSS Feeds Support
Group:          Productivity/Networking/Email/Clients
Recommends:     %{_name}-lang
Provides:       %{name} = %{version}

%description -n %{_name}
This plugin for Evolution adds RSS Feeds support and enables the use of
Evolution as a RSS Reader.

%lang_package -n %{_name}

%prep
%autosetup -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-schemas-install \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%files -n %{_name}
%{_bindir}/evolution-import-rss
%{_datadir}/appdata/evolution-rss.metainfo.xml
%{_datadir}/applications/evolution-rss.desktop
%{_datadir}/evolution/ui/rss-html-rendering.ui
%{_datadir}/evolution/ui/rss-main.ui
%{_datadir}/GConf/gsettings/evolution-rss.convert
%{_datadir}/glib-2.0/schemas/org.gnome.evolution.plugin.evolution-rss.gschema.xml
%{_eds_moduledir}/module-eds-rss.so
%{_evo_errordir}/org-gnome-evolution-rss.error
%{_evo_imagesdir}/pix.png
%{_evo_imagesdir}/rss-16.png
%{_evo_imagesdir}/rss-22.png
%{_evo_imagesdir}/rss-24.png
%{_evo_imagesdir}/rss-icon-read.png
%{_evo_imagesdir}/rss-icon-unread.png
%{_evo_imagesdir}/rss-text-html.png
%{_evo_imagesdir}/rss-text-x-generic.png
%{_evo_imagesdir}/rss.png
%{_evo_plugindir}/liborg-gnome-evolution-rss.so
%{_evo_plugindir}/org-gnome-evolution-rss.eplug
%{_evo_plugindir}/org-gnome-evolution-rss.xml
%{_libdir}/evolution/modules/evolution-module-rss.so

%files -n %{_name}-lang -f %{name}.lang

%changelog
