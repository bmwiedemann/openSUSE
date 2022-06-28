#
# spec file for package ibus-table-others
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


Name:           ibus-table-others
Version:        1.3.13
Release:        0
Summary:        Other non-Chinese tables for ibus
License:        GPL-3.0-or-later
Group:          System/Localization
URL:            https://github.com/moebiuscurve/ibus-table-others
Source:         https://github.com/moebiuscurve/ibus-table-others/releases/download/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gnome-common
BuildRequires:  ibus-table >= 1.9.1
BuildRequires:  pkg-config
BuildRequires:  python3
BuildRequires:  pkgconfig(ibus-table) >= 1.9.1
BuildArch:      noarch

%description
This package contains all other non-Chinese tables for ibus e.g. CNS11643,
Compose, Emoji, Ipx-x-sampa, Latex, Rustrad, Thai, Translit-ua, Translit, Viqr,
Yawerty. This package contains only COPYING and Documents, Please select the
table you want to use.

%package -n ibus-table-latex
Summary:        Latex input method for IBus framework
Group:          System/Localization
Requires:       ibus-table

%description -n ibus-table-latex
ibus-table-latex provides Latex input method on IBus Table under IBus framework.

%package -n ibus-table-cns11643
Summary:        CNS11643 input method for IBus framework
Group:          System/Localization
Requires:       ibus-table

%description -n ibus-table-cns11643
ibus-table-cns11643 provides CNS11643 input method on IBus Table under IBus
framework.

%package -n ibus-table-emoji
Summary:        Emoji input method for IBus framework
Group:          System/Localization
Requires:       ibus-table

%description -n ibus-table-emoji
ibus-table-emoji provides Emoji input method on IBus Table under IBus framework.

%package -n ibus-table-rustrad
Summary:        Rustrad input method for IBus framework
Group:          System/Localization
Provides:       locale(ibus:ru)
Requires:       ibus-table

%description -n ibus-table-rustrad
ibus-table-rustrad provides Rustrad input method on IBus Table under IBus
framework.

%package -n ibus-table-translit
Summary:        Translit input method for IBus framework
Group:          System/Localization
Provides:       locale(ibus:ru)
Requires:       ibus-table

%description -n ibus-table-translit
ibus-table-translit provides Translit input method on IBus Table under IBus
framework.

%package -n ibus-table-translit-ua
Summary:        Translit-ua input method for IBus framework
Group:          System/Localization
Provides:       locale(ibus:uk)
Requires:       ibus-table

%description -n ibus-table-translit-ua
ibus-table-translit-ua provides Translit-ua input method on IBus Table under
IBus framework.

%package -n ibus-table-yawerty
Summary:        Yawerty input method for IBus framework
Group:          System/Localization
Requires:       ibus-table

%description -n ibus-table-yawerty
ibus-table-yawerty provides Yawerty input method on IBus Table under IBus
framework.

%package -n ibus-table-compose
Summary:        The Compose table for ibus-table
Group:          System/Localization
Requires:       ibus-table

%description -n ibus-table-compose
ibus-table-compose provides the Compose table for ibus-table.

%package -n ibus-table-ipa-x-sampa
Summary:        The ipa-x-sampa table for ibus-table
Group:          System/Localization
Requires:       ibus-table

%description -n ibus-table-ipa-x-sampa
ibus-table-ipa-x-sampa provides the ipa-x-sampa table for ibus-table.

%package -n ibus-table-thai
Summary:        The Thai table for ibus-table
Group:          System/Localization
Requires:       ibus-table

%description -n ibus-table-thai
ibus-table-thai provides the Thai table for ibus-table.
ภาษาไทย / Thai

%package -n ibus-table-viqr
Summary:        The Viqr (Vietnamese) table for ibus-table
Group:          System/Localization
Provides:       locale(ibus:vi)
Requires:       ibus-table

%description -n ibus-table-viqr
ibus-table-viqr provides the Viqr (Vietnamese) table for ibus-table. Tiếng Việt
/ Vietnamese

%package -n ibus-table-mathwriter
Summary:        Mathematics symbols table for ibus-table
Group:          System/Localization
Requires:       ibus-table

%description -n ibus-table-mathwriter
The package contains table for writing Unicode mathematics symbols.

%package -n ibus-table-rusle
Summary:        Rusle table for ibus-table
Group:          System/Localization
Requires:       ibus-table

%description -n ibus-table-rusle
ibus-table-rusle provides the Rusle table for ibus-table.

%package -n ibus-table-hu-old-hungarian-rovas
Summary:        Hu old hungarian rovas table for ibus-table
Group:          System/Localization
Requires:       ibus-table

%description -n ibus-table-hu-old-hungarian-rovas
ibus-table-rusle provides the Hu old hungarian rovas table for ibus-table.

%package -n ibus-table-mongol-bichig
Summary:        Mongol Bichig table for ibus-table
Group:          System/Localization
Requires:       ibus-table

%description -n ibus-table-mongol-bichig
ibus-table-mongol-bichig provides the Mongol Bichig table for ibus-table.

%package -n ibus-table-telex
Summary:        Telex table for ibus-table
Group:          System/Localization
Requires:       ibus-table

%description -n ibus-table-telex
ibus-table-telex provides the Vietnamese telex table for ibus-table.

%package -n ibus-table-vni
Summary:        Vni table for ibus-table
Group:          System/Localization
Requires:       ibus-table

%description -n ibus-table-vni
ibus-table-mongol-bichig provides the Vietnamese Vni table for ibus-table.

%prep
%setup

%build
./autogen.sh
%configure
alias python=python3
make %{?jobs:-j%jobs}

%install
make DESTDIR=${RPM_BUILD_ROOT} NO_INDEX=true install

%files
%defattr(-,root,root)
%doc ChangeLog README AUTHORS
%license COPYING

%files -n ibus-table-latex
%{_datadir}/ibus-table/icons/latex*
%{_datadir}/ibus-table/tables/latex*

%files -n ibus-table-cns11643
%{_datadir}/ibus-table/icons/cns11643*
%{_datadir}/ibus-table/tables/cns11643*

%files -n ibus-table-emoji
%{_datadir}/ibus-table/icons/ibus-emoji*
%{_datadir}/ibus-table/tables/emoji*

%files -n ibus-table-rustrad
%{_datadir}/ibus-table/icons/rustrad.png
%{_datadir}/ibus-table/tables/rustrad.db

%files -n ibus-table-translit
%{_datadir}/ibus-table/icons/translit.svg
%{_datadir}/ibus-table/tables/translit.db

%files -n ibus-table-translit-ua
%{_datadir}/ibus-table/icons/translit-ua.svg
%{_datadir}/ibus-table/tables/translit-ua.db

%files -n ibus-table-yawerty
%{_datadir}/ibus-table/icons/yawerty.png
%{_datadir}/ibus-table/tables/yawerty.db

%files -n ibus-table-compose
%{_datadir}/ibus-table/icons/compose.svg
%{_datadir}/ibus-table/tables/compose.db

%files -n ibus-table-ipa-x-sampa
%{_datadir}/ibus-table/icons/ipa-x-sampa.svg
%{_datadir}/ibus-table/tables/ipa-x-sampa.db

%files -n ibus-table-thai
%{_datadir}/ibus-table/icons/thai.png
%{_datadir}/ibus-table/tables/thai.db

%files -n ibus-table-viqr
%{_datadir}/ibus-table/icons/viqr.png
%{_datadir}/ibus-table/tables/viqr.db

%files -n ibus-table-mathwriter
%{_datadir}/ibus-table/icons/mathwriter.png
%{_datadir}/ibus-table/tables/mathwriter-ibus.db

%files -n ibus-table-rusle
%{_datadir}/ibus-table/icons/rusle.png
%{_datadir}/ibus-table/tables/rusle.db

%files -n ibus-table-hu-old-hungarian-rovas
%{_datadir}/ibus-table/icons/hu-old-hungarian-rovas.svg
%{_datadir}/ibus-table/tables/hu-old-hungarian-rovas.db

%files -n ibus-table-mongol-bichig
%{_datadir}/ibus-table/icons/mongol_bichig.svg
%{_datadir}/ibus-table/tables/mongol_bichig.db

%files -n ibus-table-telex
%{_datadir}/ibus-table/icons/telex.png
%{_datadir}/ibus-table/tables/telex.db

%files -n ibus-table-vni
%{_datadir}/ibus-table/icons/vni.png
%{_datadir}/ibus-table/tables/vni.db

%changelog
