#
# spec file for package abook
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           abook
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
Recommends:     %{name}-lang
Summary:        Text-based addressbook program
License:        GPL-2.0-or-later
Group:          Productivity/Other
Version:        0.6.1
Release:        0
Source0:        http://abook.sourceforge.net/devel/%{name}-%{version}.tar.gz
Source1:        http://abook.sourceforge.net/devel/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Url:            http://abook.sourceforge.net/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Abook is a text-based addressbook program designed to
use with mutt mail client.

%lang_package

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -fiv
export CFLAGS="%{optflags} -fgnu89-inline"
%configure
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name}

%files
%defattr(-,root,root)
%doc AUTHORS BUGS ChangeLog FAQ NEWS README THANKS TODO sample.abookrc
%license COPYING
%{_bindir}/abook
%{_mandir}/man1/abook.*
%{_mandir}/man5/abookrc.*

%files lang -f %{name}.lang
%defattr(-,root,root)

%changelog
