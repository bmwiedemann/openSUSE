#
# spec file for package gnome-nettool
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gnome-nettool
Version:        3.8.1+20180208.1e8ca5d
Release:        0
Summary:        GNOME Interface for Various Networking Tools
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            http://www.gnome.org
#Source0:       http://download.gnome.org/sources/gnome-nettool/3.8/%%{name}-%%{version}.tar.xz
Source:         %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM gnome-nettool-bnc866643-predictable-name.patch bnc#866643 glin@suse.com -- Detect the predictable network device name
Patch1:         gnome-nettool-bnc866643-predictable-name.patch
BuildRequires:  fdupes
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:  pkgconfig(libgtop-2.0)
Recommends:     %{name}-lang
# For dig
Recommends:     bind-utils
# For ping and tracepath
Recommends:     iputils
# For netstat and traceroute
Recommends:     net-tools
# Other tools that can be used
Suggests:       finger
Suggests:       nmap
Suggests:       whois
%glib2_gsettings_schema_requires

%description
GNOME Nettool is a set of front-ends to various networking command line
tools, like ping, netstat, ifconfig, whois, traceroute, and finger.

%lang_package

%prep
%setup -q
%patch1 -p1
translation-update-upstream

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-scrollkeeper \
	%{nil}
%make_build

%install
%make_install
# Note: I guess X-SuSE-Core-System is not the best thing for the non-GNOME menu, but we need something for the build to work. Oh well...
%suse_update_desktop_file -r gnome-nettool GNOME GTK System X-SuSE-Core-System
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}/%{_datadir}

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/gnome-nettool
%{_datadir}/applications/gnome-nettool.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-nettool.gschema.xml
%{_datadir}/gnome-nettool/
%{_datadir}/icons/hicolor/*/apps/gnome-nettool.png
%{_datadir}/icons/hicolor/scalable/apps/gnome-nettool*.svg
%{_datadir}/appdata/gnome-nettool.appdata.xml

%files lang -f %{name}.lang

%changelog
