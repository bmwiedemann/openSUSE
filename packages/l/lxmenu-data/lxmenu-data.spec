#
# spec file for package lxmenu-data
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


Name:           lxmenu-data
Version:        0.1.5
Release:        0
Url:            http://www.lxde.org
Source0:        %{name}-%{version}.tar.xz
# PATCH-FEATURE-OPENSUSE lxmenu-data-0.1.1-menu-customization.patch -- Guido Berhörster guido+opensuse.org@berhoerster.name
# Clean up lxde menu and improve user experience
Patch0:         %name-0.1.1-menu-customization.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc
BuildRequires:  gettext-tools
BuildRequires:  intltool
BuildRequires:  perl
BuildRequires:  perl-XML-Parser
BuildRequires:  pkg-config
Requires(pre):	desktop-file-utils
Requires(post):	desktop-file-utils
BuildArch:      noarch
Summary:        A tool to build desktop menu for LXDE 
License:        GPL-2.0
Group:          System/GUI/LXDE

%description
LXSession is the default X11 session manager of LXDE.
(LXDE: Lightweight X11 Desktop Environment)
http://lxde.sourceforge.net/

This package provides files required to build freedesktop.org 
menu spec-compliant desktop menus for LXDE.

%prep
%setup -q
%patch0 -p1

%build
%configure
%__make %{?jobs:-j%{jobs}} V=1

%install
%makeinstall

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc README AUTHORS COPYING
%dir %_sysconfdir/xdg/menus
%config %_sysconfdir/xdg/menus/lxde-applications.menu
%{_datadir}/desktop-directories

%changelog
