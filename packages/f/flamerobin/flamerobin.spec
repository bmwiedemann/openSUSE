#
# spec file for package flamerobin
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


Name:           flamerobin
Version:        0.9.3.1
Release:        0
Summary:        Graphical client for Firebird
License:        MIT AND LGPL-2.1-or-later
Group:          Productivity/Databases/Tools
URL:            http://www.flamerobin.org/
Source0:        https://github.com/mariuz/flamerobin/archive/%{version}.tar.gz
# PATCH-FIX-UPSTREAM flamerobin-desktop-file.patch gh#mariuz/flamerobin#5 badshah400@gmail.com -- Unhardcode icon path in GNU/Linux laucher; patch taken from upstream git
Patch0:         flamerobin-desktop-file.patch
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  icns-utils
BuildRequires:  libfbclient2-devel >= 2.0.0.12748
BuildRequires:  update-desktop-files
BuildRequires:  wxWidgets-devel >= 3.0
Requires(post): update-desktop-files
Requires(postun): update-desktop-files
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FlameRobin is a database administration tool for Firebird DBMS based on wxgtk
toolkit.

%prep
%setup -q
%patch0 -p1

%build
# FIX A TRAILING SEMICOLON ISSUE FOR KEYWORDS TAG IN .desktop FILE
sed -i "s/^Keywords=firebird/Keywords=firebird;/" res/%{name}.desktop

export CFLAGS="%{optflags} -fpermissive"
export CXXFLAGS="$CFLAGS"
%configure
%make_build

%install
%make_install

%suse_update_desktop_file -r %{name} Office Database
rm -rf %{buildroot}%{_datadir}/%{name}/docs

# INSTALL HICOLOR ICONS EXTRACTED FROM ICNS FILE
pushd res
icns2png -x -d 32 flamerobin.icns
for sz in 16 32 48 128
do
  install -Dm0644 flamerobin_${sz}x${sz}x32.png %{buildroot}%{_datadir}/icons/hicolor/${sz}x${sz}/apps/%{name}.png
done
popd
rm %{buildroot}%{_datadir}/pixmaps/*.png

%post
%icon_theme_cache_post
%desktop_database_post

%postun
%icon_theme_cache_postun
%desktop_database_postun

%files
%defattr(-,root,root)
%doc docs/*
%{_mandir}/man1/flamerobin.1*
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png

%changelog
