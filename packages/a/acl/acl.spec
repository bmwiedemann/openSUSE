#
# spec file for package acl
#
# Copyright (c) 2021 SUSE LLC
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


# Ring0 does not have system-user-bin/system-user-daemon
%bcond_without acl_tests

Name:           acl
%define lname	libacl1
Summary:        Commands for Manipulating POSIX Access Control Lists
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Filesystems
Version:        2.3.1
Release:        0
URL:            https://savannah.nongnu.org/projects/acl
#Git-Web:	http://git.savannah.gnu.org/cgit/acl.git/
#Git-Clone:	git://git.sv.gnu.org/acl
Source:         https://download.savannah.nongnu.org/releases/acl/acl-%version.tar.xz
Source1:        https://download.savannah.nongnu.org/releases/acl/acl-%version.tar.xz.sig
Source2:        baselibs.conf
# http://savannah.nongnu.org/project/memberlist-gpgkeys.php?group=acl
Source3:        %name.keyring

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-tools-mini
BuildRequires:  libattr-devel
BuildRequires:  libtool
BuildRequires:  pkg-config
%if %{with acl_tests} && 0%{?suse_version} > 1320
BuildRequires:  user(bin)
BuildRequires:  user(daemon)
%endif

%description
getfacl and setfacl commands for retrieving and setting POSIX access
control lists.

%package -n %lname
Summary:        A dynamic library for accessing POSIX Access Control Lists
Group:          System/Libraries
%ifarch ppc64
# bug437293
Obsoletes:      libacl-64bit
%endif
# Added for 12.1
Provides:       libacl = %version-%release
Obsoletes:      libacl < %version-%release

%description -n %lname
This package contains the libacl.so dynamic library which contains the
POSIX 1003.1e draft standard 17 functions for manipulating access
control lists.

%package -n libacl-devel
Summary:        Header files for the POSIX ACL library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version
Requires:       glibc-devel
Provides:       acl-devel = %version
Obsoletes:      acl-devel < %version
%ifarch ppc64
# bug437293
Obsoletes:      libacl-devel-64bit
%endif

%description -n libacl-devel
This package contains all necessary include files and libraries needed
to develop applications that require libacl.

%prep
%setup -q

%build
autoreconf -fi
export OPTIMIZER="%optflags -fPIC"
export DEBUG=-DNDEBUG
CFLAGS="%optflags"

%ifarch %ix86 i586
export CFLAGS="%optflags -D_FILE_OFFSET_BITS=64"
%endif

%configure \
	--disable-static \
	--docdir=%_defaultdocdir/%name
make %{?_smp_mflags} V=1

%check
%if %{with acl_tests}
    if ./setfacl -m u:`id -u`:rwx .; then
        make check || (cat test-suite.log ; false)
    else
        echo '*** ACLs are probably not supported by the file system,' \
             'the test-suite will NOT run ***'
    fi
%endif

%install
%make_install
rm -v %buildroot/%_libdir/lib%name.la
rm -rvf %buildroot/%_defaultdocdir/%name
%find_lang %name

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files -f %name.lang
%license doc/COPYING
%doc doc/PORTING doc/extensions.txt doc/libacl.txt doc/CHANGES
%_bindir/chacl
%_bindir/getfacl
%_bindir/setfacl
%_mandir/man1/*.1*
%_mandir/man5/*.5*

%files -n libacl-devel
%_includedir/acl/
%_includedir/sys/acl.h
%_libdir/libacl.so
%_mandir/man3/*.3*
%_libdir/pkgconfig/libacl.pc

%files -n %lname
%license doc/COPYING.LGPL
%_libdir/libacl.so.1*

%changelog
