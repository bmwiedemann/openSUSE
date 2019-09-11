#
# spec file for package direvent
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


Name:           direvent
Version:        5.2
Release:        0
Summary:        Monitor a file system directory for changes
License:        GPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://www.gnu.org/software/direvent/
Source:         http://ftp.gnu.org/gnu/direvent/%{name}-%{version}.tar.gz
Source2:        http://ftp.gnu.org/gnu/direvent/%{name}-%{version}.tar.gz.sig
Source3:        https://puszcza.gnu.org.ua/people/viewgpg.php?user_id=101#/%{name}.keyring
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
GNU Direvent monitors events in the file system directories. For each event
that occurs in a set of pre-configured directories, the program calls an
external program associated with it, supplying it with the information about
the event and the location within the file system where it occured.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%check
make %{?_smp_mflags} tests

%install
%make_install
%find_lang %{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files -f %{name}.lang
%license COPYING
%doc NEWS README THANKS AUTHORS
%{_bindir}/*
%{_mandir}/man*/*.gz
%{_infodir}/*.info%{?ext_info}

%changelog
