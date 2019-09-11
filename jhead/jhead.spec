#
# spec file for package jhead
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           jhead
Version:        3.00
Release:        0
Summary:        Tool to Manipulate the Nonimage Part of EXIF Compliant JPEG Files
License:        SUSE-Public-Domain
Group:          Productivity/Graphics/Other
Url:            http://www.sentex.net/~mwandel/jhead/
Source0:        http://www.sentex.net/~mwandel/jhead/jhead-%{version}.tar.gz
Source1:        %{name}.changes
Patch0:         CVE-2018-6612.patch
# PATCH-FIX-SECURITY CVE-2016-3822.patch CVE-2016-3822 boo1108480 sbrabec@suse.com -- Integer overflow fix from Debian (31_CVE-2016-3822.patch).
Patch1:         CVE-2016-3822.patch
# PATCH-FIX-SECURITY CVE-2018-17088.patch CVE-2018-17088 boo1108672 sbrabec@suse.com -- Integer overflow fix.
Patch2:         CVE-2018-17088.patch
# PATCH-FIX-SECURITY CVE-2018-16554.patch CVE-2018-16554 boo1108480 mcalabkova@suse.com -- Buffer overflow fix.
Patch3:         CVE-2018-16554.patch
Requires:       %{_bindir}/jpegtran
Requires:       %{_bindir}/mogrify
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Jhead is a command line utility for extracting digital camera settings
from the EXIF format files used by many digital cameras. It handles the
various confusing ways these can be expressed and displays them as
F-stop, shutter speed, and more. It is also able to reduce the size of
digital camera JPEG files without loss of information by deleting
thumbnails that digital cameras put into the EXIF header.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE1}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""

%build
make %{?_smp_mflags} CC="cc %{optflags} -D__DATE__=$DATE"

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -m 755 jhead %{buildroot}%{_bindir}
install -m 644 jhead.1  %{buildroot}%{_mandir}/man1

%files
%defattr(-,root,root)
%doc changes.txt readme.txt usage.html
%{_bindir}/*
%{_mandir}/man1/*.*

%changelog
