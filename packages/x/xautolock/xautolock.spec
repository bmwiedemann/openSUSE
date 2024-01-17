#
# spec file for package xautolock
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

Name:           xautolock
Version:        2.2
Release:        0
License:        GPL-2.0
Summary:        An automatic X screen-locker/screen-saver
Url:            http://freecode.com/projects/xautolock/
Group:          System/X11/Utilities
Source:         http://www.ibiblio.org/pub/Linux/X11/screensavers/%{name}-%{version}.tgz
Patch0:         xautolock-fixbuild.patch
Provides:       xautolck = %{version}
Obsoletes:      xautolck <= %{version}
BuildRequires:  imake
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Xautolock monitors console activity under the X window system, and fires up a
program of your choice if nothing happens during a user configurable period of
time. You can use this to automatically start up a screen locker in case you
tend to forget to do so manually before having a coffee break.

%prep
%setup -q
%patch0 -p1

%build
xmkmf -a
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install install.man

%files
%defattr(-,root,root)
%doc Todo Readme License Changelog VMS.notes
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1x.gz

%changelog
