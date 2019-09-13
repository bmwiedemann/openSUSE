#
# spec file for package ptools (Version 0.1)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Url:            ftp://ftp.suse.com/pub/people/jblunck/ptools/

Name:           ptools
Summary:        The process tools collection
Version:        0.1
Release:        11
License:        GPL-2.0+
Group:          Development/Tools/Debuggers
Source:         %{name}-%{version}.tar.bz2
Patch0:         output-l_addr.diff
Patch1:         commit-a42a099
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libelf-devel popt-devel
AutoReqProv:    on
#ExclusiveArch:  %{ix86} x86_64

%description
pbuildid dumps the build-ids of an executable, core file or a process,
given the pid of that process.



Authors:
--------
    Jan Blunck <jblunck@suse.de>

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR="$RPM_BUILD_ROOT" install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/pbuildid
%{_mandir}/man1/pbuildid.1*

%changelog
