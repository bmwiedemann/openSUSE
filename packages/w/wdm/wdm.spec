#
# spec file for package wdm
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


#
%define _dminitdir %{_prefix}/lib/X11/displaymanagers

Name:           wdm
BuildRequires:  WindowMaker-devel
BuildRequires:  automake
BuildRequires:  freetype2-devel
BuildRequires:  libselinux-devel
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xau)
BuildRequires:  pkgconfig(xdmcp)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xt)
Version:        1.28
Release:        0
PreReq:         /etc/X11/xdm/xdm-config
Source:         %{name}-%{version}.tar.bz2
Source2:        SUSE.png
Source3:        wdm-config
Source4:        wdmLogin
Source5:        wdm
Patch2:         %{name}-%{version}-pam.patch
Patch3:         %{name}-%{version}-WINGs.patch
Patch4:         %{name}-%{version}-reserve.patch
Patch5:         %{name}-%{version}-composite.patch
Url:            http://voins.program.ru/wdm/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        WINGs Display Manager
License:        GPL-2.0+
Group:          System/X11/Displaymanagers

%description
WDM is a modification and enhancement of X11's XDM that provides a more
flexible login panel while maintaining the basic XDM code to interface
with pam and other packages.



Authors:
--------
    Jerome Alet <alet@unice.fr>
    Gene Czarcinski <genec@mindspring.com>

%define wdmdir /etc/X11/wdm

%prep
%setup
%patch2
%patch3
%patch4
%patch5

%build
autoreconf --force --install
export CFLAGS="$RPM_OPT_FLAGS -DDEV_RANDOM=\\\"/dev/random\\\""
export CXXFLAGS="$CFLAGS"
%configure \
    --enable-pam \
    --enable-selinux \
    --with-gfxdir=/etc/X11/wdm/pixmaps \
    --with-wdmdir=%{wdmdir} \
    --with-nlsdir=%{_datadir}/locale

%install
mkdir -p $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
mkdir -p $RPM_BUILD_ROOT/sbin/conf.d
install -m 644 %{S:3} $RPM_BUILD_ROOT/%{wdmdir}
mkdir -p $RPM_BUILD_ROOT/%{wdmdir}/Defaults
install -m 644 %{S:4} $RPM_BUILD_ROOT/%{wdmdir}/Defaults
install -m 644 %{S:2} $RPM_BUILD_ROOT/%{wdmdir}/pixmaps
rm $RPM_BUILD_ROOT/etc/pam.d/wdm
rm `find $RPM_BUILD_ROOT/%{wdmdir} -type f -maxdepth 1 -not -name wdm-config -print`
%find_lang %{name}
mkdir -p %{buildroot}%{_dminitdir}/
cp %{SOURCE5} %{buildroot}%{_dminitdir}/
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-displaymanager
ln -s %{_sysconfdir}/alternatives/default-displaymanager %{buildroot}%{_libexecdir}/X11/displaymanagers/default-displaymanager

%post
%{_sbindir}/update-alternatives --install %{_libexecdir}/X11/displaymanagers/default-displaymanager \
  default-displaymanager %{_libexecdir}/X11/displaymanagers/wdm 10

%postun
[ -f %{_libexecdir}/X11/displaymanagers/wdm ] || %{_sbindir}/update-alternatives \
  --remove default-displaymanager %{_libexecdir}/X11/displaymanagers/wdm

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README README.pam TODO
%{_bindir}/wdm*
%{_mandir}/man1/*
%dir %{wdmdir}
%dir %{wdmdir}/pixmaps
%dir %{wdmdir}/Defaults
%dir %{_dminitdir}
%config %{wdmdir}/pixmaps/*
%config %{wdmdir}/Defaults/*
%config(noreplace) %{wdmdir}/wdm-config
%{_dminitdir}/wdm
%{_dminitdir}/default-displaymanager
%ghost %{_sysconfdir}/alternatives/default-displaymanager

%changelog
