#
# spec file for package obconf
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           obconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  libglade2-devel
BuildRequires:  startup-notification-devel
BuildRequires:  update-desktop-files
BuildRequires:  xorg-x11
BuildRequires:  pkgconfig(obrender-3.5)
BuildRequires:  pkgconfig(obt-3.5)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(sm)
Requires:       openbox
Version:        2.0.4
Release:        0
Summary:        Openbox Configuration Tool
License:        GPL-2.0+
Group:          System/GUI/Other
Url:            http://openbox.org/
Source0:        %{name}-%{version}.tar.bz2
Patch0:         %{name}-2.0.4-no_nb.patch
Patch1:         %{name}-2.0.4-Spanish-translation-update.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is the official application from the Openbox developers to
configure the Openbox window manager. It is not needed, but highly
recommended when installing Openbox.



Authors:
--------
    Ben Jansens <ben@openbox.org>
    Tim Riley <tr@slackzone.org>

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
mv po/no.po po/nb.po
%configure
pushd po
make update-gmo
popd
%__make clean
%__make

%install
%makeinstall
%__rm -rf %buildroot/%_datadir/mimelnk
%suse_update_desktop_file %name Utility Settings DesktopSettings
%find_lang %{name}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING README
%_bindir/%name
%_datadir/%name
%_datadir/mime/packages/obconf.xml
%_datadir/applications/%name.desktop
%_datadir/pixmaps/obconf.png

%changelog
