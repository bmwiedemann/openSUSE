#
# spec file for package libmikmod
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libmikmod
%define lname	libmikmod3
BuildRequires:  makeinfo
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libpulse-simple)
Url:            http://mikmod.raphnet.net/
Summary:        MikMod Sound Library
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Version:        3.3.7
Release:        0
Source:         http://sourceforge.net/projects/mikmod/files/%{name}/%{version}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch1:         libmikmod-config.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libmikmod is a portable sound library, capable of playing samples as
well as module files. It was originally written by Jean-Paul Mikkers
(MikMak) for DOS. It supports OSS /dev/dsp, ALSA, and Esound and can
also write wav files. Supported file formats include mod, stm, s3m,
mtm, xm, and it.

%package -n %lname
Summary:        MikMod Sound Library
Group:          System/Libraries
# bug437293
%ifarch ppc64
Obsoletes:      libmikmod-64bit
%endif
#
# O/P added 2012-06-11
Provides:       libmikmod = %version-%release
Obsoletes:      libmikmod < %version-%release

%description -n %lname
Libmikmod is a portable sound library, capable of playing samples as
well as module files. It was originally written by Jean-Paul Mikkers
(MikMak) for DOS. It supports OSS /dev/dsp, ALSA, and Esound and can
also write wav files. Supported file formats include mod, stm, s3m,
mtm, xm, and it.

%package devel
Summary:        Development files for MikMod Sound Library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       glibc-devel
PreReq:         %install_info_prereq
# bug437293
%ifarch ppc64
Obsoletes:      libmikmod-devel-64bit
%endif
#

%description devel
This package contains files needed for compiling programs using
libmikmod.

Libmikmod is a portable sound library, capable of playing samples as
well as module files. It was originally written by Jean-Paul Mikkers
(MikMak) for DOS. It supports OSS /dev/dsp, ALSA, and Esound and can
also write wav files. Supported file formats include mod, stm, s3m,
mtm, xm, and it.



%prep
%setup -q
%patch1

%build
%configure --disable-static --disable-oss
make %{?_smp_mflags}

%install
%makeinstall
cmp   $RPM_BUILD_ROOT%{_includedir}/mikmod{,_build}.h &&
ln -f $RPM_BUILD_ROOT%{_includedir}/mikmod{,_build}.h
%{__rm} -f %{buildroot}%{_libdir}/*.la

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/mikmod.info.gz

%postun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/mikmod.info.gz

%files -n %lname
%defattr(-,root,root)
%doc COPYING.LIB COPYING.LESSER
%{_libdir}/libmikmod.so.3*

%files devel
%defattr(-,root,root)
%doc README AUTHORS NEWS TODO
%{_bindir}/*-config
%{_datadir}/aclocal/libmikmod.m4
%{_includedir}/*
%{_libdir}/pkgconfig/libmikmod.pc
%doc %{_infodir}/mikmod*
%{_libdir}/libmikmod.so
%doc %{_mandir}/man1/*-config.*

%changelog
