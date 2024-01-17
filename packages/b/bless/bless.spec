#
# spec file for package bless
#
# Copyright (c) 2022 SUSE LLC
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


Name:           bless
Version:        0.6.3
Release:        0
Summary:        Gtk#-based Hex-editor written in C#
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://github.com/afrantzis/bless
Source:         https://github.com/afrantzis/bless/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  itstool
BuildRequires:  meson >= 0.46
BuildRequires:  nunit-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glade-sharp-2.0) >= 2.8
BuildRequires:  pkgconfig(gtk-sharp-2.0) >= 2.8
BuildRequires:  pkgconfig(mono)

%description
Bless is a hex editor written in Mono/Gtk#. It features:

* Efficient editing of large data files and block devices.
* Multilevel undo - redo operations.
* Customizable data views.
* Multiple tabs.
* A data conversion table.
* Advanced copy/paste capabilities.
* Highlighting of selection pattern matches in the file.
* Plugin-based architecture.
* Export of data to text and HTML (others with plugins).
* Bitwise operations on data.

%package doc
Summary:        Documentation for Bless
Group:          Development/Tools/Other

%description doc
Bless is a hex editor.

This package contains the documentation.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%check
#System.InvalidCastException:
#%%meson_test

%files
%license COPYING
%doc AUTHORS NEWS README
%{_bindir}/bless
%{_libdir}/bless
%{_datadir}/applications/bless.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/bless

%files doc
%doc %{_datadir}/help/C/%{name}/

%changelog
