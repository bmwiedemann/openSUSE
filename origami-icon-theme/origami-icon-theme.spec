#
# spec file for package origami-icon-theme
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           origami-icon-theme
Version:        1.1.1
Release:        0
Summary:        Origami icon theme for Linux
License:        LGPL-3.0
Group:          System/GUI/Other
Url:            https://github.com/LelCP/origami-icon-theme
Source:         https://github.com/LelCP/origami-icon-theme/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  inkscape
Requires(post): gtk3-tools
BuildArch:      noarch
%if 0%{?suse_version} < 1500
Requires(post): hicolor-icon-theme
Requires(postun): hicolor-icon-theme
%endif

%description
Origami - A free and open source SVG icon theme for Linux systems, based on Paper and Papirus with a few extras like. The theme is available for GTK and KDE.

This package contains the following icon themes:

Origami
Origami Dark

%prep
%setup -q

%build
./yast-fix.sh

%install
%make_install
%fdupes %{buildroot}

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post Origami
%icon_theme_cache_post Origami-dark
%endif

%if 0%{?suse_version} < 1500
%postun
%icon_theme_cache_postun Origami
%icon_theme_cache_postun Origami-dark
%endif

%files
%doc README.md
%license LICENSE
%{_datadir}/icons/Origami
%{_datadir}/icons/Origami-dark

%changelog
