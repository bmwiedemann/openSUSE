#
# spec file for package mingetty
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


Name:           mingetty
Version:        1.0.8s
Release:        0
Summary:        Minimal Getty for Virtual Consoles Only
License:        GPL-2.0+
Group:          System/Base
Url:            http://mingetty.sourceforge.net
Source:         mingetty-1.0.8s.tar.bz2
Patch0:         mingetty-1.0.8s.dif
Provides:       sysvinit:/sbin/mingetty
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The mingetty program is a lightweight, minimalistic getty program for
use on virtual consoles only. Mingetty is not suitable for serial lines
(you should use the mgetty program for this purpose).

%prep
%setup -q
%patch0

%build
%ifarch s390 s390x
DEFTERM=dumb
%else
DEFTERM=linux
%endif
make \
  %{?_smp_mflags} \
  CC="gcc" \
  RPM_OPT_FLAGS="%{optflags} \
  -D_FILE_OFFSET_BITS=64" \
  DEFTERM=${DEFTERM}

%install
mkdir -p ${RPM_BUILD_ROOT}{/sbin,%{_mandir}/man8}
make install MANPATH=%{_mandir} DESTDIR=%{buildroot}

%files
%defattr(-,root,root,755)
/sbin/mingetty
%{_mandir}/man8/mingetty.8.gz

%changelog
