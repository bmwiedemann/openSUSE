#
# spec file for package purple-facebook
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


Name:           purple-facebook
Version:        0.9.6
Release:        0
Summary:        Facebook protocol plugin for libpurple
License:        GPL-2.0+
Group:          Productivity/Networking/Instant Messenger
Url:            https://github.com/dequis/purple-facebook
Source:         https://github.com/dequis/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0) >= 2.28.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(purple)

%description
Purple Facebook implements the Facebook Messenger protocol into
pidgin, finch, and libpurple. While the primary implementation is
for libpurple3, this plugin is backported for libpurple2.

%package -n libpurple-plugin-facebook
Summary:        Facebook protocol plugin for libpurple
Group:          Productivity/Networking/Instant Messenger
Enhances:       libpurple
# purple-facebook was last used in openSUSE Leap 42.2.
Provides:       purple-facebook = %{version}
Obsoletes:      purple-facebook < %{version}

%description -n libpurple-plugin-facebook
Purple Facebook implements the Facebook Messenger protocol into
pidgin, finch, and libpurple. While the primary implementation is
for libpurple3, this plugin is backported for libpurple2.

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -fi
%configure
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%files -n libpurple-plugin-facebook
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/purple-2/libfacebook.so

%changelog
