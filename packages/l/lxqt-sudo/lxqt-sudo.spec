#
# spec file for package lxqt-sudo
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


Name:           lxqt-sudo
Version:        0.16.0
Release:        0
Summary:        GUI frontend for sudo
License:        LGPL-2.1-only
Group:          System/X11/Utilities
URL:            http://lxqt.org
Source:         https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
BuildRequires:  cmake >= 3.1.0
BuildRequires:  gcc-c++
BuildRequires:  lxqt-build-tools-devel >= 0.8.0
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(lxqt) >= %{version}
Requires:       sudo
Recommends:     %{name}-lang

%description
A graphical frontend for plain sudo (for requesting optional password in GUI
fashion).
When invoked it simply spawns child sudo process with requested command (and
arguments). If sudo requests user's password, the GUI password dialog is shown
and (after submit) the password is provided to sudo.

%lang_package

%prep
%setup -q

%build
%cmake -DPULL_TRANSLATIONS=No
make %{?_smp_mflags}

%install
%cmake_install

%find_lang %{name} --with-qt

%files
%license LICENSE
%doc AUTHORS
%{_bindir}/%{name}
%{_bindir}/lxsu*
%{_mandir}/man?/%{name}.*
%{_mandir}/man?/lxsu*.*

%files lang -f %{name}.lang
%dir %{_datadir}/lxqt
%dir %{_datadir}/lxqt/translations
%{_datadir}/lxqt/translations/lxqt-sudo

%changelog
