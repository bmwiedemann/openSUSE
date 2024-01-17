#
# spec file for package libiptcdata
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


Name:           libiptcdata
Version:        1.0.5
Release:        0
Summary:        IPTC Metadata Tag Manipulation Library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
URL:            https://github.com/ianw/libiptcdata/
Source:         https://github.com/ianw/libiptcdata/releases/download/release_1_0_5/libiptcdata-%{version}.tar.gz
BuildRequires:  pkgconfig
Requires:       libiptcdata0

%description
libiptcdata is a library for parsing, editing, and saving IPTC
(International Press Telecommunications Council) data. stored within
multimedia files such as images.

%package -n libiptcdata0
Summary:        IPTC Metadata Tag Manipulation Library
Group:          System/Libraries
Requires:       %{name} = %{version}

%description -n libiptcdata0
libiptcdata is a library for parsing, editing, and saving
International Press
Telecommunications Council (IPTC) metadata stored within multimedia
files such as images. This metadata can include captions and keywords,
often used by popular photo management applications. The library
provides routines for parsing, viewing, modifying, and saving this
metadata. The libiptcdata package also includes a command line utility,
iptc, for editing IPTC data in JPEG files. The library implements the
IPTC Information Interchange Model according to its specification.

%package devel
Summary:        Development files for the IPTC Metadata Tag Manipulation Library
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
libiptcdata is a library for parsing, editing, and saving IPTC
(International Press Telecommunications Council) data. stored within
multimedia files such as images.

This subpackage contains the header files for the library.

%package doc
Summary:        Documentation for the IPTC Metadata Tag Manipulation Library
Group:          Documentation/HTML

%description doc
libiptcdata is a library for parsing, editing, and saving IPTC
(International Press Telecommunications Council) data. stored within
multimedia files such as images.

This subpackage contains the documentation for it.

%lang_package

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%make_install
%find_lang %{name}
%find_lang iptc %{name}.lang
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libiptcdata0 -p /sbin/ldconfig
%postun -n libiptcdata0 -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS ChangeLog INSTALL NEWS README TODO
%{_bindir}/*

%files -n libiptcdata0
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%files doc
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/*

%files lang -f %{name}.lang

%changelog
