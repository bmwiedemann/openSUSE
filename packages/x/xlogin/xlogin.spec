#
# spec file for package xlogin
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           xlogin
Requires:       textutils
BuildRequires:  imake
Version:        0.2
Release:        0
Summary:        xlogin, xtelnet
License:        GPL-2.0+
Group:          Productivity/Networking/Other
Source:         xlogin-0.2.tar.gz
Patch:          xlogin-0.2.dif
Patch1:         xlogin-0.2-fix-bashisms.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains two scripts, which, called with the name of a
remote host, will open an xterm window on the local X display with a
remote session or login shell.

The script xlogin starts by a rsh call (remote shell) an xterm on the
remote host.  If necessary, the access will be allowed by sending the
magic key (cookie) of the display to the remote host.

The script xtelnet starts a local xterm with a telnet session on the
remote host.



Authors:
--------
    Werner Fink <werner@suse.de>

%prep
%setup
%patch
%patch1 -p1
  xmkmf

%build

%install
  make DESTDIR=$RPM_BUILD_ROOT install
  make DESTDIR=$RPM_BUILD_ROOT install.man

%clean
  rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_mandir}/*/*
%{_bindir}/*

%changelog
