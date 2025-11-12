#
# spec file for package mate-user-guide
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

Name:           mate-user-guide
Version:        1.28.0
Release:        0
Summary:        User guide for the MATE desktop
License:        GFDL-1.1-or-later
Group:          Documentation/HTML
URL:            https://mate-desktop.org/
Source:         https://pub.mate-desktop.org/releases/%{_version}/%{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  mate-common >= %{_version}
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(glib-2.0)
Requires:       yelp
Recommends:     %{name}-lang
BuildArch:      noarch

%description
This package contains documentation targeted for end-users of
MATE Desktop Environment with general MATE applicability.

%lang_package

%prep
%autosetup -p1

%build
%if %{pkg_vcmp gettext-devel >= 0.24.1}
export ACLOCAL_PATH=/usr/share/gettext/m4/
%endif
NOCONFIGURE=1 mate-autogen
%configure
%make_build

%install
%make_install
%find_lang %{name} %{?no_lang_C}

%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc AUTHORS NEWS README
%{_datadir}/applications/%{name}.desktop
%doc %{_datadir}/help/C/%{name}/

%files lang -f %{name}.lang

%changelog
