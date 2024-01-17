#
# spec file for package texamator
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


Name:           texamator
Version:        3.0+git.20190226.91432e4
Release:        0
Summary:        Manage databases of exercises written in (La)TeX
License:        GPL-3.0-only
Group:          Productivity/Publishing/TeX/Utilities
URL:            http://alexisfles.ch/en/texamator/texamator.html
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.in
BuildRequires:  ImageMagick
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python3-base
# Check list of dependencies:
BuildRequires:  python3-qt5
BuildRequires:  update-desktop-files
Requires:       python3-base
Requires:       python3-poppler-qt5
Requires:       python3-qt5
Requires:       texlive-latex
Recommends:     %{name}-lang
BuildArch:      noarch

%description
TeXamator is written using PyQt5. It is aimed at helping you making your
exercise sheets. Basically, it browses a specified directory, looks for
.tex files containing exercices and builds a tree with all your exercises.
You can click on an element of the tree to have a preview of the exercise
sheet and then add exercises to a list if you wish to. Then you can save
your work to a .tex file or you can generate a pdf file.

%lang_package

%prep
%setup -q

sed -i 's|/usr/bin/env python3|/usr/bin/python3|' partielatormods/other/qpdfview.py
sed -i 's|#!/usr/bin/python$|#!/usr/bin/python3|' partielatormods/guis/*.py
sed -i 's|#!/usr/bin/python$|#!/usr/bin/python3|' partielatormods/other/*.py
sed -i 's|#!/usr/bin/python$|#!/usr/bin/python3|' partielatormods/__init__.py

cp %{SOURCE1} .

sed -e 's|@python3_sitelib@|%{python3_sitelib}/%{name}|' \
    -e 's|@name@|%{name}.py|' \
    < %{name}.in > %{name}

%build
# There is nothing to build.

%install
mkdir -p %{buildroot}%{python3_sitelib}/%{name}
for _dir in $(ls -1F | grep '.*\/' | sed 's/\/$//'); do
  cp -rp $_dir %{buildroot}%{python3_sitelib}/%{name}
done

pushd %{buildroot}%{python3_sitelib}
for _file in $(grep -rl '^\#\!'); do
  find -name ${_file##*/} -type f -perm -644 -exec sed '/^\#\!/d' -i {} \;
done
%py3_compile .
popd

install -Dm0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm0755 %{name}.py %{buildroot}%{python3_sitelib}/%{name}

_file=$(find -name TeXamator.png)
_width=$(identify -format %w $_file)
_height=$(identify -format %h $_file)
if [ "$_width" -eq $_height ]; then
  if [ "$_width" -ge 256 ]; then
    for s in 16 32 48 64 128 256; do
      mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
      convert -strip \
        $_file -resize $s \
        %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
    done
  fi
fi

%{suse_update_desktop_file -c \
%{name} TeXamator "Manage databases of exercises written in (La)TeX" %{name} %{name} Qt Office Database}

langlist=$PWD/%{name}.lang
langdir=%{python3_sitelib}/%{name}/ts_files
basedir=$(basename $langdir)
pushd $basedir
  /bin/ls -1 *.qm | while read qm; do
    [ -e "$qm" ] || continue
    if ! grep -wqs "\%dir\ $langdir" $langlist; then
      echo "%dir $langdir" >> $langlist
    fi
    install -Dm0644 $qm %{buildroot}$langdir/$qm
    lang=$(echo $qm | sed 's/.*\_\(.*\)\..*/\1/')
    [ "$(echo $lang | wc -c)" -le 6 ] || exit $?
    lang=${lang:+%lang($lang)\ }
    echo "$lang$langdir/$qm" >> $langlist
  done
popd

find %{buildroot} -type f \( -name \*.sh -o -name \*.ts \) -delete -print

%fdupes -s %{buildroot}%{python3_sitelib}

%post
%icon_theme_cache_post

%postun
%icon_theme_cache_postun

%files
%doc README.md gpl-3.0.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.??g
%{python3_sitelib}/%{name}/
%exclude %{python3_sitelib}/%{name}/ts_files

%files lang -f %{name}.lang

%changelog
