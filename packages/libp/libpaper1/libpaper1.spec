#
# spec file for package libpaper1
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


Name:           libpaper1
Version:        1.1.28
Release:        0
Summary:        Library to handle papers
License:        GPL-2.0-or-later
Group:          System/Libraries
URL:            https://packages.debian.org/unstable/source/libpaper
Source:         http://ftp.de.debian.org/debian/pool/main/libp/libpaper/libpaper_%{version}.tar.gz
Source1:        libpaper1-rpmlintrc
%if 0%{?suse_version}
BuildRequires:  autoconf
BuildRequires:  libtool
Recommends:     groff
 %if 0%{?suse_version} > 1020
BuildRequires:  fdupes
 %endif
%endif

%description
This package contains a simple library for use by programs needing to
handle papers. It lets program automatically recognize a lot of
different papers with their properties (actually their size).

%package -n libpaper-utils
Summary:        Utilities for handling paper characteristics
Group:          System/Libraries
Requires:       %{name} = %{version}

%description -n libpaper-utils
This package contains utilities for setting the system's default
paper type and for accessing paper type information from shell
scripts.

%package -n libpaper-devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description -n libpaper-devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q -n libpaper-%{version}

%build
autoreconf -fi
%configure --disable-static
%make_build

%install
%make_install
# remove unneeded files
rm %{buildroot}%{_libdir}/libpaper.la
# build the docdir
mkdir -p %{buildroot}%{_defaultdocdir}/libpaper
cp COPYING README ChangeLog debian/changelog %{buildroot}%{_defaultdocdir}/libpaper/
%if 0%{?suse_version} > 1020
%fdupes -s %{buildroot}
%endif

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%{_libdir}/libpaper.so.1*

%files -n libpaper-utils
%if 0%{?suse_version} >= 01500
%license %{_defaultdocdir}/libpaper/COPYING
%doc %{_defaultdocdir}/libpaper/{README,ChangeLog,changelog}
%dir %{_defaultdocdir}/libpaper
%else
%doc %{_defaultdocdir}/libpaper
%endif
%{_mandir}/man1/*
%{_mandir}/man8/*
%{_bindir}/paperconf
%{_sbindir}/paperconfig

%files -n libpaper-devel
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_includedir}/paper.h
%{_libdir}/libpaper.so

%changelog
