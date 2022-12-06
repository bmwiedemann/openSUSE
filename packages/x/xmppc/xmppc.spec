#
# spec file for package xmppc
#
# Copyright (c) 2022 SUSE LLC
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


Name:           xmppc
Version:        0.1.2
Release:        0
Summary:        Command Line Interface Tool for XMPP
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Instant Messenger
URL:            https://codeberg.org/Anoxinon_e.V./xmppc
Source:         https://codeberg.org/Anoxinon_e.V./xmppc/archive/%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  glib2-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  libgpgme-devel
BuildRequires:  libstrophe-devel
BuildRequires:  libtool

%description
xmppc is a XMPP command line interface client.

%prep
%setup -q -n %{name}

%build
./bootstrap.sh
%configure
%make_build

%install
%make_install

%files
%license LICENSE
%doc changelog README.md
%{_bindir}/xmppc
%dir %{_datadir}/doc/xmppc
%{_datadir}/doc/xmppc/README.md
%{_datadir}/doc/xmppc/xmppc.1.html
%{_mandir}/man1/xmppc.1%{?ext_man}

%changelog
