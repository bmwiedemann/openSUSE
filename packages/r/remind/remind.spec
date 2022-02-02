#
# spec file for package remind
#
# Copyright (c) 2022 SUSE LLC
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


Name:           remind
Version:        3.3.12
Release:        0
%define tar_version 03.03.12
Summary:        A sophisticated calendar and alarm program
License:        GPL-2.0-only
Group:          Productivity/Office/Organizers
URL:            http://www.roaringpenguin.com/products/remind
Source0:        %{name}-%{tar_version}.tar.gz
Source100:      %{name}-rpmlintrc
Patch0:         remind-nostrip.patch
BuildRequires:  perl
BuildRequires:  perl-Getopt-Long-Descriptive
BuildRequires:  perl-JSON-MaybeXS
Requires:       perl
Requires:       perl-Getopt-Long-Descriptive
Requires:       perl-JSON-Any
Requires:       tcllib

%description
Remind is a sophisticated calendar and alarm program.
It includes the following features:

* A sophisticated scripting language and intelligent
  handling of exceptions and holidays.
* Plain-text, PostScript and HTML output.
* Timed reminders and pop-up alarms.
* A friendly graphical front-end for people who don't
  want to learn the scripting language.
* Facilities for both the Gregorian and Hebrew calendars.
* Support for 12 different languages.

%prep
%setup -q -n %{name}-%{tar_version}
%patch0 -p1

%build
CFLAGS="%{optflags}" ./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

##%%check
##make test

%files
%defattr(-,root,root,-)
%doc %{_mandir}/man1/rem.1%{ext_man}
%doc %{_mandir}/man1/rem2ps.1%{ext_man}
%doc %{_mandir}/man1/remind.1%{ext_man}
%doc %{_mandir}/man1/tkremind.1%{ext_man}

%{_bindir}/rem
%attr(0755,root,root) %{_bindir}/rem2ps
%attr(0755,root,root) %{_bindir}/remind
%attr(0755,root,root) %{_bindir}/tkremind
%attr(0755,root,root) %{_bindir}/rem2html

%changelog
