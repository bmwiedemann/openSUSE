#
# spec file for package rnnoise
#
# Copyright (c) 2024 SUSE LLC
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


%define libname librnnoise0
Name:           rnnoise
Version:        0.2
Release:        0
Summary:        Recurrent neural network for audio noise reduction
License:        BSD-3-Clause
URL:            https://gitlab.xiph.org/xiph/rnnoise
Source:         https://gitlab.xiph.org/xiph/rnnoise/-/archive/v%{version}/rnnoise-v%{version}.tar.gz
Source1:        https://media.xiph.org/rnnoise/models/rnnoise_data-0b50c45.tar.gz
# PATCH-FIX-UPSTREAM - https://github.com/xiph/rnnoise/issues/222
Patch1:         372f7b4.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
Requires:       python3-Keras

%description
RNNoise is a noise suppression library based on a recurrent neural network.
This package holds the training tools.

%package -n %{libname}
Summary:        Recurrent neural network for audio noise reduction - Shared library

%description -n %{libname}
RNNoise is a noise suppression library based on a recurrent neural network.

This package holds the shared library.

%package devel
Summary:        Recurrent neural network for audio noise reduction - Development Files
Requires:       %{libname} = %{version}

%description devel
RNNoise is a noise suppression library based on a recurrent neural network.

This package holds the development files.

%prep
%autosetup -p1 -n %{name}-v%{version}

%build
cp -p %{SOURCE1} .
./autogen.sh
%configure \
 --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_datadir}/doc/%{name}/{AUTHORS,COPYING,README}

%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%doc README TRAINING-README
%license COPYING
%{_libdir}/librnnoise.so.0*

%files devel
%{_includedir}/rnnoise.h
%{_libdir}/librnnoise.so
%{_libdir}/pkgconfig/rnnoise.pc

%changelog
