#
# spec file for package imageburner
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           imageburner
Version:        1.0.2
Release:        0
Summary:        Image burner
License:        GPL-3.0-or-later
Group:          Hardware/Other
URL:            https://github.com/artemanufrij/imageburner
Source:         https://github.com/artemanufrij/imageburner/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
Recommends:     %{name}-lang

%description
An image burner, written especially for Elementary OS.

%lang_package

%prep
%setup -q

mv debian/copyright COPYING

%build
%meson
%meson_build

%install
%meson_install
%suse_update_desktop_file -r com.github.artemanufrij.imageburner GTK System Utility Archiving
%find_lang com.github.artemanufrij.imageburner %{name}.lang
%fdupes %{buildroot}/%{_datadir}

%files
%license COPYING
%doc README.md
%{_bindir}/com.github.artemanufrij.imageburner
%{_datadir}/applications/com.github.artemanufrij.imageburner.desktop
%{_datadir}/icons/hicolor/*/*/com.github.artemanufrij.imageburner.??g
%{_datadir}/metainfo/com.github.artemanufrij.imageburner.appdata.xml
%{_datadir}/contractor/

%files lang -f %{name}.lang

%changelog
