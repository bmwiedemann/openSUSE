#
# spec file for package poster
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


Name:           poster
Version:        20060221
Release:        0
Summary:        Tool for printing posters over multiple pages
License:        GPL-2.0+
Group:          Productivity/Publishing/PS
Url:            http://printing.kde.org/
Source:         poster.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This program scales a PostScript page to a given size (a poster). The
output can be tiled on multiple sheets, and output media size can be
chosen independently. Each tile (sheet) of a will bear cropmarks and
slightly overlapping image for easier poster assembly. In principle it
requires the input file to adhere to 'eps' (encapsulated postscript)
conventions but it will work for many 'normal' postscript files as
well.



Authors:
--------
    Jos T.J. van Eijndhoven <J.T.J.v.Eijndhoven@ele.tue.nl>
    Michael Goffioul <goffioul@imec.be>

%prep
%setup -q

%build
    make CFLAGS="$RPM_OPT_FLAGS"

%install
	mkdir -p		${RPM_BUILD_ROOT}/usr/bin
	install -m 0755 poster	${RPM_BUILD_ROOT}/usr/bin/
	mkdir -p		${RPM_BUILD_ROOT}%{_mandir}/man1
	install -m 0644 poster.1	${RPM_BUILD_ROOT}%{_mandir}/man1/

%files
%defattr(-,root,root)
%doc README COPYING ChangeLog manual.ps
%doc %{_mandir}/man1/poster.1.gz
/usr/bin/poster

%changelog
