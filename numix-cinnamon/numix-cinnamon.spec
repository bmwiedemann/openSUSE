#
# spec file for package numix-cinnamon
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


%define _theme  Numix
%define _name   numix
%define _version 2.8--v3.0
%define __version 2.8-v3.0
Name:           numix-cinnamon
Version:        3.0
Release:        0
Summary:        Numix Cinnamon theme
License:        AGPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/zagortenay333/numix-cinnamon
Source:         https://github.com/zagortenay333/%{name}/archive/v%{_version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  metatheme-%{_name}-common
BuildArch:      noarch

%description
Numix is a modern flat theme with a combination of light and dark
elements.
This package adds Cinnamon support for Numix.

%package -n cinnamon-metatheme-%{_name}
Summary:        Numix Cinnamon Theme
Group:          System/GUI/Other
Requires:       cinnamon >= 3.0
Requires:       metatheme-%{_name}-common
Supplements:    packageand(metatheme-%{_name}-common:cinnamon)

%description -n cinnamon-metatheme-%{_name}
Numix is a modern flat theme with a combination of light and dark
elements.
This package contains the Cinnamon theme.

%prep
%setup -q -n %{name}-%{__version}

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_datadir}/themes/%{_theme}/
cp -a %{_theme}-Cinnamon/cinnamon/ %{buildroot}%{_datadir}/themes/%{_theme}/

%files -n cinnamon-metatheme-%{_name}
%license LICENSE
%doc CREDITS.md README.md
%{_datadir}/themes/%{_theme}/cinnamon/

%changelog
