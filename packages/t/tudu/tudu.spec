#
# spec file for package tudu
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


Name:           tudu
Version:        0.10.4
Release:        0
Summary:        A command line interface tasks manager
License:        GPL-3.0-only
Group:          Productivity/Office/Organizers
URL:            https://code.meskio.net/tudu/
Source:         https://code.meskio.net/%{name}/%{name}-%{version}.tar.gz
# Fix configure check which fails due to openSUSE using -Werror=return-value
Patch1:         configure-check.patch
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  ncurses-devel

%description
TuDu is a command line interface to manage hierchical todos.
Each task has a title and description, a deadline and scheduled date as well
as categories and priorities.

%prep
%setup -q
%patch1

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/%{name}
%{_datadir}/%{name}/tudu.dtd
%{_datadir}/%{name}/welcome.xml
%config %{_sysconfdir}/tudurc

%changelog
