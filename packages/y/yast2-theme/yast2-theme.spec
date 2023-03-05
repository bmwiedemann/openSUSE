#
# spec file for package yast2-theme
#
# Copyright (c) 2023 SUSE LLC
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


Name:           yast2-theme
Version:        4.6.0
Release:        0

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools
BuildRequires:  rubygem(%{rb_default_ruby_abi}:yast-rake)
%if 0%{?is_opensuse}
BuildRequires:  breeze5-icons
BuildRequires:  oxygen5-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  yast2-qt-branding
%endif

Requires:       hicolor-icon-theme

%if 0%{?is_opensuse}
# bsc#1105792: firstboot wizard missing branding
Requires:       yast2-qt-branding
Requires:       google-poppins-fonts
%else
# on SLE the qt branding files are included in yast2-them so they
# conflict with the separate package that exists on openSUSE
# (boo#1133415)
Obsoletes:      yast2-qt-branding-openSUSE
Conflicts:      yast2-qt-branding-openSUSE
%endif

# Since yast2-branding is provided by this package, OBS needs some help to bootstrap
#!BuildIgnore:  yast2-branding
Provides:       yast2-branding = %{version}
Provides:       yast2-theme = %{version}
Provides:       yast2_theme = %{version}

Conflicts:      otherproviders(yast2-branding)
Conflicts:      otherproviders(yast2-theme)
Conflicts:      otherproviders(yast2_theme)

Obsoletes:      yast2-branding-openSUSE
Obsoletes:      yast2-theme < %{version}
Obsoletes:      yast2-theme-SLE
Obsoletes:      yast2-theme-openSUSE
Obsoletes:      yast2-theme-openSUSE-Crystal < %{version}

BuildArch:      noarch
Summary:        YaST2 - Theme

# icons/**/pattern-deepin.svg is GPL-3.0,
# pattern-budgie.svg is licensed under CC-BY-SA-4.0
# the rest is GPL-2.0
License:        CC-BY-SA-4.0 AND GPL-2.0-only AND GPL-3.0-only
Group:          System/YaST
URL:            http://github.com/yast/yast-theme

%description
Contains necessary theming resources to use YaST2.

%if 0%{?is_opensuse}
%package oxygen
Summary:        YaST2 - Oxygen icon theme
Group:          System/YaST
Supplements:    (yast2-theme and oxygen5-icon-theme)
PreReq:         yast2-branding = %{version}
Requires:       oxygen5-icon-theme
Provides:       yast2-theme-oxygen = %{version}
Obsoletes:      yast2-theme-openSUSE-Oxygen < %{version}
Obsoletes:      yast2-theme-oxygen < %{version}

%description oxygen
Contains icons in KDE Oxygen style (from KDE Plasma 4).

%package breeze
Summary:        YaST2 - Breeze icon theme
Group:          System/YaST
Supplements:    (yast2-theme and breeze5-icons)
PreReq:         yast2-branding = %{version}
Requires:       breeze5-icons
Provides:       yast2-theme-breeze = %{version}
Obsoletes:      yast2-theme-breeze < %{version}

%description breeze
Contains icons in KDE Breeze style (from KDE Plasma 5).
%endif

%prep
%setup -n %{name}-%{version}

%build
mkdir -p %{buildroot}%{_datadir}/icons/breeze/apps/32
mkdir -p %{buildroot}%{_datadir}/icons/breeze/apps/48
mkdir -p %{buildroot}%{_datadir}/icons/breeze-dark/apps/32
mkdir -p %{buildroot}%{_datadir}/icons/breeze-dark/apps/48
cd icons/breeze/
sh make-symlinks.sh %{buildroot}%{_datadir}/icons/breeze
sh make-symlinks.sh %{buildroot}%{_datadir}/icons/breeze-dark

%install
rake install DESTDIR=%{buildroot}

# Distro specific config (should be moved to distro specific branding packages!)
mkdir -p %{buildroot}/etc/icewm/
%if 0%{?is_opensuse}
mv %{buildroot}%{yast_themedir}/openSUSE %{buildroot}%{yast_themedir}/current
cp theme/openSUSE/wmconfig/* %{buildroot}/etc/icewm/
%else
mv %{buildroot}%{yast_themedir}/SLE %{buildroot}%{yast_themedir}/current
cp theme/SLE/wmconfig/* %{buildroot}/etc/icewm/
# SLE doesn't have those icon themes:
rm -rf %{buildroot}%{yast_icondir}/oxygen
rm -rf %{buildroot}%{yast_icondir}/breeze
rm -rf %{buildroot}%{yast_icondir}/breeze-dark
%endif

# We only need current theme
rm -rf %{buildroot}%{yast_themedir}/SLE %{buildroot}%{yast_themedir}/openSUSE

# Clean out duplicates
%fdupes %{buildroot}%{yast_themedir}
%fdupes %{buildroot}%{yast_icondir}

%pre
# CPIO can't remove links on its own
if test -L %{yast_themedir}/current ; then
  rm %{yast_themedir}/current
fi
# No longer used
if test -L %{yast_themedir}/current/icons ; then
  rm %{yast_themedir}/current/icons
fi

%files
%defattr(-,root,root)
%dir %{yast_themedir}
%{yast_themedir}/current
%config %{_sysconfdir}/icewm
%{yast_icondir}/hicolor/*
%doc %{yast_docdir}
%license COPYING*

%if 0%{?is_opensuse}
%files oxygen
%{yast_icondir}/oxygen/*

%files breeze
%{yast_icondir}/breeze/*
%{yast_icondir}/breeze-dark/*
%endif

%changelog
