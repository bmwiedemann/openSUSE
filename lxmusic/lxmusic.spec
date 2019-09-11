#
# spec file for package lxmusic
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%bcond_with gtk3

Name:           lxmusic
Version:        0.4.7
Release:        0
Summary:        Lightweight Audio Player
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Players
Url:            http://www.lxde.org/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  docbook-utils
BuildRequires:  fdupes
%if %{with gtk3}
BuildRequires:  gtk3-devel
%else
BuildRequires:  gtk2-devel
%endif
BuildRequires:  intltool
BuildRequires:  libnotify-devel
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  xmms2-devel >= 0.7
Requires:       xmms2
Recommends:     %{name}-lang
Recommends:     xmms2-plugin-restricted
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
LXMusic is just a lightweight audio player,
that uses xmms2 as back-end.

%lang_package

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%configure \
%if %{with gtk3}
  --enable-gtk3
%endif

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
%find_lang %{name}
%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root,0755)
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/lxmusic
%{_datadir}/lxmusic/*.ui.glade
%{_datadir}/pixmaps/lxmusic.png
%{_mandir}/man1/lxmusic.1.gz

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
