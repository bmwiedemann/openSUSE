#
# spec file for package gnome-nettool
#
# Copyright (c) 2025 SUSE LLC
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


Name:           gnome-nettool
Version:        42.0+24
Release:        0
Summary:        GNOME Interface for Various Networking Tools
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            http://www.gnome.org
Source:         %{name}-%{version}.tar.zst
# PATCH-FIX-UPSTREAM gnome-nettool-bnc866643-predictable-name.patch bnc#866643 glin@suse.com -- Detect the predictable network device name
Patch1:         gnome-nettool-bnc866643-predictable-name.patch

BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.0.0
BuildRequires:  pkgconfig(libgtop-2.0)
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
%autosetup -p1

%build
%meson \
	%{nil}
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

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
%{_datadir}/metainfo/gnome-nettool.appdata.xml

%files lang -f %{name}.lang

%changelog
