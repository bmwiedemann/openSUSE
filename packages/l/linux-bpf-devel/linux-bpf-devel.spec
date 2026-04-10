#
# spec file for package linux-bpf-devel
#
# Copyright (c) 2026 SUSE LLC and contributors
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
# needssslcertforbuild


%define build_flavor default
%define kernel_package_name kernel-%build_flavor
%define kver %(rpm -q --qf '%%{VERSION}' %kernel_package_name)
%define krel %(rpm -q --qf '%%{RELEASE}' %kernel_package_name)
# Extract the source release (e.g., removing the build number for directory
# matching if needed)
%define source_rel %(echo %krel | sed -r 's/\\.[0-9]+($|\\.[^.]*[^.0-9][^.]*$)/\\1/')

Name:           linux-bpf-devel
BuildRequires:  %kernel_package_name
BuildRequires:  bpftool
BuildRequires:  coreutils
BuildRequires:  gzip
BuildRequires:  xz
# DEBUG
BuildRequires:  findutils
Summary:        Provides vmlinux.h for BPF CO-RE development
License:        GPL-2.0-only
Group:          Development/Languages/C and C++
URL:            http://www.kernel.org/
Version:        %kver
Release:        %krel.<RELEASE>
# Does not have BTF
ExcludeArch:    %ix86 %arm

%description
This package contains a "vmlinux.h" header file generated from the
corresponding kernel's BTF (BPF Type Format) data.

This file provides all kernel types and definitions in a single header,
intended for use with BPF CO-RE (Compile Once - Run Everywhere) development. It
serves as a reference template; actual runtime relocation is handled by libbpf.

%prep
%setup -c -T

%build
VMLINUX="/lib/modules/%{kver}-%{source_rel}-%{build_flavor}/vmlinux"
VMLINUX_BOOT="/boot/vmlinux-%{kver}-%{source_rel}-%{build_flavor}"

echo "Looking for vmlinux in: $VMLINUX or $VMLINUX_BOOT"

find_compressed(){
	local uncompressed="$1"
	local target="$(basename "$uncompressed")"
	if [ -f "$uncompressed".gz ] ; then
		gzip -dc "$uncompressed".gz > "$target"
		echo "$target"
		return 0
	elif [ -f "$uncompressed".xz ]; then
		unxz -c "$uncompressed".xz > "$target"
		echo "$target"
		return 0
	fi
}

DECOMPRESSED=""

for file in "$VMLINUX" "$VMLINUX_BOOT" ; do
	if [ -f "$file" ]; then
		echo "Found uncompressed vmlinux..."
		DECOMPRESSED="$file"
		break
	fi
	DECOMPRESSED="$(find_compressed "$file")"
	if [ -n "$DECOMPRESSED" ] ; then
		echo "Found and decompressed a compressed vmlinux..."
		break
	fi
done

if [ -z "$DECOMPRESSED" ] ; then
	echo "No vmlinux found"
	exit 1
fi

echo "Generating vmlinux.h..."
/usr/sbin/bpftool btf dump file "$DECOMPRESSED" format c > vmlinux.h
# Fail explicitly if bpftool produced an empty file (e.g., no BTF section).
[ -s vmlinux.h ] || { echo "Error: bpftool produced an empty vmlinux.h." >&2; exit 1; }
rm -f ./vmlinux

%install
install -d -m 755 %{buildroot}%{_includedir}/bpf
install -m 644 vmlinux.h %{buildroot}%{_includedir}/bpf/vmlinux.h

%files
%dir %{_includedir}/bpf
%{_includedir}/bpf/vmlinux.h

%changelog
