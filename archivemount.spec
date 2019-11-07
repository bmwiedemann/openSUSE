#
# spec file for package archivemount
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


Name:           archivemount
Version:        0.8.7
Release:        0
Summary:        Mounts an archive for access as a file system
License:        LGPL-2.1-or-later AND BSD-2-Clause
Url:            http://www.cybernoia.de/software/archivemount/
Source:         http://www.cybernoia.de/software/archivemount/%{name}-%{version}.tar.gz
Patch0:         archivemount.dif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fuse-devel
BuildRequires:  libarchive-devel
BuildRequires:  pkgconfig

%description
Archivemount is a piece of glue code between libarchive (http://code.google.com/p/libarchive/) and FUSE
(http://fuse.sourceforge.net). It can be used to mount a (possibly compressed) archive (as in .tar.gz or
.tar.bz2) and use it like an ordinary filesystem.

%prep
%setup -q
%patch0

%build
autoreconf --force --install
export CFLAGS="%{optflags}"
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc CHANGELOG README COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
