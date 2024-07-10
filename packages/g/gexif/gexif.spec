#
# spec file for package gexif
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


Name:           gexif
BuildRequires:  fdupes
BuildRequires:  gtk2-devel
BuildRequires:  libexif-gtk-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
Summary:        GTK Tool for Viewing EXIF Information
License:        LGPL-2.1-or-later
Group:          Productivity/Graphics/Other
Version:        0.5
Release:        0
Source:         %{name}-%{version}.tar.bz2
Source1:        gexif.png
Patch0:         gexif-0.5-xx.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
URL:            http://libexif.sourceforge.net/
Requires:       %{name}-lang = %{version}

%description
This tool contains simple GTK interface for viewing EXIF information
within JPEG images created by some digital cameras.

%lang_package

%prep
%autosetup -p1

%build
autoreconf -f -i
%configure
make %{?jobs:-j%jobs}

%install
%makeinstall
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/
%find_lang %{name}
%if %suse_version > 1020
%fdupes -s $RPM_BUILD_ROOT
%endif
%if %suse_version > 1000
%suse_update_desktop_file -C "GTK EXIF Tag Viewer" -c %{name} "GExif" "EXIF Tag Viewer" %{name} gexif Graphics Photography
%else
%suse_update_desktop_file -c %{name} "GExif" "EXIF Tag Viewer" %{name} gexif Graphics Photograph
%endif

%files
%defattr(-,root,root)
%license COPYING
# NEWS README are empty
%doc AUTHORS ChangeLog
%{_bindir}/gexif
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png

%files lang -f %{name}.lang

%changelog
