#
# spec file for package git-review
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           git-review
Version:        1.28.0
Release:        0
Summary:        Tool to submit code to Gerrit
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://git.openstack.org/cgit/openstack-infra/git-review
Source:         https://files.pythonhosted.org/packages/source/g/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
# Note that this package is intentionally not using singlespec because
# it is not a library but a plain CLI tool, and it doesn't make sense to
# build a python2.x version of it anymore in 2019.
BuildRequires:  python-rpm-macros
BuildRequires:  python3-fixtures >= 0.3.14
BuildRequires:  python3-mock
BuildRequires:  python3-pbr
BuildRequires:  python3-requests >= 1.1
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-stestr
BuildRequires:  python3-testtools >= 0.9.34
Requires:       python3-requests >= 1.1
Requires:       python3-setuptools
Requires:       python3-six
Provides:       python3-git-review = %version
Obsoletes:      python3-git-review < %version
BuildArch:      noarch

%description
A git command for submitting branches to Gerrit

git-review is a tool that helps submitting git branches to gerrit for
review.

%prep
%setup -q -n git-review-%{version}

%build
%python3_build

%install
%python3_install

%check
# Can't be executed because it fetches java from web and launches own gerrit
# instance to test against
#%%{python_expand $python -m git_review.tests.check_test_id_hashes discover --list
#$python -m git_review.tests.prepare
#$python setup.py testr}

%files
%license LICENSE
%doc AUTHORS README.rst
%{python3_sitelib}/*
%{_bindir}/git-review
%{_mandir}/man1/git-review.1%{?ext_man}

%changelog
