#
# spec file for package blame
#
# Copyright (c) 2025 SUSE LLC
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


%define origversion 1.4
%define tversion t20250101

Name:           blame
Version:        %{origversion}+%{tversion}
Release:        0
Summary:        An RCS file annotator
License:        GPL-2.0-only
Group:          Development/Tools/Version Control
URL:            https://invisible-island.net/rcs-blame/rcs-blame.html
Source:         https://github.com/ThomasDickey/rcs-blame-snapshots/archive/refs/tags/%{tversion}.tar.gz#/rcs-%{name}-snapshots-%{tversion}.tar.gz

%description
Blame displays the last modification for each line in an RCS file.
It is the RCS equivalent of CVS's "annotate" command.

%prep
%autosetup -n rcs-%{name}-snapshots-%{tversion}

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
