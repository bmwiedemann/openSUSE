#
# spec file for package kye
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           kye
Version:        1.0
Release:        0
Summary:        Logic puzzle game with arcade elements
License:        GPL-2.0+
Group:          Amusements/Games/Strategy/Turn Based
Url:            http://games.moria.org.uk/kye/

Source:         http://games.moria.org.uk/kye/download/%name-%version.tar.gz
Source1:        %name.desktop
Source2:        %name-edit.desktop
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-setuptools
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
Requires:       gdk-pixbuf-loader-rsvg
Requires:       python-gtk
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif

%description
This is a clone of the original Kye game for Windows, by Colin Garbutt.

Kye is a puzzle game with arcade game elements. The game takes place
in a small playing area, where the player controls Kye - a
distinctive green blob. The player moves around and tries to collect
all of the diamonds. However, there are many other objects in the
game, which can obstruct, trap or kill the Kye.

Kye is one of those games like Chess, where a small number of
different playing pieces, obeying simple rules, combine to create a
game of enormous variety and complexity.

%prep
%setup -q

%build
perl -i -pe 's{(http://games.moria.org.uk/kye/)pygtk}{$1}g' \
	kye/dialogs.py setup.py README

python setup.py build;

# Workaround for librsvg bug [bnc#789728]
mkdir t;
pushd t/;
tar -xzf ../images.tar.gz;
perl -i -pe 's{<style>}{<style type="text/css">}gs' *.svg;
tar --use-compress-program="gzip -n9" --owner=0 --group=0 --numeric-owner --pax-option=exthdr.name=%d/PaxHeaders/%f,atime:=0,ctime:=0 --mtime=1990-01-01 -cf ../images.tar.gz *;
popd;

%install
python setup.py install --prefix=%_prefix --root=%buildroot;
mkdir -p "%buildroot/%_datadir/pixmaps";
cp -a kye*icon.png "%buildroot/%_datadir/pixmaps/";
# convenience
ln -s Kye "%buildroot/%_bindir/kye";
ln -s Kye-edit "%buildroot/%_bindir/kye-edit";

c="%buildroot/%_datadir/applications"
mkdir -p "$c"
install -Dpm0644 "%{S:1}" "%{S:2}" "$c/"

%if 0%{?suse_version}
%suse_update_desktop_file %name %name-edit
%fdupes -s %buildroot/%_prefix
%endif

%files
%defattr(-,root,root)
%_bindir/kye*
%_bindir/Kye*
%_datadir/%name
%_datadir/applications/kye*
%_datadir/pixmaps/kye*
%python_sitelib/%name
%python_sitelib/%name-%version-py%py_ver.egg-info
%doc COPYING README

%changelog
