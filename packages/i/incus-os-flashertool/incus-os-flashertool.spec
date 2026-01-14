#
# spec file for package incus-os-flashertool
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


Name:           incus-os-flashertool
Version:        202601100100
Release:        0
Summary:        CLI tool to download and customize a IncusOS installation image
License:        Apache-2.0
URL:            https://linuxcontainers.org/incus-os/docs/main/getting-started/download/
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
BuildRequires:  go1.24 >= 1.24.7

%description
The flasher tool is provided for more advanced users who need to perform more
customizations of the install seed than the web-based customizer supports.

When run, you will first be prompted for the image format you want to use,
either ISO (default) or raw disk image. Note that the ISO isn’t a hybrid image;
if you want to boot from a USB stick you should choose the raw disk image
format.

The flasher tool will then connect to the Linux Containers CDN and download the
latest release.

Once downloaded, you will be presented with an interactive menu you can use to
customize the install options.

%prep
%autosetup -p 1 -a 1
mv vendor ./incus-osd

%build
COMMIT_HASH="$(sed -n 's/commit: \(.*\)/\1/p' %_sourcedir/%{name}.obsinfo)"

DATE_FMT="+%%Y-%%m-%%dT%%H:%%M:%%SZ"
BUILD_DATE=$(date -u -d "@${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u -r "${SOURCE_DATE_EPOCH}" "${DATE_FMT}" 2>/dev/null || date -u "${DATE_FMT}")

cd incus-osd || exit 1
go build \
   -mod=vendor \
   -buildmode=pie \
   -o ../bin/%{name} ./cmd/flasher-tool

%install
# Install the binary.
install -D -m 0755 bin/%{name} %{buildroot}/%{_bindir}/%{name}

%files
%doc README.md
%license ./incus-osd/COPYING
%{_bindir}/%{name}

%changelog
