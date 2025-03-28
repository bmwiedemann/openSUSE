#
# spec file for package gnome-shell-extension-customize-ibus
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2022 Hollow Man
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


%global uuid customize-ibus@hollowman.ml
%global forgeurl https://github.com/openSUSE/Customize-IBus
Name:           gnome-shell-extension-customize-ibus
Version:        91
Release:        0
Summary:        IBus customization extension for GNOME Shell
License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/refs/tags/v%{version}.tar.gz#/Customize-IBus-%{version}.tar.gz
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  make
Requires:       gnome-shell
Requires:       gnome-tweaks
BuildArch:      noarch

%description
This GNOME shell extension customizes the appearance and behavior of the IBus
input framework, including its system tray. It also implements an input source
indicator.

%prep
%setup -q -n Customize-IBus-%{version}

%build
%make_build _build VERSION=%{version}

%install
mkdir -p %{buildroot}/%{_datadir}/gnome-shell/extensions
mv _build %{buildroot}%{_datadir}/gnome-shell/extensions/%{uuid}
%find_lang customize-ibus

%files -f customize-ibus.lang
%license LICENSE
%doc README.md
%dir %{_datadir}/gnome-shell
%dir %{_datadir}/gnome-shell/extensions
%{_datadir}/gnome-shell/extensions/%{uuid}/

%changelog
