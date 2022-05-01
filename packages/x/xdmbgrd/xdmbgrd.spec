#
# spec file for package xdmbgrd
#
# Copyright (c) 2022 SUSE LLC
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


Name:           xdmbgrd
Version:        0.8
Release:        0
Summary:        SUSE Linux background
License:        GPL-2.0-or-later
Group:          System/X11/Displaymanagers
Source:         xdmbgrd-%{version}.tar.bz2
Source1:        xdmbgrd-rpmlintrc
BuildRequires:  pkgconfig
BuildRequires:  xdm
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(zlib)

%description
The SUSE Linux background for your XDM workstation.

%prep
%setup -q

%build
PATH=$PATH:.
make XLIBD=%{_libdir} openSUSE=SuSE_Linux_6 SLES=SuSE_Linux_8

%install
if test -x %{_bindir}/chooser ; then
	mkdir -p %{buildroot}%{_bindir}
	install -m 0755 BackGround %{buildroot}%{_bindir}
	echo %{_bindir}/BackGround > file-list
else
    if test -x /etc/X11/xdm/chooser ; then
	mkdir -p %{buildroot}%{_sysconfdir}/X11/xdm
	install -m 0755 BackGround %{buildroot}%{_sysconfdir}/X11/xdm/
	echo /etc/X11/xdm/BackGround           > file-list
    else
	mkdir -p %{buildroot}%{_libdir}/X11/xdm
	install -m 0755 BackGround %{buildroot}%{_libdir}/X11/xdm
	echo %{_libdir}/X11/xdm/BackGround > file-list
    fi
fi

%files -f file-list
%defattr(-,root,root)

%changelog
