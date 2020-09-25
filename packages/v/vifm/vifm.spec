#
# spec file for package vifm
#
# Copyright (c) 2020 SUSE LLC
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


Name:           vifm
Version:        0.11
Release:        0
Summary:        Ncurses based file manager with vi like keybindings
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
URL:            http://%{name}.info
Source0:        https://github.com/vifm/vifm/releases/download/v%{version}/%{name}-%{version}.tar.bz2
Source1:        https://github.com/vifm/vifm/releases/download/v%{version}/%{name}-%{version}.tar.bz2.asc
Source2:        %{name}.keyring
BuildRequires:  file-devel
BuildRequires:  groff
BuildRequires:  ncurses-devel
BuildRequires:  pkgconfig
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif
%if 0%{?suse_version} > 1110
BuildRequires:  pkgconfig(x11)
%else
BuildRequires:  xorg-x11-devel
%endif

%description
Vifm is a ncurses based file manager with vi like keybindings that allow complete
keyboard control over your files without having to learn a new set of commands.
It supports UTF-8, a quick file view similar to midnight commander's quick view,
and configurable color schemes.

%prep
%setup -q
sed -i 's/#!\/usr\/bin\/env perl/#!\/usr\/bin\/perl/' src/vifm-convert-dircolors

%build
%configure \
	--with-curses \
	--with-libmagic \
	--without-gtk \
	--disable-developer
%make_build
gzip -9c ChangeLog > ChangeLog.gz

%install
make install DESTDIR="%{?buildroot}"
%if 0%{?suse_version}
%suse_update_desktop_file %{name}
%endif
rm -rf %{buildroot}%{_datadir}/doc/vifm/*
rm -rf %{buildroot}%{_datadir}/vifm/vifmrc-osx
rm -rf %{buildroot}%{_datadir}/vifm/vifm-media-osx
rm -rf %{buildroot}%{_datadir}/vifm/vim-doc/doc/tags
rm -rf %{buildroot}%{_datadir}/vifm/vim-doc/doc/vifm-app.txt

%files
%license COPYING
%doc AUTHORS BUGS ChangeLog.* README TODO
%doc %{_datadir}/%{name}/%{name}-help.txt
%dir %{_datadir}/%{name}
%{_bindir}/*
%{_datadir}/%{name}/vim
%{_datadir}/%{name}/%{name}rc
%{_datadir}/%{name}/colors/
%{_datadir}/%{name}/vifm-media
%{_mandir}/man1/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions/
%{_datadir}/bash-completion/completions/vifm
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/
%{_datadir}/zsh/site-functions/_vifm
%{_sysconfdir}/vifm/
%{_sysconfdir}/vifm/colors/

%changelog
