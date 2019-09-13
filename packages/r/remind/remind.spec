#
# spec file for package remind
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           remind
Version:        3.1.15
Release:        0
%define tar_version 03.01.15
Summary:        A sophisticated calendar and alarm program
License:        GPL-2.0
Group:          Productivity/Office/Organizers
Url:            http://www.roaringpenguin.com/products/remind
Source0:        %{name}-%{tar_version}.tar.gz
Source100:      %{name}-%{version}-rpmlintrc
Patch0:         remind-nostrip.patch
Requires:       tcllib
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc %{_mandir}/man1/cm2rem.1%{ext_man}
%doc %{_mandir}/man1/rem.1%{ext_man}
%doc %{_mandir}/man1/rem2ps.1%{ext_man}
%doc %{_mandir}/man1/remind.1%{ext_man}
%doc %{_mandir}/man1/tkremind.1%{ext_man}
%attr(0755,root,root) %{_bindir}/cm2rem.tcl
%attr(0755,root,root) %{_bindir}/rem
%attr(0755,root,root) %{_bindir}/rem2ps
%attr(0755,root,root) %{_bindir}/remind
%attr(0755,root,root) %{_bindir}/tkremind

%changelog
