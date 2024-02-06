#
# spec file for package jigdo
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           jigdo
Version:        0.8.2
Release:        0
Summary:        Jigsaw Download
License:        GPL-2.0-only
Group:          Productivity/Networking/Other
URL:            https://www.einval.com/~steve/software/jigdo/
Source:         https://www.einval.com/~steve/software/jigdo/download/%{name}-%{version}.tar.xz
Source2:        https://www.einval.com/~steve/software/jigdo/download/%{name}-%{version}.tar.xz.sig
Source3:        https://www.einval.com/~steve/pgp/587979573442684E.asc#/%{name}.keyring
Patch3:         jigdo-0.8.2-makefile-paths.patch
Patch6:         jigdo-0.8.2-docbook-sgml.patch
Patch7:         jigdo-0.8.2-docbook-install-language.patch
BuildRequires:  c++_compiler
BuildRequires:  db-devel
BuildRequires:  docbook-utils-minimal
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(zlib)
Requires:       wget

%description
Jigsaw Download, or jigdo, is an intelligent tool that can be used on
the pieces of any chopped-up big file to create a special template file
that makes reassembly of the file very easy for users who only have the
pieces. What makes jigdo special is that there are no restrictions on
what offsets or sizes the individual pieces have in the original big
image. This makes the program very well suited for distributing CD or
DVD images (or large zip or tar archives) because you can put the files
of the CD on an FTP server--when jigdo is presented the files along
with the template you generated, it is able to recreate the CD image.

%prep
%autosetup -p1

%build
%configure \
	--with-gui=no \
	%{nil}
%make_build

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc changelog README THANKS doc/*.html doc/*.txt
%{_bindir}/*
%{_mandir}/*/*
%{_datadir}/%{name}

%changelog
