#
# spec file for package xapian-core
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


Name:           xapian-core
Version:        1.4.9
Release:        0
Summary:        The Xapian Probabilistic Information Retrieval Library
License:        GPL-2.0-only
Group:          Productivity/Databases/Servers
Url:            http://www.xapian.org/
Source0:        http://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.xz
Source1:        http://www.oligarchy.co.uk/xapian/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Source3:        baselibs.conf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gcc-c++ >= 4.6
BuildRequires:  libuuid-devel
BuildRequires:  pkg-config
BuildRequires:  xz
BuildRequires:  zlib-devel
Requires:       libxapian30 = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Xapian is a Probabilistic Information Retrieval library. It offers an
adaptable toolkit for adding indexing and search facilities to
applications.

%package -n libxapian30
Summary:        Xapian search engine libraries
Group:          System/Libraries

%description -n libxapian30
Xapian is a Probabilistic Information Retrieval library. It offers an
adaptable toolkit for adding indexing and search facilities to
applications.

%package -n libxapian-devel
Summary:        Files needed for building packages which use Xapian
Group:          Development/Libraries/C and C++
Requires:       gcc-c++
Requires:       libuuid-devel
Requires:       libxapian30 = %{version}
Requires:       zlib-devel

%description -n libxapian-devel
Xapian is a Probabilistic Information Retrieval library. It offers an
adaptable toolkit for adding indexing and search facilities to
applications.

This subpackage contains the header files for the library.

%package doc
Summary:        Documentation for the xapian-core libraries
Group:          Documentation/HTML
Requires:       %{name} = %{version}

%description doc
Xapian is a Probabilistic Information Retrieval library.

This subpackage provides the documentation for Xapian.

%package examples
Summary:        Examples for Xapian-core libraries
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description examples
Xapian is a Probabilistic Information Retrieval Library.

This subpackage contains some examples for Xapian.

%prep
%setup -q

%build
%configure \
%ifarch i586
      --disable-sse \
%endif
      --docdir=%{_docdir}/%{name}/

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} docdatadir=%{_docdir}/%{name} install %{?_smp_mflags}
rm -rf examples/{.libs,.deps,.dirstamp,*.o,quest,delve,simplesearch,simpleexpand,simpleindex,copydatabase,xapian-metadata,xapian-pos}
cp -vr examples  %{buildroot}%{_docdir}/%{name}/
find . -name \*.spec -delete
install -m 644 AUTHORS ChangeLog README NEWS HACKING PLATFORMS ChangeLog.examples %{buildroot}%{_docdir}/%{name}
# SLE12 support needs to copy this manually, since %doc would include the examples subdirectory too
%if 0%{suse_version} < 1500 && !0%{?is_opensuse}
install -m 644 COPYING %{buildroot}%{_docdir}/%{name}
%endif
%fdupes %{buildroot}%{_docdir}/%{name}

%post -n libxapian30 -p /sbin/ldconfig

%postun -n libxapian30 -p /sbin/ldconfig

%files
%defattr(-, root, root)
%dir %{_docdir}/%{name}
%if 0%{suse_version} < 1500 && !0%{?is_opensuse}
%{_docdir}/%{name}/COPYING
%else
%license COPYING
%endif
%{_docdir}/%{name}/AUTHORS
%{_docdir}/%{name}/ChangeLog
%{_docdir}/%{name}/README
%{_docdir}/%{name}/NEWS
%{_docdir}/%{name}/HACKING
%{_docdir}/%{name}/PLATFORMS
%{_bindir}/xapian-tcpsrv
%{_bindir}/xapian-progsrv
%{_bindir}/quest
%{_bindir}/copydatabase
%{_bindir}/simpleindex
%{_bindir}/simplesearch
%{_bindir}/simpleexpand
%{_bindir}/xapian-compact
%{_bindir}/xapian-check
%{_bindir}/xapian-delve
%{_bindir}/xapian-metadata
%{_bindir}/xapian-pos
%{_bindir}/xapian-replicate
%{_bindir}/xapian-replicate-server
%{_mandir}/man1/xapian-check.1*
%{_mandir}/man1/xapian-delve.1*
%{_mandir}/man1/copydatabase.1*
%{_mandir}/man1/quest.1*
%{_mandir}/man1/xapian-compact.1*
%{_mandir}/man1/xapian-config.1*
%{_mandir}/man1/xapian-progsrv.1*
%{_mandir}/man1/xapian-tcpsrv.1*
%{_mandir}/man1/xapian-metadata.1*
%{_mandir}/man1/xapian-pos.1*
%{_mandir}/man1/xapian-replicate.1*
%{_mandir}/man1/xapian-replicate-server.1*
%{_datadir}/xapian-core/

%files -n libxapian30
%defattr(-, root, root)
%{_libdir}/libxapian.so.*

%files -n libxapian-devel
%defattr(-, root, root)
%{_bindir}/xapian-config
%{_includedir}/xapian
%{_includedir}/xapian.h
%{_libdir}/libxapian.so
%{_libdir}/libxapian.la
%{_datadir}/aclocal/xapian.m4
%dir %{_libdir}/cmake/
%{_libdir}/cmake/xapian/
%{_libdir}/pkgconfig/xapian-core.pc

%files doc
%defattr(-, root, root)
%{_docdir}/%{name}/*.html
%{_docdir}/%{name}/apidoc*

%files examples
%defattr(-, root, root)
%{_docdir}/%{name}/ChangeLog.examples
%{_docdir}/%{name}/examples/

%changelog
