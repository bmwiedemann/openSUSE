#
# spec file for package kdbg
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define kf6_version 6.6.0
%define qt6_version 6.6.2
#
Name:           kdbg
Version:        3.2.0
Release:        0
Summary:        Graphical User Interface for GDB
License:        GPL-2.0-or-later
URL:            https://www.kdbg.org/
Source0:        https://github.com/j6t/kdbg/archive/refs/tags/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  cmake(KF6Config) >= %{kf6_version}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_version}
BuildRequires:  cmake(KF6I18n) >= %{kf6_version}
BuildRequires:  cmake(KF6IconThemes) >= %{kf6_version}
BuildRequires:  cmake(KF6WindowSystem) >= %{kf6_version}
BuildRequires:  cmake(KF6XmlGui) >= %{kf6_version}
BuildRequires:  cmake(Qt6Core) >= %{qt6_version}
BuildRequires:  cmake(Qt6Core5Compat) >= %{qt6_version}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_version}
Requires:       gdb
Suggests:       kdbg-doc = %{version}

%description
KDbg is a graphical user interface for GDB, the GNU debugger. It
provides an intuitive interface for setting breakpoints, inspecting
variables, and stepping through code.

%package doc
Summary:        Documentation for kdbg
Requires:       kdbg = %{version}

%description doc
This package provides the documentation for kdbg

%lang_package

%prep
%autosetup -p1 -n kdbg-kdbg-%{version}

%build
%cmake_kf6 -DBUILD_FOR_KDE_VERSION:STRING=6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}

%find_lang %{name} --all-name --with-html

%files
%license COPYING
%doc README ReleaseNotes-*
%config %{_kf6_configdir}/kdbgrc
%doc %lang(en) %{_kf6_htmldir}/en/kdbg
%{_kf6_applicationsdir}/kdbg.desktop
%{_kf6_bindir}/kdbg
%{_kf6_iconsdir}/hicolor/
%{_kf6_kxmlguidir}/kdbg/
%{_kf6_sharedir}/kdbg/

%files lang -f %{name}.lang
%exclude %{_kf6_htmldir}/en/kdbg

%changelog
