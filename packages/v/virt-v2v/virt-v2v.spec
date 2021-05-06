#
# spec file for package virt-v2v
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
# needsbinariesforbuild


# If there are patches which touch autotools files, set this to 1.
%global patches_touch_autotools %{nil}
# The source directory.
%global source_directory 1.43-development
Name:           virt-v2v
Version:        1.43.5
Release:        0
Summary:        Tools to convert a virtual machine to run on KVM
License:        GPL-2.0-or-later
Group:          System/Management
URL:            https://github.com/libguestfs/virt-v2v
Source0:        http://download.libguestfs.org/virt-v2v/%{source_directory}/%{name}-%{version}.tar.gz
BuildRequires:  augeas-devel
BuildRequires:  file-devel
#BuildRequires: /usr/bin/pod2man
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel
BuildRequires:  libguestfs-devel >= 1.42
BuildRequires:  libjansson-devel
BuildRequires:  libosinfo-devel
BuildRequires:  libvirt-devel
BuildRequires:  libxml2-devel
BuildRequires:  mkisofs
BuildRequires:  ocaml >= 4.01
BuildRequires:  ocaml-fileutils-devel
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-gettext-devel
BuildRequires:  ocaml-gettext-stub-devel
BuildRequires:  ocaml-hivex-devel
BuildRequires:  ocaml-libguestfs
BuildRequires:  ocaml-libguestfs-devel
BuildRequires:  ocaml-libvirt-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  pcre2-devel
BuildRequires:  pkgconfig
BuildRequires:  po4a
BuildRequires:  perl(Sys::Guestfs)
BuildRequires:  pkgconfig(bash-completion) >= 2.0
Requires:       %{_bindir}/gawk
Requires:       %{_bindir}/gzip
Requires:       %{_bindir}/virsh
Requires:       curl
Requires:       guestfs-tools >= 1.42
Requires:       libguestfs0%{?_isa} >= 1.42
Requires:       unzip
Recommends:     nbdkit
Recommends:     nbdkit-curl-plugin
Recommends:     nbdkit-python-plugin
Recommends:     nbdkit-ssh-plugin
Recommends:     nbdkit-vddk-plugin
# libguestfs hasn't been built on i686 for a while since there is no
# kernel built for this architecture any longer and libguestfs rather
# fundamentally depends on the kernel.  Therefore we must exclude this
# arch.  Note there is no bug filed for this because we do not ever
# expect that libguestfs or virt-v2v will be available on i686 so
# there is nothing that needs fixing.
ExcludeArch:    %{ix86}
%if 0%{patches_touch_autotools}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
%endif

%description
Virt-v2v converts a single guest from a foreign hypervisor to run on
KVM.  It can read Linux and Windows guests running on VMware, Xen,
Hyper-V and some other hypervisors, and convert them to KVM managed by
libvirt, OpenStack, oVirt, Red Hat Virtualisation (RHV) or several
other targets.  It can modify the guest to make it bootable on KVM and
install virtio drivers so it will run quickly.

%package bash-completion
Summary:        Bash tab-completion for %{name}
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion >= 2.0
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Install this package if you want intelligent bash tab-completion
for %{name}.

%package man-pages-ja
Summary:        Japanese (ja) man pages for %{name}
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description man-pages-ja
%{name}-man-pages-ja contains Japanese (ja) man pages
for %{name}.

%package man-pages-uk
Summary:        Ukrainian (uk) man pages for %{name}
Group:          System/Management
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description man-pages-uk
%{name}-man-pages-uk contains Ukrainian (uk) man pages
for %{name}.

%prep
%autosetup -p1
%if 0%{patches_touch_autotools}
autoreconf -i
%endif

%build
%configure
%make_build

%install
%make_install

# Delete libtool crap.
find %{buildroot} -type f -name "*.la" -delete -print

# Virt-tools data directory.  This contains a symlink to rhsrvany.exe
# which is satisfied by the dependency on mingw32-srvany.
mkdir -p %{buildroot}/%{_datadir}/virt-tools

# Delete the v2v test harness (except for the man page).
rm -r %{buildroot}/%{_libdir}/ocaml/v2v_test_harness
rm -r %{buildroot}/%{_libdir}/ocaml/stublibs/dllv2v_test_harness*

# Find locale files.
%find_lang %{name}

%check
# All tests fail at the moment because of bugs in libvirt blockdev.
# # Tests fail on both armv7 and ppc64le in Fedora 31 because the kernel
# # cannot boot on qemu.
# %ifnarch %{arm} ppc64le

# # On x86_64 this single test fails with: "virt-v2v: warning: the
# # target hypervisor does not support a x86_64 KVM guest".  Missing
# # BuildRequires?
# %ifarch x86_64
# truncate -s 0 tests/test-v2v-o-libvirt.sh
# %endif

# # This test fails in mock.
# truncate -s 0 tests/test-v2v-oa-option.sh

# # Make sure we can see the debug messages (RHBZ#1230160).
# export LIBGUESTFS_DEBUG=1
# export LIBGUESTFS_TRACE=1

# make %{?_smp_mflags} check || {
#     cat tests/test-suite.log
#     exit 1
#   }

# %endif

%files -f %{name}.lang
%license COPYING
#doc README
%{_bindir}/virt-v2v
%{_bindir}/virt-v2v-copy-to-local
%{_mandir}/man1/virt-v2v.1%{?ext_man}
%{_mandir}/man1/virt-v2v-copy-to-local.1%{?ext_man}
%{_mandir}/man1/virt-v2v-hacking.1%{?ext_man}
%{_mandir}/man1/virt-v2v-input-vmware.1%{?ext_man}
%{_mandir}/man1/virt-v2v-input-xen.1%{?ext_man}
%{_mandir}/man1/virt-v2v-output-local.1%{?ext_man}
%{_mandir}/man1/virt-v2v-output-openstack.1%{?ext_man}
%{_mandir}/man1/virt-v2v-output-rhv.1%{?ext_man}
%{_mandir}/man1/virt-v2v-release-notes-1.42.1%{?ext_man}
%{_mandir}/man1/virt-v2v-support.1%{?ext_man}
%{_mandir}/man1/virt-v2v-test-harness.1%{?ext_man}
%{_datadir}/virt-tools

%files bash-completion
%license COPYING
%{_datadir}/bash-completion/completions/virt-v2v
%{_datadir}/bash-completion/completions/virt-v2v-copy-to-local

%files man-pages-ja
%license COPYING
%lang(ja) %{_mandir}/ja/man1/*.1*
%dir %{_mandir}/ja
%dir %{_mandir}/ja/man1/

%files man-pages-uk
%license COPYING
%lang(uk) %{_mandir}/uk/man1/*.1*
%dir %{_mandir}/uk
%dir %{_mandir}/uk/man1/

%changelog
