#
# spec file for package pidgin-mrim
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


%define _name   mrim-prpl
Name:           pidgin-mrim
Version:        0.1.28.1
Release:        0
Summary:        Pidgin plugin for Mail.Ru Agent
License:        GPL-2.0+
Group:          Productivity/Networking/Instant Messenger
Url:            https://bitbucket.org/mrim-prpl-team/mrim-prpl
Source:         https://bitbucket.org/mrim-prpl-team/%{_name}/downloads/%{_name}-%{version}.tar.xz
BuildRequires:  gtk2-devel
BuildRequires:  libpurple-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is a Mail.Ru Agent plugin for Pidgin.
It provides support for the MRA/MRIM protocol, popular in ex-USSR.

%package -n libpurple-plugin-mrim
Summary:        Libpurple plugin for Mail.Ru Agent
Group:          Productivity/Networking/Instant Messenger
Recommends:     libpurple-plugin-mrim-lang
Enhances:       libpurple

%description -n libpurple-plugin-mrim
This is a Mail.Ru Agent plugin for libpurple.
It provides support for the MRA/MRIM protocol, popular in ex-USSR.

%lang_package -n libpurple-plugin-mrim

%package -n pidgin-plugin-mrim
Summary:        Pidgin plugin for Mail.Ru Agent
Group:          Productivity/Networking/Instant Messenger
Requires:       libpurple-plugin-mrim = %{version}
Supplements:    packageand(libpurple-plugin-mrim:pidgin)
%requires_ge    pidgin
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description -n pidgin-plugin-mrim
This is a Mail.Ru Agent plugin for Pidgin.
It provides support for the MRA/MRIM protocol, popular in ex-USSR.

This package provides the icon set for Pidgin.

%prep
%setup -q -n %{_name}-%{version}

%build
%configure --gtk
make %{?_smp_mflags} V=1

%install
%make_install LIBDIR=%{_lib}
%find_lang %{_name}

%files -n libpurple-plugin-mrim
%defattr(-,root,root)
%doc ChangeLog LICENSE README
%{_libdir}/purple-2/libmrim.so

%files -n libpurple-plugin-mrim-lang -f %{_name}.lang
%defattr(-,root,root)
%if 0%{?suse_version} < 1140
%dir %{_datadir}/locale/be_BY/
%dir %{_datadir}/locale/be_BY/LC_MESSAGES/
%endif

%files -n pidgin-plugin-mrim
%defattr(-,root,root)
%dir %{_datadir}/pixmaps/pidgin/
%dir %{_datadir}/pixmaps/pidgin/protocols/
%dir %{_datadir}/pixmaps/pidgin/protocols/*/
%{_datadir}/pixmaps/pidgin/protocols/*/mrim.*

%changelog
