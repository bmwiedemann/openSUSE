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


Name:           hicolor-icon-theme
Version:        0.17
Release:        0
Summary:        Fallback Icon Theme
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
URL:            https://freedesktop.org/wiki/Software/icon-theme/
Source:         http://icon-theme.freedesktop.org/releases/%{name}-%{version}.tar.xz
Source1:        macros.hicolor
Source99:       %{name}-rpmlintrc
BuildArch:      noarch

%description
This is the default fallback theme used by implementations of the icon
theme specification.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
touch %{buildroot}%{_datadir}/icons/hicolor/icon-theme.cache
chmod -x COPYING
# Install rpm macros
install -D -m644 %{SOURCE1} %{buildroot}%_rpmmacrodir/macros.hicolor
# Add 1024x1024 directory for package ownership [default-icon-theme#3]
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/1024x1024/{actions,\
animations,apps,categories,devices,emblems,emotes,filesystems,\
intl,mimetypes,places,status,stock}

%files
%license COPYING
%doc ChangeLog README
%ghost %{_datadir}/icons/hicolor/icon-theme.cache
%{_datadir}/icons/hicolor/
%_rpmmacrodir/macros.hicolor

%changelog
