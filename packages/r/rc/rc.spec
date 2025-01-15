#
# spec file for package harec
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


%define  haredir  %{_usrsrc}/hare
Name:           rc
Release:        0
Version:        0+git.1725436050.2b2d211
Summary:        A simple shell
URL:            https://git.sr.ht/~sircmpwn/rc
Source0:        %{name}-%{version}.tar.zst
# PATCH-FIX-OPENSUSE no-rebuild.patch mcepl@suse.com
# rc target is quite certainly not PHONY (REJECTed upstream)
Patch0:         no-rebuild.patch
BuildRequires:  make
BuildRequires:  hare
BuildRequires:  madeline
BuildRequires:  scdoc
BuildRequires:  zstd
# For testing
BuildRequires:  bc
# End testing
# Because it conflicts with /usr/bin/rc
Conflicts:      rtags
License:        GPL-3.0-only

%description
rc is an experimental shell for Unix inspired by Plan 9's rc.

More information on the original rc is at
https://doc.cat-v.org/plan_9/4th_edition/papers/rc, or
https://en.wikipedia.org/wiki/Rc.

%prep
%autosetup -p1

%build
%make_build


%install
# Shells should go to /bin
%make_install PREFIX="%{_prefix}"


%check
make check

%files
%{_bindir}/%{name}*
%license COPYING
%doc README.md
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
