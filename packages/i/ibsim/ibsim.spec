#
# spec file for package ibsim
#
# Copyright (c) 2021 SUSE LLC
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


%define git_ver .0.7c2a604ec49a

Summary:        InfiniBand fabric simulator for management
License:        BSD-2-Clause OR GPL-2.0-only
Group:          Productivity/Networking/Diagnostic

Name:           ibsim
Version:        0.9
Release:        0
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         ibsim-%{version}%{git_ver}.tar.gz
Patch1:         ibsim-fix_type_punning.patch
Patch2:         ibsim-PIE.patch
URL:            https://github.com/linux-rdma/ibsim
BuildRequires:  infiniband-diags-devel
BuildRequires:  libibumad-devel
BuildRequires:  make

%description
ibsim provides simulation of infiniband fabric for using with OFA
OpenSM, diagnostic and management tools.

%prep
%setup -q -n  %{name}-%{version}%{git_ver}
%patch1
%patch2 -p1

%build
export CFLAGS="${CFLAGS:-%{optflags}}"
export LDFLAGS="${LDFLAGS:-%{optflags}}"
make prefix=%_prefix libpath=%_libdir binpath=%_bindir %{?_smp_mflags}

%install
export CFLAGS="${CFLAGS:-%{optflags}}"
export LDFLAGS="${LDFLAGS:-%{optflags}}"
make DESTDIR=%{buildroot} prefix=%_prefix libpath=%_libdir binpath=%_bindir install

%files
%defattr(-,root,root)
%dir %{_libdir}/umad2sim
%{_libdir}/umad2sim/libumad2sim*.so*
%{_bindir}/ibsim
%doc README TODO net-examples scripts
%license COPYING

%changelog
