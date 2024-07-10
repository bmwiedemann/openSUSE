#
# spec file for package direvent
#
# Copyright (c) 2021 SUSE LLC
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


Name:           direvent
Version:        5.4
Release:        0
Summary:        File system directory change monitoring tool
License:        GPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://www.gnu.org/software/direvent/
Source:         http://ftp.gnu.org/gnu/direvent/%{name}-%{version}.tar.gz
Source2:        http://ftp.gnu.org/gnu/direvent/%{name}-%{version}.tar.gz.sig
Source3:        https://puszcza.gnu.org.ua/people/viewgpg.php?user_id=101#/%{name}.keyring

%description
GNU Direvent monitors events in the file system directories. For each event
that occurs in a set of pre-configured directories, the program calls an
external program associated with it, supplying it with the information about
the event and the location within the file system where it occured.

%prep
%autosetup -p1

%build
%configure
%make_build

%check
%make_build tests

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc NEWS README THANKS AUTHORS
%{_bindir}/*
%{_mandir}/man*/*.gz
%{_infodir}/*.info%{?ext_info}

%changelog
