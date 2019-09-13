#
# spec file for package lxtask
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           lxtask
Version:        0.1.8
Release:        0
Summary:        Lightweight Task Manager
License:        GPL-2.0-only
Group:          System/GUI/LXDE
Url:            http://www.lxde.org/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  docbook-utils
BuildRequires:  fdupes
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%lang_package

%description
LXTask is a lightweight Task Manager.
This is the default LXDE task manager.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%suse_update_desktop_file %{name} System Monitor
%find_lang %{name}
%fdupes -s %{buildroot}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root,0755)
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/lxtask.1.gz

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
