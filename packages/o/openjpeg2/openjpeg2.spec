#
# spec file for package openjpeg2
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define library_name  libopenjp2-7
%define base_version 2.3

Name:           openjpeg2
Version:        2.3.1
Release:        0
Summary:        Opensource JPEG 2000 Codec Implementation
License:        BSD-2-Clause
Group:          Productivity/Graphics/Other
Url:            http://www.openjpeg.org/
Source0:        https://github.com/uclouvain/openjpeg/archive/v%{version}.tar.gz#/openjpeg-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  cmake > 2.8.2
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The OpenJPEG library is an open-source JPEG 2000 codec written in C language.
It has been developed in order to promote the use of JPEG 2000, the new
still-image compression standard from the Joint Photographic Experts Group
(JPEG).

This package provides the codec executables.

%package -n %{library_name}
Summary:        Opensource JPEG 2000 Codec Implementation
Group:          System/Libraries

%description -n %{library_name}
The OpenJPEG library is an open-source JPEG 2000 codec written in C language.
It has been developed in order to promote the use of JPEG 2000, the new
still-image compression standard from the Joint Photographic Experts Group
(JPEG).

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:       %{library_name} = %{version}
Requires:       %{name} = %{version}

%description    devel
The OpenJPEG library is an open-source JPEG 2000 codec written in C language.
It has been developed in order to promote the use of JPEG 2000, the new
still-image compression standard from the Joint Photographic Experts Group
(JPEG).

This package provides the development files for %{name}.

%prep
%setup -q -n openjpeg-%{version}
# do not embed timestamps into html documentation
sed -i 's|^HTML_TIMESTAMP[ =].*$|HTML_TIMESTAMP = NO|' doc/Doxyfile.dox.cmake.in

# ensure no bundled libraries are used
for d in thirdparty/*; do
    [ -d "$d" ] && rm -rf "$d"
done

%build
%cmake \
  -DBUILD_SHARED_LIBS=ON \
  -DBUILD_CODEC=ON \
  -DBUILD_JPIP=OFF \
  -DBUILD_JPWL=OFF \
  -DBUILD_MJ2=OFF \
  -DBUILD_TESTING=OFF \
  -DBUILD_DOC=ON \
  -DBUILD_THIRDPARTY=OFF \
  -DOPENJPEG_INSTALL_LIB_DIR=%{_lib}

make %{?_smp_mflags} VERBOSE=1 all doc

cat << END > libopenjp2.pc

Name:           openjpeg
Version:        %{version}
Url:            %{url}
Description: Opensource JPEG 2000 Codec Implementation
Libs: -L%{_libdir} -lopenjp2
Libs.private: -lm
Cflags: -I%{_includedir}/openjpeg-%{base_version}
END
%fdupes -s doc/html/

%install
%cmake_install

mkdir -p %{buildroot}%{_libdir}/pkgconfig/
install -m 644 build/libopenjp2.pc %{buildroot}%{_libdir}/pkgconfig/
rm -rf %{buildroot}%{_datadir}/doc

%post -n %{library_name} -p /sbin/ldconfig

%postun -n %{library_name} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS.md CHANGELOG.md NEWS.md LICENSE README.md THANKS.md
%{_bindir}/opj_*
%{_mandir}/man1/opj_*.1%{ext_man}

%files -n %{library_name}
%defattr(-,root,root,-)
%{_libdir}/libopenjp2.so.*

%files devel
%defattr(-,root,root,-)
%doc build/doc/html/
%{_includedir}/openjpeg-%{base_version}/
%{_libdir}/libopenjp2.so
%{_libdir}/pkgconfig/libopenjp2.pc
%{_libdir}/openjpeg-%{base_version}/
%{_mandir}/man3/libopenjp2.3%{ext_man}

%changelog
