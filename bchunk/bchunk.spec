#
# spec file for package bchunk
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2005-2007 Toni Graffy (oc2pus) <toni@links2linux.de>
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


Name:           bchunk
Version:        1.2.2
Release:        0
Summary:        A CD image format converter from .bin/.cue to .iso/.cdr/.wav
License:        GPL-2.0+
Group:          Productivity/File utilities
URL:            http://he.fi/bchunk/
Source:         http://he.fi/bchunk/%{name}-%{version}.tar.gz

%description
The bchunk package contains a UNIX/C rewrite of the BinChunker
program. BinChunker converts a CD image in a .bin/.cue format
(sometimes .raw/.cue) into a set of .iso and .cdr/.wav tracks.
The .bin/.cue format is used by some non-UNIX CD-writing
software, but is not supported on most other CD-writing programs.

%prep
%setup -q

%build
make CFLAGS="%{optflags}" %{?_smp_mflags}

%install
install -dm 755 %{buildroot}%{_bindir}
install -m 755 \
	%{name} %{buildroot}%{_bindir}

install -dm 755 %{buildroot}%{_mandir}/man1
install -m 644 %{name}.1 %{buildroot}%{_mandir}/man1

%files
%doc COPYING ChangeLog README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
