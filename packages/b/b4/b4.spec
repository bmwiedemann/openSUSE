#
# spec file for package b4
#
# Copyright (c) 2024 SUSE LLC
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


%if 0%{suse_version} >= 1600
%global pythons python3
%global pprefix python3
%else
%{?sle15_python_module_pythons}
%global pprefix python311
%endif
Name:           b4
Version:        0.14.0
Release:        0
Summary:        Helper scripts for kernel.org patches
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://git.kernel.org/pub/scm/utils/b4/b4.git
Source0:        https://github.com/mricon/b4/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module dkimpy >= 1.0.5}
BuildRequires:  %{python_module patatt >= 0.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.24.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  git-filter-repo >= 2.30
BuildRequires:  python-rpm-macros
Requires:       %{pprefix}-dkimpy
Requires:       %{pprefix}-patatt
Requires:       %{pprefix}-requests
Requires:       git-core
Requires:       git-filter-repo >= 2.30
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
sed -i.old '1{/#!.*/d}' src/b4/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm -rf %{buildroot}%{$python_sitelib}/{tests,b4/man}/
install -m644 -Dt %{buildroot}%{_mandir}/man5/ src/b4/man/b4.5

%check
%pytest --ignore=build
export PYTHONPATH="./build/lib"
THEIRS=`%{buildroot}/%{_bindir}/b4 --version`
OURS=`sed -n "s/__VERSION__ = '\(.*\)'/\1/p" src/b4/__init__.py`
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
