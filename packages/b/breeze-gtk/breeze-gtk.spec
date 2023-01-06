#
# spec file for package breeze-gtk
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

%bcond_without released

%define _name   breeze
Name:           breeze-gtk
Version:        5.26.5
Release:        0
Summary:        GTK+ theme matching KDE's Breeze
License:        LGPL-2.1-only
Group:          System/GUI/KDE
URL:            https://projects.kde.org/breeze-gtk
Source:         https://download.kde.org/stable/plasma/%{version}/breeze-gtk-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/breeze-gtk-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  breeze5-style
BuildRequires:  cmake >= 3.16
BuildRequires:  extra-cmake-modules >= 5.98.0
BuildRequires:  fdupes
BuildRequires:  kf5-filesystem
BuildRequires:  python3-cairo
BuildRequires:  sassc

%description
A GTK+ theme created to match with the new Plasma 5 Breeze theme.

%package -n metatheme-%{_name}-common
Summary:        GTK+ theme matching KDE's Breeze -- Common Files
Group:          System/GUI/KDE
# Default cursor theme
Recommends:     breeze5-cursors
Suggests:       gtk2-metatheme-%{_name}
Suggests:       gtk3-metatheme-%{_name}
Provides:       %{_name}-gtk = %{version}
Obsoletes:      %{_name}-gtk < %{version}

%description -n metatheme-%{_name}-common
A GTK+ theme created to match with the new Plasma 5 Breeze theme.

%package -n gtk2-metatheme-%{_name}
Summary:        GTK+ theme matching KDE's Breeze -- GTK+ 2 Support
Group:          System/GUI/KDE
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    (breeze4-style and gtk2)
Supplements:    (breeze5-style and gtk2)
BuildArch:      noarch

%description -n gtk2-metatheme-%{_name}
A GTK+ theme created to match with the new Plasma 5 Breeze theme.

%package -n gtk3-metatheme-%{_name}
Summary:        GTK+ theme matching KDE's Breeze -- GTK+ 3 Support
Group:          System/GUI/KDE
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    (breeze4-style and gtk3)
Supplements:    (breeze5-style and gtk3)
BuildArch:      noarch

%description -n gtk3-metatheme-%{_name}
A GTK+ theme created to match with the new Plasma 5 Breeze theme.

%prep
%autosetup -p1

%build
%cmake_kf5
%cmake_build

%install
%kf5_makeinstall
%fdupes %{buildroot}%{_datadir}/

%files -n metatheme-%{_name}-common
%license LICENSES/*
%doc README.md
%{_datadir}/themes/Breeze*/
%exclude %{_datadir}/themes/Breeze*/gtk-*/
%dir %{_kf5_sharedir}/themes/Breeze*/assets/

%files -n gtk2-metatheme-%{_name}
%{_datadir}/themes/Breeze*/gtk-2.0/

%files -n gtk3-metatheme-%{_name}
%{_datadir}/themes/Breeze*/gtk-3.*/

%changelog
