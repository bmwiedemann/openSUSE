#
# spec file for package nvptx-tools
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           nvptx-tools
Version:        1.0
Release:        0
Summary:        PTX language tools
License:        GPL-3.0+
Group:          Development/Tools/Building
Url:            https://github.com/MentorEmbedded/nvptx-tools/
# tarball built from https://github.com/MentorEmbedded/nvptx-tools.git
Source0:        nvptx-tools.tar.xz
Patch:          nvptx-tools.patch
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
* nvptx-none-run-single: like nvptx-none-run, but locked, such that
  system-wide, only one instance of it is running at a time.

%prep
%setup -q -n nvptx-tools
%patch -p1

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
%{_bindir}/nvptx-none-ranlib
%doc COPYING3

%changelog
