#
# spec file for package soxr
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


%define lname   libsoxr0
%define lname_lsr libsoxr-lsr0
Name:           soxr
Version:        0.1.3
Release:        0
Summary:        The SoX Resampler library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Url:            http://soxr.sourceforge.net/
Source:         http://downloads.sf.net/%{name}/%{name}-%{version}-Source.tar.xz#/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pkg-config

%description
The SoX Resampler library performs one-dimensional sample-rate
conversion – it may be used, for example, to resample PCM-encoded
audio.

%package -n %{lname}
Summary:        The SoX Resampler library
Group:          System/Libraries

%description -n %{lname}
The SoX Resampler library performs one-dimensional sample-rate
conversion – it may be used, for example, to resample PCM-encoded
audio.

%package -n %{lname_lsr}
Summary:        Compatibility layer with libsamplerate
Group:          System/Libraries

%description -n %{lname_lsr}
soxr libsamplerate API compatibility layer (to some extent).

%package devel
Summary:        Development files of soxr
Group:          Development/Libraries/C and C++
Requires:       %{lname_lsr} = %{version}
Requires:       %{lname} = %{version}

%description devel
The soxr development package includes the header files,
libraries, development tools necessary for compiling and linking
application which will use libsoxr/libsoxr-lsr.

%prep
%setup -q -n %{name}-%{version}-Source

%build

%ifarch %arm
%define _lto_cflags %{nil}
%endif

%cmake \
  -DDOC_INSTALL_DIR=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%cmake_install

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%post -n %{lname_lsr} -p /sbin/ldconfig

%postun -n %{lname_lsr} -p /sbin/ldconfig

%files -n %{lname}
%defattr(-,root,root)
%doc AUTHORS NEWS
%license COPYING.LGPL LICENCE
%{_libdir}/libsoxr.so.*

%files -n %{lname_lsr}
%defattr(-,root,root)
%license COPYING.LGPL LICENCE
%{_libdir}/libsoxr-lsr.so.*

%files devel
%defattr(-,root,root)
%doc %{_docdir}/%{name}/
%{_includedir}/soxr*.h
%{_libdir}/libsoxr*.so
%{_libdir}/pkgconfig/soxr*.pc

%changelog
