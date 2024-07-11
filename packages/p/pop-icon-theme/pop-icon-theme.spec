#
# spec file for package pop-icon-theme
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


Name:           pop-icon-theme
Version:        3.5.0
Release:        0
Summary:        System76 Pop icon theme for Linux
License:        CC-BY-SA-4.0
URL:            https://github.com/pop-os/icon-theme
Source0:        %{name}-%{version}.tar.zst
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  zstd
BuildArch:      noarch
Requires:       adwaita-icon-theme
Requires:       hicolor-icon-theme

%description
Pop_Icons use a semi-flat design with raised 3D motifs to help give depth to
icons. Included in the theme are flat symbolic (single-color) icons as well as
full-color stylized icons.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
%fdupes %{buildroot}

%files
%license LICENSE COPYING
%doc README.md
%{_iconsdir}/Pop

%changelog
