#
# spec file for package macrofusion
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           macrofusion
Version:        0.7.4
Release:        0
Summary:        GUI to combine photos to get deeper DOF or HDR
License:        GPL-3.0-only
Group:          Productivity/Graphics/Other
Url:            http://sourceforge.net/projects/macrofusion/
Source:         https://sourceforge.net/projects/macrofusion/files/%{name}-%{version}/%{name}_%{version}.orig.tar.gz
Patch0:         frombytes.patch
BuildRequires:  update-desktop-files
Requires:       enblend-enfuse >= 4.0
Requires:       hugin
Requires:       python3-Pillow
Requires:       python3-cairo
Requires:       python3-gobject-Gdk
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
MacroFusion is a neat little GUI for great tool Enfuse
(command line) It makes easy fusion few photos to one with great
DOF (Depth of Field) or DR (Dynamic Range)
It can be useful for enthusiasts of landscape or macro imagery.

MacroFusion is a fork of EnfuseGui of Chez Gholyo and has been
rebranded to avoid conflict with another EnfuseGui (for MacOS).

%prep
%setup -q
%patch0
sed -e '/Exec/s/macrofusion/macrofusion\.py/' \
    -i %{name}.desktop
# fixes the shebang line
sed -e 's/env //' -i macrofusion.py

%build

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/mfusion
install -d -m 755 %{buildroot}%{_datadir}/applications
install -d -m 755 %{buildroot}%{_datadir}/pixmaps
install -d -m 755 %{buildroot}%{_datadir}/mfusion/images
install -d -m 755 %{buildroot}%{_datadir}/mfusion/ui
install -d -m 755 %{buildroot}%{_datadir}/mfusion/locale
install -d -m 755 %{buildroot}%{_datadir}/mfusion/locale/fr
install -d -m 755 %{buildroot}%{_datadir}/mfusion/locale/pl
install -d -m 755 %{buildroot}%{_datadir}/mfusion/locale/ru
# files
install -m 644 %{name}.desktop %{buildroot}%{_datadir}/applications/
install -m 755 %{name}.py %{buildroot}%{_bindir}/
install -m 644 ./images/logoSplash.png %{buildroot}%{_datadir}/mfusion/images/
install -m 644 ./images/%{name}.png %{buildroot}%{_datadir}/pixmaps/
install -m 644 ui/progress.xml ui/ui.xml -t %{buildroot}%{_datadir}/mfusion/ui
%if 0%{?suse_version} >= 1140
%desktop_database_post
%endif
%suse_update_desktop_file -n -i %{name}

if (update-desktop-database -v &> /dev/null); then
    update-desktop-database > /dev/null
fi

%files
%defattr(-,root,root)
%doc CHANGELOG LICENSE README TODO
# files should be path to installed files
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_bindir}/%{name}.py
%{_datadir}/mfusion/images/logoSplash.png
%{_datadir}/mfusion/ui/progress.xml
%{_datadir}/mfusion/ui/ui.xml
%dir %{_datadir}/mfusion/
%dir %{_datadir}/mfusion/locale/
%dir %{_datadir}/mfusion/locale/fr/
%dir %{_datadir}/mfusion/locale/pl/
%dir %{_datadir}/mfusion/locale/ru/
%dir %{_datadir}/mfusion/images/
%dir %{_datadir}/mfusion/ui/

%changelog
