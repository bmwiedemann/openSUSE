#
# spec file for package tclx
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


Name:           tclx
Version:        8.4.4
Release:        0
Summary:        TclX - Extended Tcl
License:        SUSE-Permissive and BSD-3-Clause
URL:            http://tclx.sourceforge.net/
Group:          Development/Languages/Tcl
Source0:        https://github.com/flightaware/tclx/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  tcl-devel

%description 
Extended Tcl is a superset of standard Tcl. Extended Tcl has three
basic functional areas: A set of new commands, a Tcl shell (a Unix
shell-style command line and interactive environment), and a
user-extensible library of useful Tcl procedures, any of which can be
automatically loaded on the first attempt to execute it.

In addition, a detailed help system is available for Tcl/Tk: tclhelp.

%prep
%setup -q

%build
autoreconf -fi
export CFLAGS="%optflags -fno-strict-aliasing"
%configure \
	--with-tcl=%_libdir \
	--with-help \
	--enable-threads
%make_build

%install
%make_install pkglibdir=%tcl_archdir/%{name}8.4

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%tcl_archdir/%{name}8.4
%_mandir/mann/*
%_includedir/*

%changelog
