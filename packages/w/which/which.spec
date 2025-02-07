#
# spec file for package which
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


Name:           which
Version:        2.23
Release:        0
Summary:        Displays where a particular program in your path is located
License:        GPL-3.0-or-later
Group:          System/Base
URL:            https://savannah.gnu.org/projects/which/
Source0:        https://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.gz.sig
Source2:        https://savannah.gnu.org/people/viewgpg.php?user_id=3639#/%{name}.keyring
Provides:       util-linux:%{_bindir}/which

%description
The which command shows the full pathname of a specified program, if the
specified program is in your PATH.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc EXAMPLES README README.alias AUTHORS NEWS
%{_bindir}/which
%{_infodir}/which.info%{?ext_info}
%{_mandir}/man1/which.1%{?ext_man}

%changelog
