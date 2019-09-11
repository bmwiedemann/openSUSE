#
# spec file for package pidgin-birthday-reminder
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2011 Christoph Miebach <christoph.miebach@web.de>
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


Name:           pidgin-birthday-reminder
Version:        1.12
Release:        0
Summary:        Pidgin plugin to remind you of the birthdays of your buddies
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Instant Messenger
Url:            https://github.com/kgraefe/pidgin-birthday-reminder
Source:         https://github.com/kgraefe/pidgin-birthday-reminder/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://github.com/kgraefe/pidgin-birthday-reminder/releases/download/v%{version}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(pidgin)

%description
Pidgin Birthday Reminder reminds you of your buddies birthdays.
Birthdays can be set by hand or be automatically filled-in for ICQ,
Skype and XMPP protocols.

%package -n pidgin-plugin-birthday-reminder
Summary:        Pidgin plugin to remind you of the birthdays of your buddies
Group:          Productivity/Networking/Instant Messenger
%requires_ge    pidgin
Recommends:     pidgin-plugin-birthday-reminder-lang
# pidgin-birthday-reminder was last used in openSUSE 12.1.
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
# pidgin-birthday-reminder-lang was last used in openSUSE Leap 14.2.
Obsoletes:      %{name}-lang < %{version}

%description -n pidgin-plugin-birthday-reminder
Pidgin Birthday Reminder reminds you of your buddies birthdays.
Birthdays can be set by hand or be automatically filled-in for ICQ,
Skype and XMPP protocols.

%lang_package -n pidgin-plugin-birthday-reminder

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags} V=1

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%files -n pidgin-plugin-birthday-reminder
%if 0%{?suse_version} >= 1500
%license COPYING
%else
%doc COPYING
%endif
%doc AUTHORS.md CHANGES.md
%{_libdir}/pidgin/birthday_reminder.so
%{_datadir}/pixmaps/pidgin/birthday_reminder/
%dir %{_datadir}/sounds/pidgin/
%{_datadir}/sounds/pidgin/birthday_reminder/
%dir %{_datadir}/appdata/
%{_datadir}/appdata/%{name}.metainfo.xml

%files -n pidgin-plugin-birthday-reminder-lang -f %{name}.lang

%changelog
