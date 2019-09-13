#
# spec file for package vegastrike-data
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           vegastrike-data
Version:        0.5.1.r1
Release:        0
Summary:        Data files for Vega Strike
License:        GPL-2.0+
Group:          Amusements/Games/3D/Simulation
Url:            http://vegastrike.sourceforge.net/
# This is the core game data, without music, speech or extra textures
Source0:        http://ufpr.dl.sourceforge.net/project/vegastrike/vegastrike/0.5.1/%{name}-%{version}.tar.bz2
Source2:        vegastrike.desktop
Source3:        Sol.system
# PATCH-FIX-UPSTREAM vegastrike-data-0.5.1.r1-r13368.patch -- fixes a crash with some GPU drivers
Patch0:         vegastrike-data-0.5.1.r1-r13368.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  hicolor-icon-theme
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
BuildArch:      noarch
Requires:       hicolor-icon-theme
Requires:       vegastrike >= %{version}
%if 0%{?suse_version}
Suggests:       vegastrike-music >= 0.5.1.beta1, vegastrike-speech >= %{version}
%endif
Conflicts:      vegastrike-extra < 0.5.1.r1, vegastrike-speech < 0.5.1.r1
ExcludeArch:    %{ix86}

%description
Data files for Vega Strike, a GPL 3D OpenGL Action RPG space sim that allows
a player to trade and bounty hunt.


%prep
%setup -q
%patch0 -p0
# some cleanup
find -name '*~' -delete
find -name '*.orig' -delete
find cockpits -name '#*#' -delete
find -name .cvsignore -delete
find -iname '*.xmesh' -delete
rm -rf modules/builtin
find . -type f -exec chmod -x "{}" "+"
chmod +x units/findunits.py modules/webpageize.py
sed -i 's/\r//g' documentation/mission_howto.txt
# remove the stale included manpages and the .xls abonimation
rm documentation/*.1 documentation/*.xls
cp -f %{SOURCE3} sectors/Sol/.

%build
# nothing to build; data only

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/vegastrike
mkdir -p $RPM_BUILD_ROOT%{_datadir}/vegastrike/documentation
for i in `cat Version.txt` ai animations bases cockpits communications \
         history meshes mission modules movies programs sectors sounds \
         sprites techniques textures units universe \
         *.xml *.csv *.config *.cur New_Game Version.txt ; do
  cp -a $i $RPM_BUILD_ROOT%{_datadir}/vegastrike
done
#ln -s ../doc/%{name}-data-%{version} \
#  $RPM_BUILD_ROOT%{_datadir}/vegastrike/documentation

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 vegastrike.xpm \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps

%if 0%{?suse_version}
# below is the desktop file and icon stuff.
%suse_update_desktop_file -i vegastrike 
%else
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applications
%endif

%if 0%{?suse_version}
%fdupes $RPM_BUILD_ROOT%{_datadir}/vegastrike
%endif

%post
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%postun
touch --no-create %{_datadir}/icons/hicolor || :
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
   %{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :
fi

%files
%defattr(-,root,root,-)
%doc vega-license.txt documentation/*
%{_datadir}/vegastrike
%{_datadir}/icons/hicolor/128x128/apps/vegastrike.xpm
%{_datadir}/applications/vegastrike.desktop

%changelog
