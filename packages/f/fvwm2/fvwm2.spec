#
# spec file for package fvwm2
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


Name:           fvwm2
Version:        2.7.0
Release:        0
Summary:        The F Virtual Window Manager
License:        GPL-2.0-or-later
Group:          System/GUI/Other
URL:            http://www.fvwm.org
Source0:        https://github.com/fvwmorg/fvwm/releases/download/%{version}/fvwm-%{version}.tar.gz
Source1:        fvwm_icons.tar.bz2
Source3:        %{name}.desktop
Source4:        system.fvwm2rc
Source6:        openSUSE.xpm
Patch0:         fvwm-configure.patch
Patch1:         fvwm-2.5.26-sv_SE.patch
Patch2:         fvwm-no-date-time.patch
Patch3:         fvwm-FvwmAuto-overflow.patch
Patch4:         threadlocking.patch
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  libstroke-devel
BuildRequires:  libxslt-tools
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  readline-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(xrender)
#not actually used but includes its headers anyway..
BuildRequires:  pkgconfig(xt)
Requires:       desktop-data
Requires:       mktemp
Requires:       wallpaper-branding
Requires:       xdg-menu
Requires:       xli
Requires(post): update-alternatives
Requires(postun):update-alternatives
Provides:       fvwm
Provides:       fvwmicns
Provides:       windowmanager
Provides:       xpmroot
Obsoletes:      fvwm
Obsoletes:      xpmroot

%description
FVWM is a virtual desktop window manager for the X Window System.

FVWM is intended to have a small memory footprint but a rich feature
set, to be extremely customizable and extendible, and to be very
compatible with the Motif Window Manager (mwm).

%prep
%setup -q -n fvwm-%{version}
%autopatch -p0
find . -name *sv_SE* -exec rename --verbose sv_SE sv '{}' \+
mkdir icons
tar -C icons -j -x -v -f $RPM_SOURCE_DIR/fvwm_icons.tar.bz2
cp %{SOURCE6} icons

%build
autoreconf -fvi
%configure \
    --sysconfdir=%{_sysconfdir}/X11/fvwm2 \
    --libexecdir=%{_prefix}/lib/X11/fvwm2 \
    --with-imagepath=%{_datadir}/X11/fvwm2/pixmaps:%{_datadir}/X11/fvwm2/bitmaps:%{_datadir}/pixmaps:%{_datadir}/wallpapers
make %{?_smp_mflags}

%install
%make_install

# missed main manual page
install -m 644 doc/fvwm/fvwm.1 %{buildroot}%{_mandir}/man1

# default config
install -d -m 755 %{buildroot}%{_sysconfdir}/X11/fvwm2
install -m 644 %{SOURCE4} %{buildroot}%{_sysconfdir}/X11/fvwm2/system.fvwm2rc
# documentation for modules
rm -vf sample.fvwmrc/Makefile* sample.fvwmrc/system.fvwm2rc-sample-95

rm -vf docs/Makefile*
install -d -m 755 docu-module
for i in $(find -name "README*" -not -name "*,v" -and -not -name "*.orig")
do
	TMPDIR=$(dirname ${i#./})
	if [ "x$TMPDIR" = "x." ]; then
		install -m 644 $i docu-module/${i#./}
	else
		install -m 644 $i docu-module/README.$(basename "$TMPDIR")
	fi
done

# forbidden links
pushd %{buildroot}/
	find . -type l -printf '%%P %%l\n' | while read dst src
	do
		case "$src" in
		%{buildroot}/*)
			src=${src#%{buildroot}/}
			rm -vf $dst
			ln -frsv $src $dst
			;;
		*)
			;;
		esac
	done
popd

# icons
install -d -m 755 %{buildroot}%{_datadir}/X11/fvwm2/pixmaps
install -m 644 icons/* %{buildroot}%{_datadir}/X11/fvwm2/pixmaps

# install kdm/gdm entry
install -m 0755 -d %{buildroot}%{_datadir}/xsessions/
install -m 0644 %{SOURCE3} %{buildroot}%{_datadir}/xsessions/
# removing the useless README.vms file
rm -f  %{buildroot}/%{_docdir}/fvwm2/README.vms
%suse_update_desktop_file %{buildroot}%{_datadir}/xsessions/%{name}.desktop
%find_lang fvwm %{name}.lang
%find_lang FvwmScript %{name}.lang

%post
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/fvwm2.desktop 20

%postun
[ -f %{_datadir}/xsessions/lxqt.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-xsession.desktop %{_datadir}/xsessions/fvwm2.desktop

%files -f %{name}.lang
%license COPYING
%doc NEWS docs docu-module/*
%dir %{_sysconfdir}/X11/fvwm2
%config %{_sysconfdir}/X11/fvwm2/system.fvwm2rc
%{_bindir}/*
%{_prefix}/lib/X11/fvwm2/*
%{_datadir}/X11/fvwm2/pixmaps/*
%dir %{_prefix}/lib/X11/fvwm2
%{_datadir}/fvwm
%dir %{_datadir}/X11/fvwm2
%dir %{_datadir}/X11/fvwm2/pixmaps
%{_mandir}/man1/*
%{_datadir}/xsessions/*desktop

%changelog
