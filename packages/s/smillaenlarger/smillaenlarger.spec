#
# spec file for package smillaenlarger
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           smillaenlarger
Version:        0.9.0+git.2017.11.21
Release:        0
Summary:        A graphical tool to resize bitmaps in high quality
License:        GPL-3.0-or-later
Group:          Productivity/Graphics/Bitmap Editors
URL:            https://github.com/lupoDharkael/smilla-enlarger
# git clone https://github.com/lupoDharkael/smilla-enlarger.git
# git archive --format=tar --prefix=smillaenlarger-{version}/ master | xz -z9 > smillaenlarger-{version}.tar.xz
Source0:        smillaenlarger-%{version}.tar.xz
Patch1:         smillaenlarger-0.9.0+git.2017.11.21_Qt5.11.patch

BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)

%description
SmillaEnlarger is a small graphical tool ( based on Qt ) to resize,
especially magnify bitmaps in high quality.

%prep
%setup -q
%patch1
sed \
    -i -e \
    's|0.9.0|%{version}|g' \
    ImageEnlarger.pro

%build
%{_libdir}/qt5/bin/qmake \
                         ImageEnlarger.pro \
                         QMAKE_STRIP="" \
                         QMAKE_CFLAGS+="%{optflags}" \
                         QMAKE_CXXFLAGS+="%{optflags} -fvisibility=hidden -fvisibility-inlines-hidden"
make %{?_smp_mflags}

%install
install -m0755 -D smilla-enlarger %{buildroot}%{_bindir}/%{name}
install -m0644 -D img/smilla.png %{buildroot}%{_datadir}/pixmaps/smilla.png
%suse_update_desktop_file -i smilla

%files
%license LICENSE
%doc docs/*.md docs/*.txt help/*.html README.md
%{_bindir}/%{name}
%{_datadir}/applications/smilla.desktop
%{_datadir}/pixmaps/smilla.png

%changelog
