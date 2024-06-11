#
# spec file for package caja-rename
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


%define pythons python3
# Compatibility with *SUSE 15.
%if 0%{?suse_version} && 0%{?suse_version} < 1550
%define python_compileall \
%{python_expand for d in %{buildroot}%{$python_sitelib} %{buildroot}%{$python_sitearch}; do \
  if [ -d $d ]; then \
    find $d -name '*.pyc' -delete; \
    $python -m compileall $d; \
    $python -O -m compileall $d; \
  fi; \
done \
} \
%{nil}
%endif
%define _name   cajarename
%define _version 1.28
Name:           caja-rename
Version:        24.5.1
Release:        0
Summary:        Batch renaming extension for Caja
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/tari01/caja-rename
Source0:        https://github.com/tari01/caja-rename/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM caja-rename-pre-glib2-74-compat.patch Gracefully continue when building against glib-2.0 << 2.74.0.
Patch0:         caja-rename-pre-glib2-74-compat.patch
# PATCH-FIX-UPSTREAM caja-rename-pre-glib2-76-compat.patch Gracefully continue when building against glib-2.0 << 2.76.0.
Patch1:         caja-rename-pre-glib2-76-compat.patch
BuildRequires:  %{python_module polib}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cmake
BuildRequires:  cmake-extras
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  hicolor-icon-theme
# For directory owning.
# Note that we cannot use python_module here. The package doesn't provide a
# python3-caja virtual.
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libcaja-extension)
Requires:       caja

%description
An extension for the Caja file browser allowing users to rename
multiple files/folders in a single pass.

The application can change the case, insert, replace and delete
strings, as well as enumerate the selection. Any changes are
instantly visible in the preview list. The user interface strives
to be as simple as possible, without confusing advanced
operations.

%package -n caja-extension-rename
Summary:        Rename extension for Caja
Group:          Productivity/File utilities
Requires:       %{name} = %{version}
Requires:       caja >= %{_version}

%description -n caja-extension-rename
An extension for the Caja file browser allowing users to rename
multiple files/folders in a single pass.

The application can change the case, insert, replace and delete
strings, as well as enumerate the selection. Any changes are
instantly visible in the preview list. The user interface strives
to be as simple as possible, without confusing advanced
operations.

%lang_package

%prep
%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%find_lang %{name}

%files
%license COPYING
%doc README.md
%{_datadir}/icons/hicolor/*/apps/%{name}.svg

%files -n caja-extension-rename
%{_libdir}/caja/extensions-2.0/lib%{name}.so
%{_datadir}/caja/extensions/lib%{name}.caja-extension

%files lang -f %{name}.lang

%changelog
