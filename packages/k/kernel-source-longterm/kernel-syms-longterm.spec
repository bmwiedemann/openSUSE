#
# spec file for package kernel-syms-longterm
#
# Copyright (c) 2026 SUSE LLC
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


%define git_commit bd5d4c2ccc3fe8659f3ec78f6f1d1c20f15753ce
%define variant -longterm%{nil}

%include %_sourcedir/kernel-spec-macros

Name:           kernel-syms-longterm
Version:        6.12.74
%if 0%{?is_kotd}
Release:        <RELEASE>.gbd5d4c2
%else
Release:        0
%endif
Summary:        Kernel Symbol Versions (modversions)
License:        GPL-2.0-only
Group:          Development/Sources
URL:            https://www.kernel.org/
BuildRequires:  coreutils
ExclusiveArch:  aarch64 x86_64
Prefix:         /usr/src
AutoReqProv:    off
Source:         README.KSYMS
%ifarch aarch64 x86_64
Requires:       kernel-longterm-devel = %version-%source_rel
%endif
Requires:       kernel-devel%variant = %version-%source_rel
Provides:       %name = %version-%source_rel
Provides:       %name-srchash-%git_commit
Provides:       multiversion(kernel)

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

%files
%dir %_docdir/%name
%_docdir/%name/README.SUSE

%prep

%install
install -m 644 -D %{SOURCE0} %buildroot/%_docdir/%name/README.SUSE

%changelog
