#
# spec file for package zathura-plugin-pdf-poppler
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define realname zathura-pdf-poppler
%if 0%{?suse_version} == 1600
%bcond_without gcc15
%endif
Name:           zathura-plugin-pdf-poppler
Version:        2026.05.10
Release:        0
Summary:        PDF support for zathura via poppler
License:        Zlib
URL:            https://pwmt.org/projects/%{realname}
Source0:        %{url}/download/%{realname}-%{version}.tar.xz
Source1:        %{url}/download/%{realname}-%{version}.tar.xz.asc
Source2:        %{realname}.keyring
BuildRequires:  AppStream
BuildRequires:  c_compiler
BuildRequires:  desktop-file-utils
BuildRequires:  meson >= 1.5
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(girara)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(poppler-glib) >= 21.12
BuildRequires:  pkgconfig(zathura) >= 2026.01.30
Requires:       zathura >= 2026.01.30
Provides:       %{realname}-plugin
%if %{with gcc15}
BuildRequires:  gcc15
%endif

%description
The zathura-pdf-poppler plugin adds PDF support to zathura by using the
poppler rendering engine.

%prep
%autosetup -p1 -n %{realname}-%{version}

%build
%{?with_gcc15:export CC=gcc-15}
%meson
%meson_build

%install
%meson_install
find %{buildroot} -name '*.desktop' -delete -print

%check
%meson_test

%files -n %{name}
%license LICENSE
%doc AUTHORS
%dir %{_libdir}/zathura
%{_libdir}/zathura/libpdf-poppler.so
%{_datadir}/metainfo/org.pwmt.%{realname}.metainfo.xml

%changelog
