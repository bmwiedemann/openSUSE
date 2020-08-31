#
# spec file for package ddrescueview
#
# Copyright (c) 2020 SUSE LLC
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


%define         upstream_version_1  0.4%%20alpha%%203
%define         upstream_version_2  0.4%%7Ealpha3
Name:           ddrescueview
Version:        0.4~alpha3
Release:        0
Summary:        Graphical viewer for GNU ddrescue mapfiles
License:        GPL-3.0-only
Group:          Productivity/Archiving/Backup
URL:            https://sourceforge.net/projects/ddrescueview/
Source:         https://sourceforge.net/projects/ddrescueview/files/Test%%20builds/v%{upstream_version_1}/ddrescueview-source-%{upstream_version_2}.tar.xz/download#/%{name}-%{version}.tar.xz
Source1:        %{name}.desktop
# PATCH-FIX-UPSTREAM use-getters-for-fields-in-other-classes.patch -- fixes compilation
Patch0:         https://sourceforge.net/p/ddrescueview/tickets/_discuss/thread/bdbe07cc95/5526/attachment/use-getters-for-fields-in-other-classes.patch
# PATCH-FIX-OPENSUSE pie.patch -- use PIE for linking
Patch1:         pie.patch
BuildRequires:  gtk2-devel
BuildRequires:  lazarus
BuildRequires:  libQt5Pas-devel
BuildRequires:  update-desktop-files

%description
This small tool allows the user to graphically examine ddrescue's map files in a user friendly GUI application. The Main window displays a block grid with each block's color representing the block types it contains. Many people know this type of view from defragmentation programs.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1
chmod -x *.txt

%build
lazbuild \
	--lazarusdir=%{_libdir}/lazarus \
%ifarch x86_64
	--cpu=x86_64 \
%endif
	--widgetset=qt5 \
	-B source/ddrescueview.lpi \
	&& [ -f source/ddrescueview ]
sed -i 's/\r//' *.txt

%install
install -Dm 755 source/ddrescueview %{buildroot}%{_bindir}/%{name}
install -Dm 644 resources/linux/ddrescueview.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -Dm 644 resources/linux/ddrescueview.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm
install -Dm 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license gpl.txt
%doc readme.txt changelog.txt
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm

%changelog
