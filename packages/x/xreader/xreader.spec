#
# spec file for package xreader
#
# Copyright (c) 2025 SUSE LLC
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


%define         sover   3
%define         typelib1 typelib-1_0-XreaderDocument-1_5
%define         typelib2 typelib-1_0-XreaderView-1_5
Name:           xreader
Version:        4.2.3
Release:        0
Summary:        Document viewer for documents like PDF/PostScript
License:        GPL-2.0-only AND LGPL-2.0-only
URL:            https://github.com/linuxmint/xreader
Source:         %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  intltool
#BuildRequires:  mathjax
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  texlive-devel
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(ddjvuapi) >= 3.5.17
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.36.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.6
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14.0
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libgxps) >= 0.2.0
BuildRequires:  pkgconfig(libsecret-1) >= 0.5
BuildRequires:  pkgconfig(libspectre) >= 0.2.0
BuildRequires:  pkgconfig(libtiff-4) >= 3.6
BuildRequires:  pkgconfig(libxml-2.0) >= 2.5.0
BuildRequires:  pkgconfig(poppler-glib) >= 0.22.0
BuildRequires:  pkgconfig(sm) >= 1.0.0
BuildRequires:  pkgconfig(webkit2gtk-4.1) >= 2.4.3
BuildRequires:  pkgconfig(xapp) >= 1.1.0
BuildRequires:  pkgconfig(zlib)
# Only require pdf backend subpackage to make application more lightweight for Live media
Requires:       %{name}-plugin-pdfdocument
Provides:       %{name}-backends = %{version}
Provides:       caja-extension-%{name} = %{version}
Provides:       nemo-extension-%{name} = %{version}
Obsoletes:      %{name}-backends < %{version}
Obsoletes:      caja-extension-%{name} < %{version}
Obsoletes:      nemo-extension-%{name} < %{version}

%description
Xreader is a document viewer capable of displaying multiple and
single page document formats like PDF and Postscript.

%lang_package

%package -n libxreaderdocument%{sover}
Summary:        X-Apps Document Reader -- System Library

%description -n libxreaderdocument%{sover}
Xreader is a document viewer capable of displaying multiple and
single page document formats like PDF and Postscript.

%package -n libxreaderview%{sover}
Summary:        X-Apps Document Reader -- System Library

%description -n libxreaderview%{sover}
Xreader is a document viewer capable of displaying multiple and
single page document formats like PDF and Postscript.

%package -n %{typelib1}
Summary:        XReaderDocument -- Introspection Bindings
# typelib-1_0-XreaderDocument-1_5_0 was last used in openSUSE Leap 42.3.
Provides:       typelib-1_0-XreaderDocument-1_5_0 = %{version}
Obsoletes:      typelib-1_0-XreaderDocument-1_5_0 < %{version}

%description -n %{typelib1}
Xreader is a document viewer capable of displaying multiple and
single page document formats like PDF and Postscript.

%package -n %{typelib2}
Summary:        XReaderView -- Introspection Bindings
# typelib-1_0-XreaderView-1_5_0 was last used in openSUSE Leap 42.3.
Provides:       typelib-1_0-XreaderView-1_5_0 = %{version}
Obsoletes:      typelib-1_0-XreaderView-1_5_0 < %{version}

%description -n %{typelib2}
Xreader is a document viewer capable of displaying multiple and
single page document formats like PDF and Postscript.

%package devel
Summary:        X-Apps Document Reader development files
Requires:       %{typelib1} = %{version}
Requires:       %{typelib2} = %{version}

%description devel
Xreader is a document viewer capable of displaying multiple and
single page document formats like PDF and Postscript.

#%package -n xreader-plugin-epubdocument
#Summary:        EPUB document support for Xreader
#Requires:       %{name}


#%description -n xreader-plugin-epubdocument
#A plugin for Xreader to read EPUB documents.

%package -n xreader-plugin-pdfdocument
Summary:        PDF document support for Xreader
Requires:       %{name}

%description -n xreader-plugin-pdfdocument
A plugin for Xreader to read PDF documents.

%package -n xreader-plugin-psdocument
Summary:        PostScript document support for Xreader
Requires:       %{name}

%description -n xreader-plugin-psdocument
A plugin for Xreader to read PostScript documents.

%package -n xreader-plugin-tiffdocument
Summary:        TIFF document support for Xreader
Requires:       %{name}

%description -n xreader-plugin-tiffdocument
A plugin for Xreader to read TIFF documents.

%package -n xreader-plugin-xpsdocument
Summary:        XPS document support for Xreader
Requires:       %{name}

%description -n xreader-plugin-xpsdocument
A plugin for Xreader to read XPS documents.

%package -n xreader-plugin-comicsdocument
Summary:        Comics document support for Xreader
Requires:       %{name}

%description -n xreader-plugin-comicsdocument
A plugin for Xreader to read Comics documents.

%package -n xreader-plugin-djvudocument
Summary:        DjVu document support for Xreader
Requires:       %{name}

%description -n xreader-plugin-djvudocument
A plugin for Xreader to read DjVu documents.

%package -n xreader-plugin-dvidocument
Summary:        DVI document support for Xreader
Requires:       %{name}

%description -n xreader-plugin-dvidocument
A plugin for Xreader to read DVI documents.

%package -n xreader-plugin-pixbufdocument
Summary:        Pixbuf document support for Xreader
Requires:       %{name}

%description -n xreader-plugin-pixbufdocument
A plugin for Xreader to read Pixbuf documents.

%prep
%autosetup

%build
%meson \
  -Dcomics=true \
  -Ddjvu=true \
  -Ddvi=true \
  -Dt1lib=true \
  -Depub=false \
  -Dpdf=true \
  -Dpixbuf=true \
  -Dps=true \
  -Dtiff=true \
  -Dxps=true \
  -Dgtk_unix_print=true \
  -Dkeyring=true \
  -Dpreviewer=true \
  -Dthumbnailer=true \
  -Ddocs=false \
  -Dhelp_files=true \
  -Dintrospection=true \
  -Denable_dbus=true \
  -Ddeprecated_warnings=true \
  -Denable_debug=false
%meson_build

%install
%meson_install
%find_lang %{name}
%fdupes %{buildroot}

%post -n libxreaderview%{sover} -p /sbin/ldconfig

%postun -n libxreaderview%{sover} -p /sbin/ldconfig

%post -n libxreaderdocument%{sover} -p /sbin/ldconfig

%postun -n libxreaderdocument%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-previewer
%{_bindir}/%{name}-thumbnailer
%{_datadir}/%{name}/
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{sover}/
%dir %{_datadir}/thumbnailers/
%{_libexecdir}/xreaderd
%{_datadir}/thumbnailers/%{name}.thumbnailer
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/xreader.appdata.xml
%{_datadir}/icons/hicolor/*/*/*
%{_mandir}/man?/*.?%{?ext_man}
# backends directory structure - backends go to their own packages
%dir %{_libdir}/%{name}/%{sover}/backends

%files lang -f %{name}.lang

%files -n libxreaderview%{sover}
%{_libdir}/libxreaderview.so.%{sover}*

%files -n libxreaderdocument%{sover}
%{_libdir}/libxreaderdocument.so.%{sover}*

%files -n %{typelib1}
%{_libdir}/girepository-1.0/XreaderDocument-1.5.typelib

%files -n %{typelib2}
%{_libdir}/girepository-1.0/XreaderView-1.5.typelib

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_datadir}/gir-1.0/*.gir
%{_libdir}/pkgconfig/*.pc

#%files -n xreader-plugin-epubdocument
#%{_libdir}/%{name}/%{sover}/backends/epubdocument.xreader-backend
#%{_libdir}/%{name}/%{sover}/backends/libepubdocument.so

%files -n xreader-plugin-pdfdocument
%{_libdir}/%{name}/%{sover}/backends/pdfdocument.xreader-backend
%{_libdir}/%{name}/%{sover}/backends/libpdfdocument.so

%files -n xreader-plugin-psdocument
%{_libdir}/%{name}/%{sover}/backends/libpsdocument.so
%{_libdir}/%{name}/%{sover}/backends/psdocument.xreader-backend

%files -n xreader-plugin-tiffdocument
%{_libdir}/%{name}/%{sover}/backends/tiffdocument.xreader-backend
%{_libdir}/%{name}/%{sover}/backends/libtiffdocument.so

%files -n xreader-plugin-xpsdocument
%{_libdir}/%{name}/%{sover}/backends/libxpsdocument.so
%{_libdir}/%{name}/%{sover}/backends/xpsdocument.xreader-backend

%files -n xreader-plugin-comicsdocument
%{_libdir}/%{name}/%{sover}/backends/comicsdocument.xreader-backend
%{_libdir}/%{name}/%{sover}/backends/libcomicsdocument.so

%files -n xreader-plugin-djvudocument
%{_libdir}/%{name}/%{sover}/backends/djvudocument.xreader-backend
%{_libdir}/%{name}/%{sover}/backends/libdjvudocument.so

%files -n xreader-plugin-dvidocument
%{_libdir}/%{name}/%{sover}/backends/dvidocument.xreader-backend
%{_libdir}/%{name}/%{sover}/backends/libdvidocument.so

%files -n xreader-plugin-pixbufdocument
%{_libdir}/%{name}/%{sover}/backends/pixbufdocument.xreader-backend
%{_libdir}/%{name}/%{sover}/backends/libpixbufdocument.so

%changelog
