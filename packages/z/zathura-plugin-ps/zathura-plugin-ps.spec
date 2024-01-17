#
# spec file for package zathura-plugin-ps
#
# Copyright (c) 2022 SUSE LLC
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


%define realname zathura-ps
Name:           zathura-plugin-ps
Version:        0.2.7
Release:        0
Summary:        PS support for zathura via libspectre
License:        Zlib
Group:          Productivity/Office/Other
URL:            https://pwmt.org/projects/%{realname}/
Source:         https://pwmt.org/projects/%{realname}/download/%{realname}-%{version}.tar.xz
BuildRequires:  meson >= 0.43
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(girara-gtk3)
BuildRequires:  pkgconfig(libspectre)
BuildRequires:  pkgconfig(zathura)
Requires:       zathura
Provides:       zathura-ps-plugin

%description
The zathura-ps plugin adds PostScript support to zathura by using the libspectre library.

%prep
%setup -q -n %{realname}-%{version}

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name "*.desktop" -delete -print

%files -n %{name}
%license LICENSE
%doc AUTHORS
%dir %{_libdir}/zathura
%{_libdir}/zathura/libps.so
%{_datadir}/metainfo/org.pwmt.zathura-ps.metainfo.xml

%changelog
