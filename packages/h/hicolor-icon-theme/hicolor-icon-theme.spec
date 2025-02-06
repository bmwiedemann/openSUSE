#
# spec file for package hicolor-icon-theme
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

%define hicolor_dir_list {{actions,\
animations,apps,categories,devices,emblems,emotes,filesystems,\
intl,mimetypes,places,status,\
stock,stock/chart,stock/code,stock/data,stock/form,\
stock/image,stock/io,stock/media,stock/navigation,\
stock/net,stock/object,stock/table,stock/text}} %{nil}

Name:           hicolor-icon-theme
Version:        0.18
Release:        0
Summary:        Fallback Icon Theme
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
URL:            https://freedesktop.org/wiki/Software/icon-theme/
Source0:        https://icon-theme.freedesktop.org/releases/%{name}-%{version}.tar.xz
Source1:        macros.hicolor
Source99:       %{name}-rpmlintrc
BuildRequires:  meson
BuildArch:      noarch

%description
This is the default fallback theme used by implementations of the icon
theme specification.

%package devel
Summary:        Development files for hicolor-icon-theme
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}

%description devel
A package containing the development files for hicolor-icon-theme
Currently, there is only a pkgconfig file

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install
touch %{buildroot}%{_datadir}/icons/hicolor/icon-theme.cache
chmod -x COPYING
# Install rpm macros
install -D -m644 %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.hicolor
# Add 1024x1024 (+HiDPI) directory for package ownership [default-icon-theme#3]
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/{1024x1024,1024x1024@2}/%{hicolor_dir_list}
# Make symbolic reflect scalable
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/symbolic/%{hicolor_dir_list}

%files
%license COPYING
%doc NEWS README.md
%ghost %{_datadir}/icons/hicolor/icon-theme.cache
%{_datadir}/icons/hicolor/
%{_rpmmacrodir}/macros.hicolor

%files devel
%{_datadir}/pkgconfig/default-icon-theme.pc

%changelog
