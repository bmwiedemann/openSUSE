#
# spec file for package linuxrc
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           linuxrc
Version:        7.0.21
Release:        0
Summary:        SUSE Installation Program
License:        GPL-3.0+
Group:          System/Boot
Source:         %{name}-%{version}.tar.xz
BuildRequires:  e2fsprogs-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  libmediacheck-devel
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(hwinfo)
BuildRequires:  pkgconfig(libcurl)
%ifarch s390x
BuildRequires:  qclib-devel
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
SUSE installation program.

%prep
%setup -q

%build
  make

%install
  install -d -m 755 %{buildroot}%{_prefix}/{s,}bin
make %{?_smp_mflags} DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%{_sbindir}/linuxrc
%{_bindir}/mkpsfu
%{_datadir}/linuxrc
%doc COPYING *.html *.md *.txt *.png

%changelog
