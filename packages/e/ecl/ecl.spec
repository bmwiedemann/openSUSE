#
# spec file for package ecl
#
# Copyright (c) 2022 SUSE LLC
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


%global major 24
%global minor 5
%global micro 10
Name:           ecl
Version:        %{major}.%{minor}.%{micro}
Release:        0
Summary:        Embeddable Common-Lisp
# "ECL is LGPL-2.1+.",
# see https://common-lisp.net/project/ecl/posts/ECL-license.html
License:        LGPL-2.1-or-later
Group:          Development/Languages/Other
URL:            https://common-lisp.net/project/%{name}/
Source0:        %{url}/static/files/release/%{name}-%{version}.tgz
Source1:        %{name}.rpmlintrc
BuildRequires:  gmp-devel
BuildRequires:  info
BuildRequires:  m4
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
BuildRequires:  texinfo
BuildRequires:  texlive-plain
BuildRequires:  texlive-texinfo
BuildRequires:  pkgconfig(atomic_ops)
BuildRequires:  pkgconfig(libffi)
Requires:       %{name}-devel
Requires:       gmp-devel
Requires:       pkgconfig(atomic_ops)
Requires:       pkgconfig(libffi)

%description
ECL (Embeddable Common-Lisp) is an interpreter of the Common-Lisp language as
described in the X3J13 Ansi specification, featuring CLOS (Common-Lisp Object
System), conditions, loops, etc, plus a translator to C, which can produce
standalone executables.

ECL supports the operating systems Linux, FreeBSD, NetBSD, OpenBSD, OS X,
Solaris and Windows, running on top of the Intel, Sparc, Alpha, PowerPC and ARM
processors.

%package -n lib%{name}%{major}_%{minor}
Summary:        Embeddable Common-Lisp -- shared library
Group:          System/Libraries

%description -n lib%{name}%{major}_%{minor}
This package contains the ECL shared library.

%package devel
Summary:        Embeddable Common-Lisp -- development files
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{major}_%{minor} = %{version}
%if 0%{?suse_version}
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
%endif

%description devel
ECL (Embeddable Common-Lisp) is an interpreter of the Common-Lisp language as
described in the X3J13 Ansi specification, featuring CLOS (Common-Lisp Object
System), conditions, loops, etc, plus a translator to C, which can produce
standalone executables.

ECL supports the operating systems Linux, FreeBSD, NetBSD, OpenBSD, OS X,
Solaris and Windows, running on top of the Intel, Sparc, Alpha, PowerPC and ARM
processors.

This package contains development files for ECL.

%prep
%autosetup

%build
export TEX='tex -recorder'
export TEXI2DVI_USE_RECORDER=yes
%if 0%{?suse_version} >= 1550
# disable LTO on Tumbleweed as it breaks at least 'ecl -compile' 
%define _lto_cflags %{nil}
%endif
%configure \
	--enable-soname \
	--disable-rpath \
	--enable-gmp \
	--enable-unicode \
	--enable-threads \
	--enable-libatomic=system \
	--with-dffi \
	--with-defsystem \
	CFLAGS="%{optflags} -Wno-unused -Wno-return-type -Wno-unknown-pragmas" \
	%{nil}

%make_build
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150400
sed -i -e '/@macro seealso{node}/,+4d' src/doc/manual/macros.txi
sed -i -e '/@pxref{si_safe_eval}/ d' src/doc/manual/standards/evaluation.txi
%endif
%make_build -C src/doc/manual pdf

%install
%make_install
rm -f %{buildroot}%{_libdir}/%{name}-%{version}/{TAGS,*.a}
rm -f %{buildroot}%{_infodir}/dir

%post -n lib%{name}%{major}_%{minor} -p /sbin/ldconfig
%postun -n lib%{name}%{major}_%{minor} -p /sbin/ldconfig
%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%postun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%license COPYING LICENSE
%{_bindir}/%{name}
%{_libdir}/%{name}-%{version}/
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_infodir}/*
%doc README.md CHANGELOG src/doc/manual/manual.pdf

%files -n lib%{name}%{major}_%{minor}
%license COPYING LICENSE
%{_libdir}/lib%{name}.so.*

%files devel
%license COPYING LICENSE
%{_bindir}/%{name}-config
%{_libdir}/lib%{name}.so
%{_includedir}/%{name}/
%{_mandir}/man1/%{name}-config.1%{?ext_man}

%changelog
