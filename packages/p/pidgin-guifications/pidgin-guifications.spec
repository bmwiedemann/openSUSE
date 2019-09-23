#
# spec file for package pidgin-guifications
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


%define _name   guifications
Name:           pidgin-guifications
Version:        2.16
Release:        0
Summary:        Pidgin plugin to display "toaster" popups
License:        GPL-2.0+
Group:          Productivity/Networking/Instant Messenger
Url:            https://guifications.org/
Source:         https://bitbucket.org/rw_grim/guifications2/downloads/%{name}-%{version}.tar.bz2
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  libxml2-devel
BuildRequires:  pango-devel
BuildRequires:  pidgin-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Guifications is a Pidgin plugin that displays "toaster" popups in a
user-defined corner of the screen, similar to features to be seen
in other common messenger clients. It's highly configurable, easy
to use, and has theme support. It really is the end-all, be-all
toaster pop-up plugin for Pidgin!

%package -n pidgin-plugin-%{_name}
Summary:        Pidgin plugin to display "toaster" popups
Group:          Productivity/Networking/Instant Messenger
Recommends:     pidgin-plugin-%{_name}-lang
# pidgin-guifications was last used in openSUSE 12.1.
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}
# pidgin-guifications-lang was last used in openSUSE Leap 42.2.
Obsoletes:      %{name}-lang < %{version}-%{release}
%requires_ge    pidgin

%description -n pidgin-plugin-%{_name}
Guifications is a Pidgin plugin that displays "toaster" popups in a
user-defined corner of the screen, similar to features to be seen
in other common messenger clients. It's highly configurable, easy
to use, and has theme support. It really is the end-all, be-all
toaster pop-up plugin for Pidgin!

%lang_package -n pidgin-plugin-%{_name}

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} V=1

%install
%make_install

%if 0%{?suse_version} < 1140
mv %{buildroot}%{_datadir}/locale/no %{buildroot}%{_datadir}/locale/nb
mv %{buildroot}%{_datadir}/locale/sr@Latn %{buildroot}%{_datadir}/locale/sr@latin
%endif

find %{buildroot} -type f -name "*.la" -delete -print
%find_lang guifications

%files -n pidgin-plugin-%{_name}
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README TODO
%{_libdir}/pidgin/%{_name}.so
%{_datadir}/pixmaps/pidgin/%{_name}/

%files -n pidgin-plugin-%{_name}-lang -f %{_name}.lang
%defattr(-,root,root)

%changelog
