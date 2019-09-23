#
# spec file for package pv
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


Name:           pv
Version:        1.6.6
Release:        0
Summary:        PipeViewer - Monitor the Progress of Data through Pipes
License:        Artistic-2.0
Group:          System/Base
Url:            http://ivarch.com/programs/pv.shtml

Source:         http://ivarch.com/programs/sources/%name-%version.tar.bz2
Source2:        http://ivarch.com/programs/sources/%name-%version.tar.bz2.txt
Source3:        %name.keyring
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  glibc-devel
BuildRequires:  intltool
BuildRequires:  make
%if 0%{?suse_version} && 0%{?suse_version} <= 1200
# The testsuite wants the "usleep" utility
BuildRequires:  sysvinit
%else
BuildRequires:  sysvinit-tools
%endif

%description
PV ("Pipe Viewer") is a tool for monitoring the progress of data through a
pipeline. It can be inserted into any normal pipeline between two processes
to give a visual indication of how quickly data is passing through, how long
it has taken, how near to completion it is, and an estimate of how long it
will be until completion.

%prep
%setup -q

%build
%configure --enable-lfs --enable-nls --disable-debugging
make %{?_smp_mflags}

%install
%make_install
%find_lang %name

%check
make test

%files -f %name.lang
%defattr(-,root,root)
%doc README doc/COPYING doc/NEWS
%_bindir/pv
%doc %_mandir/man1/pv.1%ext_man

%changelog
