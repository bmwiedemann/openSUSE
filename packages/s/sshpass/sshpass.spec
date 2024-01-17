#
# spec file for package sshpass
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


Name:           sshpass
Version:        1.10
Release:        0
Summary:        Non-interactive SSH authentication utility
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://sshpass.sourceforge.net/
Source0:        https://downloads.sourceforge.net/sshpass/sshpass-%{version}.tar.gz

%description
Tool for non-interactively performing password authentication with so called
"interactive keyboard password authentication" of SSH. Most users should use
more secure public key authentication of SSH instead.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS
%{_bindir}/sshpass
%{_mandir}/man1/sshpass.1%{?ext_man}

%changelog
