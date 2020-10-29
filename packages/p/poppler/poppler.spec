#
# spec file for package poppler
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
%global sname poppler
%if "%{flavor}" == ""
%else
%global psuffix -%{flavor}
%endif

Name:           poppler%{?psuffix}
Version:        20.10.0
Release:        0
# Actual version of poppler-data:
%define poppler_data_version 0.4.9
%define poppler_sover 103
%define poppler_cpp_sover 0
%define poppler_glib_sover 8
%define poppler_qt5_sover 1
%define poppler_api 0.18
%define poppler_apipkg 0_18
Summary:        PDF Rendering Library
License:        GPL-2.0-only OR GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://poppler.freedesktop.org/
Source:         http://poppler.freedesktop.org/%{sname}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  cmake >= 3.5
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  libboost_headers-devel >= 1.58
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  openjpeg2
%if "%{flavor}" == "qt5"
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Xml)
%endif
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(cairo) >= 1.10.0
BuildRequires:  pkgconfig(cairo-ft) >= 1.10.0
BuildRequires:  pkgconfig(cairo-pdf)
BuildRequires:  pkgconfig(cairo-ps)
BuildRequires:  pkgconfig(cairo-svg)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gobject-2.0) >= 2.41
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(poppler-data)

%description
Poppler is a PDF rendering library, forked from the xpdf PDF viewer
developed by Derek Noonburg of Glyph and Cog, LLC.

%package -n     libpoppler%{poppler_sover}
Summary:        PDF Rendering Library
Group:          System/Libraries
Recommends:     poppler-data >= %{poppler_data_version}

%description -n libpoppler%{poppler_sover}
Poppler is a PDF rendering library, forked from the xpdf PDF viewer
developed by Derek Noonburg of Glyph and Cog, LLC.

%package -n     libpoppler-cpp%{poppler_cpp_sover}
Summary:        C++ API of the Poppler PDF rendering library
Group:          System/Libraries

%description -n libpoppler-cpp%{poppler_cpp_sover}
Poppler is a PDF rendering library, forked from the xpdf PDF viewer
developed by Derek Noonburg of Glyph and Cog, LLC.

%package -n     libpoppler-glib%{poppler_glib_sover}
Summary:        Glib wrapper for the poppler PDF rendering library
Group:          System/Libraries
Requires:       libpoppler%{poppler_sover} >= %{version}

%description -n libpoppler-glib%{poppler_glib_sover}
Poppler is a PDF rendering library, forked from the xpdf PDF viewer
developed by Derek Noonburg of Glyph and Cog, LLC.

%package -n     typelib-1_0-Poppler-%{poppler_apipkg}
Summary:        Introspection bindings for the Poppler PDF rendering library
Group:          System/Libraries

%description -n typelib-1_0-Poppler-%{poppler_apipkg}
Poppler is a PDF rendering library, forked from the xpdf PDF viewer
developed by Derek Noonburg of Glyph and Cog, LLC.

This package provides the GObject Introspection bindings for Poppler.

%package -n     libpoppler-qt5-%{poppler_qt5_sover}
Summary:        Qt5 wrapper for the Poppler PDF rendering library
Group:          System/Libraries
Requires:       libpoppler%{poppler_sover} >= %{version}

%description -n libpoppler-qt5-%{poppler_qt5_sover}
Poppler is a PDF rendering library, forked from the xpdf PDF viewer
developed by Derek Noonburg of Glyph and Cog, LLC.

%package        tools
Summary:        PDF Rendering Library Tools
Group:          Productivity/Publishing/PDF
Requires:       libpoppler%{poppler_sover} >= %{version}

%description    tools
Poppler is a PDF rendering library, forked from the xpdf PDF viewer
developed by Derek Noonburg of Glyph and Cog, LLC.

%package -n     libpoppler-devel
Summary:        Development files for the Poppler PDF rendering library
Group:          Development/Libraries/C and C++
Requires:       libboost_headers-devel >= 1.58
Requires:       libpoppler%{poppler_sover} = %{version}
Requires:       libpoppler-cpp%{poppler_cpp_sover} = %{version}
Requires:       libstdc++-devel

%description -n libpoppler-devel
Poppler is a PDF rendering library, forked from the xpdf PDF viewer
developed by Derek Noonburg of Glyph and Cog, LLC.

%package -n     libpoppler-glib-devel
Summary:        Development files for the Poppler Glib wrapper library
Group:          Development/Libraries/C and C++
Requires:       libpoppler-glib%{poppler_glib_sover} = %{version}
Requires:       typelib-1_0-Poppler-%{poppler_apipkg} = %{version}

%description -n libpoppler-glib-devel
Poppler is a PDF rendering library, forked from the xpdf PDF viewer
developed by Derek Noonburg of Glyph and Cog, LLC.

%package -n     libpoppler-qt5-devel
Summary:        Development files for the Poppler Qt5 wrapper library
Group:          Development/Libraries/C and C++
Requires:       libpoppler-devel = %{version}
Requires:       libpoppler-qt5-%{poppler_qt5_sover} = %{version}
Requires:       pkgconfig(Qt5Core)
Requires:       pkgconfig(Qt5Gui)
Requires:       pkgconfig(Qt5Widgets)
Requires:       pkgconfig(Qt5Xml)

%description -n libpoppler-qt5-devel
Poppler is a PDF rendering library, forked from the xpdf PDF viewer
developed by Derek Noonburg of Glyph and Cog, LLC.

%prep
%setup -q -n poppler-%{version}

%build
# Leap 15.0 doesn't know %%cmake_build
%{?!cmake_build:%define cmake_build() make %{?_smp_mflags} VERBOSE=1}

%if "%{flavor}" == "qt5"
export MOCQT5='%{_libqt5_bindir}/moc'
export MOCQT52='%{_libqt5_bindir}/moc'
%endif
# make introspection scanner (g-ir-scanner) work with older build envs
export LD_LIBRARY_PATH=$(pwd)/build
%cmake \
	-DENABLE_GTK_DOC=ON \
	-DENABLE_UNSTABLE_API_ABI_HEADERS=ON \
	-DENABLE_ZLIB=ON \
	-DENABLE_LIBCURL=ON \
	-DBUILD_GTK_TESTS=OFF \
%if "%{flavor}" == "qt5"
	-DENABLE_QT5=ON \
	-DENABLE_GLIB=OFF \
	-DENABLE_CPP=OFF \
%endif
	%{nil}
%cmake_build

%install
%cmake_install
%if "%{flavor}" == "qt5"
cd %{buildroot} && find . -type f -o -type l | grep -v qt | xargs rm -v
%endif

echo > %SOURCE99
%if "%{flavor}" == "qt5"
echo "libpoppler-qt5-%{poppler_qt5_sover}" >> %SOURCE99
%else
echo "libpoppler%{poppler_sover}" >> %SOURCE99
echo "libpoppler-glib%{poppler_glib_sover}" >> %SOURCE99
echo "libpoppler-cpp%{poppler_cpp_sover}" >> %SOURCE99
%endif

%post -n libpoppler%{poppler_sover} -p /sbin/ldconfig
%postun -n libpoppler%{poppler_sover} -p /sbin/ldconfig

%post -n libpoppler-glib%{poppler_glib_sover} -p /sbin/ldconfig
%postun -n libpoppler-glib%{poppler_glib_sover} -p /sbin/ldconfig

%post -n libpoppler-cpp%{poppler_cpp_sover} -p /sbin/ldconfig
%postun -n libpoppler-cpp%{poppler_cpp_sover} -p /sbin/ldconfig

%post -n libpoppler-qt5-%{poppler_qt5_sover} -p /sbin/ldconfig
%postun -n libpoppler-qt5-%{poppler_qt5_sover} -p /sbin/ldconfig

%if "%{flavor}" == "qt5"

%files -n libpoppler-qt5-%{poppler_qt5_sover}
%{_libdir}/libpoppler-qt5.so.%{poppler_qt5_sover}*

%files -n libpoppler-qt5-devel
%dir %{_includedir}/poppler
%{_includedir}/poppler/qt5
%{_libdir}/libpoppler-qt5.so
%{_libdir}/pkgconfig/poppler-qt5.pc

%else

%files -n libpoppler%{poppler_sover}
%license COPYING COPYING3
%doc NEWS README.md README-XPDF
%{_libdir}/libpoppler.so.%{poppler_sover}*

%files -n libpoppler-glib%{poppler_glib_sover}
%{_libdir}/libpoppler-glib.so.%{poppler_glib_sover}*

%files -n typelib-1_0-Poppler-%{poppler_apipkg}
%{_libdir}/girepository-1.0/Poppler-%{poppler_api}.typelib

%files tools
%license COPYING COPYING3
%{_bindir}/*
%doc %{_mandir}/man1/*.*

%files -n libpoppler-cpp%{poppler_cpp_sover}
%{_libdir}/libpoppler-cpp.so.%{poppler_cpp_sover}*

%files -n libpoppler-devel
%doc AUTHORS NEWS README.contributors
%{_includedir}/poppler
%exclude %{_includedir}/poppler/glib
%{_libdir}/libpoppler.so
%{_libdir}/libpoppler-cpp.so
%{_libdir}/pkgconfig/poppler.pc
%{_libdir}/pkgconfig/poppler-cairo.pc
%{_libdir}/pkgconfig/poppler-cpp.pc
%{_libdir}/pkgconfig/poppler-splash.pc

%files -n libpoppler-glib-devel
%{_includedir}/poppler/glib
%{_libdir}/libpoppler-glib.so
%{_libdir}/pkgconfig/poppler-glib.pc
%{_datadir}/gir-1.0/Poppler-%{poppler_api}.gir
%doc %{_datadir}/gtk-doc/html/poppler

%endif

%changelog
