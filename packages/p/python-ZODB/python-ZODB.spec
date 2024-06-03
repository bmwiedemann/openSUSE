#
# spec file for package python-ZODB
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2013 LISA GmbH, Bingen, Germany.
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


Name:           python-ZODB
Version:        6.0
Release:        0
Summary:        Zope Object Database: object database and persistence
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/ZODB
Source:         https://files.pythonhosted.org/packages/source/Z/ZODB/ZODB-%{version}.tar.gz
BuildRequires:  %{python_module BTrees >= 4.2.0}
BuildRequires:  %{python_module ZConfig}
BuildRequires:  %{python_module manuel}
BuildRequires:  %{python_module persistent-devel >= 4.4.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module transaction >= 2.4.0}
BuildRequires:  %{python_module zc.lockfile}
BuildRequires:  %{python_module zodbpickle >= 1.0.1}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  %{python_module zope.testing}
BuildRequires:  %{python_module zope.testrunner >= 4.4.6}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-BTrees >= 4.2.0
Requires:       python-ZConfig
Requires:       python-persistent >= 4.4.0
Requires:       python-transaction >= 2.4.0
Requires:       python-zc.lockfile
Requires:       python-zodbpickle >= 1.0.1
Requires:       python-zope.interface
Requires(post): update-alternatives
Requires(preun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
The Zope Object Database provides an object-oriented database for Python that
provides a high-degree of transparency. Applications can take advantage of
object database features with few, if any, changes to application logic. ZODB
includes features such as a plugable storage interface, rich transaction
support, and undo.

%package     -n %{name}-doc
Summary:        Zope Object Database: object database and persistence
Provides:       %{python_module ZODB-doc = %{version}}

%description -n %{name}-doc
This package contains documentation files for %{name}.

%prep
%setup -q -n ZODB-%{version}
# delete backup files
find . -name "*~" -print -delete
# remove unwanted shebang
find src -name "*.py" | xargs sed -i '1 { /^#!/ d }'
rm -rf src/ZODB.egg-info
# do not test docu generating
rm -f src/ZODB/tests/testdocumentation.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/fsdump
%python_clone -a %{buildroot}%{_bindir}/fsoids
%python_clone -a %{buildroot}%{_bindir}/fsrefs
%python_clone -a %{buildroot}%{_bindir}/fstail
%python_clone -a %{buildroot}%{_bindir}/repozo

mkdir -p %{buildroot}%{_defaultdocdir}/python-ZODB-doc/docs
cp -r docs/* %{buildroot}%{_defaultdocdir}/python-ZODB-doc/docs/
%fdupes %{buildroot}%{_defaultdocdir}/python-ZODB-doc

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} zope-testrunner-%{$python_bin_suffix} --test-path=src

%post
%python_install_alternative fsdump fsoids fsrefs fstail repozo

%postun
%python_uninstall_alternative fsdump

%files %{python_files}
%license LICENSE.txt COPYRIGHT.txt
%doc 3.11.txt CHANGES.rst HISTORY.rst README.rst
%{python_sitelib}/ZODB/
%{python_sitelib}/ZODB-%{version}-py*.egg-info
%python_alternative %{_bindir}/fsdump
%python_alternative %{_bindir}/fsoids
%python_alternative %{_bindir}/fsrefs
%python_alternative %{_bindir}/fstail
%python_alternative %{_bindir}/repozo

%files -n %{name}-doc
%doc %{_defaultdocdir}/python-ZODB-doc

%changelog
