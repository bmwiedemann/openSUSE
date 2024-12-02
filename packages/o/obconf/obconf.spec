#
# spec file for package obconf
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


Name:           obconf
Version:        2.0.4
Release:        0
Summary:        Openbox Configuration Tool
License:        GPL-2.0-or-later
URL:            http://openbox.org/
Source0:        https://openbox.org/dist/obconf/%{name}-%{version}.tar.gz
Patch0:         %{name}-2.0.4-no_nb.patch
Patch1:         %{name}-2.0.4-Spanish-translation-update.patch
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  xorg-x11
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(obrender-3.5)
BuildRequires:  pkgconfig(obt-3.5)
BuildRequires:  pkgconfig(sm)
Requires:       openbox

%description
This is the official application from the Openbox developers to
configure the Openbox window manager. It is not needed, but highly
recommended when installing Openbox.

%lang_package

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -Wno-implicit-function-declaration"
mv po/no.po po/nb.po
%configure
pushd po
%make_build update-gmo
popd
%make_build

%install
%make_install
%__rm -rf %buildroot/%_datadir/mimelnk
%find_lang %{name}

%files
%doc AUTHORS COPYING README
%_bindir/%name
%_datadir/%name
%_datadir/mime/packages/obconf.xml
%_datadir/applications/%name.desktop
%_datadir/pixmaps/obconf.png

%files lang -f %{name}.lang

%changelog
