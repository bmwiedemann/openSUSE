#
# spec file for package lxappearance
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           lxappearance
Version:        0.6.2
Release:        0
Summary:        It's a desktop-independent theme switcher for GTK+
License:        GPL-2.0
Group:          System/GUI/LXDE
Url:            http://www.lxde.org/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  dbus-1-devel
BuildRequires:  dbus-1-glib-devel
BuildRequires:  docbook-utils
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  gnome-icon-theme
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libxslt
BuildRequires:  perl
BuildRequires:  perl-XML-Parser
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
Recommends:     %{name}-lang
Recommends:     %{name}-obconf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
LXAppearance is part of LXDE project.
It's a desktop-independent theme switcher for GTK+.

%package devel
Summary:        Lxappearance development files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
Development files to build lxappearance plugins

%lang_package

%prep
%setup -q

%build
%configure \
	--enable-dbus \
    --sysconfdir=/etc
make %{?_smp_mflags} V=1

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
# own the pugins dir so that we don't need it
# for each plugin we will install later
mkdir -p %{buildroot}/%{_libdir}/lxappearance/plugins
%suse_update_desktop_file %{name}
%fdupes -s %{buildroot}
%find_lang %{name}

%post
%desktop_database_post

%postun
%desktop_database_postun

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/ui
%{_datadir}/%{name}/ui/lxappearance.ui
%{_datadir}/%{name}/ui/about.ui
%{_mandir}/man1/%{name}.1.gz
%dir %{_libdir}/lxappearance
%dir %{_libdir}/lxappearance/plugins

%files devel
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/%{name}.h
%{_libdir}/pkgconfig/%{name}.pc

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
