#
# spec file for package eaglemode
#
# Copyright (c) 2023 SUSE LLC
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


Name:           eaglemode
Version:        0.96.0
Release:        0
Summary:        A zoomable user interface (ZUI) with file manager, file viewers, games, etc.
License:        GPL-3.0-only
Group:          Development/Tools/Other
URL:            https://eaglemode.sourceforge.net/
Source0:        https://downloads.sourceforge.net/%{name}/%{name}-%{version}/%{name}-%{version}.tar.bz2
Source1:        %{name}-icons.tar
Source2:        %{name}.desktop
Source3:        %{name}-rpmlintrc
Patch0:         01-eaglemode.patch
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  perl
Requires:       abiword
Requires:       xorg-x11
%if 0%{?sles_version}
BuildRequires:  gtk2-devel
%else
BuildRequires:  pkgconfig(gtk+-2.0)
%endif
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpoppler-glib-devel
BuildRequires:  librsvg-devel
BuildRequires:  update-desktop-files
BuildRequires:  vlc-devel
BuildRequires:  xorg-x11-devel
%endif
%if 0%{?mandriva_version}
BuildRequires:  libpoppler-glib-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libxine-devel
BuildRequires:  x11-server-devel
%endif
%if 0%{?fedora_version}
BuildRequires:  libX11-devel
BuildRequires:  librsvg2-devel
BuildRequires:  poppler-glib-devel
BuildRequires:  xine-lib-devel
%endif
%if 0%{?suse_version}
Requires:       binutils
Requires:       bzip2
Requires:       gcc
Requires:       gedit
Requires:       ghostscript-x11
Requires:       gzip
Requires:       lzop
Requires:       perl
Requires:       tar
Requires:       texlive-bin-dvilj
Requires:       transfig
Requires:       unzip
Requires:       zip
# Remove when p7zip-full is in all products
%if 0%{?suse_version} > 1500
Requires:       p7zip-full
%else
Requires:       p7zip
%endif
%if 0%{?suse_version} > 1320
Requires:       xterm-bin
%else
Requires:       xterm
%endif
%endif

%description
Eagle Mode is an implementation of a futuristic style of man-machine
communication in which the user can visit almost everything simply by
zooming in. It has a file manager, file viewers and players for most
of the common file types, a chess game, a 3D mines game, a netwalk
game, a multi-function clock and some fractal fun, all integrated in
a virtual cosmos. That cosmos also provides a Linux kernel
configurator in form of a kernel patch.

It features a separate popup-zoomed control view, help texts in the
things they are describing, editable bookmarks, multiple input
methods, anti-aliased graphics, a virtually unlimited deep panel
tree, and a C++ API.

%prep
%setup -q -a 1
%patch0 -p1

%build
# stupid build scripts don't allow passing custom flags
mkdir .bin
cat > .bin/gcc <<\EOF
#!/bin/sh
exec %{_bindir}/gcc %{optflags} "$@"
EOF
chmod +x .bin/gcc
PATH=$PWD/.bin:$PATH
perl make.pl build

%install
perl make.pl install dir=%{buildroot}/%{_libdir}/eaglemode

# install icons
for i in 16 24 32 48 ; do
    install -Dm 0644 icons/%{name}-${i}.png \
            %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{name}.png
done

cd %{buildroot}/%{_libdir}/eaglemode
mkdir -p  ../../../%{_docdir}/eaglemode
cp -r doc ../../../%{_docdir}/eaglemode
mkdir -p ../../share/eaglemode
cp -r res ../../share/eaglemode
mkdir -p %{buildroot}%{_sysconfdir}/eaglemode
cp -r etc/* %{buildroot}%{_sysconfdir}/eaglemode
mkdir -p %{buildroot}%{_bindir}
cd %{buildroot}%{_bindir}
ln -s ../../%{_libdir}/eaglemode/eaglemode.sh eaglemode
mkdir -p %{buildroot}%{_prefix}/lib
cd %{buildroot}/%{_libdir}
ln -s eaglemode/lib/*.so .
mkdir -p %{buildroot}%{_includedir}
cd %{buildroot}%{_includedir}
ln -s ../../%{_libdir}/eaglemode/include/* .

# install Desktop file
install -Dm 0644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}.desktop

%if 0%{?suse_version}
    %suse_update_desktop_file %{name}
    %fdupes -s %{buildroot}%{_prefix}
%endif

%files
%{_bindir}/%{name}
%doc %{_docdir}/%{name}
%{_datadir}/%{name}
%{_libdir}/*.so
%{_libdir}/%{name}
%{_sysconfdir}/%{name}
%{_includedir}/*
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
