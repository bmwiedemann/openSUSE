#
# spec file for package ptools
#
# Copyright (c) 2023 SUSE LLC
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


Name:           ptools
Version:        0.1
Release:        0
Summary:        The process tools collection
License:        GPL-2.0-or-later
Group:          Development/Tools/Debuggers
URL:            ftp://ftp.suse.com/pub/people/jblunck/ptools/
Source:         %{name}-%{version}.tar.bz2
Patch0:         output-l_addr.diff
Patch1:         commit-a42a099
BuildRequires:  libelf-devel
BuildRequires:  popt-devel
#ExclusiveArch:  %{ix86} x86_64

%description
pbuildid dumps the build-ids of an executable, core file or a process,
given the pid of that process.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc README
%{_bindir}/pbuildid
%{_mandir}/man1/pbuildid.1%{?ext_man}

%changelog
