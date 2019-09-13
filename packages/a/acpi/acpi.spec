#
# spec file for package acpi
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


Name:           acpi
Version:        1.7
Release:        0
Summary:        Command-line ACPI client
License:        GPL-2.0+
Group:          System/Daemons
Url:            http://sourceforge.net/projects/acpiclient/
Source:         http://sourceforge.net/projects/acpiclient/files/acpiclient/%{version}/%{name}-%{version}.tar.gz
# Package was split from acpid package
Provides:       acpid:%{_bindir}/acpi
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %ix86 x86_64 ia64 aarch64

%description
Linux ACPI client is a small command-line program that attempts to
replicate the functionality of the 'old' apm command on ACPI systems.
It includes battery and thermal information.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README COPYING
%{_bindir}/acpi
%{_mandir}/man1/acpi.1.gz

%changelog
