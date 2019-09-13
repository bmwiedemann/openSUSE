#
# spec file for package pidgin-prpltwtr
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


Name:           pidgin-prpltwtr
Version:        0.14.0
Release:        0
Summary:        Libpurple/Pidgin plugin supporting microblogging
License:        GPL-2.0+
Group:          Productivity/Networking/Instant Messenger
Url:            https://github.com/mikeage/prpltwtr
Source:         https://github.com/mikeage/prpltwtr/archive/%{version}.tar.gz#/prpltwtr-%{version}.tar.gz
# PATCH-FIX-OPENSUSE pidgin-prpltwtr-avoid-sover.patch sor.alexei@meowr.ru -- Avoid sover for libprpltwtr.so.
Patch0:         pidgin-prpltwtr-avoid-sover.patch
# PATCH-FIX-UPSTREAM 0001-Fix-html-entities-showing-up-in-tweets.patch
Patch1:         0001-Fix-html-entities-showing-up-in-tweets.patch
# PATCH-FIX-UPSTREAM 0002-Tweak-config-defaults-to-prevent-rate-limits-at-API.patch
Patch2:         0002-Tweak-config-defaults-to-prevent-rate-limits-at-API.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(json-glib-1.0) >= 0.6.2
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(pidgin)
BuildRequires:  pkgconfig(purple)

%description
This is a libpurple Pidgin, Finch, etc plugin which treats
microblogging sites GNU social, Twitter as IM protocols.

%package -n libpurple-plugin-prpltwtr
Summary:        Libpurple/Pidgin plugin supporting microblogging
Group:          Productivity/Networking/Instant Messenger
Enhances:       libpurple
Recommends:     libpurple-plugin-prpltwtr-lang
# pidgin-prpltwtr was last used in openSUSE Leap 42.2.
Provides:       pidgin-prpltwtr = %{version}-%{release}
Obsoletes:      pidgin-prpltwtr < %{version}-%{release}

%description -n libpurple-plugin-prpltwtr
This is a libpurple Pidgin, Finch, etc plugin which treats
microblogging sites GNU social, Twitter as IM protocols.

%lang_package -n libpurple-plugin-prpltwtr

%package -n pidgin-plugin-prpltwtr
Summary:        Libpurple/Pidgin plugin supporting microblogging
Group:          Productivity/Networking/Instant Messenger
Requires:       libpurple-plugin-prpltwtr = %{version}
Supplements:    packageand(libpurple-plugin-prpltwtr:pidgin)
%requires_ge    pidgin

%description -n pidgin-plugin-prpltwtr
This is a Pidgin plugin which treats microblogging sites
GNU social, Twitter as IM protocols.

%prep
%setup -q -n prpltwtr-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
NOCONFIGURE=1 ./autogen.sh
%configure
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -type f -name "*.debug" -delete -print
%find_lang prpltwtr

%files -n libpurple-plugin-prpltwtr
%defattr(-,root,root)
%doc COPYING README.md
%{_libdir}/purple-2/libprpltwtr*.so

%files -n libpurple-plugin-prpltwtr-lang -f prpltwtr.lang
%defattr(-,root,root)

%files -n pidgin-plugin-prpltwtr
%defattr(-,root,root)
%{_libdir}/pidgin/libgtkprpltwtr.so
%{_datadir}/pixmaps/pidgin/protocols/*/prpltwtr.*

%changelog
