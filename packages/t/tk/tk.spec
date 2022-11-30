#
# spec file for package tk
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


Name:           tk
BuildRequires:  fontconfig-devel
BuildRequires:  imake
BuildRequires:  libX11-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXft-devel
BuildRequires:  libXt-devel
BuildRequires:  pkg-config
BuildRequires:  tcl-devel
URL:            http://www.tcl.tk
Version:        8.6.13
Release:        0
%define         rrc %{nil}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        Graphical User Interface Toolkit for Tcl
License:        TCL
Group:          Development/Languages/Tcl
Obsoletes:      tkcon < 2.7
Provides:       tkcon = 2.7
# bug437293
%ifarch ppc64
Obsoletes:      tk-64bit
%endif
#
Provides:       wish
Provides:       wish8.6
Requires:       tcl >= %version
Requires:       xhost
PreReq:         /bin/rm
Source0:        http://prdownloads.sourceforge.net/tcl/%name%{version}%{rrc}-src.tar.gz
Source1:        tk-rpmlintrc
Source2:        baselibs.conf
Source3:        http://tkcon.cvs.sourceforge.net/tkcon/tkcon/tkcon.tcl

%description
Tk is a graphical user interface toolkit that takes developing desktop
applications to a higher level than conventional approaches. Tk is the
standard GUI not only for Tcl, but for many other dynamic languages,
and can produce rich, native applications that run unchanged across
Windows, Mac OS X, Linux and more.



Authors:
--------
    The Tcl Core Team <tcl-core@lists.sourceforge.net>

%package devel
Summary:        Header Files and C API Documentation for Tk
Group:          Development/Libraries/Tcl
Requires:       tcl-devel
Requires:       tk = %version
Requires:       xorg-x11-libX11-devel
# bug437293
%ifarch ppc64
Obsoletes:      tk-devel-64bit
%endif
#

%description devel
This package contains header files and documentation needed for writing
Tk extensions in compiled languages like C, C++, etc., or for embedding
Tk in programs written in such languages.

This package is not needed for writing extensions or applications for
Tk in the Tcl language itself.



Authors:
--------
    The Tcl Core Team <tcl-core@lists.sourceforge.net>

%define TK_MINOR %(echo %version | cut -c1-3)
%define scriptdir %(echo 'puts -nonewline [file dirname $tcl_library]' | tclsh)/tk%TK_MINOR

%prep
%setup -q -n %name%version

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
cd unix
%configure \
	--with-tcl=%_libdir \
	--enable-threads \
	--enable-man-symlinks \
	--enable-man-compression=gzip
make %{?_smp_mflags} \
	TK_LIBRARY="%scriptdir" \
	TK_PKG_DIR="tcl/tk%TK_MINOR"

%install
# these renamings are needed to avoid some file name clashes with other packages
mv doc/menubar.n doc/tk_menubar.n
mv doc/dialog.n doc/tk_dialog.n
mv doc/panedwindow.n doc/tk_panedwindow.n
make -C unix install install-private-headers \
	INSTALL_ROOT=%buildroot \
	TK_LIBRARY="%scriptdir" \
	TK_PKG_DIR="tcl/tk%TK_MINOR"
ln -sf wish%TK_MINOR %buildroot%_prefix/bin/wish
ln -sf wish.1.gz %buildroot%_mandir/man1/wish%TK_MINOR.1.gz
install -m 0755 %{S:3} %buildroot%_bindir/tkcon
# The information in TK_LIBS is not needed for shared libraries
# and we don't support static linking.
sed -i "/^TK_LIBS=/s/'.*'$//" %buildroot%_libdir/tkConfig.sh
sed -i "/^Libs.private: /s/ .*$//" %buildroot%_libdir/pkgconfig/tk.pc

%if "%_lib" == "lib64"

%post
test -L /usr/lib/tk%TK_MINOR && rm -f /usr/lib/tk%TK_MINOR
exit 0
%endif

%files
%defattr(-,root,root)
%doc README.md changes license.terms ChangeLog*
%docdir %_mandir/mann
%doc %_mandir/man1/*
%doc %_mandir/mann/*
%_prefix/bin/*
%_libdir/*.so
%scriptdir
%exclude %scriptdir/tkAppInit.c

%files devel
%defattr(-,root,root)
%doc %_mandir/man3/*
%_prefix/include/*
%scriptdir/tkAppInit.c
%attr(0644,root,root) %_libdir/*.a
%_libdir/tkConfig.sh
%_libdir/pkgconfig/*

%changelog
