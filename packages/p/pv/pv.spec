#
# spec file for package pv
#
# Copyright (c) 2020 SUSE LLC
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


Name:           pv
Version:        1.6.6
Release:        0
Summary:        PipeViewer - Monitor the Progress of Data through Pipes
License:        Artistic-2.0
Group:          System/Base
URL:            http://ivarch.com/programs/pv.shtml

Source:         http://ivarch.com/programs/sources/%name-%version.tar.bz2
Source2:        http://ivarch.com/programs/sources/%name-%version.tar.bz2.txt
Source3:        %name.keyring
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  glibc-devel
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  sysvinit-tools

%description
PV ("Pipe Viewer") is a tool for monitoring the progress of data through a
pipeline. It can be inserted into any normal pipeline between two processes
to give a visual indication of how quickly data is passing through, how long
it has taken, how near to completion it is, and an estimate of how long it
will be until completion.

%prep
%autosetup -p1

%build
%configure --enable-lfs --enable-nls --disable-debugging
%make_build

%install
%make_install
%find_lang %name

%check
%make_build test

%files -f %name.lang
%license doc/COPYING
%doc README doc/NEWS
%_bindir/pv
%_mandir/man1/pv.1%ext_man

%changelog
