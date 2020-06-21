#
# spec file for package breezy
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


Name:           breezy
Version:        3.1.0
Release:        0
Summary:        Friendly distributed version control system
License:        GPL-2.0-or-later
URL:            https://www.breezy-vcs.org/
Source:         https://files.pythonhosted.org/packages/source/b/breezy/breezy-%{version}.tar.gz
# PATCH-FIX-UPSTREAM 7531_7530.diff lp#1882589 mcepl@suse.com
# Fix handling of a particular kind of broken committer id
Patch1:         7531_7530.diff
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3-configobj
Requires:       python3-dulwich >= 0.19.11
Requires:       python3-fastimport >= 0.9.8
Requires:       python3-patiencediff
Requires:       python3-six >= 1.9.0
Suggests:       python3-launchpadlib >= 1.6.3
Provides:       bzr = %{version}
Obsoletes:      bzr < %{version}
# SECTION test requirements
BuildRequires:  python3-configobj
BuildRequires:  python3-dulwich >= 0.19.11
BuildRequires:  python3-fastimport >= 0.9.8
BuildRequires:  python3-fixtures >= 1.3.0
BuildRequires:  python3-patiencediff
BuildRequires:  python3-python-subunit
BuildRequires:  python3-six >= 1.9.0
BuildRequires:  python3-testtools
# /SECTION

%description
Friendly distributed version control system

%prep
%setup -q -n breezy-%{version}
%autopatch -p1
sed -ie "s,man/man1,share/man/man1," setup.py

%build
export CFLAGS="%{optflags}"
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitearch}

# backwards compatible symbolic links
ln -s brz %{buildroot}%{_bindir}/bzr
echo ".so man1/brz.1" > %{buildroot}%{_mandir}/man1/bzr.1

%check
export PYTHONPATH=%{buildroot}%{python3_sitearch}
export LANG=en_US.UTF8
# log_C log_BOGUS - borked with py3.8+ as you can't change encoding
# test_pack_revision - endswith first arg must be bytes or a tuple of bytes, not str
# test_ancient_{ctime,mtime} - broken on aarch64 %%arm ppc ppc64le
# test_distant_{ctime,mtime} - broken on %%arm
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
  -x breezy.tests.test_xml.TestSerializer.test_pack_revision_5 \
  -x breezy.tests.test_xml.TestSerializer.test_revision_text_v8 \
  -x breezy.tests.test_xml.TestSerializer.test_revision_text_v7 \
  -x breezy.tests.test_xml.TestSerializer.test_revision_text_v6

%files
%doc NEWS README.rst README_BDIST_RPM
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
