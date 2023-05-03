#
# spec file for package MyGUI
#
# Copyright (c) 2023 SUSE LLC
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


%define capname MYGUI
%define _sover  3_4_1
Name:           MyGUI
Version:        3.4.1
Release:        0
Summary:        A GUI library for Ogre Rendering Engine
License:        MIT
Group:          Development/Tools/GUI Builders
URL:            http://mygui.info/
Source:         https://github.com/MyGUI/mygui/archive/MyGUI%{version}.tar.gz
Source1:        %{name}.png
Source99:       %{name}-rpmlintrc
# PATCH-FIX-UPSTREAM MyGUI-install-libCommon.patch -- https://github.com/MyGUI/mygui/pull/233
Patch0:         MyGUI-install-libCommon.patch
# PATCH-FIX-UPSTREAM 0001-Fix-linking-with-Wl-no-undefined.patch -- https://github.com/MyGUI/mygui/pull/232
Patch1:         0001-Fix-linking-with-Wl-no-undefined.patch
# PATCH-FIX-UPSTREAM mygui-add-missing-include.patch -- Add missing include
Patch2:         mygui-add-missing-include.patch
BuildRequires:  cmake
BuildRequires:  dejavu
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libOIS-devel
BuildRequires:  libX11-devel
BuildRequires:  libboost_system-devel
BuildRequires:  ogre-devel
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(uuid)

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

%package -n libMyGUICommon%{_sover}
Summary:        Shared library for MyGUI
Group:          System/Libraries

%description -n libMyGUICommon%{_sover}
MyGUI is a library for creating Graphical User Interfaces (GUIs)
for games and 3D applications.

This package contains the shared library used by most MyGUI tools and demos.

%package tools
Summary:        Tools applications for MyGUI
Group:          Development/Tools/GUI Builders
Requires:       %{name} = %{version}

%description tools
MyGUI is a library for creating Graphical User Interfaces (GUIs)
for games and 3D applications.

This package contains tools applications for package MyGUI.

%package devel
Summary:        Development files for MyGUI
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       libMyGUICommon%{_sover} = %{version}
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
%autopatch -p1

%build
%cmake \
  -DMYGUI_STATIC=OFF \
  -DMYGUI_USE_FREETYPE=ON \
  -DMYGUI_BUILD_PLUGINS=ON \
  -DMYGUI_BUILD_TOOLS=ON \
  -DMYGUI_BUILD_WRAPPER=OFF \
  -DMYGUI_INSTALL_TOOLS=ON \
  -DMYGUI_INSTALL_DEMOS=ON \
  -DMYGUI_INSTALL_DOCS=ON \
  -DMYGUI_INSTALL_MEDIA=ON \
  -DMYGUI_FULL_RPATH=OFF \
  -DCMAKE_SKIP_RPATH=ON \
  -DCMAKE_BUILD_TYPE=release \
  -DOGRE_CONFIG_DIR=%{_datadir}/OGRE

%cmake_build

pushd ../Docs
  doxygen -s -g Doxyfile 2> /dev/null
  doxygen Doxyfile
popd

%install
%cmake_install

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
sed -i -e 's|PluginFolder=%{_prefix}/local/lib/OGRE|%{_libdir}/OGRE|g' %{buildroot}%{_datadir}/%{capname}/plugins.cfg

# wrapper-script for binaries
cat > %{name}.sh <<EOF
#!/bin/bash
if [[ -z "\$1" ]]; then
  echo "missing parameter..."
  echo ""
  echo "usage:"
  echo "\$0 LayoutEditor"
  echo "\$0 ImageSetViewer"
  echo "\$0 FontViewer"
  echo ""
  echo "or one of the installed demo applications:"
  ls -1 %{_bindir}/%{name}-Demo_* | sed -e 's|%{_bindir}/||g'
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
exec "%{_bindir}/\$1"
EOF
install -m 755 -t %{buildroot}%{_bindir} %{name}.sh

# use system fonts
pushd %{buildroot}%{_datadir}/%{capname}/Media/MyGUI_Media
  ln -sf %{_datadir}/fonts/truetype/DejaVuSans.ttf .
  ln -sf %{_datadir}/fonts/truetype/DejaVuSans-ExtraLight.ttf .
popd

# icon
install -D -m 644 -t %{buildroot}%{_datadir}/pixmaps %{SOURCE1}

# menu-entries
for i in FontEditor ImageEditor LayoutEditor SkinEditor; do
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

%fdupes -s %{buildroot}

%post -n libMyGUIEngine%{_sover} -p /sbin/ldconfig
%postun -n libMyGUIEngine%{_sover} -p /sbin/ldconfig

%post -n libMyGUICommon%{_sover} -p /sbin/ldconfig
%postun -n libMyGUICommon%{_sover} -p /sbin/ldconfig

%files
%doc README.md
%license COPYING.MIT
%{_libdir}/Plugin_*.so
%{_datadir}/%{capname}/
%exclude %{_datadir}/%{capname}/Media/Demos/
%exclude %{_datadir}/%{capname}/Media/Tools/

%files devel
%{_includedir}/%{capname}/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%files devel-doc
%doc Docs/html/*

%files -n libMyGUIEngine%{_sover}
%{_libdir}/libMyGUIEngine.so.*

%files -n libMyGUICommon%{_sover}
%{_libdir}/libMyGUICommon.so.*

%files demo
%{_bindir}/%{name}-Demo_*
%{_datadir}/%{capname}/Media/Demos/

%files tools
%{_bindir}/%{name}.sh
%{_bindir}/FontEditor
%{_bindir}/ImageEditor
%{_bindir}/LayoutEditor
%{_bindir}/SkinEditor
%{_datadir}/%{capname}/Media/Tools/
%{_datadir}/applications/FontEditor.desktop
%{_datadir}/applications/ImageEditor.desktop
%{_datadir}/applications/LayoutEditor.desktop
%{_datadir}/applications/SkinEditor.desktop
%{_datadir}/pixmaps/*.png

%changelog
