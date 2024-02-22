#
# spec file for package xdg-menu
#
# Copyright (c) 2024 SUSE LLC
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


Name:           xdg-menu
Version:        0.2
Release:        0
Summary:        XDG Menus for WindowMaker and other Window Managers
License:        GPL-2.0-or-later
Group:          System/GUI/Other
Source0:        %{name}.tar.bz2
Patch0:         %{name}-xfce4.patch
Patch1:         %{name}-box.patch
Patch2:         %{name}-twm.patch
Patch3:         %{name}-xfce4-icon.patch
Patch4:         %{name}-gnome-path.patch
Patch5:         %{name}-icewm.patch
Patch6:         %{name}-pekwm.patch
Patch7:         %{name}-translation-bnc463972.patch
Patch8:         %{name}-accept-defaultlayout-bnc529057.patch
# PATCH-FIX-OPENSUSE xdg-menu-su.patch asterios.dramis@gmail.com -- Use "su" instead of "sux" to run commands with root privileges in xdg_menu_su (sux is deprecated)
Patch9:         xdg-menu-su.patch
Requires:       desktop-data
Requires:       perl-XML-Parser
%if 0%{?suse_version} > 1320
Requires:       xterm-bin
%else
Requires:       xterm
%endif
Requires:       perl(Locale::gettext)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package contains a Perl script which converts XDG menus to formats
used by WindowMaker and other window managers.

%prep
%setup -q -n xdg-menu
%patch -P 0
%patch -P 1 -p1
%patch -P 2
%patch -P 3
%patch -P 4
%patch -P 5
%patch -P 6
%patch -P 7
%patch -P 8
%patch -P 9

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -pm 0755 * %{buildroot}%{_bindir}

%files
%defattr(-,root,root,-)
%{_bindir}/xdg_menu
%{_bindir}/xdg_menu_su

%changelog
