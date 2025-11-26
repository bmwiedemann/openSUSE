#
# spec file for package ghostview
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           ghostview
Version:        1.5
Release:        0
Summary:        Ghostview
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/PS
URL:            https://pages.cs.wisc.edu/~ghost/gv/index.htm
Source:         ghostview-1.5.tar.bz2
Source1:        ghostview.desktop
Source2:        ghostview.png
Patch0:         ghostview-1.5.dif
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
Conflicts:      gs_serv
Conflicts:      gs_vga
%define _x11data    %{_datadir}/X11
%define _appdefdir  %{_x11data}/app-defaults

%description
Ghostview offers an X11 GUI for viewing PostScript files. This is an
X11 interface to ghostscript.

%prep
%autosetup -p0

%build
xmkmf -a
make CCOPTIONS="--std=gnu99 %{optflags}" %{?_smp_mflags} \
	MANPATH=%{_mandir} XAPPLOADDIR=%{_appdefdir}

%install
make install     DESTDIR=%{buildroot} \
	MANPATH=%{_mandir} XAPPLOADDIR=%{_appdefdir}
make install.man DESTDIR=%{buildroot} \
	MANPATH=%{_mandir} XAPPLOADDIR=%{_appdefdir}
%suse_update_desktop_file -i ghostview Office Viewer
rm -rf %{buildroot}/etc
rm -rf %{buildroot}/usr/lib/X11

%files
%defattr(-,root,root)
%{_datadir}/applications/ghostview.desktop
%{_datadir}/pixmaps/ghostview.png
%{_bindir}/ghostview
%dir %{_appdefdir}
%config %{_appdefdir}/Ghostview
%doc %{_mandir}/man1/ghostview.1x.gz

%changelog
