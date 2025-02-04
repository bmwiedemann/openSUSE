#
# spec file for package bluebird-theme
#
# Copyright (c) 2025 SUSE LLC
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


%define _name Bluebird

Name:           bluebird-theme
Version:        1.3
Release:        0
URL:            https://github.com/shimmerproject/Bluebird
Summary:        A Clean Minimalistic Theme for GNOME, XFCE, GTK+ 2 and 3
License:        CC-BY-SA-3.0 OR GPL-2.0-or-later
Group:          System/GUI/GNOME
Source:         https://github.com/shimmerproject/%{_name}/archive/v%{version}/%{_name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This theme for GTK2/3 and xfwm4/emerald/metacity started out on the basis of
Bluebird, but aims at reworking the intense blue tone to a more neutral
blue-ish look that will be more pleasant to look at in everyday use.

%package -n metatheme-bluebird-common
Summary:        A Clean Minimalistic Theme for GNOME, XFCE, GTK+ 2 and 3 -- Common Files
Group:          System/GUI/GNOME
Suggests:       gtk2-metatheme-bluebird
Suggests:       gtk3-metatheme-bluebird

%description -n metatheme-bluebird-common
The Bluebird theme for GTK2/3 and xfwm4/emerald/metacity started out on the
basis of Bluebird, but aims at reworking the intense blue tone to a more
neutral blue-ish look that will be more pleasant to look at in everyday use.

This package provides the files common to the GTK+ themes and the window
manager themes as well as background images.

%package -n gtk2-metatheme-bluebird
Summary:        A Clean Minimalistic Theme for GNOME, XFCE, GTK+ 2 and 3 -- GTK+ 2 Support
Group:          System/GUI/GNOME
Requires:       gtk2-engine-murrine
Requires:       metatheme-bluebird-common = %{version}
Supplements:    packageand(metatheme-bluebird-common:gtk2)

%description -n gtk2-metatheme-bluebird
The Bluebird Theme for GTK2/3 and xfwm4/emerald/metacity started out on the
basis of Bluebird, but aims at reworking the intense blue tone to a more
neutral blue-ish look that will be more pleasant to look at in everyday use.

This package provides the GTK+ 2 support of Bluebird.

%if 0%{?suse_version} >= 1210
%package -n gtk3-metatheme-bluebird
Summary:        A Clean Minimalistic Theme for GNOME, XFCE, GTK+ 2 and 3 -- GTK+ 3 Support
Group:          System/GUI/GNOME
Requires:       metatheme-bluebird-common = %{version}
Supplements:    packageand(metatheme-bluebird-common:gtk3)

%description -n gtk3-metatheme-bluebird
The Bluebird Theme for GTK2/3 and xfwm4/emerald/metacity started out on the
basis of Bluebird, but aims at reworking the intense blue tone to a more
neutral blue-ish look that will be more pleasant to look at in everyday use.

This package provides the GTK+ 3 support of Bluebird.

%endif

%prep
%autosetup -n %{_name}-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/themes/%{_name}
%if 0%{?suse_version} >= 1210
cp -a gtk-3.0 $RPM_BUILD_ROOT%{_datadir}/themes/%{_name}
%endif
cp -a gtk-2.0 metacity-1 xfwm4 \
    $RPM_BUILD_ROOT%{_datadir}/themes/%{_name}
%fdupes -s $RPM_BUILD_ROOT/%{_datadir}/themes/%{_name}

%files -n metatheme-bluebird-common
%defattr (-, root, root)
%doc README.md
%license LICENSE.CC LICENSE.GPL
%dir %{_datadir}/themes/%{_name}/
%{_datadir}/themes/%{_name}/metacity-1
#%%{_datadir}/themes/%%{_name}/xfce-notify-4.0
%{_datadir}/themes/%{_name}/xfwm4
#%%{_datadir}/themes/%%{_name}/xfwm4_compact
#%%{_datadir}/themes/%%{_name}/Bluebird.emerald

%files -n gtk2-metatheme-bluebird
%defattr (-, root, root)
%{_datadir}/themes/%{_name}/gtk-2.0

%if 0%{?suse_version} >= 1210
%files -n gtk3-metatheme-bluebird
%defattr (-, root, root)
%{_datadir}/themes/%{_name}/gtk-3.0
%endif

%changelog
