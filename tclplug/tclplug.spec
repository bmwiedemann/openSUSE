#
# spec file for package tclplug
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           tclplug
BuildRequires:  autoconf
BuildRequires:  tk-devel
Requires:       tcl
Requires:       tk
Requires:       web_browser
Summary:        Tcl/Tk Plug-In for Netscape Navigator
License:        BSD-3-Clause
Group:          Development/Libraries/Tcl
Version:        3.1.0
Release:        0
Source:         tclplugin-3.1.0-20060613-tar.bz2
Source2:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
With this plug-in, download special Tcl/Tk scripts (also known as
tclets) from the Internet and execute them inside your browser like
Java applets.

Find the documentation in /opt/netscape/tclplug/2.0/doc.



Authors:
--------
    Sunscript <sunscript-plugin@sunscript.sun.com>

%prep
%setup -q -n tclplugin

%build
autoconf
CFLAGS="%optflags -fno-strict-aliasing" \
./configure \
	--prefix=/usr \
	--with-tcl=%_libdir \
	--with-tk=%_libdir
make libdir=%_libdir/tcl

%install
make install \
	DESTDIR=%buildroot \
	NSP_DESTDIR=%_libdir/browser-plugins \
	libdir=%_libdir/tcl

%clean
rm -fr %buildroot

%files
%defattr(-,root,root)
%doc ChangeLog changes
%doc doc/features-2.0.txt doc/principles.txt doc/oldFAQ doc/license.terms
%_libdir/browser-plugins/*
%_libdir/tcl

%changelog
