#
# spec file for package fsvs
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           fsvs
Version:        1.2.7
Release:        0
Url:            http://fsvs.tigris.org/
Summary:        Backup/Restore/Versioning of large Data Sets with Meta-Data
License:        GPL-3.0+
Group:          Productivity/Archiving/Backup
Source:         https://download.fsvs-software.org/fsvs-%{version}.tar.bz2
Patch1:         fsvs-destdir.patch
Patch2:         fsvs-1.2.5-linking.patch
# PATCH-FIX-UPSTREAM -- TODO
Patch3:         reproducible.patch
BuildRequires:  apache2-devel
BuildRequires:  ctags
BuildRequires:  db-devel
BuildRequires:  ed
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gdbm
BuildRequires:  gdbm-devel
BuildRequires:  glibc-devel
BuildRequires:  libapr-util1-devel
BuildRequires:  libapr1-devel
BuildRequires:  make
BuildRequires:  neon-devel
BuildRequires:  openldap2-devel
BuildRequires:  openssl-devel
BuildRequires:  pcre-devel
BuildRequires:  pkgconfig
BuildRequires:  subversion-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FSVS is the abbreviation for “Fast System VerSioning”, and is pronounced
[fisvis].

It is a complete backup/restore/versioning tool for all files in a directory
tree or whole filesystems, with a subversionTM repository as the backend.

You may think of it as some kind of tar or rsync with versioned storage. 




Author:
-------
    Philipp Marek <pmarek@tigris.org>

%prep
%setup -q
%patch1
%patch2
%patch3 -p1

%build
export CFLAGS="%{optflags} $(pkg-config --includes apr-1)"
export CFLAGS="$CFLAGS -fno-strict-aliasing -fgnu89-inline"
%configure --disable-silent-rules
%__make %{?jobs:-j%{jobs}}

%install
%makeinstall

%__rm -rf doc/develop
echo -n >manfiles.lst
for p in doc/*.{1,5}; do
    f="${p##*/}"
    m="${f##*.}"
    %__install -D -m0644 "$p" "%{buildroot}%{_mandir}/man${m}/${f}"
    %__rm "$p"
    echo "%doc %{_mandir}/man${m}/${f}"'*' >>manfiles.lst
done

%files -f manfiles.lst
%defattr(-,root,root)
%doc doc CHANGES LICENSE README
%{_bindir}/fsvs

%changelog
