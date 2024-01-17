#
# spec file for package bumpversion
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


Name:           bumpversion
Version:        0.6.0
Release:        0
Summary:        Version-bump your software with a single command
License:        MIT
Group:          Development/Tools/Version Control
URL:            https://github.com/peritus/bumpversion
Source:         https://files.pythonhosted.org/packages/source/b/bumpversion/bumpversion-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
Requires:       python3-base
Provides:       python-bumpversion = %version
Obsoletes:      python-bumpversion < %version
BuildArch:      noarch

%description
Version-bump your software with a single command!

bumpversion updates all version strings in your source tree by the correct
increment, commits that change to git or Mercurial and tags it.

%prep
%setup -q -n bumpversion-%{version}

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%doc README.rst
%{python3_sitelib}/bumpversion*

%changelog
