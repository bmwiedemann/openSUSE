#
# spec file for package terminology
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


%define e_branding_package %(rpm -q --qf '%%{name}' --whatprovides enlightenment-branding)
%if 0%{?suse_version} && 0%{?is_opensuse}
%define e_branding_version %(rpm -q --qf '%%{version}' %{e_branding_package})
%else
%define e_branding_version 0.1
%endif
Name:           terminology
Version:        1.13.0
Release:        0
Summary:        EFL based terminal emulator
License:        BSD-2-Clause AND OFL-1.1
Group:          System/X11/Terminals
URL:            https://enlightenment.org
Source:         https://download.enlightenment.org/rel/apps/terminology/%{name}-%{version}.tar.xz
Patch0:         fix-desktop.patch
# Creates a "Flat" colorscheme so we can ship the "Default" from branding packages
Patch1:         feature-flat-colorscheme.patch
BuildRequires:  ImageMagick
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson >= 0.40.1
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ecore)
BuildRequires:  pkgconfig(ecore-evas)
BuildRequires:  pkgconfig(ecore-file)
BuildRequires:  pkgconfig(ecore-imf)
BuildRequires:  pkgconfig(ecore-imf-evas)
BuildRequires:  pkgconfig(ecore-input)
BuildRequires:  pkgconfig(ecore-ipc)
BuildRequires:  pkgconfig(edje)
BuildRequires:  pkgconfig(eet)
BuildRequires:  pkgconfig(efreet)
BuildRequires:  pkgconfig(eina)
BuildRequires:  pkgconfig(elementary) >= 1.8.0
BuildRequires:  pkgconfig(emotion)
BuildRequires:  pkgconfig(ethumb_client)
BuildRequires:  pkgconfig(evas)
Requires:       efl
Requires:       elementary >= 1.8.0
# provides default.edj
Requires:       terminology-theme-dft
Recommends:     %{name}-lang
Conflicts:      evas-generic-loaders < 1.8.0
%if 0%{?suse_version}
Recommends:     evas-generic-loaders >= 1.8.0
Recommends:     terminology-theme-Flat
Recommends:     terminology-theme-dark
Recommends:     terminology-theme-misc
Recommends:     terminology-theme-openSUSE
Recommends:     terminology-theme-openSUSE-oliveleaf
%endif
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%if 0%{?is_opensuse}
BuildRequires:  enlightenment-branding-openSUSE
%endif
%endif

%description
Fast and lightweight terminal emulator using EFL libraries.

%package theme-upstream
Summary:        Default Enlightenment theme
Group:          System/X11/Terminals
Conflicts:      otherproviders(terminology-theme-dft)
Provides:       terminology-theme = %{e_branding_version}
Provides:       terminology-theme-dft

%description  theme-upstream
For use with upstream branding, when using openSUSE themes, when using
openSUSE themes.

Use the Dark theme instead.

%package theme-Flat
Summary:        Default terminology theme(Flat)
Group:          System/X11/Terminals
Provides:       terminology-theme

%description  theme-Flat
The default theme for terminology install when using openSUSE branding.

%package theme-misc
Summary:        Miscellaneous terminology themes
Group:          System/X11/Terminals
Provides:       terminology-theme

%description  theme-misc
Miscellaneous themes provided by the terminology devs, includes Solarized,
Mild and Black themes.

%lang_package

%prep
%autosetup -p1

%build
export ECORE_NO_SYSTEM_MODULES=1
export CFLAGS="%{optflags} %{?mageia:-g}"
%meson
%meson_build

%install
%meson_install

sed -i 's/.png[[:blank:]]*$//' %{buildroot}%{_datadir}/applications/%{name}.desktop

# make 2 copys of default for branding
cp %{buildroot}%{_datadir}/%{name}/themes/default.edj %{buildroot}%{_datadir}/%{name}/themes/Flat.edj
# Colorscheme done with a patch

%find_lang %{name}
%if 0%{?suse_version}
%suse_update_desktop_file -r %{name} Enlightenment System TerminalEmulator
%fdupes %{buildroot}/%{_datadir}
%endif

%if 0%{?suse_version} < 1320
%post
%icon_theme_cache_post
%desktop_database_post

%postun
%icon_theme_cache_postun
%desktop_database_postun
%endif

%{?suse_version:%files}
%{!?suse_version:%files -f %{name}.lang}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README*
%{_bindir}/%{name}
%{_bindir}/ty*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%{_mandir}/man?/terminology*.?z
%{_mandir}/man?/ty*.?z
%exclude %{_datadir}/%{name}/themes/*
%exclude %{_datadir}/%{name}/colorschemes/*

%files theme-upstream
%{_datadir}/%{name}/themes/default.edj
%{_datadir}/%{name}/colorschemes/Default.eet

%files theme-Flat
%{_datadir}/%{name}/themes/Flat.edj
%{_datadir}/%{name}/colorschemes/Flat.eet

%files theme-misc
%{_datadir}/%{name}/themes/*
%exclude %{_datadir}/%{name}/themes/Flat.edj
%exclude %{_datadir}/%{name}/themes/default.edj

%{?suse_version:%files lang -f %{name}.lang}

%changelog
