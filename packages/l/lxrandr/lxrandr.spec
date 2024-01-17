#
# spec file for package lxrandr
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


Name:           lxrandr
Version:        0.3.2
Release:        0
Summary:        Lightweight Monitor Config Tool
License:        GPL-2.0-only
Group:          System/GUI/LXDE
URL:            http://www.lxde.org/
Source0:        https://sourceforge.net/projects/lxde/files/LXRandR%20%28monitor%20config%20tool%29/LXRandR%200.3.x/%{name}-%{version}.tar.xz
BuildRequires:  docbook-utils
BuildRequires:  fdupes
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
Recommends:     %{name}-lang
%lang_package

%description
LXRandR is a lightweight Monitor Config Tool

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install
%suse_update_desktop_file %{name}
%find_lang %{name}
%fdupes -s %{buildroot}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/lxrandr.desktop
%{_mandir}/man1/lxrandr.1%{?ext_man}

%files lang -f %{name}.lang
%license COPYING

%changelog
