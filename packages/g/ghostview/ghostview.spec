#
# spec file for package ghostview
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ghostview
Version:        1.5
Release:        0
Summary:        Ghostview
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/PS
Url:            http://pages.cs.wisc.edu/~ghost/gv/index.htm
Source:         ghostview-1.5.tar.bz2
Source1:        ghostview.desktop
Source2:        ghostview.png
Patch:          ghostview-1.5.dif
Patch1:         ghostview-1.5-ad.dif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  imake
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xmu)
BuildRequires:  pkgconfig(xt)
Provides:       ghstview
Provides:       gsview
Obsoletes:      gsview
Requires:       ghostscript_x11
Conflicts:      gs_serv gs_vga
%define _x11data    %{_datadir}/X11
%define _appdefdir  %{_x11data}/app-defaults

%description
Ghostview offers an X11 GUI for viewing PostScript files. This is an
X11 interface to ghostscript.

%prep
%setup -q
%patch
%patch1

%build
xmkmf -a
make CCOPTIONS="%{optflags}" %{?_smp_mflags}

%install
make install     DESTDIR=%{buildroot}
make install.man DESTDIR=%{buildroot}
%suse_update_desktop_file -i ghostview Office Viewer

%files
%defattr(-,root,root)
/usr/share/applications/ghostview.desktop
/usr/share/pixmaps/ghostview.png
%{_bindir}/ghostview
%dir %{_appdefdir}
%config %{_appdefdir}/Ghostview
%doc %{_mandir}/man1/ghostview.1x.gz

%changelog
