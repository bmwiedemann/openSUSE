#
# spec file for package aer-inject
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


Name:           aer-inject
Version:        0.2
Release:        0
Summary:        Inject PCIE AER errors into a running kernel
License:        GPL-2.0
Group:          Development/Hardware
Url:            https://git.kernel.org/cgit/linux/kernel/git/gong.chen/aer-inject.git
Source:         %{name}-%{version}.tar.xz
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  make
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
aer-inject allows to inject PCIE AER errors on the software level into
a running Linux kernel. This is intended for validation of the PCIE
driver error recovery handler and PCIE AER core handler.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} PREFIX=/usr/sbin install %{?_smp_mflags}

%files
%defattr(-,root,root)
%{_sbindir}/aer-inject
%doc SPEC README examples

%changelog
