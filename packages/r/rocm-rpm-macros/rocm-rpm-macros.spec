#
# spec file for package rocm-rpm-macros
#
# Copyright Fedora Project Authors.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           rocm-rpm-macros
Version:        6.4.2
Release:        2%{?dist}
Summary:        ROCm RPM macros
License:        GPL-2.0-or-later

URL:            https://github.com/trixirt/rocm-rpm-macros
Source0:        macros.rocm
Source1:        GPL
# Modules
Source2:        default
Source3:        gfx8
Source4:        gfx9
Source5:        gfx10
Source6:        gfx11
Source7:        gfx906
Source8:        gfx908
Source9:        gfx90a
Source10:       gfx942
Source11:       gfx1031
Source12:       gfx1036
Source13:       gfx1100
Source14:       gfx1101
Source15:       gfx1102
Source16:       gfx1103
Source17:       default.rhel
Source18:       gfx12
Source19:       gfx950

# Just some files
%global debug_package %{nil}

Requires:       rpm
%if 0%{?suse_version}
Requires:       Modules
%else
Requires:       environment-modules
%endif
# Only infra files
BuildArch:      noarch
# ROCm only working on x86_64
ExclusiveArch:  x86_64

%description
This package contains ROCm RPM macros for building ROCm packages.

# To use, run
# $> source /etc/profile.d/modules.sh

%package modules
Summary:        ROCm enviroment modules
%if 0%{?suse_version}
Requires:       Modules
%else
Requires:       cmake-filesystem
Requires:       rocm-llvm-filesystem
Requires:       environment(modules)
%endif

%description modules
This package contains ROCm environment modules for switching
between different GPU families.

%prep
%setup -cT
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .
mkdir modules
%if 0%{?rhel}
install -pm 644 %{SOURCE17} modules/default
%else
install -pm 644 %{SOURCE2} modules
%endif
install -pm 644 %{SOURCE3} modules
install -pm 644 %{SOURCE4} modules
install -pm 644 %{SOURCE5} modules
install -pm 644 %{SOURCE6} modules
install -pm 644 %{SOURCE7} modules
install -pm 644 %{SOURCE8} modules
install -pm 644 %{SOURCE9} modules
install -pm 644 %{SOURCE10} modules
install -pm 644 %{SOURCE11} modules
install -pm 644 %{SOURCE12} modules
install -pm 644 %{SOURCE13} modules
install -pm 644 %{SOURCE14} modules
install -pm 644 %{SOURCE15} modules
install -pm 644 %{SOURCE16} modules
install -pm 644 %{SOURCE18} modules
install -pm 644 %{SOURCE19} modules

%install
mkdir -p %{buildroot}%{_rpmmacrodir}/
install -Dpm 644 %{SOURCE0} %{buildroot}%{_rpmmacrodir}/
%if 0%{?suse_version}
mkdir -p %{buildroot}%{_datadir}/modules/rocm/
cp -p modules/* %{buildroot}%{_datadir}/modules/rocm/
%else
mkdir -p %{buildroot}%{_datadir}/modulefiles/rocm/
cp -p modules/* %{buildroot}%{_datadir}/modulefiles/rocm/
%endif

%files
%license GPL
%{_rpmmacrodir}/macros.rocm

%files modules
%license GPL
%if 0%{?suse_version}
%{_datadir}/modules
%else
%{_datadir}/modulefiles/rocm/
%endif

%changelog
