#
# spec file for package b4
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


%define pythons python3
%{?sle15_python_module_pythons}
Name:           b4
Version:        0.12.4
Release:        0
Summary:        Helper scripts for kernel.org patches
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://git.kernel.org/pub/scm/utils/b4/b4.git
Source0:        https://github.com/mricon/b4/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module dkimpy >= 1.0.5}
BuildRequires:  %{python_module dnspython >= 2.0.0}
BuildRequires:  %{python_module patatt >= 0.5}
BuildRequires:  %{python_module requests >= 2.24.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  git-filter-repo >= 2.30
BuildRequires:  python-rpm-macros
Requires:       git-core
Requires:       git-filter-repo >= 2.30
Requires:       python3-dkimpy
Requires:       python3-dnspython
Requires:       python3-patatt
Requires:       python3-requests
BuildArch:      noarch

%description
This is a helper utility to work with patches made available via a
public-inbox archive like lore.kernel.org. It is written to make it
easier to participate in a patch-based workflows, like those used in
the Linux kernel development.

The name "b4" was chosen for ease of typing and because B-4 was the
precursor to Lore and Data in the Star Trek universe.

%prep
%autosetup -p1

# use the system one
rm -rf patatt

# ditch shebang from .py files, they are non-executables anyway
sed -i.old '1{/#!.*/d}' b4/*.py

%build
%python_build

%install
%python_install
%python_expand %{$python_fix_shebang}
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py check
export PYTHONPATH="./"
THEIRS=`%{buildroot}/%{_bindir}/b4 --version`
OURS=`sed -n "s/__VERSION__ = '\(.*\)'/\1/p" b4/__init__.py`
test "$THEIRS" = "$OURS"
%{buildroot}/%{_bindir}/b4 --help | grep -q 'mbox,am,shazam,pr'
%{buildroot}/%{_bindir}/b4 mbox abc |& grep -q 'Grabbing thread from lore.kernel.org/all/abc/t.mbox.gz'

%files
%doc README.rst
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man5/b4.5%{?ext_man}
%{python_sitelib}/%{name}*

%changelog
