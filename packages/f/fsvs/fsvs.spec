#
# spec file for package fsvs
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           fsvs
Version:        1.2.13
Release:        0
Summary:        Backup/Restore/Versioning of large Data Sets with Meta-Data
License:        GPL-3.0-or-later
Group:          Productivity/Archiving/Backup
URL:            https://github.com/phmarek/fsvs
Source:         https://download.fsvs-software.org/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  db-devel
BuildRequires:  gdbm-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(apr-util-1)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  pkgconfig(libsvn_delta)
BuildRequires:  pkgconfig(libsvn_ra)

%description
FSVS is the abbreviation for “Fast System VerSioning”, and is pronounced
[fisvis].

It is a complete backup/restore/versioning tool for all files in a directory
tree or whole filesystems, with a subversionTM repository as the backend.

You may think of it as some kind of tar or rsync with versioned storage.

%prep
%autosetup -p1
# remove dangling symlinks
rm config.guess config.sub
cp -v %{_datadir}/automake-`rpm -q --queryformat %%{version} automake`/config.{guess,sub} .

%build
%configure
%make_build

%install
%make_install

%files
%license LICENSE
%doc doc CHANGES README
%{_bindir}/fsvs

%changelog
