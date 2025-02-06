#
# spec file for package atril
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


%define typelib1 typelib-1_0-AtrilDocument-1_5_0
%define typelib2 typelib-1_0-AtrilView-1_5_0
%define sover   3
%define _version 1.28

Name:           atril
Version:        1.28.1
Release:        0
Summary:        MATE Desktop document viewer
License:        GPL-2.0-only AND LGPL-2.0-only
Group:          Productivity/Office/Other
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  mate-common >= %{_version}
BuildRequires:  pkgconfig
BuildRequires:  python3-libxml2
BuildRequires:  texlive-devel
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(ddjvuapi)
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcaja-extension) >= %{_version}
BuildRequires:  pkgconfig(libgxps)
BuildRequires:  pkgconfig(libpst)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libspectre)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(mate-desktop-2.0) >= %{_version}
BuildRequires:  pkgconfig(poppler-glib) >= 0.22.0
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(webkit2gtk-4.0)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(zlib)
Requires:       %{name}-backends = %{version}
Requires:       mate-desktop-gsettings-schemas >= %{_version}
Recommends:     %{name}-lang
# mate-document-viewer was last used in openSUSE 13.1.
Provides:       mate-document-viewer = %{version}
Obsoletes:      mate-document-viewer < %{version}
Obsoletes:      mate-document-viewer-lang < %{version}
%glib2_gsettings_schema_requires

%description
Atril is a document viewer capable of displaying multiple and single
page document formats like PDF and Postscript.

%lang_package

%package -n libatrildocument%{sover}
Summary:        System library of the MATE Document Viewer
Group:          System/Libraries
Obsoletes:      mate-document-viewer-libs-3 < %{version}

%description -n libatrildocument%{sover}
Atril is a document viewer capable of displaying multiple and
singlepage document formats like PDF and PostScript.

%package -n libatrilview%{sover}
Summary:        System library of the MATE Document Viewer
Group:          System/Libraries
Obsoletes:      mate-document-viewer-libs-3 < %{version}

%description -n libatrilview%{sover}
Atril is a document viewer capable of displaying multiple and
singlepage document formats like PDF and PostScript.

%package -n %{typelib1}
Summary:        Introspection bindings for MATE Desktop's AtrilDocument
Group:          System/Libraries

%description -n %{typelib1}
Atril is a document viewer capable of displaying multiple and single
page document formats like PDF and Postscript.

%package -n %{typelib2}
Summary:        Introspection bindings for MATE Desktop's AtrilView
Group:          System/Libraries

%description -n %{typelib2}
Atril is a document viewer capable of displaying multiple and single
page document formats like PDF and Postscript.

%package backends
Summary:        Atril shared libraries (View and Document)
Requires:       mathjax
# mate-document-viewer-libs-3 was last used in openSUSE 13.1.
Provides:       mate-document-viewer-libs-3 = %{version}
Obsoletes:      mate-document-viewer-libs-3 < %{version}

%description backends
Atril is a document viewer capable of displaying multiple and single
page document formats like PDF and Postscript.

%package -n caja-extension-%{name}
Summary:        Atril extension for Caja file manager
Requires:       %{name} = %{version}
Requires:       caja >= %{_version}
Supplements:    (caja and %{name})
# atril-caja was last used in openSUSE Leap 42.1.
Provides:       %{name}-caja = %{version}
Obsoletes:      %{name}-caja < %{version}
# mate-document-viewer-caja was last used in openSUSE 13.1.
Provides:       mate-document-viewer-caja = %{version}
Obsoletes:      mate-document-viewer-caja < %{version}

%description -n caja-extension-%{name}
Atril is a document viewer capable of displaying multiple and single
page document formats like PDF and Postscript.

This package contains the Atril extension for the Caja file manager.
It adds an additional tab called "Document" to the file properties
dialog.

%package devel
Summary:        MATE Desktop document viewer development files
Requires:       %{name}-backends = %{version}
Requires:       %{typelib1} = %{version}
Requires:       %{typelib2} = %{version}
# mate-document-viewer-devel was last used in openSUSE 13.1.
Provides:       mate-document-viewer-devel = %{version}
Obsoletes:      mate-document-viewer-devel < %{version}

%description devel
Atril is a document viewer capable of displaying multiple and single
page document formats like PDF and Postscript.

%package thumbnailer
Summary:        Atril thumbnailer extension for Caja
Requires:       %{name} = %{version}
Requires:       caja >= %{_version}

%description thumbnailer
Atril is a document viewer capable of displaying multiple and single
page document formats like PDF and Postscript.

This package contains the Atril extension for the Caja file manager.

%package doc
Summary:        Documentation how to Use Atril
Group:          Documentation/HTML
Requires:       %{name} = %{version}
BuildArch:      noarch

%description doc
This package contains the documentation for atril

%prep
%autosetup -p1

%build
NOCONFIGURE=1 mate-autogen
%configure \
  --disable-static                    \
  --libexecdir=%{_libexecdir}/%{name} \
  --enable-introspection
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
find %{buildroot} -type f -name "*.la" -delete -print
%suse_update_desktop_file %{name}
%fdupes %{buildroot}%{_datadir}/

%post -n libatrilview%{sover} -p /sbin/ldconfig

%postun -n libatrilview%{sover} -p /sbin/ldconfig

%post -n libatrildocument%{sover} -p /sbin/ldconfig

%postun -n libatrildocument%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS README.md
%{_bindir}/%{name}
%{_bindir}/%{name}-previewer
%{_bindir}/%{name}-thumbnailer
%{_datadir}/%{name}/
%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/%{sover}/
%dir %{_libexecdir}/%{name}/
%{_libexecdir}/%{name}/%{name}*
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/icons/hicolor/*/*/*
%{_mandir}/man?/*.?%{?ext_man}

%files -n libatrilview%{sover}
%license COPYING
%doc AUTHORS README.md
%{_libdir}/libatrilview.so.%{sover}*

%files -n libatrildocument%{sover}
%license COPYING
%doc AUTHORS README.md
%{_libdir}/libatrildocument.so.%{sover}*

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_datadir}/gir-1.0/*.gir
%doc %{_datadir}/gtk-doc/html/

%files -n caja-extension-%{name}
%{_datadir}/caja/extensions/libatril-properties-page.caja-extension
%{_libdir}/caja/

%files -n %{typelib1}
%{_libdir}/girepository-1.0/AtrilDocument-1.5.0.typelib

%files -n %{typelib2}
%{_libdir}/girepository-1.0/AtrilView-1.5.0.typelib

%files backends
%license COPYING
%doc AUTHORS README.md
%{_libdir}/%{name}/%{sover}/backends/

%files thumbnailer
%dir %{_datadir}/thumbnailers/
%{_datadir}/thumbnailers/atril.thumbnailer

%files doc
%doc %{_datadir}/help/*/%{name}/

%files lang -f %{name}.lang
%exclude %{_datadir}/help/*

%changelog
