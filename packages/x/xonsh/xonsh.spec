#
# spec file for package xonsh
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


%define pythons python3
Name:           xonsh
Version:        0.12.4
Release:        0
Summary:        A general purpose, Python-powered shell
License:        BSD-3-Clause AND BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://xon.sh/
Source0:        https://github.com/xonsh/xonsh/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# SECTION docs
BuildRequires:  python3-Sphinx
BuildRequires:  python3-cloud-sptheme
BuildRequires:  python3-numpydoc
BuildRequires:  python3-myst-parser
BuildRequires:  python3-runthis-sphinxext
BuildRequires:  python3-markdown-it-py
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python3-base >= 3.5
BuildRequires:  python3-setuptools
Recommends:     python3-Pygments >= 2.2
Recommends:     python3-distro
Recommends:     python3-ply
Recommends:     python3-prompt_toolkit >= 2.0
Recommends:     python3-setproctitle
Requires:       python3-base >= 3.5
Suggests:       %{name}-doc
Provides:       python3-xonsh = %{version}
Obsoletes:      python3-xonsh < %{version}
BuildArch:      noarch

%package -n %{name}-doc
Summary:        Documentation files for %name
Group:          Documentation/HTML

%description
xonsh is a Python-powered, Unix-gazing shell language and command prompt. The language is a superset of Python 3.5+ with additional shell primitives. xonsh (pronounced conch) is meant for the daily use of experts and novices alike.

%description -n %{name}-doc
HTML documentation on the API and examples for %name.

%prep
%setup -q -n xonsh-%{version}
sed -i '1s/^#!.*//' xonsh/xoreutils/_which.py xonsh/webconfig/main.py

%build
%python_build
pushd docs
LANG=C.UTF-8 PYTHONPATH=.. setarch -R make html
# work around a rpmlint error file-contains-buildroot
find _build -name '*.doctree' -exec sed -i 's#/home/abuild/rpmbuild/BUILD#_WORKDIR_#g' {} \+
rm _build/html/.buildinfo
rm -r _build/doctrees
popd

%install
%python_install
%fdupes %{buildroot}
%fdupes -s docs/
%fdupes -s docs/_build/html/

%files
%{python3_sitelib}/*
%{_bindir}/xonsh
%{_bindir}/xonsh-cat
%{_bindir}/xon.sh
%{_bindir}/xonsh-uptime
%{_bindir}/xonsh-uname
%doc README.rst logo.txt CHANGELOG.rst
%doc xontrib
%license license

%files -n %{name}-doc
%doc docs/_build/html

%changelog
