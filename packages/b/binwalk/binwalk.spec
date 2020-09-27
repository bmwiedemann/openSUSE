#
# spec file for package binwalk
#
# Copyright (c) 2020 SUSE LLC
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


Name:           binwalk
Version:        2.2.0
Release:        0
Summary:        Firmware Analysis Tool
License:        MIT
URL:            https://github.com/devttys0/binwalk
Source:         https://github.com/devttys0/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  help2man
BuildRequires:  python-rpm-macros
BuildRequires:  python3-curses
BuildRequires:  python3-setuptools
# Depends on libmagic.
Requires:       file
Requires:       python3-curses
# Depends on libfuzzy.
Requires:       ssdeep
Recommends:     bzip2
Recommends:     cabextract
Recommends:     capstone
Recommends:     cpio
Recommends:     cramfs-tools
Recommends:     cramfsswap
Recommends:     gzip
Recommends:     jefferson
Recommends:     lhasa
Recommends:     lzop
Recommends:     sasquatch
Recommends:     sleuthkit
Recommends:     squashfs
Recommends:     srecord
Recommends:     ubi_reader
Recommends:     unrar
Recommends:     xz
Recommends:     yaffshiv
Recommends:     zlib
Suggests:       java
BuildArch:      noarch
%if 0%{?suse_version} > 1500
Recommends:     p7zip-full
%else
Recommends:     p7zip
%endif

%description
Binwalk is a tool for searching a given binary image for embedded
files and executable code. Specifically, it is designed for
identifying files and code embedded inside of firmware images.
Binwalk uses the libmagic library, so it is compatible with magic
signatures created for the Unix file utility. Binwalk also includes
a custom magic signature file which contains improved signatures
for files that are commonly found in firmware images such as
compressed/archived files, firmware headers, Linux kernels,
bootloaders, filesystems, etc.

%prep
%setup -q
sed -i -e '/^#!\//, 1d' src/binwalk/plugins/hilink.py

%build
%python3_build

%install
%python3_install
chmod 644 API.md
export PYTHONPATH=%{buildroot}%{python3_sitelib}
help2man %{buildroot}/%{_bindir}/binwalk --no-discard-stderr --version-string="%{version}" --no-info > binwalk.1
install -Dpm 0644 %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1
%fdupes %{buildroot}%{python3_sitelib}

%files
%license LICENSE
%doc API.md
%{_bindir}/%{name}
%{_mandir}/man1/binwalk.1%{?ext_man}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*

%changelog
