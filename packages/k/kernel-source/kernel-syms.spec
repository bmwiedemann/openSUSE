#
# spec file for package kernel-syms
#
# Copyright (c) 2022 SUSE LLC
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


%define variant %{nil}

%include %_sourcedir/kernel-spec-macros

Name:           kernel-syms
Summary:        Kernel Symbol Versions (modversions)
License:        GPL-2.0-only
Group:          Development/Sources
Version:        6.1.0
%if %using_buildservice
%if 0%{?is_kotd}
Release:        <RELEASE>.gab10a11
%else
Release:        0
%endif
%else
%define kernel_source_release %(LC_ALL=C rpm -q kernel-devel%variant-%version --qf "%{RELEASE}" | grep -v 'not installed' || echo 0)
Release:        %kernel_source_release
%endif
URL:            https://www.kernel.org/
AutoReqProv:    off
BuildRequires:  coreutils
%ifarch aarch64
Requires:       kernel-64kb-devel = %version-%source_rel
%endif
%ifarch aarch64 armv6hl armv7hl %ix86 ppc64 ppc64le riscv64 s390x x86_64
Requires:       kernel-default-devel = %version-%source_rel
%endif
%ifarch armv7hl
Requires:       kernel-lpae-devel = %version-%source_rel
%endif
%ifarch %ix86
Requires:       kernel-pae-devel = %version-%source_rel
%endif
Requires:       pesign-obs-integration
Provides:       %name = %version-%source_rel
Provides:       %name-srchash-ab10a112debd048481eeb4d1d93a7b2366be6072
Provides:       multiversion(kernel)
Source:         README.KSYMS
Requires:       kernel-devel%variant = %version-%source_rel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  %ix86 aarch64 armv6hl armv7hl ppc64 ppc64le riscv64 s390x x86_64
Prefix:         /usr/src

# Force bzip2 instead of lzma compression to
# 1) allow install on older dist versions, and
# 2) decrease build times (bsc#962356 boo#1175882)
%define _binary_payload w9.bzdio

%description
Kernel symbols, such as functions and variables, have version
information attached to them. This package contains the symbol versions
for the standard kernels.

This package is needed for compiling kernel module packages with proper
package dependencies.


%source_timestamp
%prep

%install
install -m 644 -D %{SOURCE0} %buildroot/%_docdir/%name/README.SUSE

%files
%defattr(-, root, root)
%dir %_docdir/%name
%_docdir/%name/README.SUSE

%changelog
