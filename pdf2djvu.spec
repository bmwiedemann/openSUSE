#
# spec file for package pdf2djvu
#
# Copyright (c) 2021 SUSE LLC
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


Name:           pdf2djvu
Version:        0.9.17.1
Release:        0
Summary:        PDF to DjVu Converter
License:        GPL-2.0-only
Group:          Productivity/Publishing/PDF
URL:            https://jwilk.net/software/pdf2djvu
Source0:        https://github.com/jwilk/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        https://github.com/jwilk/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
# PATCH-FIX-UPSTREAM pdf2djvu-fix-poppler-check.patch gh#jwilk/pdf2djvu#144 badshah400@gmail.com -- Check for poppler instead of poppler-splash, the latter of which is no longer installed by poppler >= 20.12
Patch0:         pdf2djvu-fix-poppler-check.patch
BuildRequires:  djvulibre
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(GraphicsMagick++)
BuildRequires:  pkgconfig(ddjvuapi) >= 3.5.25
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(poppler) >= 0.35
BuildRequires:  pkgconfig(uuid)
# SECTION For Patch1
BuildRequires:  libtool
# /SECTION
Requires:       djvulibre

%description
pdf2djvu creates DjVu files from PDF files. It's able to extract:
graphics, text layer, hyperlinks, document outline (bookmarks) and
metadata (including XMP metadata).

%lang_package

%prep
%autosetup -p1

%build
# Rebuild configure script after Patch1
autoreconf -fvi
%configure
%make_build

%install
%make_install
%find_lang %{name} --with-man

%files
%license doc/COPYING
%doc doc/changelog doc/credits doc/djvudigital doc/README
%{_bindir}/%{name}
%{_mandir}/man?/*

%files lang -f %{name}.lang

%changelog
