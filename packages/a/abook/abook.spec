#
# spec file for package abook
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


Name:           abook
Version:        0.6.1
Release:        0
Summary:        Text-based addressbook program
License:        GPL-2.0-or-later
Group:          Productivity/Other
URL:            http://abook.sourceforge.net/
Source0:        http://abook.sourceforge.net/devel/%{name}-%{version}.tar.gz
Source1:        http://abook.sourceforge.net/devel/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gettext
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
Recommends:     %{name}-lang

%description
Abook is a text-based addressbook program designed to
use with mutt mail client.

%lang_package

%prep
%setup -q

%build
autoreconf -fiv
export CFLAGS="%{optflags} -fgnu89-inline"
%configure
%make_build

%install
%make_install
%find_lang %{name}

%files
%doc AUTHORS BUGS ChangeLog FAQ NEWS README THANKS TODO sample.abookrc
%license COPYING
%{_bindir}/abook
%{_mandir}/man1/abook.*
%{_mandir}/man5/abookrc.*

%files lang -f %{name}.lang
%dir %{_datadir}/locale/*/LC_TIME

%changelog
