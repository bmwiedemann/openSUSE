#
# spec file for package timewarrior
#
# Copyright (c) 2021 SUSE LLC
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


Name:           timewarrior
Version:        1.4.2
Release:        0
Summary:        Command line time tracker
License:        MIT
Group:          Productivity/Office/Organizers
URL:            http://taskwarrior.org/docs/timewarrior/
Source:         https://github.com/GothenburgBitFactory/timewarrior/releases/download/v%{version}/timew-%{version}.tar.gz
Patch0:         timewarrior-build-compare.patch
BuildRequires:  cmake >= 2.8
BuildRequires:  gcc-c++ >= 4.7

%description
Timewarrior is a command line time tracking application, which allows you to
record time spent on activities.

%prep
%setup -q -n timew-%{version}
%patch0 -p1

%build
%cmake \
	-DTIMEW_DOCDIR=%{_datadir}/%{name} \
	.
%cmake_build

%install
%cmake_install
pushd %{buildroot}%{_datadir}/%{name}
rm -fv AUTHORS ChangeLog COPYING INSTALL LICENSE NEWS README.md
chmod -v a+x ext/*
popd

%files
%license LICENSE
%doc ChangeLog AUTHORS README.md
%{_bindir}/timew
%{_mandir}/man1/timew.*
%{_mandir}/man1/timew-*
%{_mandir}/man7/timew-*
%{_datadir}/%{name}

%changelog
