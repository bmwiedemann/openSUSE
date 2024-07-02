#
# spec file for package osinfo-db-tools
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           osinfo-db-tools
Version:        1.11.0
Release:        0
Summary:        Tools for managing the osinfo database
License:        LGPL-2.1+ and GPL-2.0+
Group:          System/Management
Url:            https://releases.pagure.org/libosinfo/
Source:         https://releases.pagure.org/libosinfo/%{name}-%{version}.tar.xz
Patch1:         001-Make-xmlError-structs-constant.patch
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel
BuildRequires:  libarchive-devel
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  libxml2-devel >= 2.6.0
BuildRequires:  libxslt-devel >= 1.0.0
BuildRequires:  meson
#BuildRequires:  perl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package provides tools for managing the osinfo database of
information about operating systems for use with virtualization

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%doc NEWS README
%{_bindir}/osinfo-db-export
%{_bindir}/osinfo-db-import
%{_bindir}/osinfo-db-path
%{_bindir}/osinfo-db-validate
%{_mandir}/man1/osinfo-db-export.1*
%{_mandir}/man1/osinfo-db-import.1*
%{_mandir}/man1/osinfo-db-path.1*
%{_mandir}/man1/osinfo-db-validate.1*

%changelog
