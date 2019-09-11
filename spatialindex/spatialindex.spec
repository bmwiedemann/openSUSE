#
# spec file for package libspatialindex
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

# See also http://en.opensuse.org/openSUSE:Shared_library_packaging_policy

Name:           spatialindex
Version:        1.8.5
Release:        0
Summary:        A library for spatial indexing
License:        MIT
Group:          Productivity/Graphics/Other
Url:            https://libspatialindex.github.io
Source0:        http://download.osgeo.org/libspatialindex/spatialindex-src-%{version}.tar.bz2
Source1:        http://download.osgeo.org/libspatialindex/spatialindex-src-%{version}.tar.bz2.md5
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkg-config

%description
An extensible framework that will support robust spatial indexing methods.

Support for sophisticated spatial queries. Range, point location, nearest
neighbor and k-nearest neighbor as well as parametric queries (defined by
spatial constraints) should be easy to deploy and run.

Easy to use interfaces for inserting, deleting and updating information.

Wide variety of customization capabilities. Basic index and storage
characteristics like the page size, node capacity, minimum fan-out, splitting
algorithm, etc. should be easy to customize.

Index persistence. Internal memory and external memory structures should be
supported. Clustered and non-clustered indices should be easy to be persisted.

%package -n lib%{name}4
Summary:        A library for spatial indexing
Group:          Productivity/Graphics/Other

%description -n lib%{name}4
libspatialindex provides a general framework for developing spatial indices.
Currently it defines generic interfaces, provides simple main memory and disk
based storage managers and a robust implementation of an R*-tree, an MVR-tree
and a TPR-tree.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       lib%{name}4 = %{version}
Provides:       lib%{name}-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-src-%{version}

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -n lib%{name}4 -p /sbin/ldconfig

%postun -n lib%{name}4 -p /sbin/ldconfig

%files -n lib%{name}4
%defattr(-,root,root,-)
%doc COPYING
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%doc COPYING
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/libspatialindex.pc

%changelog
