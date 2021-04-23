#
# spec file for package schedtop
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


Name:           schedtop
Version:        1.1
Release:        0
Summary:        Displays Scheduler Statistics
License:        GPL-2.0-or-later
Group:          System/Monitoring
Url:            https://github.com/ghaskins/schedtop
Source:         %{name}-%{version}.tar.gz
Patch0:         schedtop-cxxflags.patch
Patch1:         schedtop-boost_filesystem_changes.patch
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_program_options-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  gcc-c++
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This utility will process statistics from /proc/schedstat such that the
busiest stats will bubble up to the top.  It can alternately be sorted by
the largest stat, or by name.  Stats can be included or excluded based on
reg-ex pattern matching.

%prep
%setup -q
%patch0
%patch1

%build
make %{?_smp_mflags} CXXFLAGS="%{optflags}"

%install
make install PREFIX=%{buildroot}
install -D -m 0644 schedtop.1 %{buildroot}/%{_mandir}/man1/schedtop.1

%files
%defattr(-,root,root)
%doc schedtop.html
%{_bindir}/schedtop
%{_mandir}/man1/*

%changelog
