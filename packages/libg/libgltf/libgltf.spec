#
# spec file for package libgltf
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define libname libgltf-0_1-1
Name:           libgltf
Version:        0.1.0
Release:        0
Summary:        C++ Library for rendering OpenGL models stored in glTF format
License:        MPL-2.0
Group:          Productivity/Publishing/Word
Url:            http://dev-www.libreoffice.org/src/libgltf/
Source:         http://dev-www.libreoffice.org/src/libgltf/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glm-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(epoxy) >= 1.3.1
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_headers-devel
%else
BuildRequires:  boost-devel
%endif

%description
%{name} is a library for rendering OpenGL models stored in glTF format

%package -n %{libname}
Summary:        C++ Library for rendering OpenGL models stored in glTF format
Group:          System/Libraries

%description -n %{libname}
%{name} is a library for rendering OpenGL models stored in glTF format

%package devel
Summary:        C++ Library for rendering OpenGL models stored in glTF format
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       glm-devel
Requires:       libstdc++-devel

%description devel
%{name} is a library for rendering OpenGL models stored in glTF format

%prep
%setup -q

%build
export CXXFLAGS="%{optflags} -fvisibility-inlines-hidden"
# Tests require running X with gl extension
%configure \
	--disable-silent-rules \
	--disable-werror \
	--disable-tests \
	--disable-static \
	--docdir=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -f %{buildroot}%{_datadir}/%{name}/html*.css
%fdupes -s %{buildroot}%{_docdir}/%{name}/html

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc AUTHORS NEWS LICENSE README ChangeLog
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/libg*.pc
%{_includedir}/libg*

%changelog
