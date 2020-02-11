#
# spec file for package zathura-plugin-pdf-poppler
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


%define realname zathura-pdf-mupdf
Name:           zathura-plugin-pdf-mupdf
Version:        0.3.5
Release:        0
Summary:        PDF support for zathura via mupdf 
License:        Zlib
Group:          Productivity/Office/Other
URL:            https://pwmt.org/projects/%{realname}/
Source:         https://pwmt.org/projects/%{realname}/download/%{realname}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(girara-gtk3)
BuildRequires:  pkgconfig(zathura)
Requires:       zathura
BuildRequires:  mupdf-devel-static
Provides:       zathura-pdf-mupdf-plugin

%description
The zathura-pdf-poppler plugin adds PDF support to zathura by using the poppler rendering engine.

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
%{_libdir}/zathura/libpdf-mupdf.so
%{_datadir}/metainfo/org.pwmt.zathura-pdf-mupdf.metainfo.xml

%changelog
