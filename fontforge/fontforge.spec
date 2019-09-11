#
# spec file for package fontforge
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


Name:           fontforge
Version:        20170731
Release:        0
Summary:        A Font Editor
License:        GPL-3.0+
Group:          Productivity/Graphics/Vector Editors
Url:            http://fontforge.org/
#       Source: https://github.com/fontforge/fontforge/archive/%{version}.tar.gz
#           see bug 926061, fontforge-*-repacked.tar.xz does not contain fontforge-*/win/gold/libX11-*.noarch.rpm
Source0:        fontforge-%{version}-repacked.tar.xz
Source1:        get-source.sh
# workardound for bug 930076, imho upstream should fix this
# https://github.com/fontforge/fontforge/issues/2270
Patch0:         fontforge-version.patch
# PATCH-FIX-UPSTREAM bmwiedemann https://github.com/fontforge/fontforge/pull/3152
Patch1:         reproducible.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  cairo-devel
BuildRequires:  fdupes
BuildRequires:  fontconfig-devel
BuildRequires:  freetype2-devel
BuildRequires:  gettext-tools
BuildRequires:  giflib-devel
BuildRequires:  git
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  libuninameslist-devel
BuildRequires:  libxml2-devel
BuildRequires:  pango-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-devel
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xi)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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
Group:          Documentation/HTML
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
Group:          Development/Libraries/C and C++
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
%patch0
%patch1 -p1
sed -i 's/\r$//' doc/html/{Big5.txt,corpchar.txt}
# workaround for bug 930076; we just need the _version_of_the_release_! (see also fontforge-version.patch) ---
grep 'doversion(FONTFORGE_MODTIME_STR)' fontforgeexe/startnoui.c && \
sed -i 's:FONTFORGE_MODTIME_STR:"%{version}":' fontforgeexe/startnoui.c
grep 'doversion(FONTFORGE_MODTIME_STR)' fontforgeexe/startui.c && \
sed -i 's:FONTFORGE_MODTIME_STR:"%{version}":' fontforgeexe/startui.c
# ---

%build
./bootstrap --force
%configure \
    --disable-static \
    --enable-pyextension \
    --with-regular-link \
    --docdir=%{_docdir}/%{name}/html
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%suse_update_desktop_file -i %{name} VectorGraphics
%find_lang FontForge
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes -s %{buildroot}%{_datadir}/%{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f FontForge.lang
%defattr(-,root,root)
%doc LICENSE COPYING.gplv3
%exclude %{_docdir}/%{name}/html
%{_mandir}/man1/*.1*
%{_bindir}/*
%{_libdir}/lib*.so.*
%{_datadir}/fontforge/
%{python3_sitearch}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/mime/packages/%{name}.xml

%files doc
%defattr(-,root,root)
%doc AUTHORS LICENSE README.md
%doc %{_docdir}/%{name}/html

%files devel
%defattr(-, root, root)
%doc CONTRIBUTING.md
%{_includedir}/fontforge/
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

%changelog
