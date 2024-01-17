#
# spec file for package pidgin-privacy-please
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


Name:           pidgin-privacy-please
Version:        0.7.1
Release:        0
Summary:        Anti-spam plugin for Pidgin
License:        GPL-3.0+
Group:          Productivity/Networking/Instant Messenger
Url:            https://github.com/cockroach/pidgin-privacy-please
Source:         https://github.com/cockroach/%{name}/archive/release-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pidgin-devel
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Pidgin Privacy Please is an anti-spam plugin for the Pidgin instant
messenger. It offers the following features:
 * Block individual users.
 * Auto-reply to blocked messages.
 * Block messages from people who are not on your contact list
   (with an optional auto-reply).
 * Block messages using regular expressions, either against the
   message sender, the message content, or both.
 * Suppress repeated/all authorisation requests.
 * Suppress ICQ/AIM authorisation requests.
 * Suppress authorisation requests that contain hyperlinks.
 * Automatically show user info on authorisation requests.
 * Block jabber headline messages.
 * Block AOL system messages.
 * Challenge-response bot-check.

%package -n pidgin-plugin-privacy-please
Summary:        Anti-spam plugin for Pidgin
Group:          Productivity/Networking/Instant Messenger
Recommends:     pidgin-plugin-privacy-please-lang
%requires_ge    pidgin

%description -n pidgin-plugin-privacy-please
Pidgin Privacy Please is an anti-spam plugin for the Pidgin instant
messenger. It offers the following features:
 * Block individual users.
 * Auto-reply to blocked messages.
 * Block messages from people who are not on your contact list
   (with an optional auto-reply).
 * Block messages using regular expressions, either against the
   message sender, the message content, or both.
 * Suppress repeated/all authorisation requests.
 * Suppress ICQ/AIM authorisation requests.
 * Suppress authorisation requests that contain hyperlinks.
 * Automatically show user info on authorisation requests.
 * Block jabber headline messages.
 * Block AOL system messages.
 * Challenge-response bot-check.

%lang_package -n pidgin-plugin-privacy-please

%prep
%setup -q -n %{name}-release-%{version}

%build
NOCONFIGURE=1 ./autogen.sh
%configure
make %{?_smp_mflags} V=1

%install
%make_install

%find_lang %{name}
find %{buildroot} -type f -name "*.la" -delete -print

%files -n pidgin-plugin-privacy-please
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/pidgin/libpidgin_pp.so

%files -n pidgin-plugin-privacy-please-lang -f %{name}.lang
%defattr(-,root,root)

%changelog
