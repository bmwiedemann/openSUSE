#
# spec file for package tupitube
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016 Packman Team <packman@links2linux.de>
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


%define	_qtdir    %{_libdir}/qt5/
%define	_tupibin  %{_libdir}/%{name}/bin
%define	_tupilib  %{_libdir}/%{name}
%define	_tupidata %{_datadir}/%{name}
Name:           tupitube
Version:        0.2.13
Release:        0
Summary:        2D vectorial/animation tool
License:        GPL-2.0-or-later
Group:          Productivity/Graphics/Vector Editors
URL:            https://maefloresta.com
Source0:        https://sourceforge.net/projects/tupi2d/files/Source%20Code/tupitube.desk-%{version}.tar.gz
Patch0:         tupitube.quazip5.patch
Patch1:         tupitube.libav.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libquazip-qt5-devel
BuildRequires:  pkgconfig
BuildRequires:  ruby
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.0
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-plugins
Requires:       ffmpeg
Requires:       %(rpm -qf $(readlink -qne %{_libdir}/libogg.so) --qf '%%{NAME} >= %%{VERSION}')
Requires:       %(rpm -qf $(readlink -qne %{_libdir}/libtheora.so) --qf '%%{NAME} >= %%{VERSION}')
Provides:       ktoon = %{version}
Obsoletes:      ktoon < %{version}
Provides:       tupi = %{version}
Obsoletes:      tupi < %{version}

%description
Tupitube is a design and authoring tool for digital artists
interested in 2D animation. Its source code is based on the KTooN
project.

Some of its main features are: basic illustration tools (shapes, fill,
text), gradient tools, onion skin, brushes editor, pencil with smoothness
support and a basic object library (for SVG files and raster images).

Using its modules of animation and reproduction, 2D projects can be exported
to several formats such as OGG, MPEG, AVI, MOV and SWF. Additionally, the
option of exporting image arrays as output is available.

%package        plugins
Summary:        Tupi plugins
Group:          Productivity/Graphics/Vector Editors
Requires:       %{name} = %{version}

%description    plugins
A design and authoring tool for 2D animation.

This package contains plugins for %{name}.

%prep
%setup -q -n tupitube.desk
%patch0 -p1
%patch1 -p1

# Add path to ffmpeg
ffmpeg_include=$(pkg-config --cflags-only-I libavutil)
find . -type f -name \*.pro | while read f; do
echo "QMAKE_CXXFLAGS += %{optflags} ${ffmpeg_include}" >> "$f"
done

%build
%configure \
	--with-qtdir=%{_qtdir} \
	--bindir=%{_tupibin} \
	--libdir=%{_tupilib} \
	--sharedir=%{_tupidata}

make %{?_smp_mflags}

%install
%make_install

# Create symbolic link
install -d %{buildroot}%{_bindir}
ln -s %{_tupibin}/%{name}.desk %{buildroot}%{_bindir}/%{name}
# Remove unneeded links
pushd %{buildroot}%{_tupilib}
for so in $(find . -maxdepth 1 -name \*.so); do
rm -f $so; done
popd
# SVG icon
install -Dm 0644 launcher/icons/icon.svg \
%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
# fix icon name
mv %{buildroot}%{_datadir}/pixmaps/%{name}.desk.png \
%{buildroot}%{_datadir}/pixmaps/%{name}.png
# fix .desktop
sed -i -e '/^Exec/cExec=%{name}' -e '/^Icon/cIcon=%{name}' \
%{buildroot}%{_datadir}/applications/%{name}.desktop

%fdupes %{buildroot}%{_datadir}

%if 0%{?suse_version} < 1500
%post
%mime_database_post
%icon_theme_cache_post
%desktop_database_post

%postun
%mime_database_postun
%icon_theme_cache_postun
%desktop_database_postun
%endif

%files
%license COPYING
%doc README*
%{_bindir}/%{name}
%{_tupibin}/
%dir %{_tupilib}
%{_tupilib}/*.so.*
%{_tupidata}/
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%exclude %{_tupilib}/plugins

%files plugins
%dir %{_tupilib}/plugins
%{_tupilib}/plugins/*.so

%changelog
