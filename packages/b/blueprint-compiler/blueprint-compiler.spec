#
# spec file for package blueprint-compiler
#
# Copyright (c) 2025 SUSE LLC
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


Name:           blueprint-compiler
Version:        0.16.0
Release:        0
Summary:        A markup language for GTK user interfaces
License:        LGPL-3.0-or-later
URL:            https://gitlab.gnome.org/jwestman/blueprint-compiler
Source:         %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  meson
BuildRequires:  python3-Sphinx
BuildRequires:  python3-gobject
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
Requires:       python3-gobject
BuildArch:      noarch

%description
A markup language for GTK user interface files.

%package devel
Summary:        Development files for blueprint-compiler
Requires:       blueprint-compiler = %{version}

%description devel
A markup language for GTK user interface files.

%prep
%autosetup -n %{name}-v%{version}

%build
%meson \
  -Ddocs=true
%meson_build

%install
%meson_install

sed -i '1s|#!/usr/bin/env |#!/usr/bin/|' %{buildroot}%{_bindir}/blueprint-compiler

#%check
#python3 -m unittest

%files
%license COPYING
%doc README.md NEWS.md
%{_bindir}/blueprint-compiler
%{python_sitelib}/blueprintcompiler

%files devel
%{_datadir}/pkgconfig/blueprint-compiler.pc

%changelog
