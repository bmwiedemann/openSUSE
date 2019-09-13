#
# spec file for package mate-icon-theme
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


%define _version 1.23
Name:           mate-icon-theme
Version:        1.23.1
Release:        0
Summary:        MATE icon theme
License:        LGPL-3.0-only AND CC-BY-3.0
Group:          System/GUI/Other
URL:            https://mate-desktop.org/
Source:         http://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  icon-naming-utils >= 0.8.7
# set to %{version} when mate-common has an equal release
BuildRequires:  mate-common >= 1.22
BuildRequires:  pkgconfig
Provides:       mate-icon-theme-devel = %{version}
BuildArch:      noarch

%description
This package contains the default icon theme used by the MATE desktop.
The icons are used in the panel menu, and in nautilus and other
applications, to represent the different applications, files,
directories, and devices.

%prep
%setup -q

%build
NOCONFIGURE=1 mate-autogen
%configure
make %{?_smp_mflags} V=1

%install
%make_install
%fdupes %{buildroot}%{_datadir}/icons/mate/
%fdupes %{buildroot}%{_datadir}/icons/menta/

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post mate
%icon_theme_cache_post menta

# No need for %%icon_theme_cache_postun in %%postun since the theme won't exist anymore.
%endif

%files
%license COPYING
%doc AUTHORS NEWS
%{_datadir}/icons/mate/
%ghost %{_datadir}/icons/mate/icon-theme.cache
%{_datadir}/icons/menta/
%ghost %{_datadir}/icons/menta/icon-theme.cache

%changelog
