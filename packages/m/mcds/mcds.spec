#
# spec file for package mcds
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2019-2024, Martin Hauke <mardnh@gmx.de>
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


Name:           mcds
Version:        1.9
Release:        0
Summary:        Mutt Carddav search program
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Email/Utilities
URL:            https://github.com/t-brown/mcds
Source:         https://github.com/t-brown/mcds/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libgpgme-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libxml-2.0)

%description
mcds is a command line tool primarily used as a search query plugin
for mutt to query a carddav server.

%prep
%setup -q

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license LICENSE
%doc AUTHORS ChangeLog NEWS README.md
%{_bindir}/mcds
%{_mandir}/man1/mcds.1%{?ext_man}

%changelog
