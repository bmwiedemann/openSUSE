#
# spec file for package tint2
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


Name:           tint2
Version:        16.7
Release:        0
Summary:        A lightweight X11 desktop panel and task manager
License:        GPL-2.0-only
Group:          System/X11/Utilities
Url:            https://gitlab.com/o9000/tint2
Source0:        https://gitlab.com/o9000/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:        tint2conf.1.gz
BuildRequires:  cairo-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gtk2-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  imlib2-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  librsvg2-devel
BuildRequires:  pango-devel
BuildRequires:  startup-notification-devel
Recommends:     %{name}-lang

%description
tint2 is a simple panel/taskbar made for modern X window managers. It was
specifically made for Openbox3 but should also work with other window managers.

%lang_package

%prep
%setup -q -n %{name}-v%{version}

%build
%cmake -DENABLE_EXAMPLES=ON -DDOCDIR=%{_docdir}/%{name}
make %{?_smp_mflags}

%install
%cmake_install

# put sample/ in %%doc
rm -rf %{buildroot}%{_datadir}/tint2/*.tint2rc

# create tint2 config directory
mkdir -p %{buildroot}%{_sysconfdir}/skel/.config/tint2/

desktop-file-install	\
	--set-key=NoDisplay  --set-value=true	\
	--delete-original	\
	--dir=%{buildroot}%{_datadir}/applications	\
	%{buildroot}/%{_datadir}/applications/tint2.desktop

desktop-file-install	\
	--delete-original	\
	--dir=%{buildroot}%{_datadir}/applications	\
	%{buildroot}/%{_datadir}/applications/tint2conf.desktop

# install man page for tint2conf (written for Debian package)
install -m 0644 %{SOURCE1} %{buildroot}/%{_mandir}/man1/

%find_lang tint2conf

%if 0%{?suse_version} > 1130
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/tint2
%{_bindir}/tint2conf
%config(noreplace) %{_sysconfdir}/xdg/tint2/tint2rc
%{_sysconfdir}/skel/.config/tint2/
%{_sysconfdir}/xdg/tint2
%{_datadir}/tint2/
%{_datadir}/applications/tint2conf.desktop
%{_datadir}/applications/tint2.desktop
%{_datadir}/icons/hicolor/*/apps/tint*
%{_mandir}/man1/tint*
%dir %{_datadir}/doc/tint2
%dir %{_datadir}/doc/tint2/html
%dir %{_datadir}/doc/tint2/html/images
%{_datadir}/doc/tint2/*
%{_datadir}/mime/packages/tint2conf.xml

%files lang -f tint2conf.lang
%defattr(-,root,root)

%changelog
