#
# spec file for package zathura-plugin-djvu
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


%define realname zathura-djvu
Name:           zathura-plugin-djvu
Version:        0.2.8
Release:        0
Summary:        DjVu support for zathura using the djvulibre library
License:        Zlib
Group:          Productivity/Office/Other
URL:            http://pwmt.org/projects/zathura/plugins/zathura-djvu/
Source:         http://pwmt.org/projects/zathura/plugins/download/%{realname}-%{version}.tar.xz
BuildRequires:  meson >= 0.43
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ddjvuapi)
BuildRequires:  pkgconfig(girara-gtk3)
BuildRequires:  pkgconfig(zathura)
Requires:       zathura
Provides:       zathura-djvu-plugin

%description
The zathura-djvu plugin adds DjVu support to zathura by using the djvulibre library.

%prep
%setup -q -n %{realname}-%{version}

%build
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name '*.desktop' -delete -print

%files -n %{name}
%license LICENSE
%doc AUTHORS
%dir %{_libdir}/zathura
%{_libdir}/zathura/libdjvu.so
%{_datadir}/metainfo/org.pwmt.zathura-djvu.metainfo.xml

%changelog
