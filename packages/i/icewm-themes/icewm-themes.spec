#
# spec file for package icewm-themes
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


%define ICEWMDIR %{_datadir}/icewm
Name:           icewm-themes
Version:        0.1
Release:        0
Summary:        Themes for the IceWM Window Manager
License:        LGPL-2.1+
Group:          System/GUI/Other
Url:            http://icewm.themes.org/
Source:         icewm-themes.tar.bz2
Requires:       icewm
BuildArch:      noarch

%description
This package contains a collection of themes for the popular IceWM
window manager. Most of them have been taken from the original 0.9.42
themes package. Others have been taken from http://icewm.themes.org.

%install
mkdir -p %{buildroot}%{ICEWMDIR}
tar jxvf %{SOURCE0} -C %{buildroot}%{ICEWMDIR}
find %{buildroot}%{ICEWMDIR} -type f -exec chmod 644 {} \;
find %{buildroot}%{ICEWMDIR} -type d -exec chmod 755 {} \;
find %{buildroot}%{ICEWMDIR} -type f -name "*~" | xargs -r rm -v
# moved to main icewm as a default theme
rm -rf %{buildroot}%{ICEWMDIR}/themes/Helix

%files
%dir %{ICEWMDIR}
%{ICEWMDIR}/themes

%changelog
