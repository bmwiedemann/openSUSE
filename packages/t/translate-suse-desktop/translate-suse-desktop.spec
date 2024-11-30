#
# spec file for package translate-suse-desktop
#
# Copyright (c) 2024 SUSE LLC
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


Name:           translate-suse-desktop
Version:        0.20241115.cac1c69
Release:        0
Summary:        A Build Tool to Provide Desktop Translation
License:        GPL-3.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/suse-desktop-translations
Source:         suse-desktop-translations-%{version}.tar.xz
Source1:        translate_suse_desktop.macro
Source2:        translate_suse_desktop.sh
Requires:       intltool
BuildArch:      noarch

%description
This package provides a tool that will import translations for SUSE
specific desktop files.

For more, see
https://en.opensuse.org/openSUSE:Packaging_Conventions_RPM_Macros#%translate_suse_desktop

%prep
%setup -q -n suse-desktop-translations-%{version}
cp -a %{SOURCE1} %{SOURCE2} .

%build

%install
for PO in po/*.po ; do
	install -m0644 -D $PO $RPM_BUILD_ROOT%{_datadir}/%{name}/${PO##*/}
done
install -m0755 -D translate_suse_desktop.sh $RPM_BUILD_ROOT%{_rpmconfigdir}/translate_suse_desktop.sh
install -m0644 -D translate_suse_desktop.macro $RPM_BUILD_ROOT%{_rpmmacrodir}/macros.translate_suse_desktop

%files
%defattr(-,root,root)
%{_datadir}/%{name}
%{_rpmconfigdir}/*
%{_rpmmacrodir}/*

%changelog
