#
# spec file for package breezy
#
# Copyright (c) 2023 SUSE LLC
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


%define rustflags '-Clink-arg=-Wl,-z,relro,-z,now'

Name:           breezy
Version:        3.3.2
Release:        0
Summary:        Distributed version control system with multi-format support
License:        GPL-2.0-or-later
URL:            https://www.breezy-vcs.org/
Source0:        https://files.pythonhosted.org/packages/source/b/breezy/breezy-%{version}.tar.gz
Source90:       cargo_config
Source98:       vendor-lib-rio.tar.xz
Source99:       vendor.tar.xz
# PATCH-FIX-UPSTREAM skip_lp2003710.patch lp#2003710 mcepl@suse.com
# Skip failing tests
Patch0:         skip_lp2003710.patch
BuildRequires:  cargo >= 1.41.0
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# full stdlib for sqlite3
BuildRequires:  python3
BuildRequires:  python3-Cython
BuildRequires:  python3-PyYAML
BuildRequires:  python3-devel
BuildRequires:  python3-merge3
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-setuptools-gettext
BuildRequires:  python3-setuptools-rust
BuildRequires:  python3-wheel
BuildRequires:  rust >= 1.41.0
BuildRequires:  zstd
Requires:       python3-PyYAML
Requires:       python3-configobj
Requires:       python3-dulwich >= 0.19.11
Requires:       python3-fastbencode
Requires:       python3-fastimport >= 0.9.8
Requires:       python3-merge3
Requires:       python3-patiencediff
Suggests:       python3-launchpadlib >= 1.6.3
Provides:       bzr = %{version}
Obsoletes:      bzr < %{version}
# SECTION test requirements
BuildRequires:  python3-configobj
BuildRequires:  python3-dulwich >= 0.19.11
BuildRequires:  python3-fastbencode
BuildRequires:  python3-fastimport >= 0.9.8
BuildRequires:  python3-fixtures >= 1.3.0
BuildRequires:  python3-patiencediff
BuildRequires:  python3-python-subunit
BuildRequires:  python3-testtools
# /SECTION

%description
Breezy is a version control system implemented in Python with
multi-format support. Breezy has built-in support for the Git and
Bazaar file formats and network protocols.

%prep
%autosetup -p1 -a 98 -a 99 -n breezy-%{version}

sed -ie "s,man/man1,share/man/man1," setup.py

mkdir .cargo
cp %{SOURCE90} .cargo/config
mkdir lib-rio/.cargo
cp %{SOURCE90} lib-rio/.cargo/config

sed -i '1{\@^#!i[[:blank:]]*%{_bindir}/env python@d}' \
    breezy/dirty_tracker.py \
    breezy/tests/ssl_certs/create_ssls.py \
    breezy/tests/test_dirty_tracker.py

%build
export RUSTFLAGS=%{rustflags}
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python3_build

%install
export RUSTFLAGS=%{rustflags}
%python3_install
%fdupes %{buildroot}%{python3_sitearch}

# backwards compatible symbolic links
ln -s brz %{buildroot}%{_bindir}/bzr
echo ".so man1/brz.1" > %{buildroot}%{_mandir}/man1/bzr.1

%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
export LANG=en_US.UTF8
# log_C log_BOGUS - borked with py3.8+ as you can't change encoding
# test_ancient_{ctime,mtime} - broken on aarch64 %%arm ppc ppc64le
# test_distant_{ctime,mtime} - broken on %%arm
# test_plugins lp#1927523
# test_simple_local_git - pulls in forbidden modules with 3.10+
%{buildroot}%{_bindir}/bzr selftest -v --parallel=fork \
  -Oselftest.timeout=6000 -x bash_completion \
  -x breezy.tests.test_transport.TestSSHConnections.test_bzr_connect_to_bzr_ssh -x test_export_pot \
  -x test_log_C -x test_log_BOGUS \
%ifnarch %{ix86} x86_64 ppc64
  -x breezy.tests.test__dirstate_helpers.TestPackStat.test_ancient_ctime \
  -x breezy.tests.test__dirstate_helpers.TestPackStat.test_ancient_mtime \
%endif
%ifarch %{arm}
  -x breezy.tests.test__dirstate_helpers.TestPackStat.test_distant_ctime \
  -x breezy.tests.test__dirstate_helpers.TestPackStat.test_distant_mtime \
%endif
  -x breezy.tests.test_xml.TestSerializer.test_revision_text_v8 \
  -x breezy.tests.test_xml.TestSerializer.test_revision_text_v7 \
  -x breezy.tests.test_xml.TestSerializer.test_revision_text_v6 \
  -x breezy.tests.test_plugins.TestPlugins \
  -x breezy.tests.test_plugins.TestLoadingPlugins.test_plugin_with_error \
  -x breezy.tests.test_import_tariff.TestImportTariffs.test_simple_local_git

%files
%doc NEWS README.rst
%license COPYING.txt
%{_bindir}/bzr-receive-pack
%{_bindir}/bzr-upload-pack
%{_bindir}/git-remote-bzr
%{_bindir}/brz
%{_bindir}/bzr
%{python3_sitearch}/breezy*
%{_mandir}/man1/brz.1%{?ext_man}
%{_mandir}/man1/bzr.1%{?ext_man}
%{_mandir}/man1/git-remote-bzr.1%{?ext_man}

%changelog
