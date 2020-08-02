#
# spec file for package liblrdf
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


Name:           liblrdf
Version:        0.5.0
Release:        0
Summary:        A library to Manipulate RDF Files for LADSPA Plug-Ins
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/swh/LRDF
Source:         https://github.com/swh/LRDF/archive/%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  ladspa-devel
BuildRequires:  libraptor-devel >= 0.9.11
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig

%description
This is a library to make it easy to manipulate RDF files describing
LADSPA plug-ins. It can also be used for general RDF manipulation.

It can read RDF, XLM, and N3 files and export N3 files. Ot also has a
light taxonomic inference capability.

%package -n liblrdf2
Summary:        A library to Manipulate RDF Files for LADSPA Plug-Ins
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n liblrdf2
This is a library to make it easy to manipulate RDF files describing
LADSPA plug-ins. It can also be used for general RDF manipulation.

It can read RDF, XLM, and N3 files and export N3 files. Ot also has a
light taxonomic inference capability.

%package devel
Summary:        Development package for the liblrdf library
Group:          Development/Libraries/C and C++
Requires:       liblrdf2 = %{version}
Requires:       libraptor-devel

%description devel
This package contains the files needed to compile programs that use the
liblrdf library.

%prep
%setup -q -n LRDF-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
make -C examples distclean
rm -f examples/.gitignore
rm -rf examples/.deps
rm -f examples/Makefile.*

%post -n liblrdf2 -p /sbin/ldconfig

%postun -n liblrdf2 -p /sbin/ldconfig

%files -n liblrdf2
%defattr(-,root,root)
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/lib*.so.2*

%files devel
%defattr(-,root,root)
%doc examples
%{_libdir}/lib*.so
%{_includedir}/*
%{_datadir}/ladspa
%{_libdir}/pkgconfig/*.pc
%exclude %{_libdir}/lib*.la

%changelog
