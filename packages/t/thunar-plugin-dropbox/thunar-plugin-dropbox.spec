#
# spec file for package thunar-plugin-dropbox
#
# Copyright (c) 2020 SUSE LLC
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


%define thunar_version 1.2.0
%define plugin_name thunar-dropbox
Name:           thunar-plugin-dropbox
Version:        0.3.1
Release:        0
Summary:        Thunar Plugin That Adds Context-menu Items from Dropbox
License:        GPL-3.0-only
Group:          System/GUI/XFCE
URL:            https://github.com/Jeinzi/thunar-dropbox
Source0:        https://github.com/Jeinzi/%{plugin_name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
# not pkgconfig(thunarx-[23]), because we don't know in advance
BuildRequires:  thunar-devel
BuildRequires:  pkgconfig(gio-2.0)
Requires:       dropbox
Requires:       thunar >= %{thunar_version}
Provides:       %{plugin_name} = %{version}

%description
Thunar Dropbox is a plugin for thunar that adds context-menu items from
dropbox. This plugin does not come with dropbox itself, you will need
to install that separately.

%prep
%setup -q -n %{plugin_name}-%{version}

%build
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
%make_build

%install
cd build
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_datadir}/icons/hicolor/*/*/%{plugin_name}.png
%dir %{_prefix}/lib/thunarx-?
%{_prefix}/lib/thunarx-?/%{plugin_name}.so

%changelog
