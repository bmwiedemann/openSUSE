#
# spec file for package pidgin-advanced-sound-notification
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pidgin-advanced-sound-notification
Version:        1.2.1
Release:        0
Summary:        Pidgin plugin adding sound notifications
License:        GPL-2.0+
Group:          Productivity/Networking/Instant Messenger
Url:            https://launchpad.net/pidgin-advanced-sound-notification
Source:         https://launchpad.net/pidgin-advanced-sound-notification/trunk/%{version}/+download/%{name}-%{version}.tar.gz
Source1:        https://launchpad.net/pidgin-advanced-sound-notification/trunk/%{version}/+download/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  intltool
BuildRequires:  pidgin-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This plugin adds sounds for some sound notifications to Pidgin
(e.g. "Incoming Filetransfer" or "Authentication requested").

%package -n pidgin-plugin-advanced-sound-notification
Summary:        Pidgin plugin adding sound notifications
Group:          Productivity/Networking/Instant Messenger
Recommends:     pidgin-plugin-advanced-sound-notification-lang
Obsoletes:      %{name}-lang < %{version}-%{release}
%requires_ge    pidgin

%description -n pidgin-plugin-advanced-sound-notification
This plugin adds sounds for some sound notifications to Pidgin
(e.g. "Incoming Filetransfer" or "Authentication requested").

%lang_package -n pidgin-plugin-advanced-sound-notification

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags} V=1

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%files -n pidgin-plugin-advanced-sound-notification
%defattr (-,root,root)
%doc AUTHORS ChangeLog COPYING
%{_libdir}/pidgin/%{name}.so
%dir %{_datadir}/sounds/pidgin/
%{_datadir}/sounds/pidgin/%{name}/

%files -n pidgin-plugin-advanced-sound-notification-lang -f %{name}.lang
%defattr(-,root,root)

%changelog
