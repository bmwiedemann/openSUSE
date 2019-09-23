#
# spec file for package catfish
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_with git
%define series 1.4
Name:           catfish
Version:        1.4.10
Release:        0
Summary:        Versatile File Searching Tool
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
URL:            https://docs.xfce.org/apps/catfish/start
Source:         https://archive.xfce.org/src/apps/%{name}/%{series}/%{name}-%{version}.tar.bz2
BuildRequires:  appstream-glib
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  python3-distutils-extra
BuildRequires:  rsvg-view
BuildRequires:  update-desktop-files
# Needed for typelib() - Requires.
BuildRequires:  gobject-introspection
# Checking module dependencies...
BuildRequires:  gtk3-devel >= 3.16
BuildRequires:  python3-gobject
BuildRequires:  python3-gobject-Gdk
BuildRequires:  python3-pexpect
BuildRequires:  python3-xml
# BuildRequires:  zeitgeist
# ...OK
Requires:       findutils-locate
Requires:       gdk-pixbuf-loader-rsvg
Requires:       gsettings-backend-dconf
Requires:       python3-cairo
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-gobject-cairo
Requires:       python3-pexpect
Requires:       python3-xml
Requires:       sudo
Suggests:       zeitgeist
Recommends:     %{name}-lang
BuildArch:      noarch

%description
Catfish is a GTK+ search utility written in python. Its search is powered by
/usr/bin/find and /usr/bin/locate, with search suggestions provided by
zeitgeist.

%lang_package

%prep
%setup -q

%build
python3 ./setup.py build -g

%install
python3 ./setup.py install -O1 \
    --prefix="%{_prefix}" \
    --root="%{buildroot}"
rm -rf %{buildroot}%{_datadir}/doc/%{name}
# Fix: non-executable-script
pushd %{buildroot}
for _file in $(grep -rl '^\#\!\/'); do
  find -name ${_file##*/} -type f -not -perm /111 -exec sed '/^\#\!\//d' -i {} \+
  find -name ${_file##*/} -type f -perm /111 -exec sed '/^\#\!\/.\+py/s/env\ \+//' -i {} \+
done
%py3_compile -O .%{python3_sitelib}
popd
sed -i "s/\(Exec=\).*/\1%{name}/" %{buildroot}%{_datadir}/applications/org.xfce.Catfish.desktop
for i in 16 24 32 48; do
    install -dm 0755 %{buildroot}%{_datadir}/icons/hicolor/$i\x$i/apps
    rsvg-convert -h $i -w $i data/media/catfish.svg -o %{buildroot}%{_datadir}/icons/hicolor/$i\x$i/apps/%{name}.png
done

%suse_update_desktop_file -r org.xfce.Catfish GNOME Utility Filesystem

%fdupes %{buildroot}%{python3_sitelib}

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml

%find_lang %{name}

%files
%license COPYING
%doc AUTHORS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/org.xfce.Catfish.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}_lib
%{python3_sitelib}/%{name}-%{version}-py%{py3_ver}.egg-info
%{_mandir}/man?/%{name}.?%{ext_man}

%files lang -f %{name}.lang

%changelog
