#
# spec file for package kdbg
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


Name:           kdbg
Version:        3.0.0
Release:        0
Summary:        Graphical User Interface for GDB
License:        GPL-2.0+
Group:          Development/Tools/Debuggers
Url:            http://www.kdbg.org/
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.3
BuildRequires:  extra-cmake-modules
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Widgets)
Requires:       gdb
Recommends:     %{name}-lang = %{version}
Suggests:       %{name}-doc = %{version}

%description
KDbg is a graphical user interface for GDB, the GNU debugger. It
provides an intuitive interface for setting breakpoints, inspecting
variables, and stepping through code.

%package doc
Summary:        Documentation for %{name}
Group:          Development/Tools/Debuggers
Requires:       %{name} = %{version}

%description doc
This package provides the documentation for %{name}

%lang_package

%prep
%setup -q

%build
  %cmake_kf5 -d build
  %make_jobs

%install
  %kf5_makeinstall -C build
  %fdupes -s %{buildroot}
  %find_lang %{name} --all-name
  %{kf5_find_htmldocs}

%files lang -f %{name}.lang

%files
%doc COPYING BUGS ChangeLog-pre-2.2.0 TODO README ReleaseNotes-*
%config %{_kf5_configdir}/kdbgrc
%doc %lang(en) %{_kf5_htmldir}/en/kdbg
%{_kf5_bindir}/kdbg
%{_kf5_sharedir}/kdbg/
%{_kf5_kxmlguidir}/kdbg/
%{_kf5_iconsdir}/hicolor/
%{_kf5_applicationsdir}/kdbg.desktop

%changelog
