#
# spec file for package tcludp
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           tcludp
BuildRequires:  tcl-devel
Url:            http://tcludp.sourceforge.net/
Summary:        UDP Socket Extension for Tcl
Version:        1.0.11
Release:        0
License:        BSD-3-Clause
Group:          Development/Libraries/Tcl
Source0:        http://sourceforge.net/projects/tcludp/files/tcludp/%{version}/%{name}-%{version}.tar.gz
Source1:        man.macros
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package makes the UDP protocol available for Tcl interpreters. It
allows access to message-oriented UDP through stream-oriented Tcl
channels.

%prep
%setup -q -n %{name}
chmod a-x ChangeLog license.terms README

%build
%configure --with-tcl=%_libdir --libdir=%tcl_archdir --enable-ipv6
make
make pkgIndex.tcl-hand

%install
make install \
	DESTDIR=%buildroot
for f in %buildroot/%_mandir/*/*; do
    sed -i -e "/man\.macros/r %SOURCE1" -e "/man\.macros/d" $f 
done

%files
%defattr(-,root,root,-)
%doc ChangeLog README license.terms demos
%doc %_mandir/*/*
%tcl_archdir

%changelog
