#
# spec file for package spu-tools
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           spu-tools
Version:        2.3.0
Release:        0
Url:            http://sourceforge.net/projects/libspe
Summary:        User space tools for Cell/B.E.
License:        GPL-2.0
Group:          System/Management
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  help2man
BuildRequires:  ncurses-devel
Source:         %{name}-%{version}.tar.bz2
# match Cell for package installation
Supplements:    modalias(platform:cbe-mic)
# match ps3flash for package installation
Supplements:    modalias(ps3:8)
Patch:          spu-tools-2.3.0-as-needed.patch

%description
The spu-tools package contains user space tools for Cell/B.E.
   Currently, it contain two tools: - spu-top: a tool like top to
   watch the SPU's on a Cell BE System. It shows information about
   SPUs and running SPU contexts.

- spu-ps: a tool like ps, which dumps a report on the currently running
SPU contexts.



%prep
%setup -q
%patch

%build
make CFLAGS="$RPM_OPT_FLAGS -fgnu89-inline" CC="%__cc" %{?_smp_mflags}

%clean 
#rm -rf $RPM_BUILD_ROOT

%install
make DESTDIR=$RPM_BUILD_ROOT install

%files 
%defattr(-,root,root)
/usr/bin/spu-top
/usr/bin/spu-ps
%_mandir/man1/spu-top.1.gz
%_mandir/man1/spu-ps.1.gz

%changelog
