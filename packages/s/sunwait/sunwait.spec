#
# spec file for package sunwait
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           sunwait
Version:        20041208
Release:        0
Summary:        Sunrise, sunset and twilight calculator
License:        GPL-2.0-or-later
Group:          Productivity/Scientific/Astronomy
URL:            http://www.risacher.org/sunwait
Source:         http://www.risacher.org/sunwait/%{name}-%{version}.tar.gz
Patch0:         sunwait-no-rpm-opt-flags.patch
Patch1:         sunwait-implicit-declaration.patch
Patch2:         sunwait-no-return-in-nonvoid-function.patch
BuildRequires:  gcc

%description
Sunwait is a small C program for calculating sunrise and sunset, as well as
civil, nautical, and astronomical twilights. It has features that make it
useful for home automation tasks.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%make_build

%install
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 sunwait %{buildroot}%{_bindir}

%files
%license COPYING
%{_bindir}/sunwait

%changelog
