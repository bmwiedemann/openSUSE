#
# spec file for package gtkam
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


Name:           gtkam
Version:        1.1
Release:        0
Summary:        A GTK Digital Camera Tool
License:        GPL-2.0-or-later
Group:          Hardware/Camera
URL:            http://gphoto.org
Source:         https://github.com/gphoto/gtkam/releases/download/v%{version}/gtkam-%{version}.tar.bz2
Source1:        https://github.com/gphoto/gtkam/releases/download/v%{version}/gtkam-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
BuildRequires:  fdupes
BuildRequires:  gimp-devel
BuildRequires:  intltool
BuildRequires:  libexif-gtk-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libgphoto2)
Requires:       %{name}-lang = %{version}

%description
GTKam is a GTK and GNOME based tool for accessing a digital camera,
viewing thumbnails, and downloading pictures from the camera.

%package doc
Summary:        Documentation for gtkcam
Group:          Documentation/Man
Requires:       %{name} = %{version}

%description doc
Documentation for gtkam.

%lang_package

%prep
%autosetup -p1

%build
%configure
make %{?jobs:-j%jobs}

%install
%make_install
# cleanup
rm -r %{buildroot}%{_datadir}/doc/gtkam
%suse_update_desktop_file %{name} Graphics Photography
%find_lang %{name}
%fdupes %{buildroot}

%files
%license COPYING
%{_bindir}/gtkam
%{_datadir}/applications/*.desktop
%{_datadir}/gtkam
%dir %{_datadir}/gnome
%dir %{_datadir}/gnome/help
# FIXME: There is no generic %{_datadir}/images. Better would be %{_datadir}/pixmaps (upstream problem).
%dir %{_datadir}/images
%dir %{_datadir}/omf
%{_datadir}/images/gtkam
%{_datadir}/pixmaps/gtkam.png
%{_datadir}/pixmaps/gtkam-camera.png
%{_libdir}/gimp/2.0/plug-ins/gtkam-gimp

%files lang -f %{name}.lang

%files doc
%doc AUTHORS ChangeLog CHANGES NEWS README TODO
%{_mandir}/man1/*%{ext_man}

%changelog
