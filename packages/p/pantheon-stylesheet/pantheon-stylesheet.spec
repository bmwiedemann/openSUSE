#
# spec file for package pantheon-stylesheet
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


%define         appid io.elementary.stylesheet
Name:           pantheon-stylesheet
Version:        8.1.0
Release:        0
Summary:        The Elementary GTK theme
License:        GPL-3.0-or-later
URL:            https://github.com/elementary/stylesheet
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  sassc
BuildArch:      noarch
Provides:       elementary-theme = %{version}
Obsoletes:      elementary-theme < %{version}

%description
The official Granite theme for the Pantheon Desktop, designed to be smooth,
attractive, fast, and usable.

%prep
%autosetup -n stylesheet-%{version}

%build
%meson
%meson_build

%install
%meson_install
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc CONTRIBUTING.md README.md
%{_datadir}/themes/%{appid}.{banana,blueberry,bubblegum,cocoa,grape,lime,mint,orange,slate,strawberry}
%{_datadir}/metainfo/%{appid}.appdata.xml

%changelog
