#
# spec file for package purple-xmpp-http-upload
#
# Copyright (c) 2020 SUSE LLC
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


%define _name   xmpp-http-upload
Name:           purple-xmpp-http-upload
Version:        0.2.1
Release:        0
Summary:        XMPP HTTP File Upload plugin for libpurple
License:        GPL-3.0-or-later
URL:            https://github.com/Junker/purple-xmpp-http-upload
Source:         https://github.com/Junker/purple-xmpp-http-upload/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(purple)

%description
A XEP-0363: HTTP File Upload plugin for libpurple (Pidgin, Finch).

%package -n libpurple-plugin-%{_name}
Summary:        XMPP HTTP File Upload plugin for libpurple
Enhances:       libpurple

%description -n libpurple-plugin-%{_name}
A XEP-0363: HTTP File Upload plugin for libpurple (Pidgin, Finch).

%prep
%setup -q

%build
%make_build

%install
%make_install
mv %{buildroot}%{_libdir}/purple-2/jabber_http_file_upload.so \
  %{buildroot}%{_libdir}/purple-2/libjabber_http_file_upload.so

%files -n libpurple-plugin-%{_name}
%license LICENSE
%doc README.md
%{_libdir}/purple-2/libjabber_http_file_upload.so

%changelog
