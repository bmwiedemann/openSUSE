#
# spec file for package fdk-aac-free
#
# Copyright (c) 2020 Red Hat, Inc.
# Copyright (c) 2021 Neal Gompa <ngompa@opensuse.org>.
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

%global somajor 2
%global origname fdk-aac
%global libname lib%{origname}%{somajor}
%global devname lib%{origname}-devel

Name:           fdk-aac-free
Version:        2.0.0
Release:        0
Summary:        Modified Version of the Fraunhofer FDK AAC Codec Library for Android
Group:          Productivity/Multimedia/Other
License:        FDK-AAC
URL:            https://cgit.freedesktop.org/~wtay/fdk-aac/log/?h=fedora
Source0:        https://people.freedesktop.org/~wtay/fdk-aac-free-%{version}.tar.gz
Source99:       baselibs.conf

BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make

%description
The Third-Party Modified Version of the Fraunhofer FDK AAC Codec Library
for Android is software that implements part of the MPEG Advanced Audio Coding
("AAC") encoding and decoding scheme for digital audio.


%package -n %{libname}
Summary:        Modified Version of the FDK AAC Codec Library for Android
Group:          System/Libraries

%description -n %{libname}
The Third-Party Modified Version of the Fraunhofer FDK AAC Codec Library
for Android is software that implements part of the MPEG Advanced Audio Coding
("AAC") encoding and decoding scheme for digital audio.

%package -n %{devname}
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{?_isa} = %{version}-%{release}
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-devel%{?_isa} = %{version}-%{release}

%description -n %{devname}
The %{devname} package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup


%build
autoreconf -fiv
%configure \
  --disable-silent-rules \
  --disable-static

%make_build


%install
%make_install INSTALL="install -p"
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n %{libname}

%files -n %{libname}
%doc ChangeLog README.fedora
%license NOTICE
%{_libdir}/libfdk-aac.so.%{somajor}{,.*}

%files -n %{devname}
%doc documentation/*.pdf
%dir %{_includedir}/fdk-aac
%{_includedir}/fdk-aac/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/fdk-aac.pc

%changelog
