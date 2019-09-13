#
# spec file for package icc-examin
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           icc-examin
Version:        0.56
Release:        0
Summary:        ICC profile viewer and colour visualisation
License:        (GPL-2.0+ AND SUSE-FLTK) AND BSD-2-Clause
Group:          Productivity/Graphics/Other
Url:            http://www.oyranos.org/icc-examin
Source:         %{name}_%{version}.orig.tar.bz2
Patch0:         icc-examin-gcc7.patch
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  expat
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liboyranos-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  xdg-utils
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(ftgl)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(oyranos)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcm)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(zlib)
Requires:       oyranos
Requires:       oyranos-monitor
Requires:       oyranos-profile-graph
Requires:       oyranos-ui-fltk
Requires(post): shared-mime-info
Requires(postun): shared-mime-info
Recommends:     %{name}-lang
Recommends:     freefont
Recommends:     oyranos-qcmsevents
Obsoletes:      icc_examin <= 0.54
Provides:       icc_examin = %{version}

%description
ICC Examin is a small utility (unix name: iccexamin) for the
purpose of watching the internals of ICC profiles, measurement
data (CGATS), colour samples (named colour profiles), gamut
visualisations (vrml), video card gamma tables (Xorg/XFree86/osX).

%lang_package

%prep
%setup -q
%patch0 -p1

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install
%find_lang icc-examin       # generate a special file list
find %{buildroot} -type f -name "*.ttf" -delete -print
%suse_update_desktop_file -n  iccexamin # some openSUSE magic

%post
%mime_database_post

%postun
%mime_database_postun

%files lang -f %{name}.lang

%files
%doc AUTHORS COPYING ChangeLog.md README.md
%{_bindir}/iccexamin
%{_datadir}/applications/iccexamin.desktop
%{_datadir}/pixmaps/iccexamin.svg
%{_mandir}/man1/iccexamin.1%{ext_man}

%changelog
