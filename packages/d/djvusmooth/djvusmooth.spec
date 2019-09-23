#
# spec file for package djvusmooth
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


Name:           djvusmooth
Version:        0.3
Release:        0
Summary:        Graphical Text Editor for DjVu
License:        GPL-2.0-only
Group:          Productivity/Publishing/Other
Url:            http://jwilk.net/software/djvusmooth
Source0:        https://github.com/jwilk/djvusmooth/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/jwilk/djvusmooth/releases/download/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        djvusmooth.png
Source3:        %{name}.keyring
BuildRequires:  python-setuptools
Requires:       djvulibre
Requires:       python-wxWidgets-3_0
Requires:       python2-djvulibre
Requires:       python2-pyxdg
Requires:       python2-subprocess32
Requires(post): desktop-file-utils
Requires(post): hicolor-icon-theme
Requires(postun): desktop-file-utils
Requires(postun): hicolor-icon-theme
Recommends:     %{name}-lang
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
DjVuSmooth is a graphical text editor for DjVu documents.

%lang_package

%prep
%setup -q

%build

%install
# Replace a desktop file. Provided one isn't good enough.
cat > extra/%{name}.desktop << EOF
[Desktop Entry]
Name=DjVuSmooth
GenericName=Graphical Text Editor for DjVu
GenericName[pl]=Graficzny edytor plików DjVu
GenericName[ru]=Текстовый редактор DjVu-книг
GenericName[de]=Grafischer Editor für DjVu-Dateien
Comment=Graphical Text Editor for DjVu
Comment[pl]=Graficzny edytor plików DjVu
Comment[ru]=Граффический текстовый редактор для DjVu-книг
Comment[de]=Grafischer Editor für DjVu-Dateien
Type=Application
Exec=djvusmooth %f
Icon=djvusmooth
Categories=Utility;TextEditor;
StartupNotify=true
Terminal=false
MimeType=image/x-djvu;image/x.djvu;image/vnd.djvu;
EOF

python setup.py install \
    --root=%{buildroot} \
    --prefix=%{_prefix}
install -Dm 0644 %{SOURCE2} \
    %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

%find_lang %{name}

%if 0%{?suse_version} && 0%{?suse_version} < 1330
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%defattr(-,root,root,-)
%license doc/COPYING
%doc doc/{changelog,credits,README}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.png
%{_mandir}/man?/*
%{python_sitelib}/*

%files lang -f %{name}.lang

%changelog
