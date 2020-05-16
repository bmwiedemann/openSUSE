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


Name:           xonsh
Version:        0.9.18
Release:        0
Summary:        A general purpose, Python-ish shell
License:        BSD-3-Clause AND BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://xonsh.org
Source0:        https://github.com/xonsh/xonsh/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# SECTION docs
BuildRequires:  python3-Sphinx
BuildRequires:  python3-numpydoc
BuildRequires:  python3-runthis-sphinxext
# /SECTION
BuildRequires:  fdupes
BuildRequires:  python3-devel >= 3.4
BuildRequires:  python3-setuptools
Recommends:     python3-Pygments >= 2.2
Recommends:     python3-distro
Recommends:     python3-ply
Recommends:     python3-prompt_toolkit >= 2.0
Recommends:     python3-setproctitle
Suggests:       %{name}-doc
Provides:       python3-xonsh = %{version}
Obsoletes:      python3-xonsh < %{version}
BuildArch:      noarch

%package -n %{name}-doc
Summary:        Documentation files for %name
Group:          Documentation/HTML

%description
xonsh is a Python-ish, BASHwards-looking shell language and command prompt. The language is a superset of Python 3.4+ with additional shell primitives. xonsh (pronounced conch) is meant for the daily use of experts and novices alike.

%description -n %{name}-doc
HTML documentation on the API and examples for %name.

%prep
%setup -q -n xonsh-%{version}
sed -i '1s/^#!.*//' xonsh/xoreutils/_which.py xonsh/ply/example/classcalc/calc.py xonsh/ply/example/newclasscalc/calc.py xonsh/ply/example/yply/yply.py
sed -i '1s/^#!.*/#!\/usr\/bin\/python/' xonsh/ply/example/yply/yply.py

%build
python3 setup.py build
pushd docs
LANG=C.UTF-8 READTHEDOCS=True PYTHONPATH=.. make html
# work around a rpmlint error file-contains-buildroot
sed -i 's#/home/abuild/rpmbuild/BUILD#_WORKDIR_#g' _build/html/api/platform.html
rm _build/html/.buildinfo
popd

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
%fdupes %{buildroot}

%files
%{python3_sitelib}/*
%{_bindir}/xonsh
%{_bindir}/xonsh-cat
%{_bindir}/xon.sh
%doc README.rst logo.txt CHANGELOG.rst
%doc xontrib
%doc xonsh/ply/example xonsh/ply/doc/*.html xonsh/ply/README.md xonsh/ply/CHANGES
%license license

%files -n %{name}-doc
%doc docs/_build/html

%changelog
