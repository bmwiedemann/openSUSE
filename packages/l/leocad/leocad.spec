#
# spec file for package leocad
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


Name:           leocad
Version:        19.07.1
Release:        1
Summary:        CAD program for creating virtual LEGO models
License:        GPL-2.0-only
URL:            http://leocad.org
Source0:        https://github.com/leozide/leocad/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
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

%build
%qmake5
%make_build

%install
%suse_update_desktop_file -r -G 'CAD Application' %{name} Graphics 3DGraphics
make install INSTALL_ROOT=%{buildroot} DISABLE_UPDATE_CHECK=1 LDRAW_LIBRARY_PATH=%{_datadir}/ldraw


%files
%license %{_datadir}/doc/leocad/COPYING.txt
%doc %{_datadir}/doc/leocad/README.txt
%doc %{_datadir}/doc/leocad/CREDITS.txt
%dir %{_datadir}/doc/leocad/
%dir %{_datadir}/icons/hicolor/scalable
%{_bindir}/leocad
%{_datadir}/applications/leocad.desktop
%{_datadir}/icons/hicolor/scalable/mimetypes/
%{_mandir}/man1/leocad.1%{?ext_man}
%{_datadir}/metainfo/leocad.appdata.xml
%{_datadir}/mime/packages/leocad.xml
%{_datadir}/pixmaps/leocad.png

%changelog
