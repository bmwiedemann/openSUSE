#
# spec file for package hfsutils
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           hfsutils
Version:        3.2.6
Release:        0
Summary:        Tools Used for the Macintosh's Hierarchical File System
License:        GPL-2.0+
Group:          System/Filesystems
Url:            http://www.mars.org/home/rob/proj/hfs/
Source0:        ftp://ftp.mars.org/pub/hfs/hfsutils-%{version}.tar.gz
Patch0:         hfsutils-%{version}.dif
Patch1:         hfsutils-%{version}-ia64.dif
Patch2:         hfsutils-%{version}-seek.dif
Patch3:         hfsutils-%{version}-conf.dif
Patch4:         hfsutils-%{version}-errno.dif
Patch5:         hfsutils-exclusive-open.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
HFS is the Hierarchical File System used on modern Macintosh computers.
With this package, you can read and write Macintosh-formatted media,
such as floppy disks, CD-ROMs, and SCSI hard disks on most UNIX
platforms. You can also format raw media into an HFS volume.

%package -n xhfsutil
Version:        3.2.6
Release:        0
Summary:        Tcl/Tk Front-End for hfsutils
Group:          System/Filesystems
Requires:       hfsutils

%description -n xhfsutil
A Tcl interface for scriptable access to volumes and  Tk-based
front-end for browsing and copying files through a variety of transfer
modes (MacBinary, BinHex, text, etc.) for hfsutils.

%prep
%setup -q
%patch0
%patch1
%patch2
%patch3
%patch4
%patch5 -p1

%build
autoreconf --force --install
CFLAGS="%{optflags} -D_FILE_OFFSET_BITS=64 -DUSE_INTERP_RESULT" \
%configure \
	--with-tcl=%{_libdir} \
	--with-tk=%{_libdir}
make %{?_smp_mflags} TKLIBS="-ltk%tcl_version -ltkstub%tcl_version -ltcl%tcl_version -ltclstub%tcl_version"

%install
install -d -m 755 %{buildroot}%{_prefix}/bin
install -d -m 755 %{buildroot}%{_mandir}/man1
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files
%defattr(-,root,root)
%doc README TODO CHANGES BLURB COPYING COPYRIGHT CREDITS
%{_bindir}/hattrib
%{_bindir}/hcd
%{_bindir}/hcopy
%{_bindir}/hdel
%{_bindir}/hdir
%{_bindir}/hformat
%{_bindir}/hls
%{_bindir}/hmkdir
%{_bindir}/hmount
%{_bindir}/hpwd
%{_bindir}/hrename
%{_bindir}/hrmdir
%{_bindir}/humount
%{_bindir}/hvol
%doc %{_mandir}/man1/hattrib.1.gz
%doc %{_mandir}/man1/hcd.1.gz
%doc %{_mandir}/man1/hcopy.1.gz
%doc %{_mandir}/man1/hdel.1.gz
%doc %{_mandir}/man1/hdir.1.gz
%doc %{_mandir}/man1/hformat.1.gz
%doc %{_mandir}/man1/hls.1.gz
%doc %{_mandir}/man1/hmkdir.1.gz
%doc %{_mandir}/man1/hmount.1.gz
%doc %{_mandir}/man1/hpwd.1.gz
%doc %{_mandir}/man1/hrename.1.gz
%doc %{_mandir}/man1/hrmdir.1.gz
%doc %{_mandir}/man1/humount.1.gz
%doc %{_mandir}/man1/hvol.1.gz
%doc %{_mandir}/man1/hfsutils.1.gz

%files -n xhfsutil
%defattr(-,root,root)
%{_bindir}/hfssh
%{_bindir}/hfs
%{_bindir}/xhfs
%doc %{_mandir}/man1/hfssh.1.gz
%doc %{_mandir}/man1/hfs.1.gz
%doc %{_mandir}/man1/xhfs.1.gz

%changelog
