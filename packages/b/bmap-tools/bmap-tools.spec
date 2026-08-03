#
# spec file for package bmap-tools
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


%if 0%{?suse_version} == 1500 && 0%{?sle_version} > 150300
%bcond_with gpgtest
%else
%bcond_without gpgtest
%endif
%{?sle15_python_module_pythons}
Name:           bmap-tools
Version:        3.9.0
Release:        0
Summary:        Tools to generate block map (AKA bmap) and flash images using bmap
License:        GPL-2.0-only
Group:          Development/Tools/Other
URL:            https://github.com/yoctoproject/bmaptool
Source0:        https://github.com/yoctoproject/bmaptool/archive/refs/tags/v%{version}.tar.gz#/bmaptool-%{version}-gh.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-gpg >= 1.10
Requires:       python-six >= 1.15
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
Provides:       python-bmaptool = %{version}-%{release}
Provides:       python-bmaptools = %{version}-%{release}
Obsoletes:      python-bmaptools < %{version}-%{release}
BuildArch:      noarch
# SECTION test
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
%if %{with gpgtest}
BuildRequires:  %{python_module gpg}
%endif
# /SECTION
%python_subpackages

%description
Bmaptool is a generic tool for creating the block map (bmap) for a file, and
copying files using the block map. The idea is that large file containing
unused blocks, like raw system image files, can be copied or flashed a lot
faster with bmaptool than with traditional tools like "dd" or "cp".

%prep
%autosetup -p1 -n bmaptool-%{version}
find src -name "*.py" -exec chmod -x {} +

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/bmaptool

mkdir -p %{buildroot}/%{_mandir}/man1
install -m644 docs/man1/bmaptool.1 %{buildroot}/%{_mandir}/man1
%python_clone -a %{buildroot}%{_mandir}/man1/bmaptool.1

%python_expand %fdupes %{buildroot}%{$python_sitelib}/

%check
# no /sys/module/zfs/ in obs test environment: returns false instead of IOError
%pytest -k "not test_is_zfs_configuration_compatible_unreadable_file"

%post
%{python_install_alternative bmaptool bmaptool.1}

%postun
%python_uninstall_alternative bmaptool

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%python_alternative %{_bindir}/bmaptool
%python_alternative %{_mandir}/man1/bmaptool.1%{?ext_man}
%{python_sitelib}/bmaptool
%{python_sitelib}/bmaptool-%{version}.dist-info

%changelog
