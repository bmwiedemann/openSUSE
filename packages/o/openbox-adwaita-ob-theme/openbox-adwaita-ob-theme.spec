#
# spec file for package openbox-adwaita-ob-theme
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           openbox-adwaita-ob-theme
Version:        0.1
Release:        0
Summary:        Adwaita theme for the Openbox Window Manager
License:        GPL-3.0
Group:          System/GUI/Other
Url:            http://box-look.org/
Source:         openbox-adwaita-ob-theme.tar.xz
Requires:       openbox
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package contains an Openbox theme created to mimic GNOME's Adwaita theme.

%define THEMESDIR %{_datadir}/themes

%prep

%build

%install
mkdir -p %{buildroot}%{THEMESDIR}
tar -x --xz -f %{SOURCE0} -C %{buildroot}%{THEMESDIR}
find %{buildroot}%{THEMESDIR} -type f -exec chmod 644 {} \;
find %{buildroot}%{THEMESDIR} -type d -exec chmod 755 {} \;

%files
%defattr(-, root, root)
%{THEMESDIR}/Adwaita-ob

%changelog
