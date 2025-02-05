#
# spec file for package ibsim
#
# Copyright (c) 2025 SUSE LLC
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


%define git_ver .0.db9c0e46bf23

Name:           ibsim
Version:        0.12
Release:        0
Summary:        InfiniBand fabric simulator for management
License:        BSD-2-Clause OR GPL-2.0-only
Group:          Productivity/Networking/Diagnostic
Source:         ibsim-%{version}%{git_ver}.tar.gz
Patch1:         ibsim-PIE.patch
URL:            https://github.com/linux-rdma/ibsim
BuildRequires:  infiniband-diags-devel
BuildRequires:  libibumad-devel
BuildRequires:  make

%description
ibsim provides simulation of infiniband fabric for using with OFA
OpenSM, diagnostic and management tools.

%prep
%autosetup -p0 -n  %{name}-%{version}%{git_ver}

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{optflags}"
make prefix=%_prefix libpath=%_libdir binpath=%_bindir %{?_smp_mflags}

%install
export CFLAGS="%{optflags}"
export LDFLAGS="%{optflags}"
%make_install prefix=%_prefix libpath=%_libdir binpath=%_bindir

%files
%dir %{_libdir}/umad2sim
%{_libdir}/umad2sim/libumad2sim*.so*
%{_bindir}/ibsim
%{_bindir}/ibsim-run
%doc README TODO net-examples scripts
%license COPYING

%changelog
