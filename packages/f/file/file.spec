#
# spec file for package file
#
# Copyright (c) 2020 SUSE LLC
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
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(libseccomp)
URL:            http://www.darwinsys.com/file/
# bug437293
%ifarch ppc64
Obsoletes:      file-64bit
%endif
#
# Set Version also in python-magic.spec
Version:        5.38
Release:        0
Summary:        A Tool to Determine File Types
License:        BSD-2-Clause
Group:          Productivity/File utilities
Source0:        ftp://ftp.astron.com/pub/file/file-%{version}.tar.gz
Source2:        baselibs.conf
Source3:        file-rpmlintrc
Source4:        ftp://ftp.astron.com/pub/file/file-%{version}.tar.gz.asc
Source5:        file.keyring
Patch:          file-5.38.dif
Patch1:         file-5.19-misc.dif
Patch4:         file-4.24-autoconf.dif
Patch5:         file-5.14-tex.dif
Patch7:         file-4.20-ssd.dif
Patch8:         file-4.20-xen.dif
Patch9:         file-5.22-elf.dif
Patch10:        file-5.19-printf.dif
Patch11:        file-5.12-zip.dif
Patch12:        file-5.17-option.dif
Patch13:        file-4.21-scribus.dif
Patch15:        file-4.21-xcursor.dif
Patch22:        file-5.19-cromfs.dif
Patch25:        file-5.18-javacheck.dif
Patch26:        file-5.19-solv.dif
Patch27:        file-5.19-zip2.0.dif
Patch31:        file-5.19-biorad.dif
Patch32:        file-5.19-clicfs.dif
Patch33:        file-5.16-ocloexec.patch
Patch34:        file-5.23-endian.patch
Patch37:        file-secure_getenv.patch
Patch39:        file-5.28-btrfs-image.dif
Patch40:        file-5.38-allow-readlinkat.dif
Patch41:        undo-24c9c0.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%global         _sysconfdir /etc
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
%patch1  -p0 -b .misc
%patch4  -p0 -b .conf
%patch5  -p0 -b .tex
%patch7  -p0 -b .ssd
%patch8  -p0 -b .xen
%patch9  -p0 -b .elf
%patch10 -p0 -b .prtf
%patch11 -p0 -b .zip
%patch12 -p0 -b .opt
%patch13 -p0 -b .scri
%patch15 -p0 -b .xcur
%patch22 -p0 -b .cromfs
%patch25 -p0 -b .javacheck
%patch26 -p0 -b .solv
%patch27 -p0 -b .zip2.0
%patch31 -p0 -b .biorad
%patch32 -p0 -b .clicfs
%patch33 -p0 -b .clexe
%patch34 -p0 -b .endian
%patch37 -p1 -b .getenv
%patch39 -p1 -b .btrfs
%patch40 -p1 -b .readlinkat
%patch41 -p0 -b .undo
%patch -b .0
test -s src/magic.h.in || cp -p src/magic.h src/magic.h.in
rm -fv src/magic.h

%build
export LANG=POSIX
export LC_ALL=POSIX
rm -f Magdir/*,v Magdir/*~
rm -f ltcf-c.sh ltconfig ltmain.sh
autoreconf -fiv
export CFLAGS="%{optflags} -DHOWMANY=69632 -fPIE $(pkg-config libseccomp --cflags)"
%configure --disable-silent-rules --datadir=%{_miscdir} \
	--disable-static \
	--disable-libseccomp \
	--enable-fsect-man5
make %{?_smp_mflags} pkgdatadir='$(datadir)' LDFLAGS="-pie"

%install
export LANG=POSIX
export LC_ALL=POSIX
mkdir  %{buildroot}/etc
make DESTDIR=%{buildroot} install pkgdatadir='$(datadir)'
rm -vf %{buildroot}%{_sysconfdir}/magic
echo '# Localstuff: file(1) magic(5) for locally observed files' > %{buildroot}%{_sysconfdir}/magic
echo '#     global magic file is %{_miscdir}/magic(.mgc)'	>> %{buildroot}%{_sysconfdir}/magic
# Does not build
%if %{with decore}
install -s dcore %{buildroot}%{_bindir}
%endif

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
rm -f %{buildroot}%{_libdir}/*.la

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
%doc %{_mandir}/man3/libmagic.3.gz
%license COPYING
%doc README AUTHORS NEWS ChangeLog

%changelog
