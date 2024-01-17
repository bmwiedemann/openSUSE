#
# spec file for package remontoire
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


Name:           remontoire
Version:        1.4.0
Release:        0
Summary:        A keybinding viewer for i3 and other programs
License:        GPL-3.0-or-later
Group:          System/X11/Utilities
URL:            https://github.com/regolith-linux/remontoire
Source:         https://github.com/regolith-linux/remontoire/archive/1.4.0.tar.gz
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel >= 3.22
BuildRequires:  json-glib-devel
BuildRequires:  libgee-devel
BuildRequires:  meson >= 0.40.0
BuildRequires:  vala

%description
A keybinding viewer for i3 and other programs.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_bindir}/remontoire
%{_datadir}/appdata/org.regolith-linux.remontoire.appdata.xml
%{_datadir}/applications/org.regolith-linux.remontoire.desktop
%{_datadir}/glib-2.0/schemas/org.regolith-linux.remontoire.gschema.xml

%changelog
