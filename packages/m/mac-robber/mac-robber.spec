#
# spec file for package mac-robber
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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



Name:           mac-robber
Version:        1.02
Release:        1
Summary:        Tool to create a timeline of file activity for mounted file systems

License:        GPL-2.0+
Url:            http://sourceforge.net/projects/mac-robber/
Group:          Productivity/Security
Source0:        http://downloads.sourceforge.net/mac-robber/mac-robber-%{version}.tar.gz
Source1:        mac-robber.1
# PATCH-FIX-OPENSUSE pth@suse.de Fix function declarations
Patch0:         mac-robber-codecleanup.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
mac-robber is a digital forensics and incident response tool that can be used
with The Sleuth Kit to create a timeline of file activity for mounted
file systems.

%prep
%setup -q
%patch0

%build
make %{?_smp_mflags} GCC_OPT="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_mandir}/man1
install -pm 0755 mac-robber %{buildroot}%{_bindir}
install -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1
gzip -9 %{buildroot}%{_mandir}/man1/%{name}.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc CHANGES COPYING README
%{_bindir}/mac-robber
%{_mandir}/man1/*.gz

%changelog
