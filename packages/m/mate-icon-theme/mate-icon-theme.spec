#
# spec file for package mate-icon-theme
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define _version 1.28

Name:           mate-icon-theme
Version:        1.28.0
Release:        0
Summary:        MATE icon theme
License:        CC-BY-3.0 AND LGPL-3.0-only
Group:          System/X11/Icons
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  icon-naming-utils >= 0.8.7
BuildRequires:  mate-common >= %{_version}
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
%if %{pkg_vcmp gettext-devel >= 0.24.1}
export ACLOCAL_PATH=/usr/share/gettext/m4/
%endif
NOCONFIGURE=1 mate-autogen
%configure
%make_build

%install
%make_install
%fdupes %{buildroot}%{_datadir}/icons

%files
%license COPYING
%doc AUTHORS NEWS
%{_datadir}/icons/mate/
%ghost %{_datadir}/icons/mate/icon-theme.cache
%{_datadir}/icons/menta/
%ghost %{_datadir}/icons/menta/icon-theme.cache

%changelog
