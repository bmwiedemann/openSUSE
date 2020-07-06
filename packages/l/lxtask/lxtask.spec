#
# spec file for package lxtask
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


Name:           lxtask
Version:        0.1.9
Release:        0
Summary:        Lightweight Task Manager
License:        GPL-2.0-only
Group:          System/GUI/LXDE
URL:            http://www.lxde.org/
Source0:        https://sourceforge.net/projects/lxde/files/LXTask%20%28task%20manager%29/LXTask%200.1.x/%{name}-%{version}.tar.xz
BuildRequires:  docbook-utils
BuildRequires:  fdupes
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
Recommends:     %{name}-lang
%lang_package

%description
LXTask is a lightweight Task Manager.
This is the default LXDE task manager.

%prep
%setup -q

%build
export CFLAGS="%optflags -fcommon"
%configure
%make_build

%install
%make_install
%suse_update_desktop_file %{name} System Monitor
%find_lang %{name}
%fdupes -s %{buildroot}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/lxtask.1%{?ext_man}

%files lang -f %{name}.lang
%license COPYING

%changelog
