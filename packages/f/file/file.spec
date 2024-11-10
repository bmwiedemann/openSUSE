#
# spec file for package file
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


%define somajor 1
%define libname libmagic%{somajor}

Name:           file
BuildRequires:  bash >= 4.0
BuildRequires:  libtool
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(zlib)
URL:            http://www.darwinsys.com/file/
# bug437293
%ifarch ppc64
Obsoletes:      file-64bit
%endif
#
# Set Version also in python-magic.spec
Version:        5.45
Release:        0
Summary:        A Tool to Determine File Types
License:        BSD-2-Clause
Group:          Productivity/File utilities
Source0:        https://www.astron.com/pub/file/file-%{version}.tar.gz
Source2:        baselibs.conf
Source3:        file-rpmlintrc
Source4:        https://www.astron.com/pub/file/file-%{version}.tar.gz.asc
Source5:        file.keyring
Patch0:         file-5.45.dif
Patch1:         file-5.19-misc.dif
Patch4:         file-4.24-autoconf.dif
Patch5:         file-5.14-tex.dif
Patch7:         file-4.20-ssd.dif
Patch8:         file-4.20-xen.dif
Patch9:         file-5.22-elf.dif
Patch10:        file-5.19-printf.dif
Patch12:        file-5.17-option.dif
Patch13:        file-4.21-scribus.dif
Patch15:        file-4.21-xcursor.dif
Patch22:        file-5.19-cromfs.dif
Patch25:        file-5.18-javacheck.dif
Patch26:        file-5.19-solv.dif
Patch27:        file-5.19-zip2.0.dif
Patch31:        file-5.19-biorad.dif
Patch32:        file-5.19-clicfs.dif
Patch37:        file-secure_getenv.patch
Patch39:        file-5.28-btrfs-image.dif
# PATCH-FIX-UPSTREAM: Support max time_t on 32bit
Patch42:        file-5.45-type_t.dif
Patch43:        file-seccomp.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%global         _sysconfdir /etc
%global         magicdir    %{_datadir}/file
%global         _miscdir    %{_datadir}/misc

%description
With the file command, you can obtain information on the file type of a
specified file. File type recognition is controlled by the file
/etc/magic, which contains the classification criteria. This command is
used by apsfilter to permit automatic printing of different file types.

%package magic
Summary:        Database for libmagic to help identify files
Group:          Productivity/File utilities
Obsoletes:      libmagic-data < %{version}
Provides:       libmagic-data = %{version}
BuildArch:      noarch

%description magic
This package contains the basic magic files that libmagic reads and uses
to estimate a file's type.

%package -n %libname
Summary:        Library for heuristic file type identification
Group:          System/Libraries
Provides:       file:%{_libdir}/libmagic.so.%{somajor}
Requires:       file-magic = %{version}

%description -n %libname
This library reads magic files and detects file types. Used by file command

%package devel
Summary:        Development files for libmagic, a library to determine file types
Group:          Development/Libraries/C and C++
Provides:       file:/usr/include/magic.h
Requires:       %libname = %{version}
Requires:       glibc-devel

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require the magic "file" interface.

%prep
%setup -q -n file-%{version}
%patch -P 42 -p0 -b .t_t
%patch -P 1  -p0 -b .misc
%patch -P 4  -p0 -b .conf
%patch -P 5  -p0 -b .tex
%patch -P 7  -p0 -b .ssd
%patch -P 8  -p0 -b .xen
%patch -P 9  -p0 -b .elf
%patch -P 10 -p0 -b .prtf
%patch -P 12 -p1 -b .opt
%patch -P 13 -p0 -b .scri
%patch -P 15 -p0 -b .xcur
%patch -P 22 -p0 -b .cromfs
%patch -P 25 -p0 -b .javacheck
%patch -P 26 -p0 -b .solv
%patch -P 27 -p0 -b .zip2.0
%patch -P 31 -p0 -b .biorad
%patch -P 32 -p0 -b .clicfs
%patch -P 37 -p1 -b .getenv
%patch -P 39 -p1 -b .btrfs
%patch -P 0 -b .0
%patch -P 43 -p1 -b .seccomp
test -s src/magic.h.in || cp -p src/magic.h src/magic.h.in
rm -fv src/magic.h

%build
export LANG=POSIX
export LC_ALL=POSIX
rm -f Magdir/*,v Magdir/*~
rm -f ltcf-c.sh ltconfig ltmain.sh
autoreconf -fiv
export CFLAGS="%{optflags} -DHOWMANY=69632 -fPIE $(pkg-config libseccomp --cflags)"
%configure --disable-silent-rules --datadir=%{magicdir} \
	--disable-static \
	--enable-fsect-man5
make %{?_smp_mflags} pkgdatadir='$(datadir)' LDFLAGS="-pie"

%install
export LANG=POSIX
export LC_ALL=POSIX
mkdir  %{buildroot}/etc
make DESTDIR=%{buildroot} install pkgdatadir='$(datadir)'
rm -vf %{buildroot}%{_sysconfdir}/magic
echo '# Localstuff: file(1) magic(5) for locally observed files' > %{buildroot}%{_sysconfdir}/magic
echo '#     global magic file is %{magicdir}/magic(.mgc)'	>> %{buildroot}%{_sysconfdir}/magic
# Does not build
mkdir -p %{buildroot}%{_miscdir}
ln -s %{magicdir}/magic %{buildroot}%{_miscdir}/magic
ln -s %{magicdir}/magic.mgc %{buildroot}%{_miscdir}/magic.mgc
%if %{with decore}
install -s dcore %{buildroot}%{_bindir}
%endif
rm -f %{buildroot}%{_libdir}/*.la

%check
# Test if prctl is still allowed by the seccomp filter.
export GLIBC_TUNABLES=glibc.mem.decorate_maps=1
# Standard checks
make check
# Check out that the binary does not bail out:
LD_LIBRARY_PATH=%{buildroot}%{_libdir}
export LD_LIBRARY_PATH
%{buildroot}%{_bindir}/file -m %{buildroot}%{_miscdir}/magic %{buildroot}%{_bindir}/file
shopt -s globstar
for dir in %{_bindir} /%{_lib} %{_libdir} ; do
	echo $dir/** | \
	xargs %{buildroot}%{_bindir}/file -m %{buildroot}%{_miscdir}/magic
done
unset LD_LIBRARY_PATH
unset GLIBC_TUNABLES

%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig

%files -n %libname
%defattr (-,root,root)
%{_libdir}/lib*.so.*

%files magic
%defattr (-,root,root)
%config(noreplace) %{_sysconfdir}/magic
%{_miscdir}/magic
%{_miscdir}/magic.mgc
%dir %{magicdir}
%{magicdir}/magic
%{magicdir}/magic.mgc
%doc %{_mandir}/man5/magic.5.gz

%files
%defattr (-,root,root)
%if %{with decore}
%attr(755,root,root) %{_bindir}/dcore
%endif
%attr(755,root,root) %{_bindir}/file
%doc %{_mandir}/man1/file.1.gz
%license COPYING
%doc AUTHORS NEWS ChangeLog

%files devel
%defattr (-,root,root)
%{_libdir}/lib*.so
%{_includedir}/magic.h
%{_libdir}/pkgconfig/libmagic.pc
%doc %{_mandir}/man3/libmagic.3.gz
%license COPYING
%doc README.DEVELOPER AUTHORS NEWS ChangeLog

%changelog
