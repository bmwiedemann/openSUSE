#
# spec file for package mint-themes
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


%define _name   mint
Name:           mint-themes
Version:        2.0.7
Release:        0
Summary:        Mint Themes
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/linuxmint/mint-themes
Source:         http://packages.linuxmint.com/pool/main/m/mint-themes/%{name}_%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  python3
BuildRequires:  rubygem(sass)
BuildArch:      noarch

%description
A collection of Mint GTK+ themes.

%package -n metatheme-%{_name}-common
Summary:        Mint Themes -- Common Files
Group:          System/GUI/Other
Recommends:     mint-x-icon-theme
Recommends:     mint-y-icon-theme
Suggests:       gtk2-metatheme-%{_name}
Suggests:       gtk3-metatheme-%{_name}
Provides:       %{_name}-themes = %{version}
Obsoletes:      %{_name}-themes < %{version}
# cinnamon-themes was last used in openSUSE Leap 42.3.
Provides:       cinnamon-themes = 2018.02.08
Obsoletes:      cinnamon-themes < 2018.02.08

%description -n metatheme-%{_name}-common
A collection of Mint GTK+ themes.

%package -n gtk2-metatheme-%{_name}
Summary:        Mint Themes -- GTK+ 2 Support
Group:          System/GUI/Other
Requires:       gtk2-engine-murrine
Requires:       metatheme-%{_name}-common = %{version}
Supplements:    packageand(metatheme-%{_name}-common:gtk2)

%description -n gtk2-metatheme-%{_name}
A collection of Mint GTK+ themes.

%package -n gtk3-metatheme-%{_name}
Summary:        Mint Themes -- GTK+ 3 Support
Group:          System/GUI/Other
Requires:       metatheme-%{_name}-common
Supplements:    packageand(metatheme-%{_name}-common:gtk3)
Provides:       %{_name}-themes-gtk3 = %{version}
Obsoletes:      %{_name}-themes-gtk3 < %{version}

%description -n gtk3-metatheme-%{_name}
A collection of Mint GTK+ themes.

%prep
%setup -q -n %{name}

%build
make %{?_smp_mflags} V=1

%install
mkdir -p %{buildroot}%{_datadir}/
cp -a .%{_datadir}/themes/ %{buildroot}%{_datadir}/themes/

%fdupes %{buildroot}%{_datadir}/themes/

%files -n metatheme-%{_name}-common
%license debian/copyright
%doc debian/changelog
%{_datadir}/themes/Mint*/
%exclude %{_datadir}/themes/Mint*/gtk-?.0/
"%{_datadir}/themes/Linux Mint/"

%files -n gtk2-metatheme-%{_name}
%{_datadir}/themes/Mint*/gtk-2.0/

%files -n gtk3-metatheme-%{_name}
%{_datadir}/themes/Mint*/gtk-3.0/

%changelog
