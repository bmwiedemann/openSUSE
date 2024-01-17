#
# spec file for package gtk2-metatheme-gilouche
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


Name:           gtk2-metatheme-gilouche
Version:        11.1.2
Release:        0
Summary:        openSUSE themes and metathemes for gtk2, Xfwm4 and metacity
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
Source:         metatheme-gilouche-%{version}.tar.bz2
Source1:        metacity-theme-greygilouche.tar.bz2
Source2:        metatheme-synchronicity.tar.bz2
Source3:        %{name}-AUTHORS
Source4:        Gilouche-xfwm4.tar.bz2
Source5:        COPYING.Gilouche
BuildRequires:  fdupes
BuildRequires:  gtk2-devel
BuildRequires:  gtk2-engines-devel
BuildRequires:  icon-naming-utils-devel
BuildRequires:  intltool
# Gilouche requires engine "pixmap"
Requires:       gtk2
# Gilouche Synchronicity requires engine "clearlooks"
Requires:       gtk2-engine-clearlooks
# Gilouche icon theme inherits from tango-icon-theme
Requires:       tango-icon-theme
Enhances:       gtk2
Enhances:       metacity
# This replaces many old packages
Provides:       gtk2-theme-openSUSE = 11.1
Obsoletes:      gtk2-theme-openSUSE < 11.1
Provides:       metacity-theme-openSUSE = 11.1
Obsoletes:      metacity-theme-openSUSE < 11.1
Provides:       gtk2-theme-SLED = 11.1
Obsoletes:      gtk2-theme-SLED < 11.1
Provides:       metacity-theme-SLED = 11.1
Obsoletes:      metacity-theme-SLED < 11.1
# Existed for openSUSE <= 10.3, SLE <= 10
Obsoletes:      gnome2-SuSE
BuildArch:      noarch

%description
OpenSUSE themes and metathemes for gtk2, Xfwm4 and metacity contains several
themes in openSUSE look: Gilouche, GreyGilouche and Synchonicity.

%prep
%setup -q -T -a0 -a1 -a2 -a4 -c %{name}-%{version}
cp -a %{SOURCE3} AUTHORS
cp -a %{SOURCE5} COPYING.xfwm4

%build
cd metatheme-gilouche-%{version}
%configure
make %{?_smp_mflags}

%install
install -d %{buildroot}%{_datadir}/themes
install -d Gilouche %{buildroot}%{_datadir}/themes
for DIR in * ; do
    if test $DIR = metatheme-gilouche-%{version} ; then
	continue
    fi
    if test -d $DIR ; then
	cp -a $DIR %{buildroot}%{_datadir}/themes/
    fi
done
cd metatheme-gilouche-%{version}
%make_install
%find_lang metatheme-gilouche
%{icon_theme_cache_create_ghost Gilouche}
%fdupes %{buildroot}%{_datadir}

%post
%icon_theme_cache_post Gilouche

# No need for %%icon_theme_cache_postun in %postun since the theme won't exist anymore

%files -f metatheme-gilouche-%{version}/metatheme-gilouche.lang
%license metatheme-gilouche-%{version}/COPYING COPYING.xfwm4
%doc AUTHORS
%{_datadir}/themes/Gilouche/
%{_datadir}/themes/GreyGilouche/
%{_datadir}/themes/Synchronicity/
%ghost %{_datadir}/icons/Gilouche/icon-theme.cache
%{_datadir}/icons/Gilouche/

%changelog
