#
# spec file for package pidgin-libnotify
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


Name:           pidgin-libnotify
Version:        0.14
Release:        0
Summary:        Pidgin plugin for notifications using libnotify
License:        GPL-3.0+
Group:          Productivity/Networking/Instant Messenger
Url:            http://gaim-libnotify.sourceforge.net/
Source0:        http://downloads.sf.net/gaim-libnotify/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 0001-don-t-forget-to-set-buddy-object-it-s-required-to-sh.patch -- Don't forget to set buggy object, it's requires to show button to work.
Patch0:         0001-don-t-forget-to-set-buddy-object-it-s-required-to-sh.patch
# PATCH-FIX-UPSTREAM 0002-add-switch-to-disable-showing-msg-txt.patch -- Add switch to disable showing message text.
Patch1:         0002-add-switch-to-disable-showing-msg-txt.patch
# PATCH-FIX-UPSTREAM 0003-add-timeout-setting.patch -- Add timeout setting.
Patch2:         0003-add-timeout-setting.patch
# PATCH-FIX-UPSTREAM 0004-reload-is-not-needed.patch -- Reload is not needed.
Patch3:         0004-reload-is-not-needed.patch
# PATCH-FIX-UPSTREAM 0005-fix-compile-warnings.patch -- Fix compilation warnings.
Patch4:         0005-fix-compile-warnings.patch
# PATCH-FIX-UPSTREAM 0006-fix-build-with-libnotify-0-7.diff -- Fix build with libnotify 0.7.
Patch5:         0006-fix-build-with-libnotify-0-7.diff
# PATCH-FIX-UPSTREAM 0007-no-need-to-notify-if-the-conversation-is-already-ope.patch -- https://github.com/tony2001/pidgin-libnotify/commit/6e0f91d
Patch6:         0007-no-need-to-notify-if-the-conversation-is-already-ope.patch
# PATCH-FIX-UPSTREAM 0008-Make-notifications-work-in-chat-rooms.patch -- https://github.com/tony2001/pidgin-libnotify/commit/2fdb74f
Patch7:         0008-Make-notifications-work-in-chat-rooms.patch
# PATCH-FIX-UPSTREAM 0009-remove-duplicated-option.patch -- https://github.com/tony2001/pidgin-libnotify/commit/5c21fce
Patch8:         0009-remove-duplicated-option.patch
# PATCH-FIX-UPSTREAM 0010-add-option-to-notify-about-all-messages-in-chat-room.patch -- https://github.com/tony2001/pidgin-libnotify/commit/b225a45
Patch9:         0010-add-option-to-notify-about-all-messages-in-chat-room.patch
# PATCH-FIX-UPSTREAM 0011-fix-notify-osd.patch -- Fix working with notify-osd.
Patch10:        0011-fix-notify-osd.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  intltool
BuildRequires:  libnotify-devel
BuildRequires:  libtool
BuildRequires:  pidgin-devel
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Provides an interface to libnotify for Pidgin notifications.

%package -n pidgin-plugin-libnotify
Summary:        Pidgin plugin for notifications using libnotify
Group:          Productivity/Networking/Instant Messenger
Recommends:     pidgin-plugin-libnotify-lang
# pidgin-libnotify was last used in openSUSE Leap 42.2.
Provides:       %{name} = %{version}-%{release}
Obsoletes:      %{name} < %{version}-%{release}
Obsoletes:      %{name}-lang < %{version}-%{release}
%requires_ge    pidgin

%description -n pidgin-plugin-libnotify
Provides an interface to libnotify for Pidgin notifications.

%lang_package -n pidgin-plugin-libnotify

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
autoreconf -fi
%configure \
  --disable-static
make %{?_smp_mflags} V=1

%install
%make_install

find %{buildroot} -type f -name "*.la" -delete -print
%find_lang %{name}

%files -n pidgin-plugin-libnotify
%defattr(-,root,root)
%doc AUTHORS COPYING NEWS TODO
%{_libdir}/purple-2/%{name}.so

%files -n pidgin-plugin-libnotify-lang -f %{name}.lang
%defattr(-,root,root)

%changelog
