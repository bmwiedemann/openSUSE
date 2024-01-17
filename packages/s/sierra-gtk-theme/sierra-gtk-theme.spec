#
# spec file for package sierra-gtk-theme
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


%define         _name Sierra-gtk-theme
%define         _version 2019-12-16
Name:           sierra-gtk-theme
Version:        20191216
Release:        0
Summary:        MacOS High Sierra like theme for GTK 3, Gnome-Shell and more
License:        GPL-3.0-only
Group:          System/GUI/Other
URL:            https://github.com/vinceliuice/Sierra-gtk-theme
Source:         https://github.com/vinceliuice/Sierra-gtk-theme/archive/%{_version}.tar.gz
BuildRequires:  fdupes
# for gtk2 only
Recommends:     gtk2-engine-murrine
BuildArch:      noarch

%description
MacOS High Sierra like theme for GTK 3, GTK 2, Gnome-Shell, XFWM4 and Unity.

%prep
%setup -q -n %{_name}-%{_version}

%build

%install
mkdir -p %{buildroot}%{_datadir}/themes
./install.sh -d %{buildroot}%{_datadir}/themes
%fdupes %{buildroot}%{_datadir}/themes

%files
%license COPYING
%doc README.md
%{_datadir}/themes/

%changelog
