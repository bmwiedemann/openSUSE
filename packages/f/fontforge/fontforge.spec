#
# spec file for package fontforge
#
# Copyright (c) 2023 SUSE LLC
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


Name:           fontforge
Version:        20230101
Release:        0
Summary:        A Font Editor
License:        GPL-3.0-or-later
URL:            https://fontforge.org/
Source0:        https://github.com/fontforge/fontforge/archive/%{version}.tar.gz
# workaround for bug 930076, imho upstream should fix this
# https://github.com/fontforge/fontforge/issues/2270
Patch0:         fontforge-version.patch
Patch2:         fix-sphinx-doc.patch
Patch5:         add-bitmap-transform-support.patch
BuildRequires:  cairo-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  giflib-devel
BuildRequires:  git
BuildRequires:  gtk3-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  pango-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  python3-devel
BuildRequires:  readline-devel
BuildRequires:  update-desktop-files
BuildRequires:  woff2-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xi)
%if 0%{?suse_version} > 1210
BuildRequires:  libspiro-devel
%endif

%description
FontForge allows editing of outline and bitmap fonts.  With it, you can
create new fonts or modify old ones.  It also converts font formats and
can convert among PostScript (ASCII & binary Type 1, some Type 3s, and
some Type 0s), TrueType, OpenType (Type2), and CID-keyed fonts.

%package doc
Summary:        Documentation for FontForge
%if 0%{?suse_version} >= 1230
BuildArch:      noarch
%endif

%description doc
FontForge allows editing of outline and bitmap fonts. With it, you can
create new fonts or modify old ones. It also converts font formats and
can convert among PostScript, TrueType, OpenType, and CID-keyed fonts.

This subpackage contains the documentation to FontForge.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Requires:       %{name} = %{version}
Requires:       freetype2-devel

%description devel
FontForge allows editing of outline and bitmap fonts. With it, you can
create new fonts or modify old ones. It also converts font formats and
can convert among PostScript, TrueType, OpenType, and CID-keyed fonts.

This subpackage contains all necessary include files and libraries needed
to develop applications that use FontForge libraries.

%prep
%setup -q
%patch0 -p1
%if %{?suse_version} < 1550
%patch2 -p1
%endif
%patch5 -p1

%build
%cmake \
    -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name}/html

%install
%cmake_install
%suse_update_desktop_file -i org.fontforge.FontForge VectorGraphics
%find_lang FontForge
find %{buildroot} -type f -name "*.la" -delete -print
rm %{buildroot}%{_docdir}/%{name}/html/.buildinfo
rm %{buildroot}%{_docdir}/%{name}/html/.nojekyll
%fdupes -s %{buildroot}%{_datadir}/%{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f FontForge.lang
%license LICENSE COPYING.gplv3
%exclude %{_docdir}/%{name}/html
%{_mandir}/man1/*.1%{?ext_man}
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_datadir}/fontforge/
%{python3_sitearch}/*
%{_datadir}/applications/org.fontforge.FontForge.desktop
%{_datadir}/icons/hicolor/*/apps/org.fontforge.FontForge.png
%{_datadir}/icons/hicolor/scalable/apps/org.fontforge.FontForge.svg
%{_datadir}/metainfo/org.fontforge.FontForge.*.xml
# %{_datadir}/pixmaps/org.fontforge.FontForge.*
%{_datadir}/mime/packages/%{name}.xml
%dir %{_docdir}/fontforge

%files doc
%license LICENSE
%doc AUTHORS README.md
%doc %{_docdir}/%{name}/html

%files devel
%doc CONTRIBUTING.md
%{_libdir}/lib*.so

%changelog
