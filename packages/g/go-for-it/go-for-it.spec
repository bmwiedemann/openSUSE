#
# spec file for package go-for-it
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


%define _name com.github.jmoerman.go-for-it
Name:           go-for-it
Version:        1.6.3
Release:        0
Summary:        A to-do list with built-in productivity timer
License:        GPL-3.0
Group:          Productivity/Office/Organizers
Url:            https://github.com/mank319/Go-For-It
Source:         https://github.com/mank319/Go-For-It/archive/%{version}.tar.gz
BuildRequires:  cmake >= 2.8
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala >= 0.26
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.14.0
BuildRequires:  pkgconfig(libnotify)
Recommends:     %{name}-lang

%description
Go For It! keeps track of tasks and assists in processing
them subsequently. The timer avoids distraction by keeping the user's
focus on the recent task, while issuing reminders to take short breaks
on a regular basis.

%lang_package

%prep
%setup -q -n Go-For-It-%{version}

%build
%cmake
make %{?_smp_mflags} V=1

%install
%cmake_install
%suse_update_desktop_file -r %{_name} Utility DesktopUtility
%find_lang %{_name}
%fdupes %{buildroot}%{_datadir}

%if 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%doc AUTHORS CHANGELOG.md COPYING README.md
%{_bindir}/%{_name}
%{_datadir}/%{_name}/
%{_datadir}/applications/%{_name}.desktop
%{_datadir}/icons/hicolor/*/*/%{_name}*
# Own this directory for legacy reasons
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/%{_name}.appdata.xml

%files lang -f %{_name}.lang

%changelog
