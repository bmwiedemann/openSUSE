#
# spec file for package nedit
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           nedit
Version:        5.7
Release:        0
Summary:        A GUI text editor
License:        GPL-2.0+
Group:          Productivity/Text/Editors
Url:            http://sourceforge.net/projects/nedit/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}-src.tar.gz
Source1:        %{name}-icon.png
Source2:        %{name}.desktop
#PATCH-FIX-OPENSUSE Use optflags for build
Patch1:         %{name}-5.5CVS-makefiles.patch
#PATCH-FIX-OPENSUSE Do not use tmpnam
Patch2:         %{name}-5.5CVS-security.patch
#PATCH-FIX-OPENSUSE Change nc to nedit-client to avoid conflict with netcat
Patch3:         %{name}-5.5CVS-nc-manfix.patch
#PATCH-FIX-UPSTREAM Set "Default" visual to avoid crashes
Patch4:         %{name}-5.5-visfix.patch
#PATCH-FIX-OPENSUSE do not use UTF-8 by default, as it is not supported
Patch5:         %{name}-5.5CVS-utf8.patch
#PATCH-FIX-OPENSUSE do not include data and time in binary
Patch6:         %{name}-5.6_builddate_fix.patch
BuildRequires:  bison
BuildRequires:  openmotif-devel
BuildRequires:  update-desktop-files
Requires(post): update-desktop-files
Requires(postun): update-desktop-files

%description
NEdit is a GUI style plain text editor for workstations with the X Window System
and Motif. NEdit provides all of the standard menu, dialog, editing,
mouse support, macro extension language, syntax highlighting,
and a lot other nice features (and extensions for programmers).

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5
%patch6 -p1

%build
make -j1 RPM_OPT_FLAGS="%{optflags}" linux

pushd doc
make -j1 all
popd

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
mv source/nc source/nedit-client
install -s -m 755 source/nedit source/nedit-client %{buildroot}%{_bindir}
install -m 644 doc/nedit.man %{buildroot}%{_mandir}/man1/nedit.1x
mv doc/nc.man doc/nedit-client.man
install -m 644 doc/nedit-client.man %{buildroot}%{_mandir}/man1/nedit-client.1x
mkdir -p %{buildroot}%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_datadir}/applications/
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/applications/
%suse_update_desktop_file %{name} TextEditor

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc doc/nedit.doc README ReleaseNotes
%{_bindir}/nedit
%{_bindir}/nedit-client
%{_mandir}/man1/nedit.1x%{ext_man}
%{_mandir}/man1/nedit-client.1x%{ext_man}
%{_datadir}/applications/nedit.desktop
%{_datadir}/pixmaps/nedit-icon.png

%changelog
