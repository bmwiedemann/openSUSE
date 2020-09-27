# vim: set ts=4 sw=4 et:
#
# spec file for package lnav
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2010-2013 Pascal Bleser <pascal.bleser@opensuse.org>
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


Name:           lnav
Version:        0.9.0
Release:        0
Summary:        Logfile Navigator
License:        BSD-2-Clause
Group:          System/Monitoring
URL:            http://lnav.org
#Git-Clone:     https://github.com/tstack/lnav.git
Source:         https://github.com/tstack/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        lnav.desktop
%if 0%{?suse_version} >= 1500
BuildRequires:  gcc-c++
%define cxx g++
%else
BuildRequires:  gcc6-c++
%define cxx g++-6
%endif
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libcurl-devel
BuildRequires:  ncurses-devel
BuildRequires:  pcre-devel
BuildRequires:  readline-devel
BuildRequires:  zlib-devel
%if 0%{?suse_version}
BuildRequires:  sqlite3-devel >= 3.9.0
%else
BuildRequires:  sqlite-devel >= 3.9.0
%endif
%if 0%{?suse_version} > 0
BuildRequires:  update-desktop-files
%endif

%description
The Logfile Navigator, lnav for short, is a curses-based tool for viewing and
analyzing log files. The value added by lnav over text viewers or editors is
that it takes advantage of any semantic information that can be gleaned from
the log file, such as timestamps and log levels. Using this extra semantic
information, lnav can do things like interleaving messages from different
files, generate histograms of messages over time, and provide hotkeys for
navigating through the file. These features are meant to allow the user to
quickly and efficiently focus on problems.

%prep
%setup -q

%build
export CXX=%cxx
autoreconf -fiv
%configure \
     --disable-silent-rules \
     --disable-static \
     --with-ncurses \
     --with-readline

#     --with-yajl       local copy contains changes that will probably be merged for next release (after 2.1.0).

make %{?_smp_mflags}

%install
%make_install

%if %{defined suse_version}
install -D -m0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/applications/%{name}.desktop"
%suse_update_desktop_file -r "%{name}" System Monitor
%endif

%files
%license LICENSE
%doc AUTHORS NEWS README
%{_bindir}/lnav
%{_mandir}/man1/lnav.1%{?ext_man}
%if %{defined suse_version}
%{_datadir}/applications/%{name}.desktop
%endif

%changelog
