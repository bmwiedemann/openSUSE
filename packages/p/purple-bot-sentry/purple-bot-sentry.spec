#
# spec file for package purple-bot-sentry
#
# Copyright (c) 2026 SUSE LLC and contributors
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%define _name   bot-sentry
Name:           purple-bot-sentry
Version:        1.3.0
Release:        0
Summary:        Libpurple plugin to prevent Instant Message spam
# LICENCE NOTE: COPYING says GPLv3+, but all files are GPLv2+ and the COPYING file comes from autotools magic (2012-01-19 -- vuntz).
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            http://pidgin-bs.sourceforge.net/
Source0:        http://downloads.sf.net/pidgin-bs/%{_name}-%{version}.tar.bz2
Source1:        https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
BuildRequires:  intltool
BuildRequires:  pkgconfig(purple) < 3.0

%description
Bot Sentry is a libpurple plug-in to prevent Instant Message spam.
It allows you to ignore IMs unless the sender is in your Buddy List
or Allow List, or the sender correctly answers a question you have
predefined.

%package -n libpurple-plugin-%{_name}
Summary:        Libpurple plugin to prevent Instant Message spam
Group:          Productivity/Networking/Instant Messenger
Recommends:     libpurple-plugin-%{_name}-lang
Enhances:       libpurple
Provides:       pidgin-%{_name} = %{version}-%{release}
Obsoletes:      pidgin-%{_name} < %{version}-%{release}

%description -n libpurple-plugin-%{_name}
Bot Sentry is a libpurple plug-in to prevent Instant Message spam.
It allows you to ignore IMs unless the sender is in your Buddy List
or Allow List, or the sender correctly answers a question you have
predefined.

%lang_package -n libpurple-plugin-%{_name}

%prep
%autosetup -n %{_name}-%{version}
cp %{SOURCE1} .

%build
%configure
%make_build

%install
%make_install
%find_lang %{_name}

find %{buildroot} -type f -name "*.la" -delete -print

%files -n libpurple-plugin-%{_name}
%license gpl-2.0.txt
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/purple-2/%{_name}.so

%files -n libpurple-plugin-%{_name}-lang -f %{_name}.lang

%changelog
