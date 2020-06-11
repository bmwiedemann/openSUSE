#
# spec file for package xdg-utils
#
# Copyright (c) 2020 SUSE LLC
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


Name:           xdg-utils
Version:        1.1.3+20200220
Release:        0
Summary:        Utilities to uniformly interface desktop environments
License:        MIT
Group:          System/GUI/Other
URL:            https://www.freedesktop.org/wiki/Software/xdg-utils/
# http://portland.freedesktop.org/download/xdg-utils-%%{version}.tar.gz
Source:         xdg-utils-%{version}.tar.xz
# PATCH-FEATURE-OPENSUSE install-some-more-scripts.diff jslaby@suse.cz
Patch0:         install-some-more-scripts.diff
# PATCH-FIX-UPSTREAM 0001-Don-t-run-kreadconfig-if-KDE_SESSION_VERSION-is-5.patch
Patch1:         0001-Don-t-run-kreadconfig-if-KDE_SESSION_VERSION-is-5.patch
BuildRequires:  make
# for xmlto to be able to generate text from html
BuildRequires:  w3m
BuildRequires:  xmlto
Requires:       perl
Requires:       perl-Net-DBus
Requires:       perl-X11-Protocol
Requires:       which
BuildArch:      noarch

%description
The xdg-utils package is a set of simple scripts that provide basic
desktop integration functions for any Free Desktop, such as Linux.

They are intended to provide a set of de-facto standards.
This means that:
 * Third party software developers can rely on these xdg-utils for
   all of their simple integration needs.

*  Developers of desktop environments can make sure that their
   environments are well supported.

   If a desktop developer wants to be certain that their
   environment functions with all third party software, then can
   simply make sure that these utilities work properly in their
   environment.

%prep
%autosetup -p1

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc ChangeLog README TODO
%license LICENSE
%{_bindir}/xdg-desktop-icon
%{_bindir}/xdg-desktop-menu
%{_bindir}/xdg-email
%{_bindir}/xdg-icon-resource
%{_bindir}/xdg-mime
%{_bindir}/xdg-open
%{_bindir}/xdg-su
%{_bindir}/xdg-screensaver
%{_bindir}/xdg-settings
%{_bindir}/xdg-terminal
%{_mandir}/man1/xdg-desktop-icon.1%{?ext_man}
%{_mandir}/man1/xdg-desktop-menu.1%{?ext_man}
%{_mandir}/man1/xdg-email.1%{?ext_man}
%{_mandir}/man1/xdg-icon-resource.1%{?ext_man}
%{_mandir}/man1/xdg-mime.1%{?ext_man}
%{_mandir}/man1/xdg-open.1%{?ext_man}
%{_mandir}/man1/xdg-terminal.1%{?ext_man}
%{_mandir}/man1/xdg-screensaver.1%{?ext_man}
%{_mandir}/man1/xdg-settings.1%{?ext_man}
%{_mandir}/man1/xdg-su.1%{?ext_man}

%changelog
