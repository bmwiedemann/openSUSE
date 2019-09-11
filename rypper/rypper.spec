#
# spec file for package rypper
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           rypper
BuildRequires:  perl
Requires:       perl
Requires:       zypper
Summary:        Wrapper around zypper for managing multiple repositories
License:        GPL-3.0+
Group:          System/Packages
Version:        0.24
Release:        0
Url:            http://www.adamspiers.org/computing/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        https://raw.github.com/aspiers/SUSE-dist/master/bin/rypper
Source1:        COPYING
BuildArch:      noarch

%description
rypper is a wrapper around zypper for performing repository operations
in batch.  It allows selection of which repositories to operate on via
a number of different repository selection specifiers.

%prep

%build
pod2man --section=8 $RPM_SOURCE_DIR/rypper > rypper.8
cp $RPM_SOURCE_DIR/COPYING .

%install
install -d %{buildroot}%{_prefix}/bin
install -d %{buildroot}%{_mandir}/man8
install $RPM_SOURCE_DIR/rypper %{buildroot}%{_prefix}/bin
install -m 644 rypper.8 %{buildroot}%{_mandir}/man8

%files
%defattr(-,root,root)
%{_bindir}/rypper
%{_mandir}/man8/*.8.gz
%doc COPYING

%changelog
