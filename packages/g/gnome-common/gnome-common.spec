#
# spec file for package gnome-common
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


Name:           gnome-common
Version:        3.18.0
Release:        0
Summary:        Common Files to Build GNOME
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            http://www.gnome.org/
Source:         http://download.gnome.org/sources/gnome-common/3.18/%{name}-%{version}.tar.xz
BuildRequires:  pkgconfig
Requires:       autoconf
# we need autoconf-archive >= 2014.10.15, as this is when ax_check_enable_debug.m4 and ax_code_coverage.m4 became part of it.
Requires:       autoconf-archive >= 2014.10.15
Requires:       automake
Requires:       gettext-tools
# Avoiding pkgconfig()-style because we want glib-gettextize
Requires:       glib2-devel
Requires:       gtk-doc
Requires:       intltool
Requires:       libtool
Requires:       pkgconfig
Requires:       yelp-tools
BuildArch:      noarch

%description
Gnome-common includes files used by to build GNOME and GNOME applications.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install
# the files ax_check_enable_debug.m4 and ax_code_coverage.m4 live in autoconf-archive
rm %{buildroot}%{_datadir}/aclocal/{ax_check_enable_debug,ax_code_coverage}.m4

%files
%doc ChangeLog
%{_bindir}/gnome-autogen.sh
%dir %{_datadir}/aclocal
%{_datadir}/aclocal/gnome-code-coverage.m4
%{_datadir}/aclocal/gnome-common.m4
%{_datadir}/aclocal/gnome-compiler-flags.m4

%changelog
