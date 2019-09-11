#
# spec file for package frink
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


Name:           frink
Url:            http://catless.ncl.ac.uk/Programs/Frink
Version:        2.3.1.a2
Release:        0
Summary:        Static Testing and Formatting for Tcl Programs
License:        BSD-3-Clause
Group:          Development/Languages/Tcl
BuildRequires:  automake
Source0:        ftp://catless.ncl.ac.uk/pub/%name-%version.tar.gz
Patch0:         %name.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Frink is a Tcl formatting and static check program. It can prettify
your program, and minimize, obfuscate, or sanity check it. It can also
do some rewriting.

See /usr/share/doc/packages/frink/README and the output of "frink -h"
for details.

%prep
%setup -q -n %{name}-2.3.1
%patch0

%build
autoreconf -i --force
%configure
make

%install
make DESTDIR="%buildroot" install

%files
%defattr(-,root,root)
%_prefix/bin/frink
%doc AUTHORS ChangeLog COPYING README TODO

%changelog
