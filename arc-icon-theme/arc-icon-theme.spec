#
# spec file for package arc-icon-theme
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           arc-icon-theme
Version:        20161122
Release:        0
Summary:        Arc Icon Theme
License:        GPL-3.0+
Group:          System/GUI/Other
Url:            https://github.com/horst3180/arc-icon-theme
Source:         https://github.com/horst3180/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  icon-naming-utils >= 0.8.7
Requires:       adwaita-icon-theme
Recommends:     moka-icon-theme
BuildArch:      noarch

%description
A flat icon theme that mainly includes icons for directories and
mimetypes.
Requires Moka or Adwaita as fallback icons.

%prep
%setup -q

%build
NOCONFIGURE=1 ./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install

%fdupes %{buildroot}%{_datadir}/icons/Arc/

%post
%icon_theme_cache_post Arc

# No need for %%icon_theme_cache_postun in %%postun since the theme won't exist anymore.

%files
%defattr(-,root,root)
%doc COPYING CREDITS README.md
%{_datadir}/icons/Arc/
%ghost %{_datadir}/icons/Arc/icon-theme.cache

%changelog
