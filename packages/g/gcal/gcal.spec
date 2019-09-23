#
# spec file for package gcal
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


Name:           gcal
Version:        4.1
Release:        0
Summary:        A Program for Printing Calendars
License:        GPL-3.0-or-later
Group:          Productivity/Office/Organizers
Url:            https://www.gnu.org/software/gcal/
Source0:        https://ftp.gnu.org/gnu/gcal/gcal-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/gcal/gcal-%{version}.tar.xz.sig
Source2:        %{name}.keyring
Patch0:         gcal-3.01-longerstrings.patch
Patch1:         gcal-3.6-cleanup.patch
Patch2:         gnulib-4af4a4a71827c0bc5e0ec67af23edef4f15cee8e-excerpt.patch
Patch3:         gnulib-74d9d6a293d7462dea8f83e7fc5ac792e956a0ad-excerpt.patch
BuildRequires:  ncurses-devel
BuildRequires:  xz
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
Gcal is a program for printing calendars.  Gcal displays a calendar for
a month or a year, eternal holiday lists, and fixed date lists.  The
program correctly omits the dates that were skipped when the current
Gregorian calendar replaced the earlier Julian calendar.

%lang_package

%prep
%setup -q
%patch0
%patch1
%patch2 -p1
%patch3 -p1

%build
%configure
make %{?_smp_mflags} "CFLAGS=%{optflags}"

%install
%make_install
%find_lang %{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files
%defattr(-,root,root)
%doc BUGS LIMITATIONS README TODO AUTHORS COPYING NEWS THANKS
%doc data/gcalrc doc/GREG-REFORM
%{_datadir}/gcal
%{_bindir}/gcal
%{_bindir}/gcal2txt
%{_bindir}/tcal
%{_bindir}/txt2gcal
%{_infodir}/gcal.info%{ext_info}

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
