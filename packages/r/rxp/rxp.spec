#
# spec file for package rxp
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


%define         sover 0
Name:           rxp
Version:        1.5.2
Release:        0
Summary:        XML Parser in C
License:        GPL-2.0-or-later
URL:            https://www.cogsci.ed.ac.uk/~richard/rxp.html
Source:         rxp-%{version}.tar.gz

%description
The current version of RXP supports XML 1.1, Namespaces 1.1, xml:id,
and XML Catalogs. To use an XML Catalog, set the environment variable
XML_CATALOG_FILES to a space-separated list of catalog files.

RXP was written by Richard Tobin at the Language Technology Group,
Human Communication Research Centre, University of Edinburgh.

A simple application (called rxp) is provided. It parses and writes XML
data, optionally expanding entities, defaulting attributes, and
translating to a different output encoding.

%package        devel
Summary:        Development files for %{name}
Conflicts:      festival-devel
Requires:       lib%{name}%{sover} = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n lib%{name}%{sover}
Summary:        Shared library for %{name}

%description -n lib%{name}%{sover}
The current version of RXP supports XML 1.1, Namespaces 1.1, xml:id,
and XML Catalogs. To use an XML Catalog, set the environment variable
XML_CATALOG_FILES to a space-separated list of catalog files.

RXP was written by Richard Tobin at the Language Technology Group,
Human Communication Research Centre, University of Edinburgh.

A simple application (called rxp) is provided. It parses and writes XML
data, optionally expanding entities, defaulting attributes, and
translating to a different output encoding.

This package contains shared library

%prep
%autosetup -p1

%build
%configure \
  --enable-shared \
  --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.a" -or -name "*.la" -delete -print

%ldconfig_scriptlets -n lib%{name}%{sover}

%files
%{_bindir}/rxp
%{_mandir}/man1/rxp.1%{?ext_man}

%files -n %{name}-devel
%license doc/COPYRIGHT doc/COPYING
%doc doc/Manual doc/Threads
%{_includedir}/%{name}*
%{_libdir}/*.so

%files -n lib%{name}%{sover}
%license doc/COPYRIGHT doc/COPYING
%{_libdir}/librxp.so.%{sover}*

%changelog
