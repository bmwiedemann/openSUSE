#
# spec file for package jurand
#
# Copyright (c) 2024 SUSE LLC
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


%{!?_rpmmacrodir:%global _rpmmacrodir %{_rpmconfigdir}/macros.d}
%{!?make_build:%global make_build make %{?_smp_mflags}}
%if 0%{?gcc_version} < 11
%define with_gcc 11
%endif
Name:           jurand
Version:        1.3.2
Release:        0
Summary:        A tool for manipulating Java symbols
License:        Apache-2.0
Group:          Development/Languages/Java
URL:            https://github.com/fedora-java/jurand
Source0:        https://github.com/fedora-java/jurand/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         jurand-cxx20.patch
BuildRequires:  %{rb_default_ruby_suffix}-rubygem-asciidoctor
BuildRequires:  diffutils
BuildRequires:  gcc%{?with_gcc}-c++
BuildRequires:  make
BuildRequires:  xmlto

%description
The tool can be used for patching .java sources in cases where using sed is
insufficient due to Java language syntax. The tool follows Java language rules
rather than applying simple regular expressions on the source code.

%prep
%setup -q
%patch -P 0 -p1

%build

%if 0%{?with_gcc}
export CXX=g++-%{with_gcc}
export CC=gcc-%{with_gcc}
%endif
%make_build test-compile manpages

%install
export buildroot=%{buildroot}
export bindir=%{_bindir}
export rpmmacrodir=%{_rpmmacrodir}
export mandir=%{_mandir}/man7

./install.sh

%check
%if 0%{?with_gcc}
export CXX=g++-%{with_gcc}
export CC=gcc-%{with_gcc}
%endif
%make_build test

%files -f target/installed_files
%dir %{_rpmconfigdir}
%dir %{_rpmmacrodir}
%license LICENSE NOTICE
%doc README.adoc

%changelog
