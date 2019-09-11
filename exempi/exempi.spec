#
# spec file for package exempi
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


%define debug_package_requires libexempi3 = %{version}
Name:           exempi
Version:        2.4.5
Release:        0
Summary:        XMP support library
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
Url:            http://libopenraw.freedesktop.org/wiki/Exempi
Source0:        http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.bz2
Source1:        http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
Source3:        baselibs.conf
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_test-devel
%else
BuildRequires:  boost-devel >= 1.33.0
%endif
BuildRequires:  gcc-c++
BuildRequires:  libexpat-devel
BuildRequires:  pkg-config
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Exempi is a library for XMP parsing and I/O. XMP is a kind of
metadata for images and PDF.

%package -n libexempi3
Summary:        XMP support library
Group:          System/Libraries

%description -n libexempi3
Exempi is a library for XMP parsing and I/O. XMP (Extensible Metadata
Platform) facilitates embedding metadata in files using a subset of
RDF. Most notably, XMP supports embedding metadata in PDF and many
image formats.

%package tools
Summary:        Tools from Exempi, an XMP support library
Group:          Productivity/Graphics/Other

%description tools
Exempi is a library for XMP parsing and I/O. XMP is a kind of
metadata for images and PDF.

This subpackage contains utilities from the Exempi project.

%package -n libexempi-devel
Summary:        Development files for the Exempi XMP support library
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libexempi3 = %{version}

%description -n libexempi-devel
Exempi is a library for XMP metadata parsing and doing I/O with it.

This subpackage contains the header files for building applications
with Exempi.

%prep
%setup -q

%build
export CXXFLAGS="%{optflags} -fno-strict-aliasing"
%configure \
  --disable-static
make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
find %{buildroot} -type f -name "*.la" -delete -print

%check
%if ! 0%{?qemu_user_space_build}
make %{?_smp_mflags} check
%endif

%post -n libexempi3 -p /sbin/ldconfig

%postun -n libexempi3 -p /sbin/ldconfig

%files -n libexempi3
%defattr(-,root,root)
%doc README COPYING ChangeLog
%{_libdir}/lib*.so.*

%files tools
%defattr(-,root,root)
%doc README COPYING ChangeLog
%{_bindir}/exempi
%{_mandir}/man1/exempi.1%{?ext_man}

%files -n libexempi-devel
%defattr(-,root,root)
%doc README COPYING ChangeLog
%{_libdir}/lib*.so
%{_includedir}/exempi-2.0
%{_libdir}/pkgconfig/*.pc

%changelog
