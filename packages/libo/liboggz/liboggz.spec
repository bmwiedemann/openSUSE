#
# spec file for package liboggz
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define _SO_nr 2
Name:           liboggz
Version:        1.1.3
Release:        0
Summary:        Shared libraries for oggz
License:        BSD-3-Clause
Group:          System/Libraries
URL:            https://xiph.org/oggz/
Source0:        https://downloads.xiph.org/releases/liboggz/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         0001-oggz-comment-Set-last-header-flag-for-vorbis-comment.patch
BuildRequires:  doxygen
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ogg)

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

%description devel
This package contains all necessary include files and libraries
needed to develop applications that require these.

%package doc
Summary:        Documentation for Oggz
Group:          Documentation/HTML
Requires:       %{name}%{_SO_nr} = %{version}
BuildArch:      noarch

%description doc
This package contains HTML documentation needed for development using
liboggz

%prep
%autosetup -p1

%build
%configure \
	--disable-static \
	--docdir=%{_docdir}/%{name} \
	%{nil}
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%ldconfig_scriptlets -n liboggz%{_SO_nr}

%files -n liboggz%{_SO_nr}
%license COPYING
%{_libdir}/%{name}.so.%{_SO_nr}
%{_libdir}/%{name}.so.%{_SO_nr}.*

%files -n oggz-tools
%license COPYING
%doc AUTHORS ChangeLog README
%{_mandir}/man1/oggz*
%{_bindir}/oggz*

%files devel
%license COPYING
%{_libdir}/%{name}.so
%{_includedir}/oggz/
%{_libdir}/pkgconfig/oggz.pc

%files doc
%license COPYING
%doc %{_docdir}/%{name}

%changelog
