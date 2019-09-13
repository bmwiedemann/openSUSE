#
# spec file for package movit
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _sonum  8
Name:           movit
Version:        1.6.3
Release:        0
Summary:        GPU video filter library
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Url:            https://movit.sesse.net
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM movit-1.6.0-versioned-shaderdir.patch -- Make shader directory versioned
Patch0:         movit-1.6.0-versioned-shaderdir.patch
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(eigen3)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(sdl2)
%if 0%{?suse_version} == 1315
# For SLE12
BuildRequires:  gcc7-c++
%else
BuildRequires:  gcc-c++
%endif

%description
Movit is a library for video filters. It uses the GPU present in many
computers to accelerate computation of common filters and
transitions, facilitating real-time HD video editing.

%package -n libmovit%{_sonum}
Summary:        GPU video filter library
Group:          System/Libraries
Requires:       %{name}%{_sonum}-data
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libmovit%{_sonum}
Movit is a library for video filters. It uses the GPU present in many
computers to accelerate computation of common filters and
transitions, facilitating real-time HD video editing.

This package contains the Movit shared library.

%package        devel
Summary:        Development files for the Movit GPU video filter library
Group:          Development/Libraries/C and C++
Requires:       libmovit%{_sonum} = %{version}

%description    devel
Movit is a library for video filters. It uses the GPU present in many
computers to accelerate computation of common filters and
transitions, facilitating real-time HD video editing.

This package contains the development files (library and header files).

%package -n     movit%{_sonum}-data
Summary:        Data files for the Movit GPU video filter library
Group:          Development/Libraries/C and C++
Provides:       %{name}-data = %{version}
Obsoletes:      %{name}-data < %{version}
BuildArch:      noarch

%description -n movit%{_sonum}-data
Movit is a library for video filters. It uses the GPU present in many
computers to accelerate computation of common filters and
transitions, facilitating real-time HD video editing.

This package contains the architecture-independent data files (GLSL
fragment shaders).

%prep
%setup -q
%patch0 -p1

%build
# For SLE12, force use of GCC 7
test -x "$(type -p gcc-7)" && export CC=gcc-7
test -x "$(type -p g++-7)" && export CXX=g++-7

./autogen.sh
%configure \
  --disable-static \
  --with-shaderdir="%{_datadir}/%{name}%{_sonum}"

make %{?_smp_mflags} TESTS=

%install
%make_install
rm %{buildroot}%{_libdir}/libmovit.la

%post -n libmovit%{_sonum} -p /sbin/ldconfig
%postun -n libmovit%{_sonum} -p /sbin/ldconfig

%files -n libmovit%{_sonum}
%license COPYING
%doc README NEWS
%{_libdir}/libmovit.so.*

%files -n movit%{_sonum}-data
%license COPYING
%{_datadir}/movit%{_sonum}/

%files devel
%license COPYING
%{_libdir}/libmovit.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
