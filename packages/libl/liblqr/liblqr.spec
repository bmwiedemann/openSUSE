#
# spec file for package liblqr
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define so_ver 0

Name:           liblqr
Version:        0.4.2
Release:        0
Summary:        Liquid Rescale seam-carving library
License:        LGPL-3.0 and GPL-3.0
Group:          System/Libraries
Url:            http://liblqr.wikidot.com/
Source0:        http://liblqr.wikidot.com/local--files/en:download-page/liblqr-1-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  glib2-devel
BuildRequires:  libxslt-tools
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The Liquid Rescale (lqr) library provides a C/C++ API for performing
non-uniform resizing of images by the seam-carving technique.

%package -n liblqr-1-%{so_ver}
Summary:        Liquid Rescale seam-carving library
License:        LGPL-3.0
Group:          System/Libraries

%description -n liblqr-1-%{so_ver}
The Liquid Rescale (lqr) library provides a C/C++ API for performing
non-uniform resizing of images by the seam-carving technique.

%package devel
Summary:        Development files for the Liquid Rescale library
License:        LGPL-3.0
Group:          Development/Libraries/C and C++
Requires:       liblqr-1-%{so_ver} = %{version}

%description devel
The Liquid Rescale (lqr) library provides a C/C++ API for performing
non-uniform resizing of images by the seam-carving technique.

This package contains the development files for liblqr.

%prep
%setup -q -n liblqr-1-%{version}

# Fix docbook path
sed -i "s,/nwalsh/html/chunk.xsl,/nwalsh/current/html/chunk.xsl," docs/lqr_style.xsl

%build
%configure
make %{?_smp_mflags}
cd docs
make
cd ..

%install
make install DESTDIR=%{buildroot}
# remove .la files
find %{buildroot} -name \*.la -exec rm -f {} \;

%post -n liblqr-1-%{so_ver} -p /sbin/ldconfig

%postun -n liblqr-1-%{so_ver} -p /sbin/ldconfig

%files -n liblqr-1-%{so_ver}
%defattr(-,root,root,-)
%doc COPYING.LESSER
%{_libdir}/liblqr-1.so.%{so_ver}*

%files devel
%defattr(-,root,root,-)
%doc AUTHORS COPYING* ChangeLog NEWS README TODO
%doc docs/{liblqr_manual.html,html/}
%{_includedir}/lqr-1/
%{_libdir}/liblqr-1.so
%{_libdir}/pkgconfig/lqr-1.pc

%changelog
