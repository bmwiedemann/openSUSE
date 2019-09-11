#
# spec file for package libt3widget
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


Name:           libt3widget
%define lname	libt3widget2
Version:        1.0.3
Release:        0
Summary:        The Tilde terminal dialog toolkit
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
Url:            http://os.ghalkes.nl/t3/libt3widget.html

#Git-Clone:	git://github.com/gphalkes/t3widget
Source:         http://os.ghalkes.nl/dist/%name-%version.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  c++_compiler
BuildRequires:  fdupes
BuildRequires:  gettext-tools
BuildRequires:  gpm-devel
BuildRequires:  libtool
BuildRequires:  libunistring-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libt3key) >= 0.2.0
BuildRequires:  pkgconfig(libt3window) >= 0.3.1
BuildRequires:  pkgconfig(libtranscript) >= 0.2.2
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)

%description
The libt3widget library provides a C++ dialog toolkit. It provides
objects for dialogs and widgets like buttons, text fields, check
boxes etc., to facilitate easy construction of dialog based programs
for Unix-type terminals.

%package -n %lname
Summary:        The Tilde terminal dialog toolkit
Group:          System/Libraries

%description -n %lname
The libt3widget library provides a C++ dialog toolkit. It provides
objects for dialogs and widgets like buttons, text fields, check
boxes etc., to facilitate easy construction of dialog based programs
for Unix-type terminals.

%package devel
Summary:        Development files for libt3widget, a terminal dialog library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description devel
The libt3widget library provides a C++ dialog toolkit. It provides
objects for dialogs and widgets like buttons, text fields, check
boxes etc., to facilitate easy construction of dialog based programs
for Unix-type terminals.

This subpackage contains libraries and header files for developing
applications that want to make use of libt3widget.

%prep
%setup -q

%build
%configure --docdir="%_docdir/%name"
make %{?_smp_mflags}

%install
%make_install
find "%buildroot/%_libdir" -type f -name "*.la" -delete
%fdupes %buildroot/%_prefix

%post   -p /sbin/ldconfig -n %lname
%postun -p /sbin/ldconfig -n %lname

%files -n %lname
%defattr(-,root,root)
%_libdir/libt3widget.so.2*
%doc COPYING

%files devel
%defattr(-,root,root)
%_includedir/t3/
%_libdir/libt3widget.so
%_libdir/pkgconfig/libt3widget.pc
%_libdir/libt3widget/
%_docdir/%name/
%exclude %_docdir/%name/COPYING

%changelog
