#
# spec file for package sleuthkit
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


%define sosuffix 13

Name:           sleuthkit
Version:        4.6.7
Release:        0
Summary:        Tools for file system and volume forensic analysis
License:        CPL-1.0 AND IPL-1.0 AND GPL-2.0-or-later
Group:          System/Monitoring
Url:            http://www.sleuthkit.org/
Source0:        https://github.com/%{name}/%{name}/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libopenssl-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#BuildRequires:  libtool

# libewf - Newer versions are plain BSD (older are BSD with advertising)
BuildRequires:  libewf-devel = 0~20140608

Requires:       file
Requires:       libtsk%sosuffix = %{version}
Requires:       mac-robber
# fiwalk has been incorporated into sleuthkit.  Last standalone version was 0.6.16
Provides:       fiwalk = %{version}
Obsoletes:      fiwalk < %{version}

%description
The Sleuth Kit (TSK) is a collection of UNIX-based command line tools that
allow you to investigate a computer. The current focus of the tools is the
file and volume systems and TSK supports FAT, Ext2/3, NTFS, UFS,
and ISO 9660 file systems

%package        -n libtsk%sosuffix
Summary:        Library for file system and volume forensic analysis
Group:          System/Libraries

%description    -n libtsk%sosuffix
The libtsk%sosuffix package contains library for %{name}.

The name of the library was changed from libtsk3 to libtsk

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:       libtsk%sosuffix = %{version}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
export LIBS=' -lpthread -ldl'
%configure --disable-static

# remove rpath from libtool
# closed by tm
sed -i.rpath 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i.rpath 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

# clean unused-direct-shlib-dependencies
#sed -i -e 's! -shared ! -Wl,--as-needed\0!g' libtool

# export CFLAGS="%%{optflags}"
# export CXXFLAGS="%%{optflags}"
export LDFLAGS="-avoid-version -module"

make %{?_smp_mflags}

%install
%if 0%{?sles_version}
make install DESTDIR=%{buildroot} INSTALL="install -p"
%else
%make_install INSTALL="install -p"
%endif
find %{buildroot} -name '*.la' -delete
mkdir -p %{buildroot}/%{_datadir}/sleuthkit
cp --archive bindings %{buildroot}/%{_datadir}/sleuthkit/bindings

%post -n libtsk%sosuffix -p /sbin/ldconfig

%postun -n libtsk%sosuffix -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc ChangeLog.txt NEWS.txt README.md licenses/*
# License is CPL 1.0 exept for some files.
%{_bindir}/blkcalc
%{_bindir}/blkcat
%{_bindir}/blkls
%{_bindir}/blkstat
#{_bindir}/disk_sreset
#{_bindir}/disk_stat
%{_bindir}/fcat
%{_bindir}/ffind
%{_bindir}/fiwalk
%{_bindir}/fls
%{_bindir}/fsstat
%{_bindir}/hfind
%{_bindir}/icat
%{_bindir}/ifind
%{_bindir}/ils
%{_bindir}/img_cat
%{_bindir}/img_stat
%{_bindir}/istat
%{_bindir}/jcat
%{_bindir}/jls
%{_bindir}/jpeg_extract
# This file is described as GPL in the doc
# But the license remains CPL in the source.
%{_bindir}/mactime
##
%{_bindir}/mmcat
%{_bindir}/mmls
%{_bindir}/mmstat
%{_bindir}/sigfind
%{_bindir}/sorter
%{_bindir}/usnjls

## This file is GPLv2+
%{_bindir}/srch_strings
#
%{_mandir}/man1/blkcalc.1*
%{_mandir}/man1/blkcat.1*
%{_mandir}/man1/blkls.1*
%{_mandir}/man1/blkstat.1*
#{_mandir}/man1/disk_sreset.1*
#{_mandir}/man1/disk_stat.1*
%{_mandir}/man1/fcat.1*
%{_mandir}/man1/ffind.1*
%{_mandir}/man1/fls.1*
%{_mandir}/man1/fsstat.1*
%{_mandir}/man1/hfind.1*
%{_mandir}/man1/icat.1*
%{_mandir}/man1/ifind.1*
%{_mandir}/man1/ils.1*
%{_mandir}/man1/img_cat.1*
%{_mandir}/man1/img_stat.1*
%{_mandir}/man1/istat.1*
%{_mandir}/man1/jcat.1*
%{_mandir}/man1/jls.1*
%{_mandir}/man1/mactime.1*
%{_mandir}/man1/mmcat.1*
%{_mandir}/man1/mmls.1*
%{_mandir}/man1/mmstat.1*
%{_mandir}/man1/sigfind.1*
%{_mandir}/man1/sorter.1*
%{_mandir}/man1/usnjls.1.gz
%dir %{_datadir}/tsk
%{_datadir}/tsk/sorter/

%{_bindir}/tsk_comparedir
%{_bindir}/tsk_gettimes
%{_bindir}/tsk_loaddb
%{_bindir}/tsk_recover
%{_mandir}/man1/tsk_comparedir.1.gz
%{_mandir}/man1/tsk_gettimes.1.gz
%{_mandir}/man1/tsk_loaddb.1.gz
%{_mandir}/man1/tsk_recover.1.gz

%files -n libtsk%sosuffix
%defattr(-,root,root,-)
# CPL and IBM
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
# CPL and IBM
%{_includedir}/tsk/
%{_libdir}/*.so
%{_datadir}/sleuthkit

%changelog
