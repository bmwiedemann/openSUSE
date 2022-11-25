#
# spec file for package budgie-backgrounds
#
# Copyright (c) 2022 SUSE LLC
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

Name:           budgie-backgrounds
Version:        0.1+9
Release:        0
Summary:        The default background set for the Budgie Desktop
License:        CC0-1.0
Group:          System/GUI/Other
URL:            https://github.com/BuddiesOfBudgie/budgie-backgrounds
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  meson
BuildRequires:  ImageMagick
BuildRequires:  jhead
BuildArch:      noarch

%description
Budgie Backgrounds is the default set of background images for the Budgie Desktop.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%dir %{_datadir}/backgrounds
%{_datadir}/backgrounds/budgie
%dir %{_datadir}/gnome-background-properties
%{_datadir}/gnome-background-properties/budgie-backgrounds.xml

%changelog
