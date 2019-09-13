#
# spec file for package xdmbgrd
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


Name:           xdmbgrd
Version:        0.6
Release:        0
Summary:        SUSE Linux background
License:        GPL-2.0+
Group:          System/X11/Displaymanagers
Source:         xdmbgrd-0.6.tar.bz2
Patch0:         xdmbgrd-0.6.dif
Patch1:         xdmbgrd-piggyback.dif
BuildRequires:  pkgconfig
BuildRequires:  xdm
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(zlib)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{expand: %%global _exec_prefix %(type -p pkg-config &>/dev/null && pkg-config --variable prefix x11 || echo /usr/X11R6)}

%description
The SUSE Linux background for your XDM workstation.

%prep
%setup -q
%patch0
%patch1

%build
PATH=$PATH:.
make XLIBD=%{_libdir} openSUSE=SuSE_Linux_6 SLES=SuSE_Linux_7

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
