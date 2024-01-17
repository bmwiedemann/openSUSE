#
# spec file for package ripit
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


%define         real_version 4.0.0_beta20140508
Name:           ripit
Version:        3.9.90
Release:        0
Summary:        Perl Script to Create .ogg or .mp3 Files from an Audio CD
# This is not the real tarball version but as it's still in beta, we could have troubles
# to update to 4.0 final so just give it a lower version
License:        GPL-2.0+
Group:          Productivity/Multimedia/CD/Grabbers
Url:            https://en.wikipedia.org/wiki/Ripit
Source:         http://www.suwald.com/ripit/%{name}-%{real_version}.tar.gz
Patch0:         %{name}-3.9.0-ogg.patch
Patch1:         %{name}-4.0.0-undefined_variables.patch
Patch2:         %{name}-man-spellfix.patch
Requires:       cdparanoia
Requires:       perl-CDDB_get
Requires:       perl-libwww-perl
Requires:       vorbis-tools
BuildArch:      noarch

%description
This Perl script makes it easy to create MP3 files from an audio CD. It
tries to find the artist and song titles with the help of CDDB.

%prep
%setup -q -n %{name}-%{real_version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build

%install
make prefix=%{buildroot}%{_prefix} etcdir=%{buildroot}/%{_sysconfdir}/%{name} install

%files
%doc README HISTORY LICENSE
%{_bindir}/ripit
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/*
%{_mandir}/man1/*

%changelog
