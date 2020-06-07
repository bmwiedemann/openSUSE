#
# spec file for package equalx
#
# Copyright (c) 2020 SUSE LLC
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


Name:           equalx
Version:        0.7.1
Release:        0
Summary:        Editor for writing and exporting TeX/LaTeX equations
License:        GPL-3.0-or-later
Group:          Productivity/Publishing/TeX/Frontends
URL:            http://equalx.sourceforge.net/
Source0:        http://downloads.sourceforge.net/equalx/%{name}-%{version}.tar.gz
Source1:        %{name}.appdata.xml
# PATCH-FIX-OPENSUSE equalx-fix-desktop-file.patch badshah400@gmail.com -- Fix icon tag in desktop file and categories for compatibility with openSUSE defined ones
Patch0:         equalx-fix-desktop-file.patch
# PATCH-FIX-UPSTREAM equalx-adapt-headers-for-qt5_11.patch badshah400@opensuse.org -- Include additional header files where needed for compilation against Qt 5.11
Patch1:         equalx-adapt-headers-for-qt5_11.patch
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  ghostscript
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkg-config
%if 0%{?suse_version} == 1500 && 0%{?sle_version} == 150100
BuildRequires:  rsvg-view
%else
BuildRequires:  rsvg-convert
%endif
%if 0%{?suse_version} > 1320
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Widgets)
%else
BuildRequires:  libqt4-devel >= 4.8.0
Requires:       libqt4-sql-sqlite
%endif
BuildRequires:  pkgconfig(exempi-2.0)
Requires:       ghostscript
Requires:       poppler-tools
Requires:       texlive-latex
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
EqualX is a helpful graphical interface to LaTeX programs. 
It gives you the power and beauty for writing TeX/LaTeX equations
in a simple to use editor.

Features included:
* Highlight find results in the Equation Preview;
* 3 modes for Refreshing the Preview
* Customise the export commands
* Professional & customisable window layout
* Equation font is computed according to desktop DPI
* Reshaping the Symbols toolbar and Templates toolbar

%prep
%setup -q
%patch0 -p1
%patch1 -p1
sed -i 's/\r$//' LICENSE README

%build
%if 0%{?suse_version} > 1320
qmake-qt5 \
%else
qmake \
%endif
DESTDIR="./bin/" QMAKE_CFLAGS="%optflags" QMAKE_CXXFLAGS="%optflags -fvisibility=hidden -fvisibility-inlines-hidden"
make %{?_smp_mflags}

%install
install -D -p bin/%{name} %{buildroot}%{_bindir}/%{name}

# GENERATE HI-RES APPLICATION ICONS
pushd resources/icons/equalx
for i in 256 512;
do
  rsvg-convert -w ${i} equalx.svg > equalx-${i}x${i}.png
done
popd

# INSTALL RESOURCES DIR
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr resources %{buildroot}%{_datadir}/%{name}/

# LINK ICON FILES TO HICOLOR ICON DIR
for i in 22 24 32 48 64 128 256 512;
do
  mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps
  ln -s %{_datadir}/%{name}/resources/icons/equalx/equalx-${i}x${i}.png \
        %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/equalx.png
done
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
ln -s %{_datadir}/%{name}/resources/icons/equalx/equalx.svg \
      %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/equalx.svg

desktop-file-install resources/%{name}.desktop
# REMOVE UNUSED DESKTOP FILE
rm %{buildroot}%{_datadir}/%{name}/resources/%{name}.desktop

# INSTALL APPDATA
install -Dm0644 %{S:1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

%fdupes %{buildroot}%{_datadir}/%{name}

%if 0%{?suse_version} < 1500
%post
%icon_theme_cache_post
%desktop_database_post

%postun
%icon_theme_cache_postun
%desktop_database_postun
%endif

%files
%defattr(-,root,root)
%doc changelog README THANKS
%license LICENSE
%{_bindir}/%{name}
# OWN THE 512x512 ICON DIR AS HICOLOR THEME DOES NOT PROVIDE IT YET
%dir %{_datadir}/icons/hicolor/512x512
%dir %{_datadir}/icons/hicolor/512x512/apps
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
