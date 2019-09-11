#
# spec file for package wxWidgets-3_0-nostl
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           wxWidgets-3_0-nostl
%define base_name wxWidgets-3_0
%define tarball_name wxWidgets
%define variant suse-nostl
%define psonum 3_0_4
%define sonum 3.0.4
Version:        3.0.4
Release:        0
%define wx_minor 3.0
# libdir for installing of all the stuff
%define wxlibdir %_libdir
# lang packages are exactly equal for all variants and versions.
# coordinate a bit between nostl and wxWidgets-3_x.
%define BUILD_LANG 0
# build non-UI toolkit related packages
%define         base_packages 1
Summary:        C++ Library for Cross-Platform Development
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Url:            http://www.wxwidgets.org/

#SVN-Clone:	https://svn.wxwidgets.org/svn/wx/wxWidgets/trunk
Source:         https://github.com/wxWidgets/wxWidgets/releases/download/v%version/wxWidgets-%version.tar.bz2
Source2:        README.SUSE
Source5:        wxWidgets-3_0-rpmlintrc
# This script is not used during build, but it makes possible to
# identify and backport wxPython fixes to wxWidgets.
Source6:        wxpython-mkdiff.sh
Source50:       baselibs.conf
Patch1:         soversion.diff
Patch17:        relax-abi.diff
Patch18:        0001-spinctrl.patch
Patch19:        0002-spinctrl.patch
Patch20:        0001-18034-stick-with-compile-settings-detected-at-config.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

#Link SDL2 for newer distros
%if 0%{?suse_version} > 1320 || (0%{?suse_version} == 1315 && 0%{?is_opensuse})
BuildRequires:  pkgconfig(sdl2)
%else
BuildRequires:  pkgconfig(sdl)
%endif
BuildRequires:  autoconf
BuildRequires:  cppunit-devel
BuildRequires:  gcc-c++
BuildRequires:  gnome-vfs2-devel
BuildRequires:  gstreamer-devel
BuildRequires:  gstreamer-plugins-base-devel
BuildRequires:  gtk2-devel
%define gtk_version 2
%if 0%{?suse_version} >= 1220
BuildRequires:  libSM-devel
%else
%if 0%{?sles_version} >= 11
BuildRequires:  xorg-x11-libSM-devel
%endif
%endif
BuildRequires:  libexpat-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libmspack-devel
BuildRequires:  libnotify-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(glu)

%description
wxWidgets is a C++ library for cross-platform GUI.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif, MS Windows, MacOS X, Windows CE, GPE) from the same source code.

This varaint of wxWidgets is built without STL types (such as
std::string), and is provided for old programs which fail to use e.g.
wxString and instead rely on the wxChar pointer API.

%package -n libwx_baseu-%variant%psonum
Summary:        wxWidgets Library
# Name up to openSUSE 11.3 and up to wxGTK-2.8:
Group:          System/Libraries
Obsoletes:      wxGTK <= %version.0
# Third party base package name:
Obsoletes:      wxWidgets < %version
# wxWidgets-lang requires wxWidgets. Provide them to fix dependencies:
Provides:       wxWidgets = %version
Recommends:     wxWidgets-lang >= %version

%description -n libwx_baseu-%variant%psonum
Library for the wxWidgets cross-platform GUI.

This varaint of wxWidgets is built without STL types (such as
std::string), and is provided for old programs which fail to use e.g.
wxString and instead rely on the wxChar pointer API.

%package -n libwx_baseu_net-%variant%psonum
Summary:        wxWidgets Library
Group:          System/Libraries

%description -n libwx_baseu_net-%variant%psonum
Library for the wxWidgets cross-platform GUI.

%package -n libwx_baseu_xml-%variant%psonum
Summary:        wxWidgets Library
Group:          System/Libraries

%description -n libwx_baseu_xml-%variant%psonum
Library for the wxWidgets cross-platform GUI.

%package -n libwx_gtk%{gtk_version}u_adv-%variant%psonum
Summary:        wxWidgets Library
Group:          System/Libraries

%description -n libwx_gtk%{gtk_version}u_adv-%variant%psonum
Library for the wxWidgets cross-platform GUI.

%package -n libwx_gtk%{gtk_version}u_aui-%variant%psonum
Summary:        wxWidgets Library
Group:          System/Libraries

%description -n libwx_gtk%{gtk_version}u_aui-%variant%psonum
Library for the wxWidgets cross-platform GUI.

%package -n libwx_gtk%{gtk_version}u_core-%variant%psonum
Summary:        wxWidgets Library
Group:          System/Libraries

%description -n libwx_gtk%{gtk_version}u_core-%variant%psonum
Library for the wxWidgets cross-platform GUI.

This varaint of wxWidgets is built without STL types (such as
std::string), and is provided for old programs which fail to use e.g.
wxString and instead rely on the wxChar pointer API.

%package -n libwx_gtk%{gtk_version}u_gl-%variant%psonum
Summary:        wxWidgets Library
Group:          System/Libraries

%description -n libwx_gtk%{gtk_version}u_gl-%variant%psonum
Library for the wxWidgets cross-platform GUI.

%package -n libwx_gtk%{gtk_version}u_html-%variant%psonum
Summary:        wxWidgets Library
Group:          System/Libraries

%description -n libwx_gtk%{gtk_version}u_html-%variant%psonum
Library for the wxWidgets cross-platform GUI.

%package -n libwx_gtk%{gtk_version}u_media-%variant%psonum
Summary:        wxWidgets Library
Group:          System/Libraries

%description -n libwx_gtk%{gtk_version}u_media-%variant%psonum
Library for the wxWidgets cross-platform GUI.

%package -n libwx_gtk%{gtk_version}u_propgrid-%variant%psonum
Summary:        wxWidgets Library
Group:          System/Libraries

%description -n libwx_gtk%{gtk_version}u_propgrid-%variant%psonum
Library for the wxWidgets cross-platform GUI.

%package -n libwx_gtk%{gtk_version}u_qa-%variant%psonum
Summary:        wxWidgets Library
Group:          System/Libraries

%description -n libwx_gtk%{gtk_version}u_qa-%variant%psonum
Library for the wxWidgets cross-platform GUI.

%package -n libwx_gtk%{gtk_version}u_ribbon-%variant%psonum
Summary:        wxWidgets Library
Group:          System/Libraries

%description -n libwx_gtk%{gtk_version}u_ribbon-%variant%psonum
Library for the wxWidgets cross-platform GUI.

%package -n libwx_gtk%{gtk_version}u_richtext-%variant%psonum
Summary:        wxWidgets Library
Group:          System/Libraries

%description -n libwx_gtk%{gtk_version}u_richtext-%variant%psonum
Library for the wxWidgets cross-platform GUI.

%package -n libwx_gtk%{gtk_version}u_stc-%variant%psonum
Summary:        wxWidgets Library
Group:          System/Libraries

%description -n libwx_gtk%{gtk_version}u_stc-%variant%psonum
Library for the wxWidgets cross-platform GUI.

%package -n libwx_gtk%{gtk_version}u_xrc-%variant%psonum
Summary:        wxWidgets Library
Group:          System/Libraries

%description -n libwx_gtk%{gtk_version}u_xrc-%variant%psonum
Library for the wxWidgets cross-platform GUI.

%package devel
Summary:        Development files for an old API variant of wxWidgets
Group:          Development/Libraries/C and C++
Requires:       gtk%gtk_version-devel
Requires:       libwx_baseu-%variant%psonum = %version
Requires:       libwx_baseu_net-%variant%psonum = %version
Requires:       libwx_baseu_xml-%variant%psonum = %version
Requires:       libwx_gtk%{gtk_version}u_adv-%variant%psonum = %version
Requires:       libwx_gtk%{gtk_version}u_aui-%variant%psonum = %version
Requires:       libwx_gtk%{gtk_version}u_core-%variant%psonum = %version
Requires:       libwx_gtk%{gtk_version}u_gl-%variant%psonum = %version
Requires:       libwx_gtk%{gtk_version}u_html-%variant%psonum = %version
Requires:       libwx_gtk%{gtk_version}u_media-%variant%psonum = %version
Requires:       libwx_gtk%{gtk_version}u_propgrid-%variant%psonum = %version
Requires:       libwx_gtk%{gtk_version}u_qa-%variant%psonum = %version
Requires:       libwx_gtk%{gtk_version}u_ribbon-%variant%psonum = %version
Requires:       libwx_gtk%{gtk_version}u_richtext-%variant%psonum = %version
Requires:       libwx_gtk%{gtk_version}u_stc-%variant%psonum = %version
Requires:       libwx_gtk%{gtk_version}u_xrc-%variant%psonum = %version
Requires:       pkgconfig(gl)
Requires:       pkgconfig(glu)
Provides:       wxWidgets-any-devel
Conflicts:      wxWidgets-any-devel

%description devel
wxWidgets is a C++ library for cross-platform GUI development.
With wxWidgets, you can create applications for different GUIs (GTK+,
Motif, MS Windows, MacOS X, Windows CE, GPE) from the same source code.

This package contains all files needed for developing with wxGTK%gtk_version.

Note: wxWidgets variant devel packages are mutually exclusive. Please
read %_docdir/%name/README.SUSE to pick a correct variant.

%package -n wxWidgets-lang
Summary:        Translations for wxWidgets
Group:          System/Localization
Provides:       wxWidgets-lang-all = %version
BuildArch:      noarch

%description -n wxWidgets-lang
Provides translations for wxWidgets.

%prep
echo "=== RPM build flags: WX_DEBUG=0%{?WX_DEBUG}"
%setup -q -n %tarball_name-%version
%patch -P 1 -p1
%patch -P 17 -p1
%patch -P 18 -p1
%patch -P 19 -p1
%patch -P 20 -p1
cp %{S:2} .

%build
autoconf -f -i
# With 2.9.1:
# --enable-objc_uniquifying is relevant only for Cocoa
# --enable-accessibility is currently supported only in msw
# --enable-extended_rtti does not compile

%if 0%{?suse_version} > 1320 || (0%{?suse_version} == 1315 && 0%{?is_opensuse})
export SDL_CONFIG=%_bindir/sdl2-config
%endif

%configure \
	--enable-vendor=%variant \
	--with-gtk=%gtk_version \
	--disable-static \
	--enable-unicode \
	--with-opengl \
	--with-libmspack \
	--with-sdl \
	--with-gnomevfs \
	--enable-ipv6 \
	--enable-mediactrl \
	--enable-optimise \
%if 0%{?WX_DEBUG}
	--enable-debug \
%else
	--disable-debug \
%endif
	--disable-stl \
	--disable-plugins
make %{?_smp_mflags} V=1
%if %BUILD_LANG
cd locale
make allmo
cd ..
%endif

%install
export VENDORTAG='-$variant' # only needed for non-MSW
make install DESTDIR="%buildroot"
%if !%base_packages
# Drop libraries already supplied by another packages
rm -f "%buildroot/%_libdir"/libwx_baseu{,_net,_xml}-%variant.so.%{sonum}* \
   "%buildroot/%_libdir/wx/%wx_minor"/sound_sdlu-*.so
%endif
%if %BUILD_LANG
# Locales for MS Windows:
rm -Rf %buildroot/%_datadir/locale/*/LC_MESSAGES/wxmsw.mo
%find_lang wxstd
%else
rm -Rf %buildroot/%_datadir/locale
%endif

# HACK: Fix wx-config symlink (bug introduced in 2.9.4).
ln -sf $(echo %buildroot/%_libdir/wx/config/* | sed "s%%%buildroot%%%%") %buildroot/%_bindir/wx-config

%post   -n libwx_baseu-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_baseu-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_baseu_net-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_baseu_net-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_baseu_xml-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_baseu_xml-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_gtk%{gtk_version}u_adv-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_gtk%{gtk_version}u_adv-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_gtk%{gtk_version}u_aui-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_gtk%{gtk_version}u_aui-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_gtk%{gtk_version}u_core-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_gtk%{gtk_version}u_core-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_gtk%{gtk_version}u_gl-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_gtk%{gtk_version}u_gl-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_gtk%{gtk_version}u_html-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_gtk%{gtk_version}u_html-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_gtk%{gtk_version}u_media-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_gtk%{gtk_version}u_media-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_gtk%{gtk_version}u_propgrid-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_gtk%{gtk_version}u_propgrid-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_gtk%{gtk_version}u_qa-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_gtk%{gtk_version}u_qa-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_gtk%{gtk_version}u_ribbon-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_gtk%{gtk_version}u_ribbon-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_gtk%{gtk_version}u_richtext-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_gtk%{gtk_version}u_richtext-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_gtk%{gtk_version}u_stc-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_gtk%{gtk_version}u_stc-%variant%psonum -p /sbin/ldconfig
%post   -n libwx_gtk%{gtk_version}u_xrc-%variant%psonum -p /sbin/ldconfig
%postun -n libwx_gtk%{gtk_version}u_xrc-%variant%psonum -p /sbin/ldconfig

%if %BUILD_LANG
%files -n wxWidgets-lang -f wxstd.lang
%endif

%if %base_packages
%files -n libwx_baseu-%variant%psonum
%defattr(-,root,root)
%_libdir/libwx_baseu-%variant.so.%{sonum}*

%files -n libwx_baseu_net-%variant%psonum
%defattr(-,root,root)
%_libdir/libwx_baseu_net-%variant.so.%{sonum}*

%files -n libwx_baseu_xml-%variant%psonum
%defattr(-,root,root)
%_libdir/libwx_baseu_xml-%variant.so.%{sonum}*
%endif

%files -n libwx_gtk%{gtk_version}u_adv-%variant%psonum
%defattr(-,root,root)
%_libdir/libwx_gtk%{gtk_version}u_adv-%variant.so.%{sonum}*

%files -n libwx_gtk%{gtk_version}u_aui-%variant%psonum
%defattr(-,root,root)
%_libdir/libwx_gtk%{gtk_version}u_aui-%variant.so.%{sonum}*

%files -n libwx_gtk%{gtk_version}u_core-%variant%psonum
%defattr(-,root,root)
%_libdir/libwx_gtk%{gtk_version}u_core-%variant.so.%{sonum}*

%files -n libwx_gtk%{gtk_version}u_gl-%variant%psonum
%defattr(-,root,root)
%_libdir/libwx_gtk%{gtk_version}u_gl-%variant.so.%{sonum}*

%files -n libwx_gtk%{gtk_version}u_html-%variant%psonum
%defattr(-,root,root)
%_libdir/libwx_gtk%{gtk_version}u_html-%variant.so.%{sonum}*

%files -n libwx_gtk%{gtk_version}u_media-%variant%psonum
%defattr(-,root,root)
%_libdir/libwx_gtk%{gtk_version}u_media-%variant.so.%{sonum}*

%files -n libwx_gtk%{gtk_version}u_propgrid-%variant%psonum
%defattr(-,root,root)
%_libdir/libwx_gtk%{gtk_version}u_propgrid-%variant.so.%{sonum}*

%files -n libwx_gtk%{gtk_version}u_qa-%variant%psonum
%defattr(-,root,root)
%_libdir/libwx_gtk%{gtk_version}u_qa-%variant.so.%{sonum}*

%files -n libwx_gtk%{gtk_version}u_ribbon-%variant%psonum
%defattr(-,root,root)
%_libdir/libwx_gtk%{gtk_version}u_ribbon-%variant.so.%{sonum}*

%files -n libwx_gtk%{gtk_version}u_richtext-%variant%psonum
%defattr(-,root,root)
%_libdir/libwx_gtk%{gtk_version}u_richtext-%variant.so.%{sonum}*

%files -n libwx_gtk%{gtk_version}u_stc-%variant%psonum
%defattr(-,root,root)
%_libdir/libwx_gtk%{gtk_version}u_stc-%variant.so.%{sonum}*

%files -n libwx_gtk%{gtk_version}u_xrc-%variant%psonum
%defattr(-,root,root)
%_libdir/libwx_gtk%{gtk_version}u_xrc-%variant.so.%{sonum}*

%files devel
%defattr(-,root,root)
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
