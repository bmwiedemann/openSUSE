#
# spec file for package librecad
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


%define tar_version 2.2.0

Name:           librecad
Version:        2.2.0
Release:        0
Summary:        Computer-aided design (CAD) software package for 2D design and drafting
License:        (Apache-2.0 OR SUSE-GPL-3.0+-with-font-exception) AND GPL-2.0-only
Group:          Productivity/Graphics/CAD
URL:            http://librecad.org/

#Git-Web:       https://github.com/LibreCAD/LibreCAD
Source:         https://github.com/LibreCAD/LibreCAD/archive/%tar_version.tar.gz
# Version is actually 8, not 3 (it is 3 in the filename due to how MediaWiki
# works -- see http://wiki.librecad.org/index.php/File:Architect3-LCAD.zip)
Source2:        https://wiki.librecad.org/images/d/d9/Architect3-LCAD.zip
Source3:        https://wiki.librecad.org/images/7/70/Electronics3-LCAD.zip
Source4:        https://wiki.librecad.org/images/9/9d/Electrical1-LCAD.zip
Source10:       ttf2lff.1
Source20:       %name-rpmlintrc
Patch4:         librecad-no-date.diff
Patch5:         librecad-use-system-libdxfrw.patch
Patch6:         librecad-install.diff
Patch7:         librecad-plugindir.diff
Patch8:         librecad-use-system-shapelib.patch
BuildRequires:  fdupes
BuildRequires:  freetype2-devel
BuildRequires:  gcc-c++ >= 4.7
BuildRequires:  libboost_headers-devel
BuildRequires:  libshp-devel
BuildRequires:  muparser-devel
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  wqy-microhei-fonts
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libdxfrw) >= 1
Requires(post): desktop-file-utils
Requires(post): shared-mime-info
Requires(postun):desktop-file-utils
Requires(postun):shared-mime-info
Recommends:     %name-parts

%description
LibreCAD is a Qt Computer-aided design (CAD) software package for 2D design
and drafting.

%package parts
Summary:        Parts collection for LibreCAD
Group:          Productivity/Graphics/CAD
Requires:       %name
BuildArch:      noarch

%description parts
Collection of parts for LibreCAD, a Qt application to design 2D
CAD drawings.

%prep
%setup -qn LibreCAD-%tar_version -a2 -a3 -a4
%autopatch -p1

pc="libdxfrw"
if ! pkg-config --exists "$pc"; then
	pc=libdxfrw0
fi
dxfrw_includedir=$(pkg-config --cflags-only-I "$pc" | sed 's|-I||g')

# Fix paths
sed -i 's|##LIBDIR##|%_libdir|g' librecad/src/lib/engine/rs_system.cpp
sed -i 's|$${DXFRW_INCLUDEDIR}|'"$dxfrw_includedir"'|g' librecad/src/src.pro
sed -i 's@LRELEASE="lrelease"@LRELEASE="lrelease-qt5"@' scripts/postprocess-unix.sh

# Make sure bundled libraries are not used
rm -rf libraries/libdxfrw
rm -rf plugins/importshp/shapelib

# Fix "wrong-file-end-of-line-encoding" rpmlint warning
sed -i 's/\r$//' licenses/{MIT,KST32B_v2,lc_opengost-fonts}.txt

%build
echo 'DISABLE_POSTSCRIPT = true' > librecad/src/custom.pri
qmake-qt5 \
librecad.pro CONFIG+="release" \
	QMAKE_CFLAGS+="%optflags" QMAKE_CXXFLAGS+="%optflags"
make %{?_smp_mflags}
rm -f unix/resources/fonts/wqy-unicode.lff
mkdir -p unix/resources/fonts
./unix/ttf2lff -L "Apache-2.0 or SUSE-GPL-3.0+-with-font-exception" \
	"%_datadir/fonts/truetype/wqy-microhei.ttc" \
	unix/resources/fonts/wqy-unicode.lff

%install
b="%buildroot"
# No make install :(
export BUILDDIR="$b/%_datadir/%name"
sh scripts/postprocess-unix.sh

install -Dpm0755 "unix/%name" "$b/%_bindir/%name"
install -Dpm0755 "unix/ttf2lff" "$b/%_bindir/ttf2lff"
install -Dpm0644 "desktop/%name.1" "$b/%_mandir/man1/%name.1"
p="$b/%_libdir/%name/plugins"
mkdir -p "$p"
install -Dpm0755 unix/resources/plugins/* "$p/"
cat desktop/librecad.desktop
perl -i -lpe 's{(MimeType=.*?);+$}{$1}' desktop/librecad.desktop
cat desktop/librecad.desktop
install -Dpm0644 "desktop/%name.desktop" "$b/%_datadir/applications/%name.desktop"
install -Dpm0644 "librecad/res/main/%name.png" "$b/%_datadir/pixmaps/%name.png"
install -Dpm0644 "desktop/%name.sharedmimeinfo" "$b/%_datadir/mime/packages/%name.xml"
install -Dpm0644 "%_sourcedir/ttf2lff.1" "$b/%_mandir/man1/"

install -d "$b/%_datadir/%name/library/architecture" \
	"$b/%_datadir/%name/library/electronics" \
	"$b/%_datadir/%name/library/electrical"
cp -a Architect8-LCAD "$b/%_datadir/%name/library/architecture/"
cp -a Electronic8-LCAD "$b/%_datadir/%name/library/electronics/"
cp -a Electrical1-LCAD "$b/%_datadir/%name/library/electrical/"

%suse_update_desktop_file -G "CAD Program" -r %name Graphics 2DGraphics VectorGraphics
# Fix rpmlint warning "invalid-desktopfile"
perl -pi -e "s|image/vnd.dxf|image/vnd.dxf;|" %buildroot%_datadir/applications/librecad.desktop

%fdupes -s %buildroot/%_prefix

%if 0%{?suse_version} && 0%{?suse_version} < 1550
%post
%mime_database_post
%desktop_database_post

%postun
%mime_database_postun
%desktop_database_postun
%endif

%files
%doc README.md
%license LICENSE licenses/*txt
%_bindir/librecad
%_bindir/ttf2lff
%_libdir/%name
%_mandir/man1/librecad.1*
%_mandir/man1/ttf2lff.1*
%_datadir/applications/librecad.desktop
%_datadir/mime/packages/%name.xml
%_datadir/pixmaps/librecad.png
%dir %_datadir/%name
%_datadir/%name/fonts
%_datadir/%name/patterns
%_datadir/%name/qm

%files parts
%dir %_datadir/%name
%_datadir/%name/library

%changelog
