#
# spec file for package love
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


%bcond_without mpg123
Name:           love
Version:        11.2
Release:        0
Summary:        2D gaming engine written in Lua
License:        Zlib
Group:          Development/Languages/Other
URL:            http://love2d.org/
Source:         https://bitbucket.org/rude/love/downloads/%{name}-%{version}-linux-src.tar.gz
Patch0:         love-11.2-return.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libtool
BuildRequires:  physfs-devel
BuildRequires:  pkgconfig
BuildRequires:  shared-mime-info
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(IL)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libenet)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(luajit)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(theora)
BuildRequires:  pkgconfig(vorbisfile)
Requires(pre):  desktop-file-utils
Requires(pre):  shared-mime-info
%if %{with mpg123}
BuildRequires:  pkgconfig(libmpg123)
%endif

%description
LÖVE is a framework for making 2D games in Lua.

%prep
%setup -q
%patch0 -p1
sed -i 's/\r$//' *.txt

%build
autoreconf -fi
%configure \
%if %{without mpg123}
	--disable-mpg123 \
%endif
	--disable-static
make %{?_smp_mflags}

%install
%make_install
rm "%{buildroot}%{_libdir}/liblove.la" "%{buildroot}%{_libdir}/liblove.so"

%post
/sbin/ldconfig
%desktop_database_post
%icon_theme_cache_post
%mime_database_post

%postun
/sbin/ldconfig
%desktop_database_postun
%icon_theme_cache_postun
%mime_database_postun

%files
%license license.txt
%doc changes.txt readme.md
%{_bindir}/love
%{_libdir}/liblove-%{version}.so
%{_datadir}/applications/love.desktop
%{_mandir}/man1/love.1%{?ext_man}
%{_datadir}/icons/hicolor/scalable/mimetypes/application-x-love-game.svg
%{_datadir}/mime/packages/love.xml
%{_datadir}/pixmaps/love.svg

%changelog
