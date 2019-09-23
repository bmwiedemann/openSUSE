#
# spec file for package lxcc
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


Name:           lxcc
Version:        0.1.0+svn733
Release:        0
Summary:        LXDE Control Center
License:        GPL-3.0
Group:          System/GUI/LXDE
Url:            https://noc.sidux.com/lxde
Source0:        %{name}.tar.xz
Source1:        %{name}_template.moo
Source2:        README.SUSE
Source3:        COPYING
BuildRequires:  fdupes
BuildRequires:  python-devel
BuildRequires:  update-desktop-files
Requires:       python-gobject2
Requires:       python-gtk >= 2.0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%py_requires

%description
%{name} provides a simple and fast LXDE Control Center

%prep
%setup -q -n %{name}
cp %{SOURCE1} .
cp %{SOURCE2} .
mv usr/share/icons usr/share/pixmaps

%build

%install
find usr -depth -print | cpio -pvd %{buildroot}
%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}
cp %{SOURCE3} .
chmod +x %buildroot/%{_bindir}/%{name}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr (-,root,root,-)
%doc %{name}_template.moo README.SUSE COPYING
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/locale/*/LC_MESSAGES/%{name}.moo

%changelog
