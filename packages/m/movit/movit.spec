#
# spec file for package movit
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        1.7.2
Release:        0
Summary:        GPU video filter library
License:        GPL-2.0-or-later
URL:            https://movit.sesse.net
Source0:        %{name}-%{version}.tar.xz
# Upstream 1.7.2 release tarball misses COPYING (present in git); fetch it
# from the 1.7.1 service-generated tarball (identical GPL-2.0 text).
Source1:        COPYING
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(eigen3) >= 3.4.0
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
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
# Shaders used to be split; Ensure upgrade path until Leap 15.5 EOL (Dec. 2024).
Provides:       %{name}%{_sonum}-data = %{version}
Obsoletes:      %{name}%{_sonum}-data < %{version}

%description -n libmovit%{_sonum}
Movit is a library for video filters. It uses the GPU present in many
computers to accelerate computation of common filters and
transitions, facilitating real-time HD video editing.

This package contains the Movit shared library.

%package        devel
Summary:        Development files for the Movit GPU video filter library
Requires:       libmovit%{_sonum} = %{version}

%description    devel
Movit is a library for video filters. It uses the GPU present in many
computers to accelerate computation of common filters and
transitions, facilitating real-time HD video editing.

This package contains the development files (library and header files).

%prep
%setup -q

%build
# For SLE12, force use of GCC 7
test -x "$(type -p gcc-7)" && export CC=gcc-7
test -x "$(type -p g++-7)" && export CXX=g++-7

./autogen.sh
%configure --disable-static

%make_build TESTS=

%install
%make_install
rm %{buildroot}%{_libdir}/libmovit.la
install -D -m 0644 %{SOURCE1} %{buildroot}%{_licensedir}/libmovit%{_sonum}/COPYING

%post -n libmovit%{_sonum} -p /sbin/ldconfig
%postun -n libmovit%{_sonum} -p /sbin/ldconfig

%files -n libmovit%{_sonum}
%license %{_licensedir}/libmovit%{_sonum}/COPYING
%dir %{_licensedir}/libmovit%{_sonum}
%doc README NEWS
%{_libdir}/libmovit.so.*

%files devel
%{_libdir}/libmovit.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%changelog
