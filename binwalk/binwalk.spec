#
# spec file for package binwalk
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           binwalk
Version:        2.1.1
Release:        0
Summary:        Firmware Analysis Tool
License:        MIT
Group:          Development/Tools/Debuggers
URL:            https://github.com/devttys0/binwalk
Source:         https://github.com/devttys0/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
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
Recommends:     cpio
Recommends:     gzip
Recommends:     unrar
Recommends:     xz
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

%build
%python3_build

%install
%python3_install
chmod 644 API.md

%files
%license LICENSE
%doc API.md
%{_bindir}/%{name}
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-*

%changelog
