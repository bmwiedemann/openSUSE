#
# spec file for package python-rethinkdb
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-rethinkdb
Version:        2.4.5
Release:        0
Summary:        Python driver library for the RethinkDB database server
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/RethinkDB/rethinkdb-python
Source:         https://github.com/rethinkdb/rethinkdb-python/archive/v%{version}.tar.gz#/rethinkdb-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/rethinkdb/rethinkdb/next/src/rdb_protocol/ql2.proto
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
Python driver library for the RethinkDB database server.

%prep
%setup -q -n rethinkdb-python-%{version}

# Excerpt from Makefile, needed because this is using the GitHub archive instead of PyPI sdist
cp %{SOURCE1} rethinkdb/ql2.proto
python3 scripts/convert_protofile.py -l python -i rethinkdb/ql2.proto -o rethinkdb/ql2_pb2.py

# These require a rethinkdb instance running
rm -r tests/integration

sed -i '1{/^#!/d}' rethinkdb/*.py

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_clone -a %{buildroot}%{_bindir}/rethinkdb-repl
%python_clone -a %{buildroot}%{_bindir}/rethinkdb-index-rebuild
%python_clone -a %{buildroot}%{_bindir}/rethinkdb-restore
%python_clone -a %{buildroot}%{_bindir}/rethinkdb-export
%python_clone -a %{buildroot}%{_bindir}/rethinkdb-dump
%python_clone -a %{buildroot}%{_bindir}/rethinkdb-import
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative rethinkdb-repl
%python_install_alternative rethinkdb-index-rebuild
%python_install_alternative rethinkdb-restore
%python_install_alternative rethinkdb-export
%python_install_alternative rethinkdb-dump
%python_install_alternative rethinkdb-import

%postun
%python_uninstall_alternative rethinkdb-repl
%python_uninstall_alternative rethinkdb-index-rebuild
%python_uninstall_alternative rethinkdb-restore
%python_uninstall_alternative rethinkdb-export
%python_uninstall_alternative rethinkdb-dump
%python_uninstall_alternative rethinkdb-import

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/rethinkdb-import
%python_alternative %{_bindir}/rethinkdb-dump
%python_alternative %{_bindir}/rethinkdb-export
%python_alternative %{_bindir}/rethinkdb-restore
%python_alternative %{_bindir}/rethinkdb-index-rebuild
%python_alternative %{_bindir}/rethinkdb-repl
%{python_sitelib}/*

%changelog
