#
# spec file for package MyGUI
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014 B1 Systems GmbH, Vohburg, Germany.
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


%define capname	MYGUI
%define _major	3.2
%define _minor	2
%define _sover	3
Name:           MyGUI
Version:        %{_major}.%{_minor}
Release:        0
Summary:        A GUI library for Ogre Rendering Engine
License:        MIT
Group:          Development/Tools/GUI Builders
Url:            http://mygui.info/
Source:         https://github.com/MyGUI/mygui/archive/MyGUI%{version}.tar.gz
Source1:        %{name}.png
# PATCH-FIX-UPSTREAM MyGUI-lib_suffix.patch
Patch0:         %{name}-lib_suffix.patch
# PATCH-FIX-UPSTREAM MyGUI-gcc47-visibility.patch
Patch1:         %{name}-gcc47-visibility.patch
# PATCH-FIX-OPENSUSE MyGUI-freetype2-include.patch
Patch2:         MyGUI-freetype2-include.patch
# PATCH-FIX-UPSTREAM MyGUI-libCommon-fixup.patch -- https://github.com/MyGUI/mygui/issues/157
Patch3:         MyGUI-libCommon-fixup.patch
BuildRequires:  cmake
BuildRequires:  dejavu
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libOIS-devel
BuildRequires:  libOgreMain-devel
BuildRequires:  libX11-devel
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(uuid)

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
MyGUI is a library for creating Graphical User Interfaces (GUIs)
for games and 3D applications.

MyGUI has overlays for text and for simple rectangles, allowing
uniting them in one batch.

The library supports plugins that allow you to create
dynamically-loaded custom controls or subsystems. Most subsystems are
expandable with plugins without the need to touch the core code. All
resources and settings are described in XML files. It is possible to
load resources like fonts, cursors, images, skins, etc. Forms
(layouts) via dynamically by using XML files.

This package contains ImageSetViewer and LayoutEditor.

%package demo
Summary:        Some demo applications for MyGUI
Group:          Development/Tools/GUI Builders
Requires:       %{name} = %{version}

%description demo
MyGUI is a library for creating Graphical User Interfaces (GUIs)
for games and 3D applications.

This package contains some demo applications for package MyGUI.

%package -n libMyGUIEngine%{_sover}
Summary:        Shared library for MyGUI
Group:          System/Libraries

%description -n libMyGUIEngine%{_sover}
MyGUI is a library for creating Graphical User Interfaces (GUIs)
for games and 3D applications.

This package contains the shared library for package MyGUI.

%package devel
Summary:        Development files for MyGUI
Group:          Development/Libraries/C and C++
Requires:       libMyGUIEngine%{_sover} = %{version}
Requires:       libOIS-devel
Requires:       libOgreMain-devel
Requires:       pkgconfig
Requires:       pkgconfig(freetype2)
Requires:       pkgconfig(uuid)

%description devel
MyGUI is a library for creating Graphical User Interfaces (GUIs)
for games and 3D applications.

This subpackage contains libraries and header files for developing
applications that want to make use of MyGUI.

%package devel-doc
Summary:        Development documentation for MyGUI
Group:          Documentation/HTML
BuildArch:      noarch

%description devel-doc
MyGUI is a library for creating Graphical User Interfaces (GUIs)
for games and 3D applications.

This subpackage contains the development documentation for MyGUI.

%prep
%setup -q -n mygui-%{name}%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0

dos2unix     *.txt COPYING.MIT
chmod 644 *.txt COPYING.MIT

%build
install -dm 755 build
# this is probably an error in OGRE packaging... but let's just fix the build.
export OGRE_LIBRARIES="`pkg-config --libs OGRE` -lboost_system"
%cmake \
	-DCMAKE_BUILD_TYPE=release \
	-DOGRE_LIBRARIES="$OGRE_LIBRARIES" \
	-DMYGUI_STATIC=FALSE \
	-DMYGUI_USE_FREETYPE=TRUE \
	-DMYGUI_BUILD_SAMPLES=TRUE \
	-DMYGUI_BUILD_PLUGINS=TRUE \
	-DMYGUI_BUILD_TOOLS=TRUE \
	-DMYGUI_BUILD_WRAPPER=FALSE \
	-DMYGUI_INSTALL_SAMPLES=TRUE \
	-DMYGUI_INSTALL_TOOLS=TRUE \
	-DMYGUI_INSTALL_DOCS=TRUE \
	-DMYGUI_INSTALL_MEDIA=TRUE \
	-DMYGUI_INSTALL_SAMPLES_SOURCE=TRUE \
	-DMYGUI_FULL_RPATH=FALSE

make %{?_smp_mflags} V=1

pushd ../Docs
	doxygen -s -g Doxyfile 2> /dev/null
	doxygen Doxyfile
popd

%install
pushd build
%make_install
# Install libCommon manually as cmake does not install it
cp -a %{_lib}/libCommon.so* %{buildroot}%{_libdir}/
popd

# rename demos to avoid duplicate names with other packages
pushd %{buildroot}%{_bindir}
	demos=`ls -1 Demo_*`
	for i in $demos; do
		mv $i %{name}-$i
	done
popd

# move those files to /usr/share/MYGUI
mv %{buildroot}%{_bindir}/plugins.cfg %{buildroot}%{_datadir}/%{capname}
mv %{buildroot}%{_bindir}/resources.xml %{buildroot}%{_datadir}/%{capname}

# adjust OGRE path
sed -i -e 's|PluginFolder=/usr/local/lib/OGRE|%{_libdir}/OGRE|g' %{buildroot}%{_datadir}/%{capname}/plugins.cfg

# wrapper-script for binaries
cat > %{name}.sh <<EOF
#! /bin/bash
if [ -z "\$1" ]; then
	echo "missing parameter..."
	echo ""
	echo "usage:"
	echo "\$0 LayoutEditor"
	echo "\$0 ImageSetViewer"
	echo "\$0 FontViewer"
	echo ""
	echo "or one of the installed demo applications:"
	myDemos=\`ls -1 %{_bindir}/%{name}-Demo_*\`
	echo \$myDemos | sed -e 's|%{_bindir}/||g'
	exit 1
fi

# create local working directory
mkdir -p \$HOME/.%{name}

# link the resources to local dir
# just in case some new files appear (update)
ln -sf %{_datadir}/%{capname}/Media \$HOME/.%{name}

if [ ! -f \$HOME/.%{name}/plugins.cfg ]; then
	# config should be user writeable
	cp %{_datadir}/%{capname}/plugins.cfg \$HOME/.%{name}
fi
if [ ! -f \$HOME/.%{name}/resources.xml ]; then
	cp %{_datadir}/%{capname}/resources.xml \$HOME/.%{name}
fi

# call binary from local working-directory
cd \$HOME/.%{name}
%{_bindir}/\$1
EOF
install -m 755 %{name}.sh \
	%{buildroot}%{_bindir}

# use system fonts
pushd %{buildroot}%{_datadir}/%{capname}/Media/MyGUI_Media
	ln -sf %{_datadir}/fonts/truetype/DejaVuSans.ttf .
	ln -sf %{_datadir}/fonts/truetype/DejaVuSans-ExtraLight.ttf .
popd

# icon
install -dm 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 %{SOURCE1} \
	%{buildroot}%{_datadir}/pixmaps

# menu-entries
for i in LayoutEditor ImageSetViewer FontViewer; do
	cat > $i.desktop << EOF
[Desktop Entry]
Name=MyGUI $i
GenericName=MyGUI $i
Comment=%{name} $i
Exec=%{name}.sh $i
Icon=%{name}
Terminal=false
Type=Application
EOF
	%suse_update_desktop_file -i $i Development GUIDesigner
done

# remove unwanted files
rm -r %{buildroot}%{_datadir}/%{capname}/Media/UnitTests
rm -r %{buildroot}%{_datadir}/%{capname}/Media/Wrapper/WrapperBaseApp
# don't ask me where this file went, it vanished with 12.1...
# for now simply ignore the error... :-)
rm Docs/html/installdox || true

%fdupes -s %{buildroot}

%post -n libMyGUIEngine%{_sover} -p /sbin/ldconfig
%postun -n libMyGUIEngine%{_sover} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc *.txt 
%license COPYING.MIT
%{_bindir}/%{name}.sh
%{_bindir}/FontEditor
%{_bindir}/ImageEditor
%{_bindir}/LayoutEditor
%{_bindir}/SkinEditor
%{_libdir}/libCommon.so.*
%dir %{_datadir}/%{capname}
%{_datadir}/%{capname}/*.cfg
%{_datadir}/%{capname}/*.xml
%dir %{_datadir}/%{capname}/Media
%{_datadir}/%{capname}/Media/Common/
%{_datadir}/%{capname}/Media/MyGUI_Media/
%dir %{_datadir}/%{capname}/Media/Tools
%dir %{_datadir}/%{capname}/Media/Tools/LayoutEditor
%dir %{_datadir}/%{capname}/Media/Tools/LayoutEditor/CodeTemplates
%{_datadir}/%{capname}/Media/Tools/FontEditor
%{_datadir}/%{capname}/Media/Tools/ImageEditor
%{_datadir}/%{capname}/Media/Tools/EditorFramework
%{_datadir}/%{capname}/Media/Tools/LayoutEditor/B*
%{_datadir}/%{capname}/Media/Tools/LayoutEditor/CodeGeneratorWindow.layout
%{_datadir}/%{capname}/Media/Tools/LayoutEditor/CodeTemplates/BaseLayoutCPP.xml
%{_datadir}/%{capname}/Media/Tools/LayoutEditor/E*
%{_datadir}/%{capname}/Media/Tools/LayoutEditor/I*
%{_datadir}/%{capname}/Media/Tools/LayoutEditor/M*
%{_datadir}/%{capname}/Media/Tools/LayoutEditor/P*
%{_datadir}/%{capname}/Media/Tools/LayoutEditor/S*
%{_datadir}/%{capname}/Media/Tools/LayoutEditor/T*
%{_datadir}/%{capname}/Media/Tools/LayoutEditor/W*
%{_datadir}/%{capname}/Media/Tools/SkinEditor
%{_datadir}/applications/FontViewer.desktop
%{_datadir}/applications/ImageSetViewer.desktop
%{_datadir}/applications/LayoutEditor.desktop
%{_datadir}/pixmaps/*.png

%files devel
%defattr(-,root,root)
%dir %{_includedir}/%{capname}
%{_includedir}/%{capname}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/%{capname}/Media/Tools/LayoutEditor/CodeTemplates/BaseLayoutTemplate.cpp
%{_datadir}/%{capname}/Media/Tools/LayoutEditor/CodeTemplates/BaseLayoutTemplate.h

%files devel-doc
%defattr(-,root,root)
%doc Docs/html/*

%files -n libMyGUIEngine%{_sover}
%defattr(-,root,root)
%{_libdir}/libMyGUIEngine.so.*

%files demo
%defattr(-,root,root)
%{_bindir}/%{name}-Demo_*
%{_datadir}/%{capname}/Media/Demos/

%changelog
