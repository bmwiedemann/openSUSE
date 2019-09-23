#
# spec file for package glyr
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define major   1

Name:           glyr
Version:        1.0.10
Release:        0
Summary:        Search engine for music related metadata
License:        LGPL-3.0
Group:          Productivity/Networking/Web/Utilities
Url:            https://github.com/sahib/glyr
Source0:        https://github.com/sahib/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source100:      baselibs.conf
# PATCH-FIX-OPENSUSE glyr-date-n-time.patch lazy.kent@opensuse.org -- remove __DATE__ and __TIME__ that causes the package to rebuild when not needed
Patch0:         glyr-date-n-time.patch
# PATCH-FIX-OPENSUSE glyr-optflags.patch lazy.kent@opensuse.org -- use default openSUSE optimization flags.
Patch1:         glyr-optflags.patch
# PATCH-FIX-OPENSUSE glyr-pkgconfig.patch crrodriguez@opensuse.org -- do not inject bogus dependencies into other packages.
Patch2:         glyr-pkgconfig.patch
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(sqlite3)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The sort of metadata glyr is searching (and downloading) is usually the
data you see in your music player. It was originally written
to serve as internal library for a music player, but has been extended
to work as a standalone program.

%package -n glyrc
Summary:        Search engine for music related metadata
Group:          Productivity/Networking/Web/Utilities
Provides:       glyr = %{version}
Obsoletes:      glyr < 1.0.0

%description -n glyrc
This subpackage contains the Glyr CLI tool.

The sort of metadata glyr is searching (and downloading) is usually the
data you see in your music player. It was originally written
to serve as internal library for a music player, but has been extended
to work as a standalone program which is able to download:

* cover art;
* lyrics;
* bandphotos;
* artist biography;
* album reviews;
* tracklists of an album;
* a list of albums from a specific artist;
* tags, either related to artist, album or title relations, for example
  links to Wikipedia;
* similar artists;
* similar songs.

%package -n lib%{name}%{major}
Summary:        Search engine for music related metadata
Group:          System/Libraries

%description -n lib%{name}%{major}
The Glyr shared library.

%package devel
Summary:        Development files for glyr, a music metadata search engine
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{major} = %{version}
Provides:       libglyr-devel = %{version}
Obsoletes:      libglyr-devel < 1.0.5

%description devel
Glyr development files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2

%build
%cmake
make %{?_smp_mflags} VERBOSE=1

%install
%cmake_install

%post -n libglyr%{major} -p /sbin/ldconfig

%postun -n libglyr%{major} -p /sbin/ldconfig

%files -n glyrc
%defattr(-,root,root,-)
%doc AUTHORS COPYING README.textile state_of_providers.txt
%{_bindir}/glyrc

%files -n lib%{name}%{major}
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS COPYING README.textile state_of_providers.txt
%doc src/examples
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
