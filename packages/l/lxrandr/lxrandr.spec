#
# spec file for package lxrandr
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


Name:           lxrandr
Version:        0.3.1
Release:        0
Summary:        Lightweight Monitor Config Tool
License:        GPL-2.0
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
LXRandR is a lightweight Monitor Config Tool

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%suse_update_desktop_file %{name}
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
%{_datadir}/applications/lxrandr.desktop
%{_mandir}/man1/lxrandr.1.gz

%files lang -f %{name}.lang
%defattr(-,root,root,-)

%changelog
