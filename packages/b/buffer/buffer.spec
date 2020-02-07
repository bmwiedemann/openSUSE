#
# spec file for package buffer
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


Name:           buffer
Version:        1.19
Release:        0
Summary:        Buffering stdin and stdout
License:        GPL-2.0-or-later
Group:          System/Base
Source:         buffer-%{version}.tar.gz
Patch0:         buffer-%{version}.dif

%description
This is a program designed to speed up writing tapes on remote tape
drives.  When this program is put "in the pipe," two processes are
started.  One process reads from standard-in and the other writes to
standard-out.  Both processes communicate via shared memory.

%prep
%autosetup -p0

%build
%make_build CFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
make install INSTBIN=%{buildroot}%{_bindir} \
    	     INSTMAN=%{buildroot}%{_mandir}/man1 S=1

%files
%attr(755,root,root) %{_bindir}/buffer
%{_mandir}/man1/buffer.1%{?ext_man}

%changelog
