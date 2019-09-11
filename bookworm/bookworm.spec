#
# spec file for package bookworm
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


Name:           bookworm
Version:        1.1.2
Release:        0
Summary:        E-book reader
License:        GPL-3.0-or-later
Group:          Productivity/Office/Other
URL:            https://babluboy.github.io/bookworm
Source:         https://github.com/babluboy/bookworm/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  ImageMagick
BuildRequires:  meson
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(sqlite3) >= 3.5.9
BuildRequires:  pkgconfig(webkit2gtk-4.0) >= 2.16.0
# Check list of dependencies
BuildRequires:  html2text
BuildRequires:  poppler-tools
Requires:       html2text
Requires:       poppler-tools
Recommends:     unrar
Recommends:     unzip
Recommends:     %{name}-lang

%description
An eBook reader for Elementary OS.

It uses poppler for decoding and read formats like EPUB, PDF, mobi, cbr, etc.

%lang_package

%prep
%setup -q

chmod -x AUTHORS

%build
%meson
%meson_build

%install
%meson_install

# fix env-script-interpreter
pushd %{buildroot}%{_datadir}
for _file in $(grep -rl '^\#\!'); do
   find -name ${_file##*/} -type f -executable -exec sed '/^\#\!/s/env\ \+//' -i {} \;
done
popd

# fix wrong-icon-size
_file=$(find -name %{name}.png)
_count=$(echo "$_file" | wc -l)
for _file in $_file; do
  ((_count -- ))
  _width=$(identify -format %w $_file)
  _height=$(identify -format %h $_file)
  _size+=$'\n'$(echo "${_width}x$_height$_file")
  [ "$_count" -eq 0 ] || continue
  _file=$(echo "$_size" | sort -rn | grep -m1 .)
  ls %{_datadir}/icons/hicolor | grep '[0-9]x[0-9]' | sort -n | while read _size; do
    if [ "${_file%x*}" -ge ${_size%x*} ]; then
      mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${_size}/apps
      convert -strip ${_file#*./} -resize $_size \
        %{buildroot}%{_datadir}/icons/hicolor/${_size}/apps/${_file##*/}
    fi
  done
done

# remove executable flags
find %{buildroot} -name \*.txt -exec chmod 0644 {} +

%suse_update_desktop_file -r com.github.babluboy.bookworm GTK Office Viewer
%find_lang com.github.babluboy.bookworm %{name}.lang
%fdupes %{buildroot}/%{_datadir}

# dirlist HiDPI icons (see: hicolor/index.theme)
touch $PWD/dir.lst
_dirlist=$PWD/dir.lst
pushd %{buildroot}
find ./ | while read _list; do
    echo $_list | grep '[0-9]\@[0-9]' || continue
    _path=$(echo $_list | sed 's/[^/]//')
    if ! ls ${_path%/*}; then
        grep -xqs "\%dir\ ${_path%/*}" $_dirlist || echo "%dir ${_path%/*}" >> $_dirlist
    fi
done
popd

%files -f dir.lst
%license COPYING
%doc AUTHORS README.md
%{_bindir}/com.github.babluboy.bookworm
%{_datadir}/applications/com.github.babluboy.bookworm.desktop
%{_datadir}/com.github.babluboy.bookworm/
%{_datadir}/glib-2.0/schemas/com.github.babluboy.bookworm.gschema.xml
%{_datadir}/icons/hicolor/*/*/com.github.babluboy.bookworm.??g
%{_datadir}/metainfo/com.github.babluboy.bookworm.appdata.xml

%files lang -f %{name}.lang

%changelog
