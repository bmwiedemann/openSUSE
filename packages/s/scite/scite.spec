#
# spec file for package scite
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2012-2021 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


%define tar_ver 532

Name:           scite
Version:        5.3.2
Release:        0
Summary:        Source Code Editor based on Scintilla
License:        MIT
URL:            https://www.scintilla.org/SciTE.html
Source0:        http://download.sourceforge.net/scintilla/%{name}%{tar_ver}.tgz
# PATCH-FEATURE-OPENSUSE scite-use-system-scintilla.patch badshah400@gmail.com -- Compile against system scintilla library
Patch0:         scite-use-system-scintilla.patch
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  libscintilla-devel >= 5.3.0
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
%autosetup -p1 -c

%build
export CXXFLAGS='%{optflags}'
export CFLAGS='%{optflags}'
%make_build GTK3=1 -C lexilla/src
%make_build GTK3=1 -C scite/gtk

%install
make GTK3=1 DESTDIR=%{buildroot} -C scite/gtk install
# Add the man page
install -d -m 0755 -p %{buildroot}%{_mandir}/man1
install -m 0644 scite/doc/scite.1 %{buildroot}%{_mandir}/man1/SciTE.1
%suse_update_desktop_file -r SciTE GTK Development Utility Building TextEditor
# Needed for non Tumbleweed releases.
%if 0%{?sle_version} && 0%{?sle_version} <= 150300
export NO_BRP_CHECK_RPATH=true
%endif

%files
%license scite/License.txt
%doc scite/README
%{_bindir}/SciTE
%{_datadir}/scite/
%{_datadir}/pixmaps/Sci48M.png
%{_datadir}/applications/SciTE.desktop
%dir %{_prefix}/lib/scite
%{_prefix}/lib/scite/liblexilla.so
%{_mandir}/man1/SciTE.1%{?ext_man}

%changelog
