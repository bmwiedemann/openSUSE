#
# spec file for package shared-mime-info
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           shared-mime-info
Version:        1.12
Release:        0
Summary:        Shared MIME Database
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
URL:            https://gitlab.freedesktop.org/xdg/shared-mime-info/
Source0:        %{name}-%{version}.tar.xz
Source1:        macros.shared-mime-info
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  libxml2-devel
# needed for xmllint
BuildRequires:  libxml2-tools
BuildRequires:  translation-update-upstream
# libgio-2_0-0 Requires: shared-mime-info, but this can't exist yet. We explicitly ignore this dependency here.
#!BuildIgnore:  shared-mime-info
# FIXME: use proper Requires(pre/post/preun/...)
PreReq:         libglib-2_0-0
# needed by update-mime-database
PreReq:         libxml2-2
Recommends:     %{name}-lang
Provides:       %{name}-devel = %{version}-%{release}

%description
This package contains:

- The freedesktop.org shared MIME database spec.

- The merged GNOME and KDE databases, in the new format.

- The update-mime-database command, used to install new MIME data.

%lang_package

%prep
%autosetup -p1
translation-update-upstream

%build
NOCONFIGURE=1 ./autogen.sh
%configure \
	--disable-default-make-check \
	%{nil}
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}
# Install rpm macros
install -D -m644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.shared-mime-info

%check
make %{?_smp_mflags} check

%filetriggerin -- %{_datadir}/mime
export PKGSYSTEM_ENABLE_FSYNC=0
%{_bindir}/update-mime-database "%{_datadir}/mime"

%filetriggerpostun -- %{_datadir}/mime
export PKGSYSTEM_ENABLE_FSYNC=0
[ -x %{_bindir}/update-mime-database ] && %{_bindir}/update-mime-database "%{_datadir}/mime"

%files
%license COPYING
%doc NEWS README
%{_bindir}/*
%{_datadir}/mime/packages/*.xml
%{_datadir}/pkgconfig/*.pc
%ghost %{_datadir}/mime/[a-ms-vxX]*
%{_mandir}/man?/*%{ext_man}
%{_rpmmacrodir}/macros.shared-mime-info

%files lang -f %{name}.lang

%changelog
