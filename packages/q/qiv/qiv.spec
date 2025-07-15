#
# spec file for package qiv
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


Name:           qiv
Version:        2.3.4
Release:        0
Summary:        A gdk/imlib based image viewer
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Viewers
URL:            https://spiegl.de/qiv/
Source0:        https://codeberg.org/ciberandy/qiv/archive/v%{version}.tar.gz#/qiv-%{version}.tgz
BuildRequires:  file-devel
BuildRequires:  gtk2-devel
BuildRequires:  imlib2-devel
BuildRequires:  libexif-devel
BuildRequires:  libjpeg8-devel
BuildRequires:  liblcms2-devel
BuildRequires:  libtiff-devel
BuildRequires:  update-desktop-files
# imlib itself only recommends that but we actually need them to
# load images
Requires:       imlib2-loaders

%description
The "Quick Image Viewer" (qiv) is a GDK/Imlib image viewer similar to
viewers like xv or xloadimage. qiv features setting an image as an
x11 background with a user-definable background color, fullscreen
viewing, a screensaver mode, brightness/contrast/gamma correction,
real transparency, zoom and slideshow.

It creates only one window, containing only the image to view.

%prep
%autosetup -p1 -n qiv

%build
export RPM_OPT_FLAGS="%{optflags}"
%make_build

%install
install -Dpm 755 qiv %{buildroot}%{_bindir}/qiv
install -Dpm 644 qiv.1 %{buildroot}%{_mandir}/man1/qiv.1
install -Dpm 0644 qiv.png %{buildroot}%{_datadir}/pixmaps/qiv.png
install -Dpm 0644 qiv.desktop %{buildroot}%{_datadir}/applications/qiv.desktop
%suse_update_desktop_file qiv

%files
%license README.COPYING
%doc README README.TODO contrib
%{_bindir}/qiv
%{_mandir}/man1/qiv.1%{?ext_man}
%{_datadir}/pixmaps/qiv.png
%{_datadir}/applications/qiv.desktop

%changelog
