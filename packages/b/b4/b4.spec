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
Version:        0.16.0
Release:        0
Summary:        Helper scripts for kernel.org patches
License:        GPL-2.0-or-later
Group:          Development/Tools/Other
URL:            https://git.kernel.org/pub/scm/utils/b4/b4.git
Source0:        https://github.com/mricon/b4/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.11}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module dkimpy >= 1.0}
BuildRequires:  %{python_module ezgb >= 0.2}
BuildRequires:  %{python_module liblore >= 0.8}
BuildRequires:  %{python_module patatt >= 0.6}
BuildRequires:  %{python_module pygit2 >= 1.14}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module requests >= 2.24}
BuildRequires:  %{python_module textual}
BuildRequires:  git-core
# /SECTION
Requires:       %{pprefix}-dkimpy
Requires:       %{pprefix}-ezgb
Requires:       %{pprefix}-liblore
Requires:       %{pprefix}-patatt
Requires:       %{pprefix}-pygit2
Requires:       %{pprefix}-requests
Requires:       git-core
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
sed -i.old '1{/#!.*/d}' src/b4/*.py src/b4/*/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
install -m644 -Dt %{buildroot}%{_mandir}/man1/ src/b4/man/b4.1

%check
%pytest --ignore=build
export PYTHONPATH="./build/lib"
THEIRS=`%{buildroot}/%{_bindir}/b4 --version`
OURS=`sed -n "s/__VERSION__: str = '\(.*\)'/\1/p" src/b4/__init__.py`
test "$THEIRS" = "$OURS"
%{buildroot}/%{_bindir}/b4 --help | grep -Fq 'mbox,am,shazam,review,pr'
%{buildroot}/%{_bindir}/b4 mbox abc |& grep -Fq 'Looking up abc'

%files
%doc README.rst
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man1/b4.1%{?ext_man}
%{python_sitelib}/%{name}*

%changelog
