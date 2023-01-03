#
# spec file for package guestfs-tools
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
# needsbinariesforbuild


%global patches_touch_autotools 1

# The source directory.
%global source_directory 1.48-stable

#
%define guestfs_docdir %{_defaultdocdir}/%{name}

# Filter perl provides.
%{?perl_default_filter}

Summary:        Tools to access and modify virtual machine disk images
Name:           guestfs-tools
Version:        1.48.2
Release:        0
License:        GPL-2.0-or-later

# Build only for architectures that have a kernel
ExclusiveArch:  x86_64 ppc64le s390x aarch64 riscv64

# Source and patches.
URL:            http://libguestfs.org/
Source0:        http://download.libguestfs.org/guestfs-tools/%{source_directory}/%{name}-%{version}.tar.gz
Source1:        http://download.libguestfs.org/guestfs-tools/%{source_directory}/%{name}-%{version}.tar.gz.sig

Patch1:         CVE-2022-2211-options-fix-buffer-overflow-in-get_keys.patch

%if 0%{patches_touch_autotools}
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  libtool
%endif

# Basic build requirements.
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libguestfs-devel >= 1.45.3-1
BuildRequires:  libguestfs-xfs
BuildRequires:  libjansson-devel
BuildRequires:  libvirt-devel
BuildRequires:  libxcrypt-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  ocaml-findlib-devel
BuildRequires:  ocaml-gettext-devel
%if 0%{?suse_version} <= 1500
BuildRequires:  ocaml-gettext-stub-devel
%endif
BuildRequires:  ocaml-libguestfs-devel
BuildRequires:  ocaml-ounit-devel
BuildRequires:  pcre2-devel
BuildRequires:  perl
BuildRequires:  po4a
BuildRequires:  qemu-tools
BuildRequires:  unzip
BuildRequires:  xorriso
BuildRequires:  xz-devel
BuildRequires:  zip
BuildRequires:  perl(Expect)
BuildRequires:  perl(Locale::TextDomain)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Man)
BuildRequires:  perl(Pod::Simple)
BuildRequires:  perl(Sys::Guestfs)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Win::Hivex)
BuildRequires:  perl(Win::Hivex::Regedit)
BuildRequires:  pkgconfig(bash-completion)

# For virt-builder:
Requires:       curl
Requires:       gpg2
###Requires:      /usr/bin/qemu-img
Requires:       xz

# Obsolete guestfs-tools from the libguestfs package
Provides:       %{name} < %{version}
Obsoletes:      %{name} < %{version}

# For virt-builder-repository:
Suggests:       osinfo-db

# For virt-inspector, since Fedora and RHEL >= 7 use XFS:
Recommends:     libguestfs-xfs

# For virt-edit and virt-customize:
Suggests:       perl

%description
guestfs-tools is a set of tools that can be used to make batch
configuration changes to guests, get disk used/free statistics
(virt-df), perform backups and guest clones, change
registry/UUID/hostname info, build guests from scratch (virt-builder)
and much more.

Virt-alignment-scan scans virtual machines looking for partition
alignment problems.

Virt-builder is a command line tool for rapidly making disk images
of popular free operating systems.

Virt-cat is a command line tool to display the contents of a file in a
virtual machine.

Virt-customize is a command line tool for customizing virtual machine
disk images.

Virt-df is a command line tool to display free space on virtual
machine filesystems.  Unlike other tools, it doesn’t just display the
amount of space allocated to a virtual machine, but can look inside
the virtual machine to see how much space is really being used.  It is
like the df(1) command, but for virtual machines, except that it also
works for Windows virtual machines.

Virt-diff shows the differences between virtual machines.

Virt-edit is a command line tool to edit the contents of a file in a
virtual machine.

Virt-filesystems is a command line tool to display the filesystems,
partitions, block devices, LVs, VGs and PVs found in a disk image
or virtual machine.  It replaces the deprecated programs
virt-list-filesystems and virt-list-partitions with a much more
capable tool.

Virt-format is a command line tool to erase and make blank disks.

Virt-get-kernel extracts a kernel/initrd from a disk image.

Virt-inspector examines a virtual machine and tries to determine the
version of the OS, the kernel version, what drivers are installed,
whether the virtual machine is fully virtualized (FV) or
para-virtualized (PV), what applications are installed and more.

Virt-log is a command line tool to display the log files from a
virtual machine.

Virt-ls is a command line tool to list out files in a virtual machine.

Virt-make-fs is a command line tool to build a filesystem out of
a collection of files or a tarball.

Virt-resize can resize existing virtual machine disk images.

Virt-sparsify makes virtual machine disk images sparse (thin-provisioned).

Virt-sysprep lets you reset or unconfigure virtual machines in
preparation for cloning them.

Virt-tail follows (tails) a log file within a guest, like 'tail -f'.

%package -n virt-win-reg
Summary:        Access and modify the Windows Registry of a Windows VM
BuildArch:      noarch

%description -n virt-win-reg
Virt-win-reg lets you look at and modify the Windows Registry of
Windows virtual machines.

%package bash-completion
Summary:        Bash tab-completion scripts for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion >= 2.0

%description bash-completion
Install this package if you want intelligent bash tab-completion
for the virt-* tools.

%package man-pages-ja
Summary:        Japanese (ja) man pages for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description man-pages-ja
%{name}-man-pages-ja contains Japanese (ja) man pages
for %{name}.

%package man-pages-uk
Summary:        Ukrainian (uk) man pages for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}

%description man-pages-uk
%{name}-man-pages-uk contains Ukrainian (uk) man pages
for %{name}.

%prep
%autosetup -p1

%if 0%{patches_touch_autotools}
autoreconf -i
%endif

%build
%{configure} \
        --docdir=%{guestfs_docdir}

# Building index-parse.c by hand works around a race condition in the
# autotools cruft, where two or more copies of yacc race with each
# other, resulting in a corrupted file.
make -j1 -C builder index-parse.c

make V=1 %{?_smp_mflags}

%check

%install
%makeinstall \
        DESTDIR=%{buildroot} \
        INSTALLDIRS=vendor

# Delete libtool files.
find %{buildroot} -name '*.la' -delete

# Move installed documentation back to the source directory so
# we can install it using a %%doc rule.
mv %{buildroot}%{_docdir}/%{name} installed-docs
gzip --best installed-docs/*.xml

# Remove virt-dib if it was built.
rm -f $RPM_BUILD_ROOT%{_bindir}/virt-dib
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/virt-dib.1*

# Find locale files.
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README
%doc installed-docs/*
%dir %{_sysconfdir}/virt-builder
%dir %{_sysconfdir}/virt-builder/repos.d
%config(noreplace) %{_sysconfdir}/virt-builder/repos.d/*
%{_bindir}/virt-alignment-scan
%{_bindir}/virt-builder
%{_bindir}/virt-builder-repository
%{_bindir}/virt-cat
%{_bindir}/virt-customize
%{_bindir}/virt-df
%{_bindir}/virt-diff
%{_bindir}/virt-edit
%{_bindir}/virt-filesystems
%{_bindir}/virt-format
%{_bindir}/virt-get-kernel
%{_bindir}/virt-index-validate
%{_bindir}/virt-inspector
%{_bindir}/virt-log
%{_bindir}/virt-ls
%{_bindir}/virt-make-fs
%{_bindir}/virt-resize
%{_bindir}/virt-sparsify
%{_bindir}/virt-sysprep
%{_bindir}/virt-tail
%{_mandir}/man1/guestfs-tools-release-notes-1.*.1.gz
%{_mandir}/man1/virt-alignment-scan.1*
%{_mandir}/man1/virt-builder-repository.1*
%{_mandir}/man1/virt-builder.1*
%{_mandir}/man1/virt-cat.1*
%{_mandir}/man1/virt-customize.1*
%{_mandir}/man1/virt-df.1*
%{_mandir}/man1/virt-diff.1*
%{_mandir}/man1/virt-edit.1*
%{_mandir}/man1/virt-filesystems.1*
%{_mandir}/man1/virt-format.1*
%{_mandir}/man1/virt-get-kernel.1*
%{_mandir}/man1/virt-index-validate.1*
%{_mandir}/man1/virt-inspector.1*
%{_mandir}/man1/virt-log.1*
%{_mandir}/man1/virt-ls.1*
%{_mandir}/man1/virt-make-fs.1*
%{_mandir}/man1/virt-resize.1*
%{_mandir}/man1/virt-sparsify.1*
%{_mandir}/man1/virt-sysprep.1*
%{_mandir}/man1/virt-tail.1*

%files -n virt-win-reg
%license COPYING
%doc README
%{_bindir}/virt-win-reg
%{_mandir}/man1/virt-win-reg.1*

%files bash-completion
%license COPYING
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/virt-*

%files man-pages-ja
%lang(ja) %{_mandir}/ja/man1/*.1*
%if 0%{?suse_version} <= 1500
%dir %{_mandir}/ja
%dir %{_mandir}/ja/man1
%endif

%files man-pages-uk
%lang(uk) %{_mandir}/uk/man1/*.1*
%if 0%{?suse_version} <= 1500
%dir %{_mandir}/uk
%dir %{_mandir}/uk/man1
%endif

%changelog
