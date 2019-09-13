#
# spec file for package buffer
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           buffer
License:        GPL-2.0+
Group:          System/Base
Version:        1.19
Release:        843
Summary:        Buffering stdin and stdout
Source:         buffer-%{version}.tar.gz
Patch:          buffer-%{version}.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is a program designed to speed up writing tapes on remote tape
drives.  When this program is put "in the pipe," two processes are
started.  One process reads from standard-in and the other writes to
standard-out.  Both processes communicate via shared memory.

%prep
%setup
%patch

%build
make CC="%__cc" CFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin $RPM_BUILD_ROOT%{_mandir}/man1
make install INSTBIN=$RPM_BUILD_ROOT/usr/bin \
     	     INSTMAN=$RPM_BUILD_ROOT%{_mandir}/man1 S=1

%files
%defattr(-,root,root)
%attr(755,root,root) /usr/bin/buffer
%doc %{_mandir}/man1/buffer.1.gz

%changelog
