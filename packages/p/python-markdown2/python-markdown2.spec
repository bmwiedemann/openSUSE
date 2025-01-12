#
# spec file for package python-markdown2
#
# Copyright (c) 2025 SUSE LLC
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


%{?sle15_python_module_pythons}
Name:           python-markdown2
Version:        2.5.2
Release:        0
Summary:        A Python implementation of Markdown
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/trentm/python-markdown2
Source:         https://files.pythonhosted.org/packages/source/m/markdown2/markdown2-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Markdown2 is a Python implementation of Markdown.
It closely matches the behaviour of the original
Perl-implemented Markdown.pl. Markdown2 also comes with a number of
extensions (called "extras") for things like syntax coloring, tables,
header-ids.

%prep
%autosetup -p1 -n markdown2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/markdown2
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd test
# Exclusion because of gh#trentm/python-markdown2#388
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python test.py -- -knownfailure || /bin/true
popd

%post
%python_install_alternative markdown2

%postun
%python_uninstall_alternative markdown2

%files %{python_files}
%license LICENSE.txt
%doc CHANGES.md CONTRIBUTORS.txt TODO.txt
%python_alternative %{_bindir}/markdown2
%{python_sitelib}/markdown2.py
%pycache_only %{python_sitelib}/__pycache__/markdown2*
%{python_sitelib}/markdown2-%{version}.dist-info

%changelog
