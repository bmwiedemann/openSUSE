#
# spec file for package tclx
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           tclx
BuildRequires:  autoconf
BuildRequires:  tcl-devel
Version:        8.4.1
Release:        0
Summary:        TclX - Extended Tcl
License:        SUSE-Permissive and BSD-3-Clause
Group:          Development/Languages/Tcl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %name%version.tar.bz2

%description 
Extended Tcl is a superset of standard Tcl. Extended Tcl has three
basic functional areas: A set of new commands, a Tcl shell (a Unix
shell-style command line and interactive environment), and a
user-extensible library of useful Tcl procedures, any of which can be
automatically loaded on the first attempt to execute it.

In addition, a detailed help system is available for Tcl/Tk: tclhelp.



Authors:
--------
    Karl Lehenbauer and Mark Diekhan <info@NeoSoft.com>

%prep
%setup -q -n %{name}8.4

%build
autoconf
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure \
	--with-tcl=%_libdir \
	--with-help \
	--enable-threads
make

%install
make install DESTDIR=%buildroot pkglibdir=%tcl_archdir/%{name}8.4

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%tcl_archdir
%doc %_mandir/mann/*
%_prefix/include/*
%doc ChangeLog README

%changelog
