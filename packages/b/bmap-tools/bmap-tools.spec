#
# spec file for package bmap-tools
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


%define skip_python2 1
Name:           bmap-tools
Version:        3.6
Release:        0
Summary:        Tools to generate block map (AKA bmap) and flash images using bmap
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://github.com/intel/bmap-tools
Source0:        https://github.com/intel/bmap-tools/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# For Patch0
Source11:       https://github.com/intel/bmap-tools/raw/ffdcbc752cb086d33f083100b4c2498914a7b8eb/tests/test-data/gnupg/pubring.kbx
Source12:       https://github.com/intel/bmap-tools/raw/ffdcbc752cb086d33f083100b4c2498914a7b8eb/tests/test-data/gnupg/random_seed
Source13:       https://github.com/intel/bmap-tools/raw/ffdcbc752cb086d33f083100b4c2498914a7b8eb/tests/test-data/gnupg/trustdb.gpg
Source14:       https://github.com/intel/bmap-tools/raw/ffdcbc752cb086d33f083100b4c2498914a7b8eb/tests/test-data/test.image.bmap.v2.0.sig-by-wrong-key
Source15:       https://github.com/intel/bmap-tools/raw/ffdcbc752cb086d33f083100b4c2498914a7b8eb/tests/test-data/test.image.bmap.v2.0.valid-sig
# PATCH-FEATURE-UPSTREAM  bmap-tools-pr103-replace-python-gpgme.patch gh#intel/bmap-tools#103 + gh#intel/bmap-tools#112
Patch0:         bmap-tools-pr103-replace-python-gpgme.patch
# PATCH-FIX-OPENSUSE remove-backports.tempfile.patch code@bnavigator.de -- no need to support Python < 3.2
Patch1:         bmap-tools-3.6-suse-fix-tests.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-gpg
Requires(post): update-alternatives
Requires(postun):update-alternatives
# SECTION test
BuildRequires:  %{python_module gpg}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
# /SECTION
Recommends:     bzip2
Recommends:     gzip
Recommends:     lz4
Recommends:     lzop
Recommends:     pbzip2
Recommends:     pigz
Recommends:     tar
Recommends:     unzip
Recommends:     xz
Recommends:     zstd
BuildArch:      noarch
%python_subpackages

%description
Bmaptool is a generic tool for creating the block map (bmap) for a file, and copying files
using the block map. The idea is that large file containing unused blocks, like
raw system image files, can be copied or flashed a lot faster with bmaptool
than with traditional tools like "dd" or "cp".

%prep
%autosetup -p1
# remove shebang
tail -n +2 bmaptools/CLI.py > bmaptools/CLI.py_new
mv bmaptools/CLI.py{_new,}
%if 0%{?suse_version} < 1550
# no python_flavored_alternatives in old python-rpm-macros
mkdir testbin
sed '1{s/env python/python3/}' bmaptool > testbin/bmaptool
chmod +x testbin/bmaptool
%endif
rm __main__.py bmaptool
cp %{SOURCE11} %{SOURCE12} %{SOURCE13} tests/test-data/gnupg/
cp %{SOURCE14} %{SOURCE15} tests/test-data/signatures/

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/bmaptool

mkdir -p %{buildroot}/%{_mandir}/man1
install -m644 docs/man1/bmaptool.1 %{buildroot}/%{_mandir}/man1
%python_clone -a %{buildroot}%{_mandir}/man1/bmaptool.1

%python_expand %fdupes %{buildroot}%{$python_sitelib}/bmaptools

%check
%if 0%{?suse_version} < 1550
export PATH=$PWD/testbin:$PATH
%endif
# no /sys/module/zfs/ in obs test environment: returns false instead of IOError
%pytest -k "not test_is_zfs_configuration_compatible_unreadable_file"

%post
%{python_install_alternative bmaptool bmaptool.1}

%postun
%python_uninstall_alternative bmaptool

%files %{python_files}
%license COPYING
%doc docs/README docs/RELEASE_NOTES
%python_alternative %{_bindir}/bmaptool
%python_alternative %{_mandir}/man1/bmaptool.1%{?ext_man}
%{python_sitelib}/bmaptools
%{python_sitelib}/bmap_tools-%{version}*-info

%changelog
