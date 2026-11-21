#
# spec file for package guile-redis
#
# Copyright (c) 2026 SUSE LLC
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


Name:           guile-redis
Version:        2.2.0
Release:        0
Summary:        Redis module for Guile
License:        GPL-3.0-or-later
URL:            https://github.com/aconchillo/guile-redis
Source0:        https://download.savannah.gnu.org/releases/guile-redis/%{name}-%{version}.tar.gz
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(guile-3.0) >= 2.2
Requires:       guile >= 2.2

%description
guile-redis is a Guile module for the Redis key-value data store. It
provides all commands up to Redis 7.0 and supports multiple commands,
pipelining and Pub/Sub.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS NEWS README
%{_datadir}/guile*
%{_libdir}/guile*

%changelog
