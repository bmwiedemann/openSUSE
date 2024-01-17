#
# spec file for package moe
#
# Copyright (c) 2023 SUSE LLC
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


Name:           moe
Version:        1.13
Release:        0
Summary:        A Text Editor
License:        GPL-2.0-or-later
Group:          Productivity/Text/Editors
URL:            https://www.gnu.org/software/moe/moe.html
Source:         https://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.lz
Source1:        https://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.lz.sig
Source2:        http://savannah.gnu.org/people/viewgpg.php?user_id=12809#/%{name}.keyring
BuildRequires:  gcc-c++
BuildRequires:  glibc-devel
BuildRequires:  libstdc++-devel
BuildRequires:  lzip
BuildRequires:  make
BuildRequires:  ncurses-devel

%description
GNU Moe is an 8-bit clean, console text editor for ISO-8859 and ASCII
character encodings. It has a modeless interface, online help,
multiple windows, unlimited undo/redo capability, unlimited line length, global
search/replace (on all buffers at once), block operations, automatic
indentation, word wrapping, file name completion, directory browser, duplicate
removal from prompt histories, delimiter matching, text conversion from/to
UTF-8 and romanization.

%prep
%autosetup

%build
%configure
%make_build CXXFLAGS="%{optflags}"

%install
%make_install install-man

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%config(noreplace) %{_sysconfdir}/moe.conf
%{_bindir}/moe
%{_infodir}/moe.info%{?ext_info}
%{_mandir}/man1/moe.1%{?ext_man}

%changelog
