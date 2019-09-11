#
# spec file for package libclastfm0
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libclastfm0
Version:        0.5
Release:        0
Summary:        Unofficial C-API for the Last.fm Web Service
License:        GPL-3.0+
Group:          System/Libraries
Url:            http://liblastfm.sourceforge.net/
Source0:        http://downloads.sourceforge.net/liblastfm/libclastfm-%{version}.tar.gz
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libcurl)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libclastfm shared library.

libclastfm is an unofficial C-API for the Last.fm web service written
with libcurl. Has support for Album, Artist and User API methods as well
as full audio scrobbler support.

%package -n libclastfm-devel
Summary:        Unofficial C-API for the Last.fm Web Service
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description -n libclastfm-devel
libclastfm development files.

libclastfm is an unofficial C-API for the Last.fm web service written
with libcurl. Has support for Album, Artist and User API methods as well
as full audio scrobbler support.

%prep
%setup -qn libclastfm-%{version}

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*.so.*

%files -n libclastfm-devel
%defattr(-,root,root,-)
# FIXME: ChangeLog and NEWS don't contain any real info at the moment --
# not packaged
%doc AUTHORS README
%{_includedir}/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
