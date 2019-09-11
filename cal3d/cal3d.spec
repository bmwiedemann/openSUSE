#
# spec file for package cal3d
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


%define major   12
%define oname   Cal3D
Name:           cal3d
Version:        0.120
Release:        0
Summary:        A 3D character animation library
License:        LGPL-2.1+
Group:          Productivity/Graphics/Convertors
Url:            http://home.gna.org/cal3d/
Source:         https://github.com/mp3butcher/Cal3D/archive/%{version}.tar.gz#/%{oname}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM fix-boolean-to-pointer.patch -- https://gna.org/bugs/index.php?24805
Patch0:         fix-boolean-to-pointer.patch
# PATCH-FIX-OPENSUSE fix-date-time.patch -- reduce warnings about data and time
Patch1:         fix-date-time.patch
# PATCH-FEATURE-UPSTREAM add-vsxu-support.patch -- https://gna.org/bugs/index.php?25601
Patch2:         add-vsxu-support.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  docbook-toys
BuildRequires:  doxygen
BuildRequires:  freeglut-devel
BuildRequires:  gcc-c++
BuildRequires:  glew-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  sgml-skel
Requires:       lib%{name}%{major} = %{version}
Requires:       pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Cal3D is a skeletal based 3D character animation library written
in C++ in a platform-/graphic API-independent way. Originally
designed to be used in a 3D client for Worldforge, it evolved
into a stand-alone product which can be used in many different
kinds of projects. It supports combining animations and actions
through a 'mixer' interface, and work is currently underway to
integrate morph targets (interpolating between one mesh and
another, using the same vertex sequence) easily into the system.

%package -n lib%{name}%{major}
Summary:        Shared libraries for cal3d
Group:          System/Libraries

%description -n lib%{name}%{major}
Cal3D is a skeletal based 3D character animation library written
in C++ in a platform-/graphic API-independent way. Originally
designed to be used in a 3D client for Worldforge, it evolved
into a stand-alone product which can be used in many different
kinds of projects. It supports combining animations and actions
through a 'mixer' interface, and work is currently underway to
integrate morph targets (interpolating between one mesh and
another, using the same vertex sequence) easily into the system.

This package contains the shared libraries for cal3d.

%package devel
Summary:        Development files for cal3d
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{major} = %{version}

%description devel
This package contains libraries, include files, and other resource
you can use to develop applications using animated characters with
cal3d.

%package doc
Summary:        Documentation files for cal3D
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description doc
This package contains modeling documention and a users guide
for cal3d.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

pushd %{name}
sed -e 's/AM_USE_UNITTESTCPP/#\ AM_USE_UNITTESTCPP/' -i configure.in
autoreconf -vi
popd

%build
pushd %{name}
%configure
make %{?_smp_mflags}

pushd docs
make %{?_smp_mflags} doc-api doc-guide
popd
popd

%install
pushd %{name}
%make_install
pushd
find %{buildroot}%{_libdir} -name *.la -delete

%post -n lib%{name}%{major} -p /sbin/ldconfig
%postun -n lib%{name}%{major} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc %{name}/AUTHORS %{name}/ChangeLog %{name}/COPYING %{name}/README %{name}/TODO
%{_bindir}/cal3d_converter
%{_mandir}/man1/*

%files -n lib%{name}%{major}
%defattr(-,root,root)
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}/
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%defattr(-,root,root)
%doc %{name}/docs/guide
%doc %{name}/docs/api/html

%changelog
