#
# spec file for package leocad
#
# Copyright (c) 2021 SUSE LLC
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


Name:           leocad
Version:        21.03
Release:        0
Summary:        CAD program for creating virtual LEGO models
License:        GPL-2.0-only
URL:            http://leocad.org
Source0:        https://github.com/leozide/leocad/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         0001-Don-t-enable-relative-transforms-by-default.patch
Patch1:         0002-Disabled-relative-movement-when-moving-pieces-withou.patch
Patch2:         0003-Fixed-moving-pieces-while-editing-submodels-in-place.patch
Patch3:         0004-Fixed-drawing-the-rotate-overlay-during-in-place-sub.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-linguist
BuildRequires:  libqt5-qtbase-devel >= 5.4.0
BuildRequires:  make
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
Requires:       povray

%description
CAD program for creating virtual LEGO models.
It has an intuitive interface, designed to allow
new users to start creating new models without
having to spend too much time learning the
application.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%qmake5
%make_build

%install
%suse_update_desktop_file -r -G 'CAD Application' %{name} Graphics 3DGraphics
make install INSTALL_ROOT=%{buildroot} DISABLE_UPDATE_CHECK=1 LDRAW_LIBRARY_PATH=%{_datadir}/ldraw
# We install it later correctly
rm -rf %{buildroot}%{_datadir}/doc
# Remove duplicates
%fdupes %{buildroot}%{_datadir}

%files
%license docs/COPYING.txt
%doc docs/{README.txt,CREDITS.txt}
%{_bindir}/leocad
%{_datadir}/applications/leocad.desktop
%{_mandir}/man1/leocad.1%{?ext_man}
%{_datadir}/metainfo/leocad.appdata.xml
%{_datadir}/mime/packages/leocad.xml
%{_datadir}/icons/hicolor/*/apps/leocad.*
%{_datadir}/icons/hicolor/*/mimetypes/application-vnd.leocad.*

%changelog
