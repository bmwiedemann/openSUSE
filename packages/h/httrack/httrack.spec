#
# spec file for package httrack
#
# Copyright (c) 2026 SUSE LLC and contributors
# Copyright (c) 2011 Malcolm Lewis malcolmlewis@opensuse.org
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


%define so_ver 3
Name:           httrack
Version:        3.50.0
Release:        0
Summary:        Offline Browser Utility
License:        GPL-3.0-or-later
URL:            https://www.httrack.com/
Source0:        https://github.com/xroche/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
## Added for invalid-desktopfile, which actually validates??
Source99:       %{name}-rpmlintrc
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
HTTrack is a free (GPL, libre/free software) and easy-to-use offline
browser utility.

It allows you to download a World Wide Web site from the Internet to a
local directory, building recursively all directories, getting HTML,
images, and other files from the server to your computer. HTTrack
arranges the original site's relative link-structure. Simply open a page
of the "mirrored" website in your browser, and you can browse the site
from link to link, as if you were viewing it online. HTTrack can also
update an existing mirrored site, and resume interrupted downloads.

HTTrack is fully configurable, and has an integrated help system.

%package devel
Summary:        Development files for httrack
Requires:       libhttrack%{so_ver} = %{version}
Requires:       pkgconfig(openssl)

%description devel
This package contains the header and library files for httrack.

%package doc
Summary:        HTTrack documentation
BuildArch:      noarch

%description doc
HTML documentation for httrack.

%package -n libhttrack%{so_ver}
Summary:        Shared library for httrack
Group:          System/Libraries

%description -n libhttrack%{so_ver}
This package contains the httrack shared libraries.

%prep
%autosetup

%build
%configure \
   --disable-static \
   --disable-example-libs \
   --docdir=%{_docdir}/%{name}
%make_build

%install
%make_install

# Remove libtool files
find %{buildroot} -type f -name "*.la" -delete -print

%fdupes -s %{buildroot}

%post -n libhttrack%{so_ver} -p /sbin/ldconfig
%postun -n libhttrack%{so_ver} -p /sbin/ldconfig

%files
%license license.txt
%{_bindir}/htsserver
%{_bindir}/httrack
%{_bindir}/proxytrack
%{_bindir}/webhttrack
%{_datadir}/applications/WebHTTrack-Websites.desktop
%{_datadir}/applications/WebHTTrack.desktop
%{_datadir}/icons/hicolor/*/apps/*.{png,svg}
%{_datadir}/pixmaps/*.xpm
%{_datadir}/%{name}
%exclude %{_datadir}/%{name}/libtest/*.{c,h}
%{_datadir}/metainfo/com.httrack.WebHTTrack.metainfo.xml
%{_mandir}/man1/*%{ext_man}

%files devel
%{_datadir}/%{name}/libtest/*.{c,h}
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/libhttrack.pc

%files doc
%doc %{_docdir}/%{name}

%files -n libhttrack%{so_ver}
%{_libdir}/*.so.%{so_ver}*

%changelog
