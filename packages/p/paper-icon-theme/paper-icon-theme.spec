#
# spec file for package paper-icon-theme
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2017 Sam Hewitt
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


Name:           paper-icon-theme
Version:        1.5.0+git32.aa3e8af7
Release:        0
Summary:        Paper Icon theme
License:        CC-BY-SA-4.0
Group:          System/GUI/Other
URL:            https://snwh.org/paper
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  icon-naming-utils >= 0.8.7
BuildRequires:  meson
BuildArch:      noarch

%description
Paper is a simple and modern icon theme with Material Design influences.

%prep
%autosetup -p1
find -L . -type l -print -delete
chmod a-x AUTHORS README.md

%build
%meson
%meson_build

%install
%meson_install
%fdupes %{buildroot}%{_datadir}/icons/Paper

%files
%doc AUTHORS README.md
%license LICENSE COPYING
%{_datadir}/icons/Paper
%{_datadir}/icons/Paper-Mono-Dark
%ghost %{_datadir}/icons/Paper/icon-theme.cache
%ghost %{_datadir}/icons/Paper-Mono-Dark/icon-theme.cache

%changelog
