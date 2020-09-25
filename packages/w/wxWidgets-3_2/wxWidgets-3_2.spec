#
# spec file for package wxWidgets-3_2
#
# Copyright (c) 2020 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == ""
Name:           wxWidgets-3_2
ExclusiveArch:  do_not_build
%endif

%if "%{flavor}" == "GTK2"
Name:           wxWidgets-3_2
%define pkgname wxWidgets-3_2
%define variant suse
%define gtk_version 2
%define toolkit gtk%gtk_version
%define base_packages 0
%bcond_with webview
%endif

%if "%{flavor}" == "GTK3"
Name:           wxGTK3-3_2
%define pkgname wxGTK3-3_2
%define variant suse
%define gtk_version 3
%define toolkit gtk%gtk_version
# build non-UI toolkit related packages
%define base_packages 1
%bcond_without webview
%endif

%if "%{flavor}" == "GTK3-nostl"
Name:           wxWidgets-3_2-nostl
%define pkgname wxWidgets-3_2-nostl
%define variant suse-nostl
%define gtk_version 3
%define toolkit gtk%gtk_version
%define base_packages 1
%bcond_with webview
%define extra_description This variant of wxWidgets is built without STL types (such as \
std::string), and is provided for old programs which fail to use e.g. \
wxString and instead rely on the wxChar pointer API.
%endif

%if "%{flavor}" == "Qt"
Name:           wxQt-3_2
%define pkgname wxQt-3_2
%define variant suse
%define toolkit qt
%define base_packages 0
%bcond_with webview
%endif

%define base_name wxWidgets-3_2
%define tarball_name wxWidgets
# Use default debug level, enabling exceptions
# Other valid values: yes/no/max
%define wx_debug %{nil}
%define psonum 4_0_0
%define sonum 4.0.0
Version:        3.1.4
Release:        0
%define wx_minor 3.1
%define wx_micro 3.1.4
Summary:        C++ Library for Cross-Platform Development
License:        LGPL-2.1-or-later WITH WxWindows-exception-3.1
Group:          Development/Libraries/C and C++
URL:            https://www.wxwidgets.org/
Source:         https://github.com/wxWidgets/wxWidgets/releases/download/v%{version}/wxWidgets-%{version}.tar.bz2#/%tarball_name-%version.tar.bz2
Source2:        README.SUSE
Source5:        wxWidgets-3_2-rpmlintrc
# This script is not used during build, but it makes possible to
# identify and backport wxPython fixes to wxWidgets.
Source6:        wxpython-mkdiff.sh
Patch1:         soversion.diff
BuildRequires:  autoconf
BuildRequires:  cppunit-devel
BuildRequires:  gcc-c++
BuildRequires:  gstreamer-devel
BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  libSM-devel
BuildRequires:  libexpat-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmspack-devel
BuildRequires:  libnotify-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  zlib-devel
%if %{toolkit} == "gtk2"
BuildRequires:  gnome-vfs2-devel
BuildRequires:  gtk2-devel
%endif
%if %{toolkit} == "gtk3"
BuildRequires:  pkgconfig(gtk+-3.0)
%if %{with webview}
BuildRequires:  pkgconfig(webkit2gtk-4.0)
%endif
%endif
%if %{toolkit} == "qt"
BuildRequires:  pkgconfig(Qt5Core) >= 5.2.1
BuildRequires:  pkgconfig(Qt5Gui) >= 5.2.1
BuildRequires:  pkgconfig(Qt5OpenGL) >= 5.2.1
BuildRequires:  pkgconfig(Qt5Test) >= 5.2.1
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2.1
BuildRequires:  pkgconfig(cairo)
%endif
BuildRequires:  pkgconfig(glu)
BuildRequires:  pkgconfig(liblzma)
%if 0%{?sle_version} < 150000 && !0%{?is_opensuse}
BuildRequires:  pkgconfig(sdl)
%else
BuildRequires:  pkgconfig(sdl2)
%endif
BuildRequires:  pkgconfig(xtst)

%description
wxWidgets is a C++ library abstraction layer for a number of GUI
backends. Applications can be created for different GUIs (GTK+,
Motif, MS Windows, MacOS X, Windows CE, GPE) from the same source
code.

%package -n libwx_baseu-%variant%psonum
Summary:        wxWidgets base library
# Name up to openSUSE 11.3 and up to wxGTK-2.8:
Group:          System/Libraries
Obsoletes:      wxGTK <= %version.0
# Third party base package name:
Obsoletes:      wxWidgets < %version
Provides:       wxWidgets = %version
Recommends:     wxWidgets-lang >= 3.0

%description -n libwx_baseu-%variant%psonum
Every wxWidgets application must link against this library. It
contains mandatory classes that any wxWidgets code depends on (e.g.
wxString) and portability classes that abstract differences between
platforms. wxBase can be used to develop console-only applications.
%{?extra_description}

%package -n libwx_baseu_net-%variant%psonum
Summary:        wxWidgets networking library
Group:          System/Libraries

%description -n libwx_baseu_net-%variant%psonum
Classes for network access with wxWidgets.

%package -n libwx_baseu_xml-%variant%psonum
Summary:        wxWidgets XML parser library
Group:          System/Libraries

%description -n libwx_baseu_xml-%variant%psonum
This library contains classes for parsing XML documents.

%package -n libwx_%{toolkit}u_adv-%variant%psonum
Summary:        wxWidgets advanced widgets and rarely-used widgets
Group:          System/Libraries

%description -n libwx_%{toolkit}u_adv-%variant%psonum
Advanced or rarely-used GUI classes for wxWidgets.

%package -n libwx_%{toolkit}u_aui-%variant%psonum
Summary:        wxWidgets advanced user interface docking library
Group:          System/Libraries

%description -n libwx_%{toolkit}u_aui-%variant%psonum
The Advanced User Interface docking library of wxWidgets.

%package -n libwx_%{toolkit}u_core-%variant%psonum
Summary:        wxWidgets basic GUI class library
Group:          System/Libraries

%description -n libwx_%{toolkit}u_core-%variant%psonum
Basic GUI classes such as GDI classes or controls are in this
library. All wxWidgets GUI applications must link against this
library, only console mode applications need not.

%package -n libwx_%{toolkit}u_gl-%variant%psonum
Summary:        wxWidgets OpenGL integration library
Group:          System/Libraries

%description -n libwx_%{toolkit}u_gl-%variant%psonum
This library contains the wxGLCanvas class for integration of OpenGL
with wxWidgets.

%package -n libwx_%{toolkit}u_html-%variant%psonum
Summary:        wxWidgets HTML parser and renderer library
Group:          System/Libraries

%description -n libwx_%{toolkit}u_html-%variant%psonum
The wxHTML library provides classes for parsing and displaying HTML.
It is not intended to be a high-end HTML browser. wxHTML can be used
as a generic rich text viewer – for example, to display an About Box
or the result of a database search.
%{?extra_description}

%package -n libwx_%{toolkit}u_media-%variant%psonum
Summary:        wxWidgets media class library
Group:          System/Libraries

%description -n libwx_%{toolkit}u_media-%variant%psonum
wxMediaCtrl is a class for displaying types of media, such as videos,
audio files, natively through native codecs.

%package -n libwx_%{toolkit}u_propgrid-%variant%psonum
Summary:        wxWidgets property grid class library
Group:          System/Libraries

%description -n libwx_%{toolkit}u_propgrid-%variant%psonum
wxPropertyGrid is a specialized grid for editing properties, in other
words, name=value pairs.

%package -n libwx_%{toolkit}u_qa-%variant%psonum
Summary:        wxWidgets quality assurance class library
Group:          System/Libraries

%description -n libwx_%{toolkit}u_qa-%variant%psonum
This is the library containing extra classes for quality
assurance, containing the wxDebugReport class. wxDebugReport is
used to generate a debug report, containing information about the
program current state.

%package -n libwx_%{toolkit}u_ribbon-%variant%psonum
Summary:        wxWidgets's ribbon user interface library
Group:          System/Libraries

%description -n libwx_%{toolkit}u_ribbon-%variant%psonum
The wxRibbon library is a set of classes for writing a ribbon user
interface.

%package -n libwx_%{toolkit}u_richtext-%variant%psonum
Summary:        wxWidgets Rich Text editor class library
Group:          System/Libraries

%description -n libwx_%{toolkit}u_richtext-%variant%psonum
wxRichTextCtrl provides a generic implementation of a rich text
editor that can handle different character styles, paragraph
formatting, and images. It is intended for "natural" text in the
sense that source code is better served by wxStyledTextCtrl.

%package -n libwx_%{toolkit}u_stc-%variant%psonum
Summary:        wxWidgets styled text class library
Group:          System/Libraries

%description -n libwx_%{toolkit}u_stc-%variant%psonum
A wxWidgets implementation of the Scintilla source code editing component.

%package -n libwx_%{toolkit}u_webview-%variant%psonum
Summary:        wxWidgets HTML/browser class library
Group:          System/Libraries

%description -n libwx_%{toolkit}u_webview-%variant%psonum
Library for a wxWidgets control that can be used to render web
(HTML / CSS / JavaScript) documents.

%package -n libwx_%{toolkit}u_xrc-%variant%psonum
Summary:        wxWidgets's XML-based resource system
Group:          System/Libraries

%description -n libwx_%{toolkit}u_xrc-%variant%psonum
The XML-based resource system of wxWidgets, known as XRC, allows user
interface elements such as dialogs, menu bars and toolbars, to be
stored in text files and loaded into the application at run-time.

%package -n %{base_name}-plugin-sound_sdlu-3_2
Summary:        wxWidgets SDL Plugin
Group:          System/Libraries

%description -n %{base_name}-plugin-sound_sdlu-3_2
SDL based sound plugin for the wxWidgets cross-platform GUI.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
%if %{toolkit} == "gtk2"
Requires:       gtk2-devel
%endif
%if %{toolkit} == "gtk3"
Requires:       pkgconfig(gtk+-3.0)
%endif
%if %{toolkit} == "qt"
Requires:       pkgconfig(Qt5OpenGL) >= 5.2.1
Requires:       pkgconfig(Qt5Widgets) >= 5.2.1
%endif
Requires:       libwx_%{toolkit}u_adv-%variant%psonum = %version
Requires:       libwx_%{toolkit}u_aui-%variant%psonum = %version
Requires:       libwx_%{toolkit}u_core-%variant%psonum = %version
Requires:       libwx_%{toolkit}u_gl-%variant%psonum = %version
Requires:       libwx_%{toolkit}u_html-%variant%psonum = %version
Requires:       libwx_%{toolkit}u_media-%variant%psonum = %version
Requires:       libwx_%{toolkit}u_propgrid-%variant%psonum = %version
Requires:       libwx_%{toolkit}u_qa-%variant%psonum = %version
Requires:       libwx_%{toolkit}u_ribbon-%variant%psonum = %version
Requires:       libwx_%{toolkit}u_richtext-%variant%psonum = %version
Requires:       libwx_%{toolkit}u_stc-%variant%psonum = %version
%if %{with webview}
Requires:       libwx_%{toolkit}u_webview-%variant%psonum = %version
%endif
Requires:       libwx_%{toolkit}u_xrc-%variant%psonum = %version
Requires:       libwx_baseu-%variant%psonum = %version
Requires:       libwx_baseu_net-%variant%psonum = %version
Requires:       libwx_baseu_xml-%variant%psonum = %version
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glu)
Provides:       wxWidgets-any-devel
Conflicts:      wxWidgets-any-devel
%if %{toolkit} == "gtk2"
Provides:       wxGTK2-devel = %version-%release
Provides:       wxWidgets-devel = %version-%release
# Name up to openSUSE 11.3 and up to wxGTK-2.8.x:
Provides:       wxGTK-devel = %version-%release
Obsoletes:      wxGTK-devel < %version-%release
%endif
%if %{toolkit} == "gtk3"
%if "%{flavor}" != "GTK3-nostl"
Provides:       wxGTK3-devel = %version-%release
%endif
%endif
%if %{toolkit} == "qt"
Provides:       wxQt-devel = %version-%release
%endif

%description devel
wxWidgets is a C++ library abstraction layer for a number of GUI
backends. Applications can be created for different GUIs (GTK+,
Motif, MS Windows, MacOS X, Windows CE, GPE) from the same source
code.

This package contains all files needed for developing with %{name}.
%{?extra_description}

Note: wxWidgets variant devel packages are mutually exclusive. Please
read %_docdir/%name/README.SUSE to pick a correct variant.

%prep
%autosetup -n %tarball_name-%version -p1
cp %{S:2} .

%build
autoconf -f -i
# NOTE: gnome-vfs is deprecated. Disabled for GTK3 build
#
# With 2.9.1:
# --enable-objc_uniquifying is relevant only for Cocoa
# --enable-accessibility is currently supported only in msw
# --enable-extended_rtti does not compile

%configure \
	--enable-vendor=%variant \
%if %{toolkit} == "qt"
	--with-qt \
%else
	--with-gtk=%gtk_version \
%if %{gtk_version} == 2
	--with-gnomevfs \
%endif
%endif
	--enable-unicode \
	--with-opengl \
	--with-libmspack \
	--with-sdl \
	--enable-ipv6 \
	--enable-mediactrl \
	--enable-optimise \
	%{wx_debug:--enable-debug=%{wx_debug}} \
        --enable-repro-build \
%if "%{flavor}" == "GTK3-nostl"
	--disable-stl \
	--disable-plugins
%else
	--enable-stl \
	--enable-plugins
%endif

make %{?_smp_mflags}

%install
export VENDORTAG='-$variant' # only needed for non-MSW
make install DESTDIR="%buildroot"
%if !%base_packages
# Drop libraries already supplied by another packages
rm -f "%buildroot/%_libdir"/libwx_baseu{,_net,_xml}-%variant.so.%{sonum}* \
   "%buildroot/%_libdir/wx/%wx_micro"/sound_sdlu-*.so
%endif
rm -Rf %buildroot/%_datadir/locale

# HACK: Fix wx-config symlink (bug introduced in 2.9.4).
ln -sf $(echo %buildroot/%_libdir/wx/config/* | sed "s%%%buildroot%%%%") %buildroot/%_bindir/wx-config

%post   -n libwx_baseu-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_baseu-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_baseu_net-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_baseu_net-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_baseu_xml-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_baseu_xml-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_%{toolkit}u_adv-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_%{toolkit}u_adv-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_%{toolkit}u_aui-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_%{toolkit}u_aui-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_%{toolkit}u_core-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_%{toolkit}u_core-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_%{toolkit}u_gl-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_%{toolkit}u_gl-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_%{toolkit}u_html-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_%{toolkit}u_html-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_%{toolkit}u_media-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_%{toolkit}u_media-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_%{toolkit}u_propgrid-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_%{toolkit}u_propgrid-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_%{toolkit}u_qa-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_%{toolkit}u_qa-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_%{toolkit}u_ribbon-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_%{toolkit}u_ribbon-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_%{toolkit}u_richtext-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_%{toolkit}u_richtext-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_%{toolkit}u_stc-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_%{toolkit}u_stc-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_%{toolkit}u_webview-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_%{toolkit}u_webview-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_%{toolkit}u_xrc-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_%{toolkit}u_xrc-%variant%psonum -p /sbin/ldconfig

%if %base_packages
%files -n libwx_baseu-%variant%psonum
%_libdir/libwx_baseu-%variant.so.%{sonum}*

%files -n libwx_baseu_net-%variant%psonum
%_libdir/libwx_baseu_net-%variant.so.%{sonum}*

%files -n libwx_baseu_xml-%variant%psonum
%_libdir/libwx_baseu_xml-%variant.so.%{sonum}*
%endif

%files -n libwx_%{toolkit}u_adv-%variant%psonum
%_libdir/libwx_%{toolkit}u_adv-%variant.so.%{sonum}*

%files -n libwx_%{toolkit}u_aui-%variant%psonum
%_libdir/libwx_%{toolkit}u_aui-%variant.so.%{sonum}*

%files -n libwx_%{toolkit}u_core-%variant%psonum
%_libdir/libwx_%{toolkit}u_core-%variant.so.%{sonum}*

%files -n libwx_%{toolkit}u_gl-%variant%psonum
%_libdir/libwx_%{toolkit}u_gl-%variant.so.%{sonum}*

%files -n libwx_%{toolkit}u_html-%variant%psonum
%_libdir/libwx_%{toolkit}u_html-%variant.so.%{sonum}*

%files -n libwx_%{toolkit}u_media-%variant%psonum
%_libdir/libwx_%{toolkit}u_media-%variant.so.%{sonum}*

%files -n libwx_%{toolkit}u_propgrid-%variant%psonum
%_libdir/libwx_%{toolkit}u_propgrid-%variant.so.%{sonum}*

%files -n libwx_%{toolkit}u_qa-%variant%psonum
%_libdir/libwx_%{toolkit}u_qa-%variant.so.%{sonum}*

%files -n libwx_%{toolkit}u_ribbon-%variant%psonum
%_libdir/libwx_%{toolkit}u_ribbon-%variant.so.%{sonum}*

%files -n libwx_%{toolkit}u_richtext-%variant%psonum
%_libdir/libwx_%{toolkit}u_richtext-%variant.so.%{sonum}*

%files -n libwx_%{toolkit}u_stc-%variant%psonum
%_libdir/libwx_%{toolkit}u_stc-%variant.so.%{sonum}*

%if %{with webview}
%files -n libwx_%{toolkit}u_webview-%variant%psonum
%_libdir/libwx_%{toolkit}u_webview-%variant.so.%{sonum}*
%dir %_libdir/wx
%dir %_libdir/wx/%wx_micro
%_libdir/wx/%wx_micro/web-extensions/
%endif

%files -n libwx_%{toolkit}u_xrc-%variant%psonum
%_libdir/libwx_%{toolkit}u_xrc-%variant.so.%{sonum}*

%if %base_packages
%if "%{flavor}" != "GTK3-nostl"
%files -n %{base_name}-plugin-sound_sdlu-3_2
%dir %_libdir/wx
%dir %_libdir/wx/%wx_micro
%_libdir/wx/%wx_micro/sound_sdlu-%wx_micro.so
%endif
%endif

%files devel
# Complete documentation is available in the docs packages.
%doc docs/*.txt README.SUSE
%_bindir/wxrc
%_bindir/wxrc-%wx_minor
%_bindir/*-config*
%_datadir/aclocal
%_datadir/bakefile
%_includedir/wx-%wx_minor
%_libdir/*.so
%dir %_libdir/wx
%_libdir/wx/config
%_libdir/wx/include

%changelog
