#
# spec file for package wyrd
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           wyrd
Version:        1.4.6
Release:        0
Summary:        Text-based front-end to Remind time organizer
License:        GPL-2.0
Group:          Productivity/Office/Organizers
Url:            http://pessimization.com/software/wyrd/
Source0:        %{name}-%{version}.tar.bz2
Patch0:         %{name}-%{version}-ncurses.patch
Patch1:         reproducible.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  camlp4
BuildRequires:  ncurses-devel
BuildRequires:  pkg-config
BuildRequires:  remind
Requires:       remind
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Wyrd is a text-based front-end to Remind, a sophisticated calendar and alarm
program. Remind's power lies in its programmability, and Wyrd does not hide
this capability behind flashy GUI dialogs. Rather, Wyrd is designed to make you
more efficient at editing your reminder files directly. It also offers a
scrollable timetable suitable for visualizing your schedule at a glance.

Unlike most of the calendar applications available today, Wyrd is designed to
be both lightweight and fast. Startup time is negligible, UI navigation is
instantaneous, and the wyrd process typically consumes less than 2MB of
resident memory.

%prep
%setup -q
%patch0
%patch1 -p1

%build
autoreconf -fi
%configure --enable-utf8
make

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/manual.html README COPYING ChangeLog
%doc %{_mandir}/man1/wyrd.1%{ext_man}
%doc %{_mandir}/man5/wyrdrc.5%{ext_man}
%config %{_sysconfdir}/wyrdrc
%attr(0755,root,root) %{_bindir}/wyrd

%changelog
