#
# spec file for package breeze6-gtk
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


%define kf6_version 6.2.0

# Full Plasma 6 version (e.g. 6.0.0)
%{!?_plasma6_bugfix: %define _plasma6_bugfix %{version}}
# Latest ABI-stable Plasma (e.g. 6.0 in KF6, but 6.0.80 in KUF)
%{!?_plasma6_version: %define _plasma6_version %(echo %{_plasma6_bugfix} | awk -F. '{print $1"."$2}')}
%define rname breeze-gtk

# Use the latest python on factory
%define pythons %{primary_python}
# Only defined for Leap 15
%{?sle15_python_module_pythons}

%bcond_without released
Name:           breeze6-gtk
Version:        6.1.2
Release:        0
Summary:        GTK+ theme matching KDE's Breeze
License:        LGPL-2.1-only
URL:            https://www.kde.org
Source:         https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz
%if %{with released}
Source1:        https://download.kde.org/stable/plasma/%{version}/%{rname}-%{version}.tar.xz.sig
Source2:        plasma.keyring
%endif
BuildRequires:  %{python_module pycairo}
BuildRequires:  breeze6-style >= %{_plasma6_bugfix}
BuildRequires:  fdupes
BuildRequires:  kf6-extra-cmake-modules >= %{kf6_version}
BuildRequires:  sassc
BuildRequires:  cmake(Breeze) >= %{_plasma6_bugfix}
BuildRequires:  cmake(Qt6CoreTools)

%description
A GTK+ theme created to match with the Plasma 6 Breeze theme.

%package -n metatheme-breeze6-common
Summary:        GTK+ theme matching KDE's Breeze -- Common Files
# Default cursor theme
Recommends:     breeze6-cursors
Suggests:       gtk2-metatheme-breeze6
Suggests:       gtk3-metatheme-breeze6
Suggests:       gtk4-metatheme-breeze6
Provides:       metatheme-breeze-common = %{version}
Obsoletes:      metatheme-breeze-common < %{version}
Provides:       breeze-gtk = %{version}
Obsoletes:      breeze-gtk < %{version}

%description -n metatheme-breeze6-common
A GTK+ theme created to match with the Plasma 6 Breeze theme.

%package -n gtk2-metatheme-breeze6
Summary:        GTK+ theme matching KDE's Breeze -- GTK+ 2 Support
Requires:       metatheme-breeze6-common = %{version}
Supplements:    (breeze4-style and gtk2)
Supplements:    (breeze5-style and gtk2)
Supplements:    (breeze6-style and gtk2)
Provides:       gtk2-metatheme-breeze = %{version}
Obsoletes:      gtk2-metatheme-breeze < %{version}
BuildArch:      noarch

%description -n gtk2-metatheme-breeze6
A GTK+ theme created to match with the Plasma 6 Breeze theme.

%package -n gtk3-metatheme-breeze6
Summary:        GTK+ theme matching KDE's Breeze -- GTK+ 3 Support
Requires:       metatheme-breeze6-common = %{version}
Supplements:    (breeze4-style and gtk3)
Supplements:    (breeze5-style and gtk3)
Supplements:    (breeze6-style and gtk3)
Provides:       gtk3-metatheme-breeze = %{version}
Obsoletes:      gtk3-metatheme-breeze < %{version}
BuildArch:      noarch

%description -n gtk3-metatheme-breeze6
A GTK+ theme created to match with the Plasma 6 Breeze theme.

%package -n gtk4-metatheme-breeze6
Summary:        GTK+ theme matching KDE's Breeze -- GTK+ 4 Support
Requires:       metatheme-breeze6-common = %{version}
Supplements:    (breeze4-style and gtk4)
Supplements:    (breeze5-style and gtk4)
Supplements:    (breeze6-style and gtk4)
Provides:       gtk4-metatheme-breeze = %{version}
Obsoletes:      gtk4-metatheme-breeze < %{version}
BuildArch:      noarch

%description -n gtk4-metatheme-breeze6
A GTK+ theme created to match with the Plasma 6 Breeze theme.

%prep
%autosetup -p1 -n %{rname}-%{version}

%build
%cmake_kf6

%kf6_build

%install
%kf6_install

%fdupes %{buildroot}%{_kf6_sharedir}

%files -n metatheme-breeze6-common
%license LICENSES/*
%doc README.md
%{_datadir}/themes/Breeze*/
%exclude %{_datadir}/themes/Breeze*/gtk-*/
%dir %{_kf6_sharedir}/themes/Breeze*/assets/

%files -n gtk2-metatheme-breeze6
%{_datadir}/themes/Breeze*/gtk-2.0/

%files -n gtk3-metatheme-breeze6
%{_datadir}/themes/Breeze*/gtk-3.*/

%files -n gtk4-metatheme-breeze6
%{_datadir}/themes/Breeze*/gtk-4.*/

%changelog
