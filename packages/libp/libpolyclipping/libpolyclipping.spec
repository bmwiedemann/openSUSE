#
# spec file for package libpolyclipping
#
# Copyright (c) 2021 SUSE LLC
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


%define packagename polyclipping
%define sonum 22
%define libname %{name}%{sonum}
Name:           libpolyclipping
Version:        6.4.2
Release:        0
Summary:        Polygon clipping library
License:        BSL-1.0
URL:            https://sourceforge.net/projects/polyclipping
Source:         https://sourceforge.net/projects/polyclipping/files/clipper_ver%{version}.zip
BuildRequires:  cmake
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  unzip

%description
This library primarily performs the boolean clipping operations -
intersection, union, difference & xor - on 2D polygons. It also performs
polygon offsetting. The library handles complex (self-intersecting) polygons,
polygons with holes and polygons with overlapping co-linear edges.
Input polygons for clipping can use EvenOdd, NonZero, Positive and Negative
filling modes. The clipping code is based on the Vatti clipping algorithm,
and outperforms other clipping libraries.

%package -n    %{libname}
Summary:        Polygon clipping library

%description -n    %{libname}
This library primarily performs the boolean clipping operations -
intersection, union, difference & xor - on 2D polygons. It also performs
polygon offsetting. The library handles complex (self-intersecting) polygons,
polygons with holes and polygons with overlapping co-linear edges.
Input polygons for clipping can use EvenOdd, NonZero, Positive and Negative
filling modes. The clipping code is based on the Vatti clipping algorithm,
and outperforms other clipping libraries.

%package        devel
Summary:        Development files for %{name}
Requires:       %{libname} = %{version}

%description    devel
The %{packagename}-devel package contains libraries and header files for
developing applications that use %{packagename}.

%prep
%setup -qc

# Delete binaries
find . \( -name "*.exe" -o -name "*.dll" \) -delete

# Correct line ends and encodings
find . -type f -exec dos2unix -k {} \;

for filename in "Third Party/perl/perl_readme.txt" README; do
  iconv -f iso8859-1 -t utf-8 "${filename}" > "${filename}".conv && \
    touch -r "${filename}" "${filename}".conv && \
    mv "${filename}".conv "${filename}"
done

# use proper directory for pkgconfig
sed -i 's|SET.*CMAKE_INSTALL_PKGCONFIGDIR.*|SET(CMAKE_INSTALL_PKGCONFIGDIR "${CMAKE_INSTALL_LIBDIR}/pkgconfig")|' \
 cpp/CMakeLists.txt

%build
pushd cpp
  %cmake
  %cmake_build
popd

%install
pushd cpp
  %cmake_install
# Install agg header with corrected include statement
  sed -e 's/\.\.\/clipper\.hpp/clipper.hpp/' < cpp_agg/agg_conv_clipper.h > %{buildroot}/%{_includedir}/%{packagename}/agg_conv_clipper.h
popd

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%license License.txt
%{_libdir}/lib%{packagename}.so.%{sonum}*

%files devel
%doc README Documentation
%{_includedir}/%{packagename}/
%{_libdir}/lib%{packagename}.so
%{_libdir}/pkgconfig/%{packagename}.pc

%changelog
