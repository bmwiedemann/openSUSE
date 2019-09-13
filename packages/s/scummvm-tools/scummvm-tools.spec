#
# spec file for package scummvm-tools
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


%bcond_without mad
Name:           scummvm-tools
Version:        2.0.0
Release:        0
Summary:        ScummVM-related tools
License:        GPL-2.0-or-later
Group:          Amusements/Games/Other
Url:            http://www.scummvm.org
Source0:        https://www.scummvm.org/frs/scummvm-tools/%{version}/scummvm-tools-%{version}.tar.xz
Source1:        %{name}.desktop
Source99:       %{name}.changes
# PATCH-FIX-UPSTREAM fix-new-wxwidgets.patch -- https://bugs.scummvm.org/ticket/9554
Patch0:         fix-new-wxwidgets.patch
BuildRequires:  ImageMagick
BuildRequires:  boost-devel >= 1.32.0
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
%if 0%{?suse_version} >= 1320
BuildRequires:  wxWidgets-devel >= 3
%else
%define _use_internal_dependency_generator 0
%define __find_requires %wx_requires
BuildRequires:  wxWidgets-devel
%endif
BuildRequires:  pkgconfig(flac) >= 1.1.3
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libpng) >= 1.2.8
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(vorbisenc)
BuildRequires:  pkgconfig(zlib)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if %{with mad}
BuildRequires:  pkgconfig(mad)
%endif

%description
This is a collection of various tools that may be useful to use in
conjunction with ScummVM.
Please note that although a tool may support a feature, certain ScummVM
versions may not. ScummVM 0.6.x does not support FLAC audio, for example.

Many games package together all their game data in a few big archive files.
The following tools can be used to extract these archives, and in some cases
are needed to make certain game versions usable with ScummVM.

The following tools can also be used to analyze the game scripts
(controlling the behavior of certain scenes and actors in a game).
These tools are most useful to developers.

%prep
%setup -q
%patch0 -p1
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE99}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g" version.cpp
# build the endianness test without optimization otherwise gcc is too smart
# and optimize everything away, making the test fail
sed -i '/tmp_endianness_check.cpp/ s/$CXXFLAGS/$CXXFLAGS -fno-lto -O0/' configure

%build
export CXXFLAGS="%{optflags}"
./configure --prefix=%{_prefix} \
            --enable-verbose-build
make %{?_smp_mflags}

%install
mkdir -p %{buildroot}%{_bindir}
make %{?_smp_mflags} DESTDIR=%{buildroot} install
# Install icons and .desktop file
index=5
for res in 128 48 32 16; do
    mkdir -p "%{buildroot}%{_datadir}/icons/hicolor/$res"x"$res/apps"
    convert -strip "gui/media/scummvmtools.ico[$index]" "%{buildroot}%{_datadir}/icons/hicolor/$res"x"$res/apps/%{name}.png"
    index=$((index+1))
done
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}
%fdupes %{buildroot}%{_datadir}

%files
%defattr(0644,root,root,0755)
%doc README TODO
%attr(0755,root,root) %{_bindir}/scummvm-tools
%attr(0755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%if 0%{?suse_version} > 1320
%license COPYING
%else
%doc COPYING
%endif

%changelog
