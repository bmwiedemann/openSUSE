#
# spec file for package ketchup
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           ketchup
Version:        1.0.1
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         %{name}-%{version}.tar.bz2
Summary:        Tool for downloading and updating Linux kernel source trees
License:        GPL-2.0+
Group:          Development/Tools/Other
BuildArch:      noarch
Url:            http://www.selenic.com/ketchup/

%description
This tool synchronises a local kernel tree with a desired kernel ver-
sion and patch set from a kernel.org mirror. The default requires a GPG
key on your keyring, to verify the identity of the patches and source
archives. Entire kernel images are not downloaded unless necessary, so
bandwidth is saved. Patches are applied and removed as necessary to
attain the requested version.



Authors:
--------
    Matt Mackall <mpm@selenic.com>

%prep
%setup -c %{name}-%{version}

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1
install -m 0755 ketchup $RPM_BUILD_ROOT/%{_bindir}
install -m 0755 contrib/quilt-pop $RPM_BUILD_ROOT/%{_bindir}
install -m 0755 contrib/quilt-push $RPM_BUILD_ROOT/%{_bindir}
install -m 0644 ketchup.1 $RPM_BUILD_ROOT/%{_mandir}/man1
gzip $RPM_BUILD_ROOT/%{_mandir}/man1/*.1

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%{_bindir}/ketchup
%{_bindir}/quilt-pop
%{_bindir}/quilt-push
%{_mandir}/man1/ketchup.1.gz

%changelog
