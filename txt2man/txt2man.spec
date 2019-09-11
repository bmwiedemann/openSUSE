#
# spec file for package txt2man
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           txt2man
Version:        1.6.0
Release:        0
Summary:        Convert Flat ASCII Text to man Page Format
License:        GPL-2.0-or-later
Group:          Development/Tools/Doc Generators
URL:            https://github.com/mvertes/txt2man
Source0:        https://github.com/mvertes/txt2man/archive/%{name}-%{version}.tar.gz
Requires:       gawk
BuildArch:      noarch

%description
Txt2man converts flat ASCII text to man page format. It is a shell
script using gnu awk, that should run on any Unix like system.

%prep
%setup -q -n txt2man-txt2man-1.6.0

%build

%install
install -Dpm 0755 bookman %{buildroot}%{_bindir}/bookman
install -Dpm 0755 src2man %{buildroot}%{_bindir}/src2man
install -Dpm 0755 txt2man %{buildroot}%{_bindir}/txt2man
install -Dpm 0644 bookman.1 %{buildroot}%{_mandir}/man1/bookman.1
install -Dpm 0644 src2man.1 %{buildroot}%{_mandir}/man1/src2man.1
install -Dpm 0644 txt2man.1 %{buildroot}%{_mandir}/man1/txt2man.1

%files
%license COPYING
%doc Changelog README
%{_bindir}/bookman
%{_bindir}/src2man
%{_bindir}/txt2man
%{_mandir}/man1/bookman.1%{?ext_man}
%{_mandir}/man1/src2man.1%{?ext_man}
%{_mandir}/man1/txt2man.1%{?ext_man}

%changelog
