#
# spec file for package nvptx-tools
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


Name:           nvptx-tools
Version:        1.0+git.20240530.96f8fc5
Release:        0
Summary:        PTX language tools
License:        GPL-3.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/MentorEmbedded/nvptx-tools/
Source:         %{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# Note that w/o a CUDA development (at least cuda.h and libcuda.so) the
# tools for executing are not built.  CUDA is not free software.
BuildRequires:  gcc-c++
# The package is used for NVPTX offloading support in GCC which is currently
# only enabled on x86_64 and aarch64
ExclusiveArch:  x86_64 aarch64

%description
A collection of tools for use with nvptx-none (NVIDIA Parallel Thread
Execution) GCC toolchains.

* nvptx-none-as: "assembler" for PTX.
* nvptx-none-ld: "linker" for PTX.
* nvptx-none-run: run PTX binaries compiled with -mmainkernel.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%files
%defattr(-,root,root)
%dir %{_prefix}/nvptx-none
%{_prefix}/nvptx-none
%{_bindir}/nvptx-none-ar
%{_bindir}/nvptx-none-as
%{_bindir}/nvptx-none-ld
%{_bindir}/nvptx-none-nm
%{_bindir}/nvptx-none-ranlib
%{_bindir}/nvptx-none-run
%doc COPYING3

%changelog
