#
# spec file for package bmap-tools
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


Name:           bmap-tools
Version:        3.6
Release:        0
Summary:        Tools to generate block map (AKA bmap) and flash images using bmap
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://github.com/intel/bmap-tools
Source0:        https://github.com/intel/bmap-tools/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-gpgme
Requires(post): update-alternatives
Requires(postun): update-alternatives
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
Tools to generate block map (AKA bmap) and flash images using bmap. Bmaptool is
a generic tool for creating the block map (bmap) for a file, and copying files
using the block map. The idea is that large file containing unused blocks, like
raw system image files, can be copied or flashed a lot faster with bmaptool
than with traditional tools like "dd" or "cp".

%prep
%setup -q
# remove shebang
tail -n +2 bmaptools/CLI.py > bmaptools/CLI.py_new
mv bmaptools/CLI.py{_new,}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/bmaptool

mkdir -p %{buildroot}/%{_mandir}/man1
install -m644 docs/man1/bmaptool.1 %{buildroot}/%{_mandir}/man1
%python_clone -a %{buildroot}%{_mandir}/man1/bmaptool.1

%python_expand %fdupes %{buildroot}%{$python_sitelib}/bmaptools

%post
%{python_install_alternative bmaptool bmaptool.1}

%postun
%python_uninstall_alternative bmaptool

%files %{python_files}
%license COPYING
%doc docs/README docs/RELEASE_NOTES
%python_alternative %{_bindir}/bmaptool
%python_alternative %{_mandir}/man1/bmaptool.1%{ext_man}
%{python_sitelib}/*

%changelog
