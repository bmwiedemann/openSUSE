#
# spec file for package httrack
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define so_ver 2
Name:           httrack
Version:        3.49.2
Release:        0
Summary:        Offline Browser Utility
License:        GPL-3.0+
Group:          Productivity/Networking/Web/Utilities
Url:            http://www.httrack.com/
Source0:        https://mirror.httrack.com/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE httrack-fix-strict-aliasing-punning.patch malcolmlewis@opensuse.org -- Add -fno-strict-aliasing to DEFAULT_CFLAGS
Patch0:         httrack-fix-strict-aliasing-punning.patch
BuildRequires:  fdupes
BuildRequires:  libopenssl-devel
BuildRequires:  update-desktop-files
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
Group:          Development/Libraries/Other
Requires:       libhttrack%{so_ver} = %{version}
Requires:       libopenssl-devel

%description devel
This package contains the header and library files for httrack.

%package -n libhttrack%{so_ver}
Summary:        Shared library for httrack
Group:          System/Libraries

%description -n libhttrack%{so_ver}
This package contains the httrack shared libraries.

%prep
%setup -q
%patch0

%build
%configure \
  --disable-static \
  --docdir=%{_docdir}/%{name} \
  --htmldir=%{_datadir}/%{name}/html
make %{?_smp_mflags}

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} install

%suse_update_desktop_file WebHTTrack-Websites Network WebBrowser
%suse_update_desktop_file WebHTTrack Network WebBrowser

# Remove generic header and libtool files
find %{buildroot} -name 'config.h' -exec rm {} \;
sed -i '/#include "config.h"/d' %{buildroot}%{_includedir}/%{name}/htsglobal.h
find %{buildroot} -type f -name "*.la" -delete -print

# Clean up icons
rm -f %{buildroot}%{_datadir}/pixmaps/httrack16x16.xpm
rm -f %{buildroot}%{_datadir}/pixmaps/httrack32x32.xpm
mv %{buildroot}%{_datadir}/pixmaps/httrack48x48.xpm %{buildroot}%{_datadir}/pixmaps/httrack.xpm

# For moving to docdir
rm -rf ./libtest ./templates
mv %{buildroot}%{_datadir}/%{name}/libtest .
mv %{buildroot}%{_datadir}/%{name}/templates .
# Install additional docs (do it manually to fix also rpmlint warning "files-duplicate")
cp -af AUTHORS COPYING README gpl-fr.txt greetings.txt history.txt httrack-doc.html license.txt templates/ %{buildroot}%{_docdir}/%{name}/
# No need to be in there
rm -f %{buildroot}%{_datadir}/%{name}/html/{greetings.txt,history.txt,httrack-doc.html,license.txt}

%fdupes -s %{buildroot}

%post -n libhttrack%{so_ver} -p /sbin/ldconfig
%postun -n libhttrack%{so_ver} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}/
%{_bindir}/htsserver
%{_bindir}/httrack
%{_bindir}/proxytrack
%{_bindir}/webhttrack
%{_datadir}/applications/WebHTTrack-Websites.desktop
%{_datadir}/applications/WebHTTrack.desktop
%dir %{_datadir}/icons/hicolor/
%dir %{_datadir}/icons/hicolor/*/
%dir %{_datadir}/icons/hicolor/*/apps/
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/pixmaps/*.xpm
%{_datadir}/%{name}/
%{_mandir}/man1/*%{ext_man}

%files devel
%defattr(-,root,root,-)
%doc libtest/
%{_includedir}/%{name}/
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/*.so
%{_libdir}/*.so

%files -n libhttrack%{so_ver}
%defattr(-,root,root,-)
%dir %{_libdir}/%{name}/
%{_libdir}/%{name}/*.so.*
%{_libdir}/*.so.%{so_ver}*

%changelog
