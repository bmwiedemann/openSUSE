#
# spec file for package itk
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define snapshot -20170728

Name:           itk
BuildRequires:  itcl-devel >= 4.0.0
BuildRequires:  tcl-devel
BuildRequires:  tk-devel
Version:        4.1.0
Release:        0
Summary:        Object Oriented Extension for Tcl
License:        MIT
Group:          Development/Languages/Tcl
Provides:       itcl:/usr/share/man/mann/itk.n.gz
Requires:       itcl
Requires:       tcl >= %{tcl_version}
Requires:       tk >= %{tcl_version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %name%version%snapshot.tar.gz

%description
Incr Tcl adds object-oriented programming facilities to Tcl.  It was
NOT designed as another whiz-bang, object-oriented programming
language. It is patterned somewhat after C++.  It was designed to
support more structured programming in Tcl.  Scripts that grow beyond a
few thousand lines become extremely difficult to maintain. [incr Tcl]
attacks this problem in the same way that any object- oriented
programming language would, by providing mechanisms for data
encapsulation behind well-defined interfaces.



Authors:
--------
    Michael J. McLennan <michael.mclennan@att.com>
    Dr. John Ousterhout <john.ousterhout@eng.sun.com>

%prep
%setup -q -n %name%version

%build
itclver=$(echo 'puts [package require itcl]' | tclsh)
%configure --with-itcl=%tcl_archdir/itcl$itclver
make

%install
%makeinstall pkglibdir=%tcl_archdir/%name%version
# We don't need the headers
rm -rf %buildroot/%_includedir

%files
%defattr(-,root,root)
%doc license.terms
%doc %_mandir/mann/*
%_libdir/tcl

%changelog
