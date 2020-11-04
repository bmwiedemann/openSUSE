#
# spec file for package zathura-plugin-cb
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


%define realname zathura-cb
Name:           zathura-plugin-cb
Version:        0.1.8
Release:        0
Summary:        Comic book support for zathura
License:        Zlib
Group:          Productivity/Office/Other
URL:            http://pwmt.org/projects/zathura/plugins/zathura-cb/
Source:         http://pwmt.org/projects/zathura/plugins/download/%{realname}-%{version}.tar.xz
BuildRequires:  meson > 0.43
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(girara-gtk3)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(zathura)
Requires:       zathura
Provides:       zathura-cb-plugin

%description
The zathura-cb plugin adds comic book support to zathura.

%prep
%setup -q -n %{realname}-%{version}

%build
export CFLAGS="%{optflags}"
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name '*.desktop' -delete -print

%files -n %{name}
%license LICENSE
%doc AUTHORS
%dir %{_libdir}/zathura
%{_libdir}/zathura/libcb.so
%{_datadir}/metainfo/org.pwmt.zathura-cb.metainfo.xml

%changelog
