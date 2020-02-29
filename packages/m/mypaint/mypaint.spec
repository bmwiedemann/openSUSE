#
# spec file for package mypaint
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

%define skip_python2 1
Name:           mypaint
Version:        2.0.0
Release:        0
Summary:        Graphics application for digital painters
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            http://mypaint.org
Source:         https://github.com/mypaint/mypaint/releases/download/v%{version}/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM mypaint-python3-pass-str-to-exec.patch badshah400@gmail.com -- Fix build with python3 by passing a str object as the first arg to exec instead of an open file object
Patch0:         mypaint-python3-pass-str-to-exec.patch
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  python3-cairo-devel
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-numpy >= 1.5
BuildRequires:  python3-numpy-devel
BuildRequires:  python3-setuptools
BuildRequires:  python-rpm-macros
BuildRequires:  librsvg
BuildRequires:  swig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libmypaint) >= 1.5.0
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(mypaint-brushes-2.0) >= 2.0.2
BuildRequires:  pkgconfig(pygobject-3.0)
Requires:       python3-numpy >= 1.7
Requires:       python3-gobject-Gdk
Recommends:     %{name}-lang = %{version}
Recommends:     mypaint-brushes >= 2.0.2
%lang_package

%description
MyPaint is a graphics application for digital painters. It supports
graphics tablets made by Wacom, and many similar devices. The
standard brushes can emulate traditional media like charcoal,
pencils, ink, or paint.

%prep
%autosetup -p1

%build
%python_build 

%install
%python_install

%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_libexecdir}/%{name}/

%check
python3 setup.py test

%files
%doc Changelog.md README.md
%license COPYING Licenses.md
%{_bindir}/%{name}
%{_datadir}/mypaint/
%{_datadir}/icons/hicolor/*/*/*.*
%{_libexecdir}/mypaint/
%{_datadir}/thumbnailers/
%{_bindir}/mypaint-ora-thumbnailer
%{_datadir}/metainfo/mypaint.appdata.xml
%{_datadir}/applications/mypaint.desktop

%files lang -f %{name}.lang

%changelog
