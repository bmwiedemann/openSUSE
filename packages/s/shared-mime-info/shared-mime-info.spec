#
# spec file for package shared-mime-info
#
# Copyright (c) 2023 SUSE LLC
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


%global __requires_exclude ^/usr/bin/pkg-config$
Name:           shared-mime-info
Version:        2.2
Release:        0
Summary:        Shared MIME Database
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
URL:            https://gitlab.freedesktop.org/xdg/shared-mime-info
Source0:        https://gitlab.freedesktop.org/xdg/shared-mime-info/-/archive/%{version}/%{name}-%{version}.tar.bz2
Source1:        macros.shared-mime-info
BuildRequires:  glib2-devel
BuildRequires:  libxml2-devel
# needed for xmllint
BuildRequires:  libxml2-tools
BuildRequires:  meson
BuildRequires:  xmlto
# libgio-2_0-0 Requires: shared-mime-info, but this can't exist yet. We explicitly ignore this dependency here.
#!BuildIgnore:  shared-mime-info
# needed by update-mime-database
Provides:       %{name}-devel = %{version}-%{release}

%description
This package contains:

- The freedesktop.org shared MIME database spec.

- The merged GNOME and KDE databases, in the new format.

- The update-mime-database command, used to install new MIME data.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
# Install rpm macros
install -D -m644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.shared-mime-info

%check
%meson_test

%filetriggerin -- %{_datadir}/mime
export PKGSYSTEM_ENABLE_FSYNC=0
%{_bindir}/update-mime-database "%{_datadir}/mime"

%filetriggerpostun -- %{_datadir}/mime
export PKGSYSTEM_ENABLE_FSYNC=0
[ -x %{_bindir}/update-mime-database ] && %{_bindir}/update-mime-database "%{_datadir}/mime"

%files
%license COPYING
%doc NEWS README.md
%{_bindir}/*
%{_datadir}/mime/packages/*.xml
%{_datadir}/pkgconfig/*.pc
%{_datadir}/gettext/its/shared-mime-info.*
%{_mandir}/man?/*%{ext_man}
%{_rpmmacrodir}/macros.shared-mime-info

%files lang -f %{name}.lang

%changelog
