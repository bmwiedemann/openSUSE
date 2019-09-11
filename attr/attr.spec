#
# spec file for package attr
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define lname	libattr1
Name:           attr
Version:        2.4.48
Release:        0
Summary:        Commands for Manipulating Extended Attributes
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Filesystems
URL:            https://savannah.nongnu.org/projects/attr/
Source:         https://download-mirror.savannah.gnu.org/releases/attr/attr-%{version}.tar.gz
Source2:        https://download-mirror.savannah.gnu.org/releases/attr/attr-%{version}.tar.gz.sig
Source3:        %{name}.keyring
Source99:       baselibs.conf
Patch0:         0001-attr-2.4.48-test-suite-perl.patch
BuildRequires:  pkgconfig
Conflicts:      xfsdump < 2.0.0

%description
A set of tools for manipulating extended attributes on file system
objects, in particular getfattr(1) and setfattr(1). An attr(1) command
is also provided, which is largely compatible with the SGI IRIX tool of
the same name.

%package -n %{lname}
Summary:        A dynamic library for filesystem extended attribute support
Group:          System/Libraries
Obsoletes:      libattr < %{version}-%{release}
Provides:       libattr = %{version}-%{release}

%description -n %{lname}
This package contains the libattr.so dynamic library, which contains
the extended attribute library functions.

%package -n libattr-devel
Summary:        Header files for libattr
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       glibc-devel
Provides:       attr-devel = %{version}-%{release}
Obsoletes:      attr-devel < %{version}-%{release}

%description -n libattr-devel
This package contains the libraries and header files needed to develop
programs which make use of extended attributes. For Linux programs, the
documented system call API is the recommended interface, but an SGI
IRIX compatibility interface is also provided.

%package -n libattr-devel-static
Summary:        Static libraries for libattr development
Group:          Development/Libraries/C and C++
Provides:       libattr-devel:%{_libdir}/libattr.a
Requires:       libattr-devel = %version

%description -n libattr-devel-static
This package contains the static library of libattr which is needed for
staticallly linking to programs that make use of extended attributes.

%prep
%setup -q
%patch0 -p1

%build
%configure \
    --enable-static \
    --disable-silent-rules
make %{?_smp_mflags}

%install
%make_install
# remove libtool archives
find %{buildroot} -type f -name "*.la" -delete -print
# handle docs on our own
rm -rf %{buildroot}/%{_datadir}/doc/%{name}
%find_lang %{name}

%check
make %{?_smp_mflags} check

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files -f %{name}.lang
%license doc/COPYING*
%doc doc/CHANGES doc/PORTING
%{_mandir}/man1/*.1%{?ext_man}
%{_bindir}/attr
%{_bindir}/getfattr
%{_bindir}/setfattr

%files -n libattr-devel
%{_includedir}/attr/
%{_libdir}/pkgconfig/libattr.pc
%{_libdir}/libattr.so
%{_mandir}/man3/*.3%{?ext_man}

%files -n libattr-devel-static
%defattr(-,root,root)
%{_libdir}/libattr.a

%files -n %{lname}
%license doc/COPYING*
%{_libdir}/libattr.so.1*
%config %{_sysconfdir}/xattr.conf

%changelog
