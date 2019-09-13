#
# spec file for package liboggz
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define _SO_nr 2
%define noarch_sub_pkg 0
%if %suse_version > 1110
%define noarch_sub_pkg 1
%endif

Name:           liboggz
Version:        1.1.1
Release:        0
Summary:        Shared libraries for oggz
License:        BSD-3-Clause
Group:          System/Libraries
Url:            http://xiph.org/oggz/
Source0:        http://downloads.xiph.org/releases/liboggz/%name-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM liboggz-1.1.1-docdir.patch https://trac.xiph.org/ticket/1758 reddwarf@opensuse.org -- This patch makes configure honor --docdir
Patch0:         liboggz-1.1.1-docdir.patch
BuildRequires:  doxygen
BuildRequires:  libogg-devel
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
liboggz is a library that provides simple parsing and seeking of
files and streams based on the Ogg file format. liboggz requires
libogg to work.
liboggz knows about Ogg speex, Ogg vorbis, Ogg theora, and the Ogg
based Annodex formats, thus allows parsing (though not decoding) of
these files.

%package -n liboggz%{_SO_nr}

Summary:        Shared Libraries For Oggz
Group:          System/Libraries

%description -n liboggz%{_SO_nr}
liboggz is a library that provides simple parsing and seeking of
files and streams based on the Ogg file format. liboggz requires
libogg to work.
liboggz knows about Ogg speex, Ogg vorbis, Ogg theora, and the Ogg
based Annodex formats, thus allows parsing (though not decoding) of
these files.

%package -n oggz-tools

Summary:        A library that provides parsing and seeking of Ogg-files
Group:          Productivity/Multimedia/Sound/Utilities

%description  -n oggz-tools
liboggz knows about Ogg speex, Ogg vorbis, Ogg theora, and the
Ogg based Annodex formats, thus allows parsing (though not decoding)
of these files. For getting decoding and encoding functionality you
will require in addition libspeex, libvorbis, libtheora, and
libannodex respectively.

%package devel

Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       %{name}%{_SO_nr} = %{version}
Requires:       libogg-devel

%description devel
This package contains all necessary include files and libraries
needed to develop applications that require these.

%package doc

Summary:        Documentation for Oggz
Group:          Documentation/HTML
Requires:       %{name}%{_SO_nr} = %{version}
%if %{noarch_sub_pkg}
BuildArch:      noarch
%endif

%description doc
This package contains HTML documentation needed for development using
liboggz

%prep
%setup -q
%patch0

%build
%configure --disable-static --docdir=%{_docdir}/%{name}
%__make %{?_smp_mflags}

%install
%makeinstall

%__rm %{buildroot}%{_libdir}/lib*.la

rm -rf %{buildroot}%{_docdir}/%{name}/latex

%check
%__make check

%post -n liboggz%{_SO_nr}  -p /sbin/ldconfig

%postun -n liboggz%{_SO_nr} -p /sbin/ldconfig

%files -n liboggz%{_SO_nr}
%defattr(0644,root,root,0755)
%{_libdir}/%{name}.so.*

%files -n oggz-tools
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%doc %{_mandir}/man1/oggz*
%{_bindir}/oggz*

%files devel
%defattr(-,root,root)
%{_libdir}/%{name}.so
%{_includedir}/oggz/
%{_libdir}/pkgconfig/oggz.pc

%files doc
%defattr(-,root,root)
%doc %{_docdir}/%{name}

%changelog
