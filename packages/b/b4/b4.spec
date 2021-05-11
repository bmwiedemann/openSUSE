#
# spec file for package b4
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


%define version_unconverted 0.6.2+5
Name:           b4
Version:        0.6.2+5
Release:        0
Summary:        Helper scripts for kernel.org patches
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://git.kernel.org/pub/scm/utils/b4/b4.git
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch
# for checks
BuildRequires:  git-core
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
Requires:       python3-dkimpy >= 1.0.5
Requires:       python3-dnspython >= 2.0.0
Requires:       python3-requests >= 2.24.0

%description
This is a helper utility to work with patches made available via a
public-inbox archive like lore.kernel.org. It is written to make it
easier to participate in a patch-based workflows, like those used in
the Linux kernel development.

The name "b4" was chosen for ease of typing and because B-4 was the
precursor to Lore and Data in the Star Trek universe.

%prep
%autosetup -p1

# ditch shebang from .py files, they are non-executables anyway
sed -i.old '1{/#!.*/d}' b4/*.py

%build
%python3_build

%install
%python3_install
mv %{buildroot}/%{_mandir}/man5 %{buildroot}/%{_mandir}/man.5

%check
python3 setup.py check
export PYTHONPATH="./"
THEIRS=`python3 ./b4/command.py --version`
OURS=`sed -n "s/__VERSION__ = '\(.*\)'/\1/p" b4/__init__.py`
test "$THEIRS" = "$OURS"
python3 ./b4/command.py --help |grep -q 'mbox,am,attest'
python3 ./b4/command.py mbox abc |& grep -q 'Looking up https://lore.kernel.org/r/abc'

%files
%doc README.rst
%license COPYING
%{_bindir}/%{name}
%dir %{_mandir}/man.5/
%{_mandir}/man.5/b4.5.gz
%{python_sitelib}/%{name}*

%changelog
