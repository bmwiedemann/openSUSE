#
# spec file for package stk
#
# Copyright (c) 2022 SUSE LLC
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


# Upstream chose to update the soname with each version
# https://github.com/thestk/stk/issues/89
%define soname %{version}
Name:           stk
Version:        4.6.2
Release:        0
Summary:        Synthesis ToolKit in C++
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://ccrma.stanford.edu/software/stk/
Source0:        %{name}-%{version}.tar.xz
Source99:       stk-rpmlintrc
# PATCH-FIX-UPSTREAM -- Don't ignore provided compiler flags
Patch0:         0001-Don-t-ignore-supplied-CXXFLAGS.patch
# PATCH-FIX-UPSTREAM
Patch1:         0002-Fix-the-library-soname.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)

%description
The Synthesis ToolKit in C++ (STK) is a set of audio signal
processing and algorithmic synthesis classes. STK facilitates
development of music synthesis and audio processing software,
focusing on realtime control and example code. STK is
user-extensible.

%package -n libstk%{soname}
Summary:        Synthesis ToolKit in C++
Group:          System/Libraries
Requires:       %{name}-data

%description -n libstk%{soname}
The Synthesis ToolKit in C++ (STK) is a set of audio signal
processing and algorithmic synthesis classes. STK facilitates
development of music synthesis and audio processing software,
focusing on realtime control and example code. STK is
user-extensible.

%package data
Summary:        Data files for STK, a music synthesis library
BuildArch:      noarch
# data were split to a subpackage before the 4.6.2 update
Conflicts:      libstk4 < 4.6.2

%description data
Data files for STK.

%package devel
Summary:        Development files for STK, a music synthesis library
Group:          Development/Libraries/C and C++
Requires:       libstk%{soname} = %{version}
Provides:       libstk-devel = %{version}-%{release}
Obsoletes:      libstk-devel < %{version}-%{release}

%description devel
The libstk-devel package contains libraries and header files for
developing applications that use stk.

%prep
%autosetup -p1

%build
autoreconf -fiv

%configure \
  --disable-static \
  --enable-shared \
  --with-jack \
  --with-alsa \
  RAWWAVE_PATH=%{_datadir}/stk/rawwaves/

%make_build

pushd doc/doxygen
doxygen
popd

%install
%make_install

# E: shared-library-not-executable
chmod +x %{buildroot}%{_libdir}/libstk-%{soname}.so

mkdir -p %{buildroot}%{_datadir}/stk/rawwaves/
cp -p rawwaves/*.raw %{buildroot}%{_datadir}/stk/rawwaves/

%post -n libstk%{soname} -p /sbin/ldconfig

%postun -n libstk%{soname} -p /sbin/ldconfig

%files -n libstk%{soname}
%doc README.md %doc doc/{README-Linux,ReleaseNotes,SKINI}.txt
%license LICENSE
%{_libdir}/libstk-%{soname}.so

%files data
%{_datadir}/stk

%files devel
%doc doc/hierarchy.txt doc/html
%{_libdir}/libstk.so
%{_includedir}/stk/

%changelog
