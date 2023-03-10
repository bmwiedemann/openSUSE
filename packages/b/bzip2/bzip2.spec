#
# spec file for package bzip2
#
# Copyright (c) 2023 SUSE LLC
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


%define libname libbz2-1
Name:           bzip2
Version:        1.0.8
Release:        0
Summary:        A Program for Compressing Files
License:        BSD-3-Clause
Group:          Productivity/Archiving/Compression
URL:            https://sourceware.org/bzip2
Source0:        https://sourceware.org/pub/bzip2/%{name}-%{version}.tar.gz
Source1:        bznew.gz
Source2:        bznew.1.gz
Source3:        baselibs.conf
Source100:      bzip2-rpmlintrc
# PATCH-FEATURE-OPENSUSE bzip2-1.0.6-autoconfiscated.patch sbrabec@suse.cz -- Convert to a standard autoconf based package.
#Patch0:         ftp://ftp.suse.com/pub/people/sbrabec/bzip2/for_downstream/bzip2-1.0.6.2-autoconfiscated.patch
Patch0:         bzip2-1.0.6.2-autoconfiscated.patch
Patch3:         bzip2-point-to-doc-pkg.patch
Patch4:         bzip2-ocloexec.patch
BuildRequires:  autoconf >= 2.57
BuildRequires:  libtool
BuildRequires:  pkgconfig
# The following is a kludge to get updating bzip2 to after the split work
Requires(pre):  %{libname}
Provides:       bzip = %{version}
Obsoletes:      bzip < %{version}
%{?suse_build_hwcaps_libs}

%description
The bzip2 program is a program for compressing files.

%package doc
Summary:        The bzip2 program and Library Documentation
Group:          Documentation/Other
BuildArch:      noarch

%description doc
The bzip2 program and library documentation.

%package -n %{libname}
Summary:        The bzip2 runtime library
Group:          System/Libraries

%description -n %{libname}
The bzip2 runtime library

%package -n libbz2-devel
Summary:        The bzip2 runtime library development files
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}
Requires:       glibc-devel

%description -n libbz2-devel
The bzip2 runtime library development files.

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
  --disable-static
%if 0%{?do_profiling}
  %make_build CFLAGS="%{optflags} %{cflags_profile_generate}"
  %make_build CFLAGS="%{optflags} %{cflags_profile_generate}" test
  %make_build clean
  %make_build CFLAGS="%{optflags} %{cflags_profile_feedback}"
%else
  %make_build CFLAGS="%{optflags}"
%endif

%install
%make_install pkgconfigdir=%{_libdir}/pkgconfig
gzip -9 manual.ps
gzip -dc %{SOURCE1} > bznew
install -Dpm 0755 bznew %{buildroot}%{_bindir}/bznew
install -m 0644 %{SOURCE2} %{buildroot}%{_mandir}/man1
# Steam and prolly others still use the 1.0 name, so we need to be
# compatible
# Remove this when all distros use the autotools based bzip2 release
ln -s libbz2.so.1 %{buildroot}/%{_libdir}/libbz2.so.1.0

find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname}  -p /sbin/ldconfig

%check
%make_build test

%files
%{_bindir}/bunzip2
%{_bindir}/bzcat
%{_bindir}/bzcmp
%{_bindir}/bzdiff
%{_bindir}/bzegrep
%{_bindir}/bzfgrep
%{_bindir}/bzgrep
%{_bindir}/bzip2
%{_bindir}/bzip2recover
%{_bindir}/bzless
%{_bindir}/bzmore
%{_bindir}/bznew
%{_mandir}/man1/bunzip2.1%{?ext_man}
%{_mandir}/man1/bzcat.1%{?ext_man}
%{_mandir}/man1/bzcmp.1%{?ext_man}
%{_mandir}/man1/bzdiff.1%{?ext_man}
%{_mandir}/man1/bzegrep.1%{?ext_man}
%{_mandir}/man1/bzfgrep.1%{?ext_man}
%{_mandir}/man1/bzgrep.1%{?ext_man}
%{_mandir}/man1/bzip2.1%{?ext_man}
%{_mandir}/man1/bzless.1%{?ext_man}
%{_mandir}/man1/bzmore.1%{?ext_man}
%{_mandir}/man1/bznew.1%{?ext_man}

%files doc
%doc manual.ps.gz manual*.html bzip2.txt manual.pdf

%files -n %{libname}
%{_libdir}/libbz2.so.*

%files -n libbz2-devel
%license LICENSE
%doc CHANGES
%{_includedir}/bzlib.h
%{_libdir}/libbz2.so
%{_libdir}/pkgconfig/bzip2.pc

%changelog
