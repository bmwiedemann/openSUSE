#
# spec file for package flickcurl
#
# Copyright (c) 2024 SUSE LLC
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


%define sover 0
Name:           flickcurl
Version:        1.26
Release:        0
Summary:        Command-Line Tools for the Flickr Web Service
License:        LGPL-2.1-only
Group:          Productivity/Networking/Other
URL:            http://librdf.org/flickcurl/
Source:         http://download.dajobe.org/flickcurl/flickcurl-%{version}.tar.gz
Source1:        baselibs.conf
Source2:        flickcurl.changes
Source99:       flickcurl-rpmlintrc
# PATCH-FIX-UPSTREAM 0001-configure-Include-stdio.h-in-vsnprintf-check.patch fcrozat@suse.com -- add missing headers
Patch0:         0001-configure-Include-stdio.h-in-vsnprintf-check.patch
# PATCH-FIX-UPSTREAM 0001-Fix-Wimplicit-function-declaration.patch fcrozat@suse.com -- fix build with gcc14
Patch1:         0001-Fix-Wimplicit-function-declaration.patch
BuildRequires:  chrpath
BuildRequires:  curl
BuildRequires:  fdupes
BuildRequires:  libcurl-devel >= 7.10.0
BuildRequires:  libraptor-devel >= 2.0.0
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Flickcurl is a C library for calling the Flickr Web service API. It handles the
API signing, token management, and parameter encoding and decoding, resulting
in C functions for the Web services APIs. It... uses libcurl to call the REST
Web service, and libxml2 to manipulate the XML responses. The library supports
reading photo, tag, and comments information, the photo upload and searching
APIs, and writing tags and comments. It provides utilities such as "flickcurl"
to exercise the API and "flickrdf" to get RDF metadata descriptions out of
photos, tags, and machine tags.

%package doc
Summary:        Documentation for flickcurl, a Flickr Web Service C library
Group:          Documentation/Other
Requires:       libflickcurl%{sover} = %{version}

%description doc
Flickcurl is a C library for calling the Flickr Web service API. It handles the
API signing, token management, and parameter encoding and decoding, resulting
in C functions for the Web services APIs. It... uses libcurl to call the REST
Web service, and libxml2 to manipulate the XML responses. The library supports
reading photo, tag, and comments information, the photo upload and searching
APIs, and writing tags and comments. It provides utilities such as "flickcurl"
to exercise the API and "flickrdf" to get RDF metadata descriptions out of
photos, tags, and machine tags.

This subpackage contains the developer documentation for %{name}.

%package -n libflickcurl%{sover}
Summary:        C Library API to the Flickr Web Service
Group:          System/Libraries

%description -n libflickcurl%{sover}
Flickcurl is a C library for calling the Flickr Web service API. It handles the
API signing, token management, and parameter encoding and decoding, resulting
in C functions for the Web services APIs. It... uses libcurl to call the REST
Web service, and libxml2 to manipulate the XML responses. The library supports
reading photo, tag, and comments information, the photo upload and searching
APIs, and writing tags and comments. It provides utilities such as "flickcurl"
to exercise the API and "flickrdf" to get RDF metadata descriptions out of
photos, tags, and machine tags.

%package -n libflickcurl-devel
Summary:        Development files for flickurl, a Flickr Web Service library
Group:          Development/Libraries/C and C++
Requires:       libcurl-devel
Requires:       libflickcurl%{sover} = %{version}
Requires:       libraptor-devel >= 1.4.0
Requires:       pkgconfig(libxml-2.0)

%description -n libflickcurl-devel
Flickcurl is a C library for calling the Flickr Web service API. It handles the
API signing, token management, and parameter encoding and decoding, resulting
in C functions for the Web services APIs. It... uses libcurl to call the REST
Web service, and libxml2 to manipulate the XML responses. The library supports
reading photo, tag, and comments information, the photo upload and searching
APIs, and writing tags and comments. It provides utilities such as "flickcurl"
to exercise the API and "flickrdf" to get RDF metadata descriptions out of
photos, tags, and machine tags.

%prep
%autosetup -p1

%build
%configure \
    --disable-static \

make %{?_smp_mflags}

%install
%make_install
%fdupes -s %{buildroot}

# Remove static libraries
find %{buildroot} -type f -name "*.la" -delete -print
#removing rpaths with chrpath
chrpath --delete %{buildroot}%{_bindir}/flickcurl
chrpath --delete %{buildroot}%{_bindir}/flickrdf

%post   -n libflickcurl%{sover} -p /sbin/ldconfig

%postun -n libflickcurl%{sover} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%license LICENSE*
%doc AUTHORS ChangeLog NEWS* NOTICE README*
%{_bindir}/flickcurl
%{_bindir}/flickrdf
%{_mandir}/man1/flickcurl.1%{ext_man}
%{_mandir}/man1/flickrdf.1%{ext_man}

%files -n libflickcurl%{sover}
%defattr(-,root,root)
%license COPYING.LIB
%{_libdir}/libflickcurl.so.%{sover}
%{_libdir}/libflickcurl.so.%{sover}.*.*

%files -n libflickcurl-devel
%defattr(-,root,root)
%{_bindir}/flickcurl-config
%{_includedir}/flickcurl.h
%{_libdir}/libflickcurl.so
%{_libdir}/pkgconfig/flickcurl.pc
%{_mandir}/man1/flickcurl-config.1%{ext_man}

%files doc
%defattr(-,root,root)
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/flickcurl

%changelog
