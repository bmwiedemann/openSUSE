#
# spec file for package mate-icon-theme-faenza
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _version 1.20
Name:           mate-icon-theme-faenza
Version:        1.20.0
Release:        0
Summary:        MATE Desktop Faenza compilation theme
License:        GPL-3.0-only
Group:          System/GUI/Other
Url:            https://mate-desktop.org/
Source:         http://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  mate-common >= %{_version}
BuildArch:      noarch

%description
This icon theme uses Faenza and Faience icon themes by ~Tiheum and
some icons customised for MATE by Rowen Stipe. Also, there are some
icons from Mint-X-F and Faenza-Fresh icon packs.

%package dark
Summary:        MATE Desktop faenza compilation theme, dark variant
Group:          System/GUI/Other
Requires:       %{name} = %{version}

%description dark
This icon theme uses Faenza and Faience icon themes by ~Tiheum and
some icons customised for MATE by Rowen Stipe. Also, there are some
icons from Mint-X-F and Faenza-Fresh icon packs.

%package gray
Summary:        MATE Desktop faenza compilation theme, grey variant
Group:          System/GUI/Other
Requires:       %{name} = %{version}

%description gray
This icon theme uses Faenza and Faience icon themes by ~Tiheum and
some icons customised for MATE by Rowen Stipe. Also, there are some
icons from Mint-X-F and Faenza-Fresh icon packs.

%prep
%setup -q

%build
NOCONFIGURE=1 mate-autogen
%configure

%install
%make_install

%fdupes %{buildroot}%{_datadir}/icons/matefaenza/
%fdupes %{buildroot}%{_datadir}/icons/matefaenzadark/
%fdupes %{buildroot}%{_datadir}/icons/matefaenzagray/
%icon_theme_cache_create_ghost matefaenza
%icon_theme_cache_create_ghost matefaenzadark
%icon_theme_cache_create_ghost matefaenzagray

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post matefaenza

%postun
%icon_theme_cache_postun matefaenza

%post dark
%icon_theme_cache_post matefaenzadark

%postun dark
%icon_theme_cache_postun matefaenzadark

%post gray
%icon_theme_cache_post matefaenzagray

%postun gray
%icon_theme_cache_postun matefaenzagray
%endif

%files
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%doc NEWS README
%{_datadir}/icons/matefaenza/
%ghost %{_datadir}/icons/matefaenza/icon-theme.cache

%files dark
%{_datadir}/icons/matefaenzadark/
%ghost %{_datadir}/icons/matefaenzadark/icon-theme.cache

%files gray
%{_datadir}/icons/matefaenzagray/
%ghost %{_datadir}/icons/matefaenzagray/icon-theme.cache

%changelog
