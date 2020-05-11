#
# spec file for package scite
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2012-2017 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


%define tar_ver 433
Name:           scite
Version:        4.3.3
Release:        0
Summary:        Source Code Editor based on Scintilla
License:        MIT
URL:            https://www.scintilla.org/SciTE.html
Source0:        http://download.sourceforge.net/scintilla/%{name}%{tar_ver}.tgz
Source1:        %{name}.changes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gail-3.0)
BuildRequires:  pkgconfig(gdk-3.0)
BuildRequires:  pkgconfig(gdk-broadway-3.0)
BuildRequires:  pkgconfig(gdk-wayland-3.0)
BuildRequires:  pkgconfig(gdk-x11-3.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-broadway-3.0)
BuildRequires:  pkgconfig(gtk+-unix-print-3.0)
BuildRequires:  pkgconfig(gtk+-wayland-3.0)
BuildRequires:  pkgconfig(gtk+-x11-3.0)

%description
SciTE is a SCIntilla based Text Editor. Originally built to demonstrate
Scintilla, it has grown to be a generally useful editor with facilities for
building and running programs.

%prep
%setup -q -c

%build
export CXXFLAGS='%{optflags}'
export CFLAGS='%{optflags}'
%make_build GTK3=1 -C scintilla/gtk
%make_build GTK3=1 -C scite/gtk

%install
make GTK3=1 DESTDIR=%{buildroot} -C scite/gtk install
# Add the man page
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 scite/doc/scite.1 %{buildroot}%{_mandir}/man1/SciTE.1
%suse_update_desktop_file -r SciTE GTK Development Utility Building TextEditor

%files
%license scite/License.txt
%doc scite/README
%{_bindir}/SciTE
%{_datadir}/scite/
%{_datadir}/pixmaps/Sci48M.png
%{_datadir}/applications/SciTE.desktop
%{_mandir}/man1/SciTE.1%{?ext_man}

%changelog
