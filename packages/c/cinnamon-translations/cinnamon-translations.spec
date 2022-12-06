#
# spec file for package cinnamon-translations
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


%define _version 5.0.0
Name:           cinnamon-translations
Version:        5.6.0
Release:        0
Summary:        Translation files for the Cinnamon desktop
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/linuxmint/cinnamon-translations
Source:         https://github.com/linuxmint/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  filesystem
BuildArch:      noarch

%description
The package contains the translation files for the Cinnamon packages.

%package -n cinnamon-lang
Summary:        Translations for package cinnamon
Group:          System/Localization
Requires:       cinnamon >= %{_version}
Supplements:    cinnamon
Provides:       cinnamon-lang-all = %{version}
Obsoletes:      cinnamon-translations < %{version}
BuildArch:      noarch

%description -n cinnamon-lang
Provides translations for the "cinnamon" package.

%package -n cinnamon-control-center-lang
Summary:        Translations for package cinnamon-control-center
Group:          System/Localization
Requires:       cinnamon-control-center >= %{_version}
Supplements:    cinnamon-control-center
Provides:       cinnamon-control-center-lang-all = %{version}
Obsoletes:      cinnamon-translations < %{version}
BuildArch:      noarch

%description -n cinnamon-control-center-lang
Provides translations for the "cinnamon-control-center" package.

%package -n cinnamon-screensaver-lang
Summary:        Translations for package cinnamon-screensaver
Group:          System/Localization
Requires:       cinnamon-screensaver >= %{_version}
Supplements:    cinnamon-screensaver
Provides:       cinnamon-screensaver-lang-all = %{version}
Obsoletes:      cinnamon-translations < %{version}
BuildArch:      noarch

%description -n cinnamon-screensaver-lang
Provides translations for the "cinnamon-screensaver" package.

%package -n cinnamon-session-lang
Summary:        Translations for package cinnamon-session
Group:          System/Localization
Requires:       cinnamon-session >= %{_version}
Supplements:    cinnamon-session
Provides:       cinnamon-session-lang-all = %{version}
Obsoletes:      cinnamon-translations < %{version}
BuildArch:      noarch

%description -n cinnamon-session-lang
Provides translations for the "cinnamon-session" package.

%package -n cinnamon-settings-daemon-lang
Summary:        Translations for package cinnamon-settings-daemon
Group:          System/Localization
Requires:       cinnamon-settings-daemon >= %{_version}
Supplements:    cinnamon-settings-daemon
Provides:       cinnamon-settings-daemon-lang-all = %{version}
Obsoletes:      cinnamon-translations < %{version}
BuildArch:      noarch

%description -n cinnamon-settings-daemon-lang
Provides translations for the "cinnamon-settings-daemon" package.

%package -n nemo-lang
Summary:        Translations for package nemo
Group:          System/Localization
Requires:       nemo >= %{_version}
Supplements:    nemo
Provides:       nemo-lang-all = %{version}
Obsoletes:      cinnamon-translations < %{version}
BuildArch:      noarch

%description -n nemo-lang
Provides translations for the "nemo" package.

%package -n nemo-extensions-lang
Summary:        Translations for nemo-extensions packages
Group:          System/Localization
Suggests:       nemo-extension-audio-tab >= %{_version}
Suggests:       nemo-extension-compare >= %{_version}
Suggests:       nemo-extension-emblems >= %{_version}
Suggests:       nemo-extension-file-roller >= %{_version}
Suggests:       nemo-extension-gtkhash >= %{_version}
Suggests:       nemo-extension-image-converter >= %{_version}
Suggests:       nemo-extension-pastebin >= %{_version}
Suggests:       nemo-extension-preview >= %{_version}
Suggests:       nemo-extension-repairer >= %{_version}
Suggests:       nemo-extension-seahorse >= %{_version}
Suggests:       nemo-extension-share >= %{_version}
Supplements:    nemo-extension-audio-tab
Supplements:    nemo-extension-compare
Supplements:    nemo-extension-emblems
Supplements:    nemo-extension-file-roller
Supplements:    nemo-extension-gtkhash
Supplements:    nemo-extension-image-converter
Supplements:    nemo-extension-pastebin
Supplements:    nemo-extension-preview
Supplements:    nemo-extension-repairer
Supplements:    nemo-extension-seahorse
Supplements:    nemo-extension-share
Provides:       nemo-extensions-lang-all = %{version}
Obsoletes:      cinnamon-translations < %{version}
# nemo-extension-compare-lang was last used in openSUSE Leap 42.3.
Provides:       nemo-extension-compare-lang = %{version}
Obsoletes:      nemo-extension-compare-lang < %{version}
# nemo-extension-emblems-lang was last used in openSUSE Leap 42.3.
Provides:       nemo-extension-emblems-lang = %{version}
Obsoletes:      nemo-extension-emblems-lang < %{version}
# nemo-extension-gtkhash-lang was last used in openSUSE Leap 42.3.
Provides:       nemo-extension-gtkhash-lang = %{version}
Obsoletes:      nemo-extension-gtkhash-lang < %{version}
# nemo-extension-image-converter-lang was last used in openSUSE Leap 42.3.
Provides:       nemo-extension-image-converter-lang = %{version}
Obsoletes:      nemo-extension-image-converter-lang < %{version}
# nemo-extension-pastebin-lang was last used in openSUSE Leap 42.3.
Provides:       nemo-extension-pastebin-lang = %{version}
Obsoletes:      nemo-extension-pastebin-lang < %{version}
# nemo-extension-preview-lang was last used in openSUSE Leap 42.3.
Provides:       nemo-extension-preview-lang = %{version}
Obsoletes:      nemo-extension-preview-lang < %{version}
# nemo-extension-repairer-lang was last used in openSUSE Leap 42.3.
Provides:       nemo-extension-repairer-lang = %{version}
Obsoletes:      nemo-extension-repairer-lang < %{version}
# nemo-extension-seahorse-lang was last used in openSUSE Leap 42.3.
Provides:       nemo-extension-seahorse-lang = %{version}
Obsoletes:      nemo-extension-seahorse-lang < %{version}
# nemo-extension-share-lang was last used in openSUSE Leap 42.3.
Provides:       nemo-extension-share-lang = %{version}
Obsoletes:      nemo-extension-share-lang < %{version}
BuildArch:      noarch

%description -n nemo-extensions-lang
Provides translations for the nemo-extensions packages.

%prep
%setup -q

%build
make buildmo %{?_smp_mflags} V=1

%install
mkdir -p %{buildroot}%{_datadir}/locale/
# Only get locales that are present in openSUSE.
ls %{_datadir}/locale/ | while read lang; do
    if [ -d .%{_datadir}/locale/$lang/ ]; then
        cp -a .%{_datadir}/locale/$lang/ %{buildroot}%{_datadir}/locale/
    fi
done

%find_lang cinnamon
%find_lang cinnamon-control-center
%find_lang cinnamon-screensaver
%find_lang cinnamon-session
%find_lang cinnamon-settings-daemon
%find_lang nemo
%find_lang nemo-extensions

%files -n cinnamon-lang -f cinnamon.lang
%license COPYING
%doc debian/changelog README.md

%files -n cinnamon-control-center-lang -f cinnamon-control-center.lang

%files -n cinnamon-screensaver-lang -f cinnamon-screensaver.lang

%files -n cinnamon-session-lang -f cinnamon-session.lang

%files -n cinnamon-settings-daemon-lang -f cinnamon-settings-daemon.lang

%files -n nemo-lang -f nemo.lang

%files -n nemo-extensions-lang -f nemo-extensions.lang

%changelog
