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


%define         upstream_version_1  0.4%%20alpha%%204
%define         upstream_version_2  0.4%%7Ealpha4
Name:           ddrescueview
Version:        0.4~alpha4
Release:        0
Summary:        Graphical viewer for GNU ddrescue mapfiles
License:        GPL-3.0-only
Group:          Productivity/Archiving/Backup
URL:            https://sourceforge.net/projects/ddrescueview/
Source:         https://sourceforge.net/projects/ddrescueview/files/Test%%20builds/v%{upstream_version_1}/ddrescueview-source-%{upstream_version_2}.tar.xz/download#/%{name}-%{version}.tar.xz
BuildRequires:  gtk2-devel
BuildRequires:  lazarus
BuildRequires:  libQt5Pas-devel
BuildRequires:  update-desktop-files

%description
This small tool allows the user to graphically examine ddrescue's map files in a user friendly GUI application. The Main window displays a block grid with each block's color representing the block types it contains. Many people know this type of view from defragmentation programs.

%prep
%setup -q -n %name-source-%version
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
install -Dm 644 resources/linux/man/man1/ddrescueview.1 %{buildroot}%{_mandir}/man1/%{name}.1
cp -r resources/linux/icons/ %{buildroot}%{_datadir}/
install -Dm 644 resources/linux/applications/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file %{name}

%files
%license gpl.txt
%doc readme.txt changelog.txt
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/

%changelog
