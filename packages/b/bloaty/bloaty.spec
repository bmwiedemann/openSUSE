#
# spec file for package creduce
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


Name:           bloaty
Version:        0.0.1+git.20161109.ca41835
Release:        0
Summary:        Bloaty McBloatface: a size profiler for binaries
License:        Apache-2.0
Group:          Development/Tools/Other
Url:		https://github.com/google/bloaty
Source0:	%{name}-%{version}.tar.xz
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Bloaty McBloatface will show you a size profile of ELF or Mach-O
binaries so you can understand what is taking up space inside.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
install -d %{buildroot}/%{_bindir}
install %{name} %{buildroot}%{_bindir}

%files
%defattr(-,root,root)
%doc LICENSE
%{_bindir}/bloaty

%changelog
