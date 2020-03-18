#
# spec file for package bless
#
# Copyright (c) 2020 SUSE LLC.
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
Version:        0.6.2
Release:        0
Summary:        Gtk#-based Hex-editor written in C#
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://github.com/afrantzis/bless
Source:         https://github.com/afrantzis/bless/archive/v%{version}/%{name}-%{version}.tar.gz
#PATCH-FIX-UPSTREAM jbicha@debian.org - build without scrollkeeper/rarian
Patch0:         dont-require-rarian.patch
#PATCH-FIX-UPSTREAM Fix building error CS0104: 'Range' is an ambiguous reference
Patch1:         bless-0.6.2-Range-ambiguous-reference.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glade-sharp-2.0)
BuildRequires:  pkgconfig(gtk-sharp-2.0)
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
%patch -p1
%patch1 -p1
./autogen.sh
# Fix Build for Mono 4.0
sed -i 's/gmcs/mcs/' configure builder/ModuleBuilder.cs
#autoreconf -fi

%build
%configure --without-scrollkeeper
sed -i 's/$(MKDIR_P)/mkdir -p/' po/Makefile
%make_build

%install
%make_install
%suse_update_desktop_file -r bless Utility TextEditor
rm %{buildroot}%{_datadir}/doc/bless/INSTALL
%fdupes %{buildroot}%{_datadir}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/bless
%{_libdir}/bless
%{_datadir}/applications/bless.desktop
%{_datadir}/bless
%{_datadir}/pixmaps/*

%files doc
%{_datadir}/doc/bless/
%{_datadir}/doc/bless/user/
%{_datadir}/doc/bless/user/figures/

%changelog
