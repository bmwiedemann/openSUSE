#
# spec file for package x11-tools
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir /var/adm/fillup-templates
%endif

Name:           x11-tools
PreReq:         %fillup_prereq
Provides:       3ddiag
Provides:       xf86tools
Obsoletes:      3ddiag
Obsoletes:      xf86tools
Version:        0.1
Release:        0
Summary:        Tools for the X Window System
License:        GPL-2.0-or-later AND MIT
Group:          System/X11/Utilities
Source2:        xf86debug
Source31:       xim
Source32:       xim.template
Source33:       none
Source34:       sysconfig.language-%{name}
Source35:       nvidia-pre-install
Source36:       nvidia-post-uninstall
Source37:       i18n.template
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Some useful tools for the X Window System.



Authors:
--------
    Stefan Dirsch <sndirsch@suse.de>
    Ludwig Nussel <lnussel@suse.de>

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin/
install -m 755 $RPM_SOURCE_DIR/xf86debug      $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/etc/X11/xim.d
install -m 644 $RPM_SOURCE_DIR/xim  $RPM_BUILD_ROOT/etc/X11
install -m 644 $RPM_SOURCE_DIR/none $RPM_BUILD_ROOT/etc/X11/xim.d
mkdir -p $RPM_BUILD_ROOT/etc/skel
install -m 644 $RPM_SOURCE_DIR/xim.template $RPM_BUILD_ROOT/etc/skel/.xim.template
install -m 644 %{S:37} $RPM_BUILD_ROOT/etc/skel/.i18n
mkdir -p  $RPM_BUILD_ROOT%{_fillupdir}/
install -c -m 644 $RPM_SOURCE_DIR/sysconfig.language-%{name} $RPM_BUILD_ROOT%{_fillupdir}/
mkdir -p $RPM_BUILD_ROOT/usr/lib/nvidia
install -m 755 $RPM_SOURCE_DIR/nvidia-pre-install \
  $RPM_BUILD_ROOT/usr/lib/nvidia/pre-install
install -m 755 $RPM_SOURCE_DIR/nvidia-post-uninstall \
  $RPM_BUILD_ROOT/usr/lib/nvidia/post-uninstall

%post
%{fillup_only -an language}

%files
%defattr(-, root, root)
%dir /etc/X11/xim.d
%dir /usr/lib/nvidia
/usr/bin/xf86debug
/usr/lib/nvidia/pre-install
/usr/lib/nvidia/post-uninstall
/etc/X11/xim
/etc/X11/xim.d/*
/etc/skel/.xim.template
/etc/skel/.i18n
%{_fillupdir}/sysconfig.language-%{name}

%changelog
