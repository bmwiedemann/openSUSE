#
# spec file for package zathura-plugin-pdf-mupdf
#
# Copyright (c) 2024 SUSE LLC
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
Version:        0.4.3
Release:        0
Summary:        Zathura PDF support through MuPDF
License:        Zlib
Group:          Productivity/Office/Other
URL:            https://pwmt.org/projects/zathura-pdf-mupdf/
Source:         https://pwmt.org/projects/%{realname}/download/%{realname}-%{version}.tar.xz
Patch1:         0001-Don-t-link-against-gumbo.patch
Patch2:         0002-Revert-Rework-detection-of-mupdf.patch
BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:  mupdf-devel-static >= 1.20
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(girara-gtk3)
%if 0%{?suse_version} > 1500
BuildRequires:  pkgconfig(jbig2dec)
%else
BuildRequires:  jbig2dec-devel
%endif
BuildRequires:  pkgconfig(lept)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(mujs)
BuildRequires:  pkgconfig(tesseract)
BuildRequires:  pkgconfig(zathura) >= 0.5.2
Requires:       mupdf >= 1.20
Requires:       zathura >= 0.5.2
Conflicts:      zathura-plugin-pdf-poppler
Provides:       zathura-pdf-mupdf-plugin

%description
Zathura-plugin-MupDF extends the document viewing support of Zathura to PDF, EPUB and OpenXPS with the help of MuPDF rendering engine.

%prep
%autosetup -p1 -n %{realname}-%{version}

%build
export CFLAGS="%{optflags}"
%meson -Dlink-external=true
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
