#
# spec file for package breezy
#
# Copyright (c) 2025 SUSE LLC
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
Version:        3.3.9
Release:        0
Summary:        Distributed version control system with multi-format support
License:        GPL-2.0-or-later
# Upstream website https://launchpad.net/brz
URL:            https://www.breezy-vcs.org/
Source0:        https://files.pythonhosted.org/packages/source/b/breezy/breezy-%{version}.tar.gz
Source98:       vendor-lib-rio.tar.zst
Source99:       vendor.tar.zst
# PATCH-FIX-UPSTREAM 03_spurious_test_failure.patch mcepl@suse.com
# fix some spurious test failures
Patch1:         03_spurious_test_failure.patch
# PATCH-FIX-UPSTREAM 08_disable_sphinx_epytext.patch mcepl@suse.com
# don't depend on sphinx_epytext
Patch2:         08_disable_sphinx_epytext.patch
# PATCH-FIX-UPSTREAM 16_generate_ids.patch mcepl@suse.com
Patch3:         16_generate_ids.patch

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
BuildRequires:  python3-tzlocal
BuildRequires:  python3-wheel
BuildRequires:  rust >= 1.41.0
BuildRequires:  zstd
Requires:       python3-PyYAML
Requires:       python3-configobj
Requires:       python3-dulwich >= 0.19.11
Requires:       python3-fastbencode
Requires:       python3-merge3
Requires:       python3-patiencediff
Requires:       python3-tzlocal
Requires:       python3-urllib3 >= 1.24.1
Recommends:     python3-launchpadlib >= 1.6.3
Provides:       bzr = %{version}
Obsoletes:      bzr < %{version}
# SECTION test requirements
BuildRequires:  python3-configobj
BuildRequires:  python3-dulwich >= 0.19.11
BuildRequires:  python3-fastbencode
BuildRequires:  python3-fixtures >= 1.3.0
BuildRequires:  python3-patiencediff
BuildRequires:  python3-python-subunit
BuildRequires:  python3-testtools
# /SECTION

%description
Breezy is a version control system implemented in Python with
multi-format support. Breezy has built-in support for the Git and
Bazaar file formats and network protocols.

%package bash-completion
Summary:        Bash completion for breezy
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (breezy and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash shell completions for breezy

%lang_package

%prep
%autosetup -p1 -a 98 -a 99 -n breezy-%{version}

sed -ie "s,man/man1,share/man/man1," setup.py

sed -i '1{\@^#!i[[:blank:]]*%{_bindir}/env python@d}' \
    breezy/dirty_tracker.py \
    breezy/tests/ssl_certs/create_ssls.py \
    breezy/tests/test_dirty_tracker.py

%build
export RUSTFLAGS=%{rustflags}
export CFLAGS="%{optflags} -fno-strict-aliasing"
%python3_pyproject_wheel
# generates brz.1
python3 tools/generate_docs.py man
# generates brz.bash_completion
python3 tools/generate_docs.py bash_completion

%install
export RUSTFLAGS=%{rustflags}
%python3_pyproject_install

# shell completions
install -Dm0644 brz.bash_completion  \
    %{buildroot}%{_datadir}/bash-completion/completions/brz

%fdupes %{buildroot}%{python3_sitearch}

# install manpage
install -D -m 0644 brz.1 %{buildroot}%{_mandir}/man1/brz.1
install -m 0644 breezy/git/git-remote-bzr.1 %{buildroot}%{_mandir}/man1/git-remote-bzr.1

# backwards compatible symbolic links
ln -s brz %{buildroot}%{_bindir}/bzr
echo ".so man1/brz.1" > %{buildroot}%{_mandir}/man1/bzr.1

%find_lang %{name}

%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
export LANG=en_US.UTF8
%{buildroot}%{_bindir}/bzr selftest -v --parallel=fork \
  -Oselftest.timeout=6000

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

%files bash-completion
%{_datadir}/bash-completion/completions/brz

%files lang -f %{name}.lang

%changelog
