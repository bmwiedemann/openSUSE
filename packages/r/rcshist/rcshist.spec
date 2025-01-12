#
# spec file for package rcshist
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


Name:           rcshist
Version:        t20250101
Release:        0
Summary:        Display RCS change history
License:        BSD-Source-Code
Group:          Development/Tools/Version Control
URL:            https://invisible-island.net/rcshist/rcshist.html
Source:         https://github.com/ThomasDickey/rcshist-snapshots/archive/%{version}.tar.gz#/%{name}-snapshots-%{version}.tar.gz

%description
This utility displays the complete revision history of a set of
RCS files including log messages and patches. The output is sorted in
reverse date order over all revisions of all files.

%prep
%autosetup -n %{name}-snapshots-%{version}

%build
%configure
%make_build

%install
%make_install

%check

%files
%license COPYING
%doc CHANGES
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
