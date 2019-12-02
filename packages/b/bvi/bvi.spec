#
# spec file for package bvi
#
# Copyright (c) 2019 SUSE LLC
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


Name:           bvi
Version:        1.4.1
Release:        0
Summary:        Editor for binary files
License:        GPL-2.0-or-later
Group:          Productivity/Text/Editors
URL:            http://bvi.sourceforge.net
Source:         http://sourceforge.net/projects/bvi/files/bvi/%{version}/bvi-%{version}.src.tar.gz
BuildRequires:  ncurses-devel

%description
The bvi is a display-oriented editor for binary files, based on the vi
texteditor. If you are familiar with vi, just start the editor and begin to
edit! A bmore program is also included in the package.  If you never heard
about vi, maybe bvi is not the best choice for you.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%license COPYING
%doc CHANGES CREDITS README
%{_bindir}/bmore
%{_bindir}/bvedit
%{_bindir}/bvi
%{_bindir}/bview
%{_datadir}/bvi
%{_mandir}/man1/bvi.1%{?ext_man}
%{_mandir}/man1/bmore.1%{?ext_man}

%changelog
