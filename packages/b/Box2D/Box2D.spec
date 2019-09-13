#
# spec file for package Box2D
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Adam Mizerski <adam@mizerski.pl>
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


%define so_ver 2_3_1
Name:           Box2D
Version:        2.3.1
Release:        0
Summary:        A 2D Physics Engine for Games
License:        Zlib
Group:          Development/Libraries/C and C++
Url:            http://box2d.org/
Source0:        https://github.com/erincatto/Box2D/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM Box2D-fix-version-2.3.1.patch -- already fixed upstream
Patch0:         %{name}-fix-version-2.3.1.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake >= 3
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
%if 0%{?suse_version}
BuildRequires:  fdupes
%endif

%description
Box2D is an open source C++ engine for simulating rigid bodies in 2D.

%package -n lib%{name}%{so_ver}
Summary:        A 2D Physics Engine for Games
Group:          System/Libraries

%description -n lib%{name}%{so_ver}
Box2D is an open source C++ engine for simulating rigid bodies in 2D.

%package -n lib%{name}-devel
Summary:        A 2D Physics Engine for Games
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{so_ver} = %{version}

%description -n lib%{name}-devel
Box2D is an open source C++ engine for simulating rigid bodies in 2D.

%package doc
Summary:        A 2D Physics Engine for Games
Group:          Documentation/Other
BuildArch:      noarch

%description doc
Box2D is an open source C++ engine for simulating rigid bodies in 2D.

%prep
%setup -q -n %{name}-%{version}/%{name}
dos2unix Changes.txt License.txt Readme.txt
%patch0

%build
%cmake \
    -DBOX2D_INSTALL=ON \
    -DBOX2D_INSTALL_DOC=ON \
    -DBOX2D_BUILD_SHARED=ON \
    -DBOX2D_BUILD_STATIC=OFF \
    -DBOX2D_BUILD_EXAMPLES=OFF \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo
make VERBOSE=1 %{?_smp_mflags}

%install
%cmake_install
%if 0%{?suse_version}
%fdupes -s %{buildroot}%{_datadir}/doc/%{name}/Documentation/API/html
%endif

%post -n lib%{name}%{so_ver} -p /sbin/ldconfig

%postun -n lib%{name}%{so_ver} -p /sbin/ldconfig

%files -n lib%{name}%{so_ver}
%defattr(-,root,root,-)
%{_libdir}/lib%{name}.so.*

%files -n lib%{name}-devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/%{name}
%{_libdir}/cmake/%{name}

%files doc
%defattr(-,root,root,-)
%doc Changes.txt License.txt Readme.txt
%{_datadir}/doc/%{name}/

%changelog
