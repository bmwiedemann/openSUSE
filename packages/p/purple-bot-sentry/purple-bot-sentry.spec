#
# spec file for package purple-bot-sentry
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


%define _name   bot-sentry
Name:           purple-bot-sentry
Version:        1.3.0
Release:        0
Summary:        Libpurple plugin to prevent Instant Message spam
# LICENCE NOTE: COPYING says GPLv3+, but all files are GPLv2+ and the COPYING file comes from autotools magic (2012-01-19 -- vuntz).
License:        GPL-2.0+
Group:          Productivity/Networking/Instant Messenger
Url:            http://pidgin-bs.sourceforge.net/
Source:         http://downloads.sf.net/pidgin-bs/%{_name}-%{version}.tar.bz2
BuildRequires:  intltool
BuildRequires:  libpurple-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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
# pidgin-bot-sentry was last used in openSUSE 12.1.
Provides:       pidgin-%{_name} = %{version}-%{release}
Obsoletes:      pidgin-%{_name} < %{version}-%{release}

%description -n libpurple-plugin-%{_name}
Bot Sentry is a libpurple plug-in to prevent Instant Message spam.
It allows you to ignore IMs unless the sender is in your Buddy List
or Allow List, or the sender correctly answers a question you have
predefined.

%lang_package -n libpurple-plugin-%{_name}

%prep
%setup -q -n %{_name}-%{version}

%build
%configure
make %{?_smp_mflags} V=1

%install
%make_install

%if 0%{?suse_version} < 1140
mv %{buildroot}%{_datadir}/locale/no %{buildroot}%{_datadir}/locale/nb
%endif

find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{_name}

%files -n libpurple-plugin-%{_name}
%defattr(-,root,root)
# FIXME: COPYING is not shipped as it is wrong (about GPLv3+, added by autotools)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/purple-2/%{_name}.so

%files -n libpurple-plugin-%{_name}-lang -f %{_name}.lang
%defattr(-,root,root)

%changelog
