#
# spec file for package fcitx-table-other
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           fcitx-table-other
Version:        0.2.4
Release:        0
Summary:        A fork of ibus-table-others for Fcitx
License:        GPL-3.0+
Group:          System/I18n/Chinese
Url:            https://github.com/fcitx/fcitx-table-other
Source:         http://download.fcitx-im.org/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  fcitx-devel >= 4.2.3
BuildRequires:  fcitx-table-tools
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  intltool
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Fcitx-table-other is a fork of ibus-table-others for Fcitx.
provides non-Chinese additional tables.

%package lang 
Summary:        Languages for package %{name} 
License:        GPL-3.0+
Group:          System/Localization 
Requires:       %{name} = %{version}
Provides:       %{name}-lang-all = %{version}
%if 0%{?suse_version}
Supplements:    packageand(bundle-lang-other:%{name}) 
%endif
BuildArch:      noarch 

%description lang 
Provides translations to the package %{name}

%package -n fcitx-table-amharic
Summary:        Amharic table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
Requires:       fcitx-table
Provides:       %{name} = %{version}
BuildArch:      noarch

%description -n fcitx-table-amharic
Fcitx Amharic table.

%package -n fcitx-table-arabic
Summary:        Arabic table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
Requires:       fcitx-table
Provides:       %{name} = %{version}
BuildArch:      noarch

%description -n fcitx-table-arabic
Fcitx Arabic table.

%package -n fcitx-table-cn-cns11643
Summary:        CNS 11643 table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
Requires:       fcitx-table
Provides:       %{name} = %{version}
BuildArch:      noarch

%description -n fcitx-table-cn-cns11643
Fcitx Chinese National Standard 11643 table for Simplified Chinese.

It's also called Chinese Standard Interchange Code.
And it's a superset of ASCII.

See: http://en.wikipedia.org/wiki/CNS_11643 for details.

If you don't know what it is, don't try.
Actually no Chinese use it either.

%package -n fcitx-table-malayalam-compose
Summary:        Malayalam Compose table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
Requires:       fcitx-table
Provides:       %{name} = %{version}
BuildArch:      noarch

%description -n fcitx-table-malayalam-compose
Fcitx Malayalam Compose table.

%package -n fcitx-table-emoji
Summary:        Emoji table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
Requires:       fcitx-table
Provides:       %{name} = %{version}
BuildArch:      noarch

%description -n fcitx-table-emoji
Fcitx Emoji (Emoticons) table.

%package -n fcitx-table-ipa-x-sampa
Summary:        IPA X-Sampa table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
Requires:       fcitx-table
Provides:       %{name} = %{version}
BuildArch:      noarch

%description -n fcitx-table-ipa-x-sampa
Fcitx International Phonetic Alphabet - Extended Speech Assessment Methods Phonetic Alphabet table.

Notice: It's used to input IPA.

%package -n fcitx-table-latex
Summary:        Latex table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
Requires:       fcitx-table
Provides:       %{name} = %{version}
BuildArch:      noarch

%description -n fcitx-table-latex
Fcitx Latex table to input Latex formula and symbols.

%package -n fcitx-table-malayalam-phonetic
Summary:        Malayalam Phonetic table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
Requires:       fcitx-table
Provides:       %{name} = %{version}
BuildArch:      noarch

%description -n fcitx-table-malayalam-phonetic
Fcitx Malayalam Phonetic table.

%package -n fcitx-table-ru-rustrad
Summary:        Traditional Russian table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
Requires:       fcitx-table
Provides:       %{name} = %{version}
BuildArch:      noarch

%description -n fcitx-table-ru-rustrad
Fcitx Traditional Russian table.

%package -n fcitx-table-tamil-remington
Summary:        Tamil Remington tables for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
Requires:       fcitx-table
Provides:       %{name} = %{version}
BuildArch:      noarch

%description -n fcitx-table-tamil-remington
Fcitx Tamil Remington tables 

%package -n fcitx-table-thai
Summary:        Thai table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
Requires:       fcitx-table
Provides:       %{name} = %{version}
BuildArch:      noarch

%description -n fcitx-table-thai
Fcitx Thai table.

%package -n fcitx-table-ru-translit
Summary:        Russian Translit table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
Requires:       fcitx-table
Provides:       %{name} = %{version}
BuildArch:      noarch

%description -n fcitx-table-ru-translit
Fcitx Russian Translit table.

%package -n fcitx-table-ua-translit
Summary:        Ukrainian Translit table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
Requires:       fcitx-table
Provides:       %{name} = %{version}
BuildArch:      noarch

%description -n fcitx-table-ua-translit
Fcitx Ukrainian Translit table.

%package -n fcitx-table-vi-qr
Summary:        Vietnamese Quoted Readable table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
Requires:       fcitx-table
Provides:       %{name} = %{version}
BuildArch:      noarch

%description -n fcitx-table-vi-qr
Fcitx Vietnamese Quoted Readable table.

%package -n fcitx-table-ru-yawerty
Summary:        Russian Yawerty table for Fcitx
License:        SUSE-Public-Domain
Group:          System/I18n/Chinese
Requires:       fcitx-table
Provides:       %{name} = %{version}
BuildArch:      noarch

%description -n fcitx-table-ru-yawerty
Fcitx Russian Yawerty table.

%prep
%setup -q

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DLIB_INSTALL_DIR=%{_libdir} ..
make %{?_smp_mflags}

%install
cd build
make DESTDIR=%{buildroot} install
cd ..

%find_lang %{name}
%if 0%{?suse_version}
%fdupes %{buildroot}
%else
fdupes -n -q -r %{buildroot}
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README COPYING

%files -n fcitx-table-amharic
%defattr(-,root,root)
%dir %{_datadir}/fcitx/table/
%dir %{_datadir}/fcitx/imicon/
%{_datadir}/fcitx/table/amharic.*
%{_datadir}/fcitx/imicon/amharic.png

%files -n fcitx-table-arabic
%defattr(-,root,root)
%dir %{_datadir}/fcitx/table/
%dir %{_datadir}/fcitx/imicon/
%{_datadir}/fcitx/table/arabic.*
%{_datadir}/fcitx/imicon/arabic.png

%files -n fcitx-table-cn-cns11643
%defattr(-,root,root)
%dir %{_datadir}/fcitx/table/
%dir %{_datadir}/fcitx/imicon/
%{_datadir}/fcitx/table/cns11643.*
%{_datadir}/fcitx/imicon/cns11643.png
%{_datadir}/icons/hicolor/*/apps/fcitx-cns11643.png

%files -n fcitx-table-malayalam-compose
%defattr(-,root,root)
%dir %{_datadir}/fcitx/table/
%dir %{_datadir}/fcitx/imicon/
%{_datadir}/fcitx/table/compose.*
%{_datadir}/fcitx/imicon/compose.png
%{_datadir}/icons/hicolor/*/apps/fcitx-compose.png

%files -n fcitx-table-emoji
%defattr(-,root,root)
%dir %{_datadir}/fcitx/table/
%dir %{_datadir}/fcitx/imicon/
%{_datadir}/fcitx/table/emoji.*
%{_datadir}/fcitx/imicon/emoji.png
%{_datadir}/icons/hicolor/*/apps/fcitx-emoji.png

%files -n fcitx-table-ipa-x-sampa
%defattr(-,root,root)
%dir %{_datadir}/fcitx/table/
%dir %{_datadir}/fcitx/imicon/
%{_datadir}/fcitx/table/ipa-x-sampa.*
%{_datadir}/fcitx/imicon/ipa-x-sampa.png
%{_datadir}/icons/hicolor/*/apps/fcitx-ipa-x-sampa.png

%files -n fcitx-table-latex
%defattr(-,root,root)
%dir %{_datadir}/fcitx/table/
%dir %{_datadir}/fcitx/imicon/
%{_datadir}/fcitx/table/latex.*
%{_datadir}/fcitx/imicon/latex.png
%{_datadir}/icons/hicolor/*/apps/fcitx-latex.png

%files -n fcitx-table-malayalam-phonetic
%defattr(-,root,root)
%dir %{_datadir}/fcitx/table/
%dir %{_datadir}/fcitx/imicon/
%{_datadir}/fcitx/table/malayalam-phonetic.*
%{_datadir}/fcitx/imicon/malayalam-phonetic.png
%{_datadir}/icons/hicolor/*/apps/fcitx-malayalam-phonetic.png

%files -n fcitx-table-ru-rustrad
%defattr(-,root,root)
%dir %{_datadir}/fcitx/table/
%dir %{_datadir}/fcitx/imicon/
%{_datadir}/fcitx/table/rustrad.*
%{_datadir}/fcitx/imicon/rustrad.png
%{_datadir}/icons/hicolor/*/apps/fcitx-rustrad.png

%files -n fcitx-table-ru-translit
%defattr(-,root,root)
%dir %{_datadir}/fcitx/table/
%dir %{_datadir}/fcitx/imicon/
%{_datadir}/fcitx/table/translit.*
%{_datadir}/fcitx/imicon/translit.png
%{_datadir}/icons/hicolor/*/apps/fcitx-translit.png

%files -n fcitx-table-ua-translit
%defattr(-,root,root)
%dir %{_datadir}/fcitx/table/
%dir %{_datadir}/fcitx/imicon/
%{_datadir}/fcitx/table/translit-ua.*
%{_datadir}/fcitx/imicon/translit-ua.png
%{_datadir}/icons/hicolor/*/apps/fcitx-translit-ua.png

%files -n fcitx-table-ru-yawerty
%defattr(-,root,root)
%dir %{_datadir}/fcitx/table/
%dir %{_datadir}/fcitx/imicon/
%{_datadir}/fcitx/table/yawerty.*
%{_datadir}/fcitx/imicon/yawerty.png
%{_datadir}/icons/hicolor/*/apps/fcitx-yawerty.png

%files -n fcitx-table-tamil-remington
%defattr(-,root,root)
%dir %{_datadir}/fcitx/table/
%dir %{_datadir}/fcitx/imicon/
%{_datadir}/fcitx/table/tamil-remington.*
%{_datadir}/fcitx/imicon/tamil-remington.png
%{_datadir}/icons/hicolor/*/apps/fcitx-tamil-remington.png

%files -n fcitx-table-thai
%defattr(-,root,root)
%dir %{_datadir}/fcitx/table/
%dir %{_datadir}/fcitx/imicon/
%{_datadir}/fcitx/table/thai.*
%{_datadir}/fcitx/imicon/thai.png
%{_datadir}/icons/hicolor/*/apps/fcitx-thai.png

%files -n fcitx-table-vi-qr
%defattr(-,root,root)
%dir %{_datadir}/fcitx/table/
%dir %{_datadir}/fcitx/imicon/
%{_datadir}/fcitx/table/viqr.*
%{_datadir}/fcitx/imicon/viqr.png
%{_datadir}/icons/hicolor/*/apps/fcitx-viqr.png

%changelog
