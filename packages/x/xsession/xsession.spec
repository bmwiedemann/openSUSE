#
# spec file for package xsession
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


Name:           xsession
BuildRequires:  imake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
Version:        1.1
Release:        0
Summary:        A session manager
License:        MIT
Group:          System/X11/Utilities
Source:         xsession-1.1.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{expand: %%global _exec_prefix %(type -p pkg-config &>/dev/null && pkg-config --variable prefix x11 || echo /usr/X11R6)}
%if "%_exec_prefix" == "/usr/X11R6"
%global _mandir     %{_exec_prefix}/man
%define _x11data    %{_exec_prefix}/lib/X11
%define _appdefdir  %{_x11data}/app-defaults
%else
%define _x11data    %{_datadir}/X11
%define _appdefdir  %{_x11data}/app-defaults
%endif

%description
The xsession program is a session manager.  It is normally executed by
your ~/.xinitrc (or ~/.xsession) script and controls your X Window
session.  As soon as it is started, xsession launches a window manager
and some applications of your choice.  At anytime during your session,
you may switch to another window manager or execute some other
applications from the xsession menus.

Examples may be found under /usr/share/doc/packages/xsession/examples.



Authors:
--------
    Alain Nissen <nissen@montefiore.ulg.ac.be>
    Raphael Quinet <quinet@stud.montefiore.ulg.ac.be>

%prep
%setup -q

%build
xmkmf -a
make CCOPTIONS="$RPM_OPT_FLAGS"

%install
make DESTDIR=%{buildroot} install
make DESTDIR=%{buildroot} install.man

%files
%defattr(-,root,root)
%doc CHANGES ChangeLog INSTALL README examples
%{_bindir}/xsession
%dir %{_appdefdir}
%config %{_appdefdir}/XSession
%config %{_appdefdir}/XSession-color
%doc %{_mandir}/man1/xsession.1x.gz

%changelog
