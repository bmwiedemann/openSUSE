#
# spec file for package libspectre
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Url:            http://libspectre.freedesktop.org/

Name:           libspectre
Version:        0.2.8
Release:        0
Summary:        Library for Rendering PostScript Documents
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Source0:        http://libspectre.freedesktop.org/releases/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-bsc975503.diff bsc#975503 fdo#97091 -- Parse ps files ignoring EOF comments which would stop parsing too soon in documents with embedded EPS files.
Patch0:         fix-bsc975503.diff
%define debug_package_requires libspectre1 = %{version}-%{release}
BuildRequires:  ghostscript-devel
BuildRequires:  ghostscript-library
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
libspectre is a small library for rendering Postscript documents. It
provides a convenient easy to use API for handling and rendering
Postscript documents.

%package -n libspectre1
Summary:        Library for Rendering PostScript Documents
Group:          Development/Libraries/C and C++

%description -n libspectre1
libspectre is a small library for rendering Postscript documents. It
provides a convenient easy to use API for handling and rendering
Postscript documents.

%package -n libspectre-devel
Summary:        Library for Rendering PostScript Documents
Group:          Development/Libraries/C and C++
Requires:       libspectre1 >= %{version}
%requires_eq ghostscript-devel

%description -n libspectre-devel
libspectre is a small library for rendering Postscript documents. It
provides a convenient easy to use API for handling and rendering
Postscript documents.

%prep
%setup -q
%patch0 -p1

%build
%configure --disable-static --enable-shared
make %{?_smp_mflags}

%install
%make_install

%post -n libspectre1 -p /sbin/ldconfig

%postun -n libspectre1 -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files -n libspectre1
%defattr(-, root, root)
%doc COPYING
%{_libdir}/libspectre.so.1*

%files -n libspectre-devel
%defattr(-, root, root)
%{_includedir}/libspectre
%{_libdir}/libspectre.la
%{_libdir}/libspectre.so
%{_libdir}/pkgconfig/libspectre.pc

%changelog
